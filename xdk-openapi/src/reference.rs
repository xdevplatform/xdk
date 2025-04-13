//! Reference handling for OpenAPI specifications
//! 
//! This module provides functionality for handling references in OpenAPI specifications.
//! References allow components to be reused across the specification, reducing duplication
//! and improving maintainability.

use serde::{Deserialize, Serialize};
use std::rc::Rc;
use crate::error::OpenApiError;
use crate::components::{Schema, Parameter};
/// A reference to another component in the OpenAPI spec
/// 
/// This type provides a way to reference other components in the OpenAPI specification.
/// It uses reference counting to efficiently share components across the specification.
#[derive(Debug)]
pub struct Reference<T> {
    /// The inner value being referenced
    inner: Rc<T>,
}

impl<T> Reference<T> {
    /// Creates a new reference to a value
    /// 
    /// # Arguments
    /// 
    /// * `value` - The value to reference
    /// 
    /// # Returns
    /// 
    /// A new reference to the value
    pub fn new(value: T) -> Self {
        Self {
            inner: Rc::new(value),
        }
    }

    /// Gets a reference to the inner value
    /// 
    /// # Returns
    /// 
    /// A reference to the inner value
    pub fn as_ref(&self) -> &T {
        &self.inner
    }
}

impl<T> Clone for Reference<T> {
    /// Creates a clone of the reference
    /// 
    /// This implementation clones the reference count, not the inner value.
    fn clone(&self) -> Self {
        Self {
            inner: Rc::clone(&self.inner),
        }
    }
}

impl<T> Serialize for Reference<T>
where
    T: Serialize,
{
    /// Serializes the reference
    /// 
    /// This implementation serializes the inner value directly.
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::Serializer,
    {
        self.inner.serialize(serializer)
    }
}

impl<'de, T> Deserialize<'de> for Reference<T>
where
    T: Deserialize<'de> + 'static,
{
    /// Deserializes a reference
    /// 
    /// This implementation deserializes the value and wraps it in a reference.
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        let value = T::deserialize(deserializer)?;
        Ok(Reference::new(value))
    }
}

/// A context for deserializing OpenAPI specs with reference resolution
/// 
/// This type provides a context for resolving references during deserialization.
/// It maintains a mapping of reference paths to their resolved values.
#[derive(Clone)]
pub struct OpenApiContext {
    /// Map of schema references to their resolved values
    schemas: std::collections::HashMap<String, Rc<Schema>>,
    /// Map of parameter references to their resolved values
    parameters: std::collections::HashMap<String, Rc<Parameter>>,
}

impl OpenApiContext {
    /// Creates a new OpenAPI context
    /// 
    /// # Returns
    /// 
    /// A new OpenAPI context with empty maps for schemas and parameters
    pub fn new() -> Self {
        Self {
            schemas: std::collections::HashMap::new(),
            parameters: std::collections::HashMap::new(),
        }
    }

    /// Adds a schema to the context
    /// 
    /// # Arguments
    /// 
    /// * `name` - The name of the schema
    /// * `schema` - The schema to add
    pub fn add_schema(&mut self, name: String, schema: Schema) {
        self.schemas.insert(format!("#/components/schemas/{}", name), Rc::new(schema));
    }

    /// Adds a parameter to the context
    /// 
    /// # Arguments
    /// 
    /// * `name` - The name of the parameter
    /// * `parameter` - The parameter to add
    pub fn add_parameter(&mut self, name: String, parameter: Parameter) {
        self.parameters.insert(format!("#/components/parameters/{}", name), Rc::new(parameter));
    }

    /// Resolves a reference to a component
    /// 
    /// # Arguments
    /// 
    /// * `reference` - The reference path to resolve
    /// 
    /// # Returns
    /// 
    /// The resolved component, or an error if the reference could not be resolved
    pub fn resolve_reference<T>(&self, reference: &str) -> Result<Rc<T>, OpenApiError>
    where
        T: Clone + 'static,
    {
        if reference.starts_with("#/components/schemas/") {
            self.schemas
                .get(reference)
                .cloned()
                .ok_or_else(|| OpenApiError::ReferenceNotFound(reference.to_string()))
                .map(|rc| unsafe { std::mem::transmute_copy(&rc) })
        } else if reference.starts_with("#/components/parameters/") {
            self.parameters
                .get(reference)
                .cloned()
                .ok_or_else(|| OpenApiError::ReferenceNotFound(reference.to_string()))
                .map(|rc| unsafe { std::mem::transmute_copy(&rc) })
        } else {
            Err(OpenApiError::ReferenceNotFound(reference.to_string()))
        }
    }
}

/// A value that can be either a reference or a direct value
/// 
/// This type is used to represent values that can be either a reference to another
/// component or a direct value.
#[derive(Debug)]
pub enum RefOrValue<T> {
    /// A reference to another component
    Reference(Reference<T>),
    /// A direct value
    Value(T),
}

impl<'de, T> Deserialize<'de> for RefOrValue<T>
where
    T: Deserialize<'de> + Clone + 'static,
{
    /// Deserializes a reference or value
    /// 
    /// This implementation handles both direct values and references.
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        #[derive(Deserialize)]
        #[serde(untagged)]
        enum Helper<T> {
            Reference { #[serde(rename = "$ref")] reference: String },
            Value(T),
        }

        match Helper::<T>::deserialize(deserializer)? {
            Helper::Reference { reference } => {
                let context = Rc::new(OpenApiContext::new());
                let resolved = context
                    .resolve_reference::<T>(&reference)
                    .map_err(serde::de::Error::custom)?;
                Ok(RefOrValue::Reference(Reference::new((*resolved).clone())))
            }
            Helper::Value(value) => Ok(RefOrValue::Value(value)),
        }
    }
} 