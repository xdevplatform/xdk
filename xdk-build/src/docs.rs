use crate::error::{BuildError, Result};
use colored::*;
use std::path::Path;
use xdk_lib::docs::generate_mintlify_docs;
use xdk_lib::{XdkConfig, log_info, log_success};
use xdk_openapi::OpenApi;

/// Generates Mintlify SDK reference MDX pages, OpenAPI `x-codeSamples` overlay,
/// `xdks/**/llms.txt`, and `docs.json` navigation updates.
pub fn generate(openapi: &OpenApi, output_dir: &Path, sync_endpoint_stubs: bool) -> Result<()> {
    log_info!(
        "Generating Mintlify XDK documentation & OpenAPI Overlay in {}...",
        output_dir.display().to_string().magenta()
    );

    let config = XdkConfig::load_default().map_err(BuildError::SdkGenError)?;
    let summary = generate_mintlify_docs(openapi, output_dir, &config, sync_endpoint_stubs)
        .map_err(BuildError::SdkGenError)?;

    log_success!(
        "Generated {} MDX reference pages across {} tags ({} operations).",
        summary.mdx_files_written,
        summary.tag_count,
        summary.operation_count
    );
    log_success!(
        "Wrote OpenAPI Overlay to {}",
        summary.overlay_path.display().to_string().magenta()
    );
    if summary.docs_json_updated {
        log_success!("Updated docs.json navigation and OpenAPI overlay settings.");
    }
    if !summary.new_endpoint_stubs.is_empty() {
        log_success!(
            "Created {} new endpoint MDX stub(s).",
            summary.new_endpoint_stubs.len()
        );
    }

    Ok(())
}
