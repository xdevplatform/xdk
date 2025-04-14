//! Reference or Value handling for OpenAPI specifications
//! 
//! This module provides the RefOrValue type which can hold either a direct value
//! or a reference to another component, resolved lazily.

use serde::{Deserialize, Serialize, Deserializer, Serializer};
use std::rc::Rc;
use std::cell::RefCell;
use std::any::Any;
use crate::context::OpenApiContextGuard;
use crate::error::OpenApiError;

/// A value that can be either a reference or a direct value, with lazy resolution for references.
/// 
/// This type is used to represent values that can be either a reference to another
/// component or a direct value.
#[derive(Debug, Clone)]
pub enum RefOrValue<T: Clone + 'static> {
    /// A reference to another component, holding the path and a cache for the resolved value.
    Reference {
        path: String,
        /// Cache for the resolved value. None initially, Some(Rc<T>) after successful resolution.
        /// RefCell allows interior mutability for caching within an immutable reference.
        resolved: RefCell<Option<Result<Rc<T>, OpenApiError>>>,
    },
    /// A direct value
    Value(T),
}

impl<T: Clone + Any> RefOrValue<T> {
    /// Resolves the reference if it hasn't been already and returns a result containing the resolved Rc<T>.
    /// Caches the result (Ok or Err) for subsequent calls.
    ///
    /// # Returns
    ///
    /// * `Ok(Rc<T>)` if it's a direct value (wrapped in a new Rc) or a successfully resolved reference.
    /// * `Err(OpenApiError)` if the reference failed to resolve (e.g., not found, type mismatch).
    pub fn try_resolve(&self) -> Result<Rc<T>, OpenApiError> {
        match self {
            RefOrValue::Value(value) => Ok(Rc::new(value.clone())),
            RefOrValue::Reference { path, resolved } => {
                if resolved.borrow().is_none() {
                    let resolution_result = OpenApiContextGuard::with_context(|ctx| {
                        ctx.resolve_reference::<T>(path)
                    }).unwrap_or_else(|| Err(OpenApiError::InternalError("OpenAPI context not available".to_string())));
                    *resolved.borrow_mut() = Some(resolution_result);
                }

                let cache_borrow = resolved.borrow();
                let cached_result = cache_borrow.as_ref().expect("Cache should be populated here");

                cached_result.clone()
            }
        }
    }

    /// Returns a mutable instance. If it's a `Value`, returns the owned value.
    /// If it's a `Reference`, it resolves, clones the resolved value, and returns the owned clone.
    /// Panics if the reference cannot be resolved.
    pub fn into_mut_owned(self) -> T {
         match self {
            RefOrValue::Value(value) => value,
            RefOrValue::Reference { .. } => { // Resolve (panics on error) and clone
                let rc = self.try_resolve().expect("Failed to resolve reference in into_mut_owned");
                rc.as_ref().clone()
            }
        }
    }

     /// Clones the inner value, resolving references if necessary.
     /// Panics if the reference cannot be resolved.
    pub fn clone_inner(&self) -> T {
        // Resolve (panics on error) and clone
        let rc = self.try_resolve().expect("Failed to resolve reference in clone_inner");
        rc.as_ref().clone()
    }

    pub fn as_ref(&self) -> Rc<T> {
        match self.try_resolve() {
            Ok(rc_value) => rc_value,
            Err(e) => panic!("Failed to resolve reference: {:?}", e),
        }
    }
}
// Custom Serialize for RefOrValue
impl<T: Clone + Serialize + Any> Serialize for RefOrValue<T> {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        match self.try_resolve() {
            Ok(rc_value) => rc_value.as_ref().serialize(serializer),
            Err(e) => Err(serde::ser::Error::custom(format!("Failed to resolve reference during serialization: {:?}", e.clone()))),
        }
    }
}

// Custom Deserialize for RefOrValue
impl<'de, T> Deserialize<'de> for RefOrValue<T>
where
    T: Deserialize<'de> + Clone + Any + 'static,
{
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        // Temporary helper enum for untagged deserialization
        #[derive(Deserialize)]
        #[serde(untagged)]
        enum Helper<Val> {
            Ref { #[serde(rename = "$ref")] path: String },
            Value(Val),
        }

        match Helper::<T>::deserialize(deserializer)? {
            Helper::Ref { path } => {
                // Store the path, don't resolve yet. Resolution happens in as_ref/try_resolve.
                Ok(RefOrValue::Reference {
                    path,
                    resolved: RefCell::new(None), // Initialize cache as empty
                })
            }
            Helper::Value(value) => Ok(RefOrValue::Value(value)),
        }
    }
} 