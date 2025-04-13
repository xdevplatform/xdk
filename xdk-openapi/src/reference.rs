use serde::{Deserialize, Serialize};
use std::rc::Rc;
use crate::error::OpenApiError;
use crate::components::{Schema, Parameter};
/// A reference to another component in the OpenAPI spec
#[derive(Debug)]
pub struct Reference<T> {
    inner: Rc<T>,
}

impl<T> Reference<T> {
    pub fn new(value: T) -> Self {
        Self {
            inner: Rc::new(value),
        }
    }

    pub fn as_ref(&self) -> &T {
        &self.inner
    }
}

impl<T> Clone for Reference<T> {
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
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        let value = T::deserialize(deserializer)?;
        Ok(Reference::new(value))
    }
}

/// A context for deserializing OpenAPI specs with reference resolution
#[derive(Clone)]
pub struct OpenApiContext {
    schemas: std::collections::HashMap<String, Rc<Schema>>,
    parameters: std::collections::HashMap<String, Rc<Parameter>>,
}

impl OpenApiContext {
    pub fn new() -> Self {
        Self {
            schemas: std::collections::HashMap::new(),
            parameters: std::collections::HashMap::new(),
        }
    }

    pub fn add_schema(&mut self, name: String, schema: Schema) {
        self.schemas.insert(format!("#/components/schemas/{}", name), Rc::new(schema));
    }

    pub fn add_parameter(&mut self, name: String, parameter: Parameter) {
        self.parameters.insert(format!("#/components/parameters/{}", name), Rc::new(parameter));
    }

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

#[derive(Debug)]
pub enum RefOrValue<T> {
    Reference(Reference<T>),
    Value(T),
}

impl<'de, T> Deserialize<'de> for RefOrValue<T>
where
    T: Deserialize<'de> + Clone + 'static,
{
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