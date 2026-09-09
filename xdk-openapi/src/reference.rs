//! Reference or Value handling for OpenAPI specifications
//!
//! This module provides the RefOrValue type which can hold either a direct value
//! or a reference to another component, resolved lazily.

use crate::context::OpenApiContextGuard;
use crate::error::OpenApiError;
use crate::error::Result;
use serde::{Deserialize, Deserializer, Serialize, Serializer};
use std::any::Any;
use std::cell::RefCell;
use std::rc::Rc;
/// A value that can be either a reference or a direct value with lazy resolution for references.
///
/// This type is used to represent values that can be either a reference to another
/// component or a direct value.
#[derive(Debug, Clone)]
pub enum RefOrValue<T: Clone + 'static> {
    /// A reference to another component, holding the path and a cache for the resolved value.
    Reference {
        path: String,
        /// Cache for the successfully resolved value ONLY. None initially, Some(Rc<T>) after successful resolution.
        /// RefCell allows interior mutability for caching within an immutable reference.
        resolved: RefCell<Option<Rc<T>>>,
    },
    /// A direct value
    Value(T),
}

impl<T: Clone + Any> RefOrValue<T> {
    /// Resolves the reference if it hasn't been successfully resolved and cached already.
    /// Returns a result containing the resolved Rc<T>. Errors are not cached.
    ///
    /// # Returns
    ///
    /// * `Ok(Rc<T>)` if it's a direct value (wrapped in a new Rc) or a successfully resolved reference (potentially cached).
    /// * `Err(OpenApiError)` if the reference failed to resolve (e.g., not found, type mismatch). Resolution will be re-attempted on the next call.
    pub fn try_resolve(&self) -> Result<Rc<T>> {
        match self {
            RefOrValue::Value(value) => Ok(Rc::new(value.clone())),
            RefOrValue::Reference { path, resolved } => {
                if let Some(cached_rc) = resolved.borrow().as_ref() {
                    return Ok(cached_rc.clone());
                }

                let resolution_result =
                    OpenApiContextGuard::with_context(|ctx| ctx.resolve_reference::<T>(path))
                        .unwrap_or_else(|| {
                            Err(OpenApiError::InternalError(
                                "OpenAPI context not available".to_string(),
                            ))
                        });

                match resolution_result {
                    Ok(rc) => {
                        *resolved.borrow_mut() = Some(rc.clone());
                        Ok(rc)
                    }
                    Err(e) => Err(e),
                }
            }
        }
    }
}
// Custom Serialize for RefOrValue
// For references, we serialize both the $ref path AND try to include resolved properties
// so templates can access either the reference name or the actual schema fields
impl<T: Clone + Serialize + Any> Serialize for RefOrValue<T> {
    fn serialize<S>(&self, serializer: S) -> std::result::Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        match self {
            RefOrValue::Reference { path, .. } => {
                // Try to resolve the reference and serialize the resolved value
                // This allows templates to access the actual schema properties
                if let Ok(resolved) = self.try_resolve() {
                    // Serialize the resolved value with $ref path included
                    // First serialize the resolved value to a serde_json::Value
                    let resolved_json = serde_json::to_value(resolved.as_ref())
                        .map_err(serde::ser::Error::custom)?;

                    if let serde_json::Value::Object(mut obj) = resolved_json {
                        // Add the $ref path to the object so templates can still extract type names
                        obj.insert("$ref".to_string(), serde_json::Value::String(path.clone()));
                        return obj.serialize(serializer);
                    }

                    // If not an object, just serialize the resolved value
                    resolved.serialize(serializer)
                } else {
                    // Fallback: just serialize the $ref path as an object
                    let mut obj = serde_json::Map::new();
                    obj.insert("$ref".to_string(), serde_json::Value::String(path.clone()));
                    serde_json::Value::Object(obj).serialize(serializer)
                }
            }
            RefOrValue::Value(value) => value.serialize(serializer),
        }
    }
}

// Custom Deserialize for RefOrValue
impl<'de, T> Deserialize<'de> for RefOrValue<T>
where
    T: Deserialize<'de> + Clone + Any + 'static,
{
    fn deserialize<D>(deserializer: D) -> std::result::Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        // Temporary helper enum for untagged deserialization
        #[derive(Deserialize)]
        #[serde(untagged)]
        enum Helper<Val> {
            Ref {
                #[serde(rename = "$ref")]
                path: String,
            },
            Value(Val),
        }

        match Helper::<T>::deserialize(deserializer)? {
            Helper::Ref { path } => Ok(RefOrValue::Reference {
                path,
                resolved: RefCell::new(None),
            }),
            Helper::Value(value) => Ok(RefOrValue::Value(value)),
        }
    }
}
