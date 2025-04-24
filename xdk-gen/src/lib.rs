/// XDK Generator Library
///
/// This library provides a framework for generating SDK code from OpenAPI specifications.
/// It abstracts common operations in the `core` module and provides language-specific
/// implementations. The `python` module serves as an example implementation.
///
/// # Creating a New Language Generator
///
/// To create a generator for a new language:
///
/// 1. Create a new module folder (e.g., `javascript/`)
/// 2. Implement the following required files:
///   - `mod.rs`: Module exports and potentially tests
///   - `generator.rs`: Implementation of the generator using the `define_generator!` macro
///   - `models.rs`: Context models for templates
///
/// Everything else (parsing, utilities, error handling) is abstracted in the `core` module.
mod core;
mod python;

pub use core::Result;
pub use core::SdkGeneratorError;
pub use core::generator::SdkGenerator;
pub use python::PythonGenerator;
