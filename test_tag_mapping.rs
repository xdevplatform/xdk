use xdk_gen::Python;
use xdk_openapi::{OpenApiContextGuard, parse_json};
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Test OpenAPI spec with "Tweets" tag
    let json_spec = r#"{
        "openapi": "3.0.0",
        "info": {
            "title": "Test API",
            "version": "1.0.0"
        },
        "paths": {
            "/2/tweets": {
                "get": {
                    "summary": "Get tweets",
                    "operationId": "getTweets",
                    "description": "Returns tweets",
                    "tags": ["Tweets"],
                    "parameters": [],
                    "responses": {
                        "200": {
                            "description": "Successful response"
                        }
                    }
                }
            }
        }
    }"#;

    // Set up the context
    let _guard = OpenApiContextGuard::new();

    // Parse the OpenAPI spec
    let openapi = parse_json(json_spec)?;

    // Create output directory
    let output_dir = Path::new("test_output");
    std::fs::create_dir_all(output_dir)?;

    // Generate the SDK
    let generator = Python;
    xdk_gen::core::generator::generate(generator, &openapi, output_dir)?;

    println!("SDK generated successfully!");
    println!("Check the test_output directory for the generated files.");
    println!("You should see a 'posts' directory instead of 'tweets'.");

    Ok(())
} 