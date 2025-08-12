use std::io;
use xdk_lib::{Result, SdkGeneratorError};

#[test]
fn test_io_error_conversion() {
    let io_error = io::Error::new(io::ErrorKind::NotFound, "File not found");
    let xdk_error: SdkGeneratorError = io_error.into();

    match xdk_error {
        SdkGeneratorError::IoError(err) => {
            assert_eq!(err.kind(), io::ErrorKind::NotFound);
            assert_eq!(err.to_string(), "File not found");
        }
        _ => panic!("Expected IoError"),
    }
}

#[test]
fn test_template_error_conversion() {
    let template_error = minijinja::Error::new(
        minijinja::ErrorKind::TemplateNotFound,
        "Template 'missing' not found",
    );
    let xdk_error: SdkGeneratorError = template_error.into();

    match xdk_error {
        SdkGeneratorError::TemplateError(err) => {
            assert!(err.to_string().contains("Template"));
        }
        _ => panic!("Expected TemplateError"),
    }
}

#[test]
fn test_framework_error_creation() {
    let framework_error = SdkGeneratorError::FrameworkError("Invalid configuration".to_string());

    match framework_error {
        SdkGeneratorError::FrameworkError(msg) => {
            assert_eq!(msg, "Invalid configuration");
        }
        _ => panic!("Expected FrameworkError"),
    }
}

#[test]
fn test_missing_field_error_creation() {
    let missing_field_error = SdkGeneratorError::MissingField("operation_id".to_string());

    match missing_field_error {
        SdkGeneratorError::MissingField(field) => {
            assert_eq!(field, "operation_id");
        }
        _ => panic!("Expected MissingField error"),
    }
}

#[test]
fn test_other_error_creation() {
    let other_error = SdkGeneratorError::Other("Custom error".to_string());

    match other_error {
        SdkGeneratorError::Other(msg) => {
            assert_eq!(msg, "Custom error");
        }
        _ => panic!("Expected Other error"),
    }
}

#[test]
fn test_string_conversion() {
    let error: SdkGeneratorError = "Test error".into();

    match error {
        SdkGeneratorError::Other(msg) => {
            assert_eq!(msg, "Test error");
        }
        _ => panic!("Expected Other error from string conversion"),
    }
}

#[test]
fn test_error_display() {
    let errors = vec![
        SdkGeneratorError::FrameworkError("Framework error".to_string()),
        SdkGeneratorError::MissingField("field_name".to_string()),
        SdkGeneratorError::Other("Other error".to_string()),
        SdkGeneratorError::IoError(io::Error::new(
            io::ErrorKind::PermissionDenied,
            "Access denied",
        )),
    ];

    for error in errors {
        let display_string = format!("{}", error);
        assert!(!display_string.is_empty());
    }
}

#[test]
fn test_error_debug() {
    let error = SdkGeneratorError::FrameworkError("Debug test".to_string());
    let debug_string = format!("{:?}", error);
    assert!(debug_string.contains("FrameworkError"));
    assert!(debug_string.contains("Debug test"));
}

#[test]
fn test_result_type() {
    fn success_function() -> Result<String> {
        Ok("Success".to_string())
    }

    fn error_function() -> Result<String> {
        Err(SdkGeneratorError::FrameworkError("Failed".to_string()))
    }

    assert!(success_function().is_ok());
    assert_eq!(success_function().unwrap(), "Success");

    assert!(error_function().is_err());
    match error_function().unwrap_err() {
        SdkGeneratorError::FrameworkError(msg) => assert_eq!(msg, "Failed"),
        _ => panic!("Expected FrameworkError"),
    }
}

#[test]
fn test_error_source() {
    let io_error = io::Error::new(io::ErrorKind::NotFound, "Original error");
    let xdk_error: SdkGeneratorError = io_error.into();

    // Test that the error chain is preserved
    assert!(std::error::Error::source(&xdk_error).is_some());
}

#[test]
fn test_error_send_sync() {
    fn assert_send<T: Send>() {}
    fn assert_sync<T: Sync>() {}

    assert_send::<SdkGeneratorError>();
    assert_sync::<SdkGeneratorError>();
}
