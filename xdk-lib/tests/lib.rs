// XDK Lib Comprehensive Test Suite
//
// This test suite covers all major functionality of the xdk-lib crate including:
// - Casing conversions and transformations
// - Data model creation and manipulation
// - Parameter processing with language-specific casing
// - Template rendering and generation
// - Test specification generation
// - Error handling and edge cases
// - End-to-end integration scenarios

mod casing_tests;
mod error_tests;
mod integration_tests;
mod models_tests;
mod testing_tests;

// Re-export for convenience in other tests
pub use xdk_lib::*;
