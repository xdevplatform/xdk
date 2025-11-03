/// XDK Generator Implementors
///
/// This crate contains the implementation of the SDK generator for each language.
/// It uses the `xdk-lib` crate to abstract common operations and provide a consistent interface.
///
/// # Overview
///
/// The XDK Generator is a tool that automatically generates SDKs (Software Development Kits)
/// for various programming languages based on OpenAPI specifications. Each language-specific
/// generator is implemented as a separate module within this crate.
///
/// # Structure
///
/// The crate is organized into language-specific modules, each containing:
/// - `mod.rs`: Module exports and potentially tests
/// - `generator.rs`: Implementation of the generator using the `language!` macro
/// - Additional files for language-specific utilities and models
///
/// # Creating a New Language Generator
///
/// To create a generator for a new language:
///
/// 1. Create a new module folder (e.g., `javascript/`)
/// 2. Implement the following required files:
///   - `mod.rs`: Module exports and potentially tests
///   - `generator.rs`: Implementation of the generator using the `language!` macro
///
/// Everything else (parsing, utilities, error handling) is abstracted in the `xdk-lib` crate.
///
/// # Example
///
/// See the `python` module for a reference implementation of a language generator.
pub use python::Python;
pub use typescript::TypeScript;

mod python;
mod typescript;
