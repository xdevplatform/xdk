use xdk_gen::Python;
use xdk_openapi::{OpenApiContextGuard, parse_json};
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Test OpenAPI spec with various operation IDs
    let json_spec = std::fs::read_to_string("test_method_naming.json")?;

    // Set up the context
    let _guard = OpenApiContextGuard::new();

    // Parse the OpenAPI spec
    let openapi = parse_json(&json_spec)?;

    // Create output directory
    let output_dir = Path::new("test_method_output");
    std::fs::create_dir_all(output_dir)?;

    // Generate the SDK
    let generator = Python;
    xdk_gen::core::generator::generate(generator, &openapi, output_dir)?;

    println!("SDK generated successfully!");
    println!("Check the test_method_output directory for the generated files.");
    println!("Expected method names:");
    println!("- searchCommunities -> search (from /2/communities/search)");
    println!("- postAccountActivityReplay -> post_replay (from /2/account_activity/...)");
    println!("- getTweets -> get (from /2/tweets)");

    Ok(())
} 