//! OpenAPI context handling
//!
//! This module provides the context for deserializing OpenAPI specs with reference resolution.
//! It maintains a mapping of reference paths to their resolved values.

use crate::components::{Parameter, Schema, SecurityScheme};
use crate::core::{RequestBody, Response};
use crate::error::{OpenApiError, Result};
use std::any::{Any, TypeId};
use std::cell::RefCell;
use std::rc::Rc;

thread_local! {
    static CONTEXT: RefCell<Option<OpenApiContext>> = const { RefCell::new(None) };
}

/// A guard that ensures the OpenAPI context is properly set up and torn down
pub struct OpenApiContextGuard;

impl OpenApiContextGuard {
    /// Creates a new context guard and sets up the thread-local context
    pub fn new() -> Self {
        CONTEXT.with(|cell| {
            *cell.borrow_mut() = Some(OpenApiContext::new());
        });
        OpenApiContextGuard
    }

    /// Gets a reference to the current context
    pub fn with_context<F, R>(f: F) -> Option<R>
    where
        F: FnOnce(&OpenApiContext) -> R,
    {
        CONTEXT.with(|cell| cell.borrow().as_ref().map(f))
    }

    /// Gets mutable access to the current context
    pub fn with_context_mut<F, R>(f: F) -> Option<R>
    where
        F: FnOnce(&mut OpenApiContext) -> R,
    {
        CONTEXT.with(|cell| cell.borrow_mut().as_mut().map(f))
    }
}

impl Default for OpenApiContextGuard {
    fn default() -> Self {
        Self::new()
    }
}

impl Drop for OpenApiContextGuard {
    fn drop(&mut self) {
        CONTEXT.with(|cell| {
            *cell.borrow_mut() = None;
        });
    }
}

/// Enum to hold different types of referenceable components
#[derive(Clone, Debug)]
enum StoredComponent {
    Schema(Rc<Schema>),
    Parameter(Rc<Parameter>),
    Response(Rc<Response>),
    RequestBody(Rc<RequestBody>),
    SecurityScheme(Rc<SecurityScheme>),
}

/// A context for deserializing OpenAPI specs with reference resolution
///
/// This type provides a context for resolving references during deserialization.
/// It maintains a mapping of reference paths to their resolved values.
#[derive(Clone, Debug)]
pub struct OpenApiContext {
    /// Map of component references to their resolved values
    components: std::collections::HashMap<String, StoredComponent>,
}

impl OpenApiContext {
    /// Creates a new OpenAPI context
    ///
    /// # Returns
    ///
    /// A new OpenAPI context with an empty component map
    pub fn new() -> Self {
        Self {
            components: std::collections::HashMap::new(),
        }
    }

    /// Adds a schema to the context
    pub fn add_schema(&mut self, name: String, schema: Schema) {
        let path = format!("#/components/schemas/{}", name);
        self.components
            .insert(path, StoredComponent::Schema(Rc::new(schema)));
    }

    /// Adds a parameter to the context
    pub fn add_parameter(&mut self, name: String, parameter: Parameter) {
        let path = format!("#/components/parameters/{}", name);
        self.components
            .insert(path, StoredComponent::Parameter(Rc::new(parameter)));
    }

    /// Adds a response to the context
    pub fn add_response(&mut self, name: String, response: Response) {
        let path = format!("#/components/responses/{}", name);
        self.components
            .insert(path, StoredComponent::Response(Rc::new(response)));
    }

    /// Adds a request body to the context
    pub fn add_request_body(&mut self, name: String, request_body: RequestBody) {
        let path = format!("#/components/requestBodies/{}", name);
        self.components
            .insert(path, StoredComponent::RequestBody(Rc::new(request_body)));
    }

    /// Adds a security scheme to the context
    pub fn add_security_scheme(&mut self, name: String, security_scheme: SecurityScheme) {
        let path = format!("#/components/securitySchemes/{}", name);
        self.components.insert(
            path,
            StoredComponent::SecurityScheme(Rc::new(security_scheme)),
        );
    }

    /// Resolves a reference to a component with type checking (safe version)
    pub fn resolve_reference<T>(&self, reference: &str) -> Result<Rc<T>>
    where
        T: Any + Clone + 'static,
    {
        let stored_component = self
            .components
            .get(reference)
            .ok_or_else(|| OpenApiError::ReferenceNotFound(reference.to_string()))?;

        let expected_type_id = TypeId::of::<T>();

        // Helper macro for casting Rc<SpecificType> to Rc<T> if types match
        macro_rules! try_cast {
            ($rc_value:expr, $specific_type:ty) => {
                if TypeId::of::<$specific_type>() == expected_type_id {
                    // SAFETY: We've just checked that T is exactly $specific_type,
                    // so the pointer cast is valid. Rc ensures the data lives long enough.
                    Ok(unsafe { Rc::from_raw(Rc::into_raw($rc_value.clone()) as *const T) })
                } else {
                    Err(OpenApiError::TypeMismatch)
                }
            };
        }

        match stored_component {
            StoredComponent::Schema(rc) => try_cast!(rc, Schema),
            StoredComponent::Parameter(rc) => try_cast!(rc, Parameter),
            StoredComponent::Response(rc) => try_cast!(rc, Response),
            StoredComponent::RequestBody(rc) => try_cast!(rc, RequestBody),
            StoredComponent::SecurityScheme(rc) => try_cast!(rc, SecurityScheme),
            // Add cases for other StoredComponent variants here as they are added
        }
    }
}

impl Default for OpenApiContext {
    fn default() -> Self {
        Self::new()
    }
}
