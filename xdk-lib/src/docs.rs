//! Mintlify MDX reference, OpenAPI Overlay `x-codeSamples`, `llms.txt`, and `docs.json` generation.

use crate::casing::{Casing, pascal_case};
use crate::config::XdkConfig;
use crate::models::{OperationGroup, OperationInfo, ParameterInfo};
use crate::openapi::extract_operations_by_tag;
use crate::types::{
    csharp_prop_ident, csharp_type_of, csharp_var_ident, java_field_ident, java_type_of,
    py_field_ident, py_type_of, snake_to_camel, ts_type_of,
};
use crate::{Result, SdkGeneratorError};
use openapi::OpenApi;
use serde::Serialize;
use serde_json::{Map as JsonMap, Value as Json, json};
use std::collections::BTreeSet;
use std::fs;
use std::path::{Path, PathBuf};

/// Summary of generated documentation artifacts.
#[derive(Debug, Clone, Default)]
pub struct DocsGenerationSummary {
    pub tag_count: usize,
    pub operation_count: usize,
    pub mdx_files_written: usize,
    pub overlay_path: PathBuf,
    pub docs_json_updated: bool,
    pub new_endpoint_stubs: Vec<PathBuf>,
}

/// Supported SDK target languages for documentation generation.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum SdkDocLang {
    Python,
    TypeScript,
    Java,
    CSharp,
}

impl SdkDocLang {
    pub const ALL: [SdkDocLang; 4] = [
        SdkDocLang::Python,
        SdkDocLang::TypeScript,
        SdkDocLang::Java,
        SdkDocLang::CSharp,
    ];

    pub fn slug(self) -> &'static str {
        match self {
            Self::Python => "python",
            Self::TypeScript => "typescript",
            Self::Java => "java",
            Self::CSharp => "csharp",
        }
    }

    pub fn display_name(self) -> &'static str {
        match self {
            Self::Python => "Python",
            Self::TypeScript => "TypeScript",
            Self::Java => "Java",
            Self::CSharp => "C#",
        }
    }

    pub fn code_fence_lang(self) -> &'static str {
        match self {
            Self::Python => "python",
            Self::TypeScript => "typescript",
            Self::Java => "java",
            Self::CSharp => "csharp",
        }
    }

    pub fn overlay_label(self) -> &'static str {
        match self {
            Self::Python => "Python (XDK)",
            Self::TypeScript => "TypeScript (XDK)",
            Self::Java => "Java (XDK)",
            Self::CSharp => "C# (XDK)",
        }
    }

    pub fn package_name(self) -> &'static str {
        match self {
            Self::Python => "xdk",
            Self::TypeScript => "@xdevplatform/xdk",
            Self::Java => "com.x:xdk",
            Self::CSharp => "XDevPlatform.Xdk",
        }
    }

    pub fn install_command(self, version: &str) -> String {
        match self {
            Self::Python => "pip install xdk".to_string(),
            Self::TypeScript => "npm install @xdevplatform/xdk".to_string(),
            Self::Java => format!("implementation(\"com.x:xdk:{version}\")"),
            Self::CSharp => "dotnet add package XDevPlatform.Xdk".to_string(),
        }
    }

    pub fn runtime_requirement(self) -> &'static str {
        match self {
            Self::Python => "Python 3.8+",
            Self::TypeScript => "Node.js 18+ (ESM & CommonJS)",
            Self::Java => "Java 17+",
            Self::CSharp => ".NET 8.0+",
        }
    }

    pub fn registry_name(self) -> &'static str {
        match self {
            Self::Python => "PyPI",
            Self::TypeScript => "npm",
            Self::Java => "Maven Central",
            Self::CSharp => "NuGet",
        }
    }

    pub fn registry_url(self) -> &'static str {
        match self {
            Self::Python => "https://pypi.org/project/xdk/",
            Self::TypeScript => "https://www.npmjs.com/package/@xdevplatform/xdk",
            Self::Java => "https://central.sonatype.com/artifact/com.x/xdk",
            Self::CSharp => "https://www.nuget.org/packages/XDevPlatform.Xdk",
        }
    }

    pub fn repo_url(self) -> &'static str {
        match self {
            Self::Python => "https://github.com/xdevplatform/xdk-python",
            Self::TypeScript => "https://github.com/xdevplatform/xdk-typescript",
            Self::Java => "https://github.com/xdevplatform/xdk-java",
            Self::CSharp => "https://github.com/xdevplatform/xdk-csharp",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum AuthKind {
    None,
    Bearer,
    AccessToken,
}

#[derive(Debug, Clone)]
struct TagDocModel {
    kebab_slug: String,
    snake_name: String,
    camel_name: String,
    pascal_name: String,
    display_name: String,
    operations: Vec<OperationDocModel>,
}

#[derive(Debug, Clone)]
struct OperationDocModel {
    info: OperationInfo,
    op_words: Vec<String>,
    class_name: String,
    py_method: String,
    ts_method: String,
    java_method: String,
    csharp_method: String,
    csharp_pages_method: Option<String>,
    java_pages_method: Option<String>,
    params_snake: Vec<ParameterInfo>,
    params_camel: Vec<ParameterInfo>,
    body_schema: Option<Json>,
    body_required: bool,
    body_is_binary: bool,
    response_schema: Option<Json>,
    response_is_binary: bool,
    is_paginated: bool,
    is_ts_stream_method: bool,
    auth_kind: AuthKind,
}

#[derive(Debug, Serialize)]
struct CodeSampleEntry {
    lang: String,
    label: String,
    source: String,
}

/// Generates Mintlify SDK reference MDX pages, `overlays/xdk-code-samples.json`,
/// `xdks/**/llms.txt`, and (when `docs.json` exists in `output_dir`) navigation updates.
pub fn generate_mintlify_docs(
    openapi: &OpenApi,
    output_dir: &Path,
    config: &XdkConfig,
    sync_endpoint_stubs: bool,
) -> Result<DocsGenerationSummary> {
    let tags = build_tag_models(openapi)?;
    let mut summary = DocsGenerationSummary {
        tag_count: tags.len(),
        operation_count: tags.iter().map(|t| t.operations.len()).sum(),
        ..Default::default()
    };

    fs::create_dir_all(output_dir)?;

    // 1. Write OpenAPI v1.1.0 Overlay for all endpoints.
    let overlay_path = output_dir.join("overlays").join("xdk-code-samples.json");
    if let Some(parent) = overlay_path.parent() {
        fs::create_dir_all(parent)?;
    }
    let overlay_json = build_code_samples_overlay(&tags, config);
    let mut overlay_text = serde_json::to_string_pretty(&overlay_json).map_err(|e| {
        SdkGeneratorError::FrameworkError(format!("Failed to serialize overlay: {e}"))
    })?;
    overlay_text.push('\n');
    fs::write(&overlay_path, overlay_text)?;
    summary.overlay_path = overlay_path;

    // 2. Clean and write SDK reference MDX trees for all 4 languages.
    for lang in SdkDocLang::ALL {
        let version = config.get_version(lang.slug()).unwrap_or("0.1.0");
        let ref_dir = output_dir.join("xdks").join(lang.slug()).join("reference");
        if ref_dir.exists() {
            fs::remove_dir_all(&ref_dir)?;
        }
        let clients_dir = ref_dir.join("clients");
        fs::create_dir_all(&clients_dir)?;

        let overview_mdx = render_language_reference_overview(lang, version, &tags);
        fs::write(ref_dir.join("overview.mdx"), overview_mdx)?;
        summary.mdx_files_written += 1;

        for tag in &tags {
            let client_mdx = render_tag_client_mdx(lang, version, tag);
            fs::write(
                clients_dir.join(format!("{}.mdx", tag.kebab_slug)),
                client_mdx,
            )?;
            summary.mdx_files_written += 1;
        }

        // Write per-language llms.txt index.
        let lang_llms = render_language_llms_txt(lang, version, &tags);
        let lang_dir = output_dir.join("xdks").join(lang.slug());
        fs::create_dir_all(&lang_dir)?;
        fs::write(lang_dir.join("llms.txt"), lang_llms)?;
    }

    // 3. Write unified xdks/llms.txt index.
    let xdks_dir = output_dir.join("xdks");
    fs::create_dir_all(&xdks_dir)?;
    fs::write(
        xdks_dir.join("llms.txt"),
        render_root_xdks_llms_txt(config, &tags),
    )?;

    // 4. Optionally create minimal MDX stubs for new OpenAPI operations not yet present in `output_dir`.
    if sync_endpoint_stubs {
        summary.new_endpoint_stubs = create_missing_endpoint_stubs(output_dir, &tags)?;
    }

    // 5. Update docs.json navigation & api.openapi.overlays if docs.json exists.
    let docs_json_path = output_dir.join("docs.json");
    if docs_json_path.exists() {
        update_docs_json(&docs_json_path, &tags)?;
        summary.docs_json_updated = true;
    }

    // 6. Sync Maven/Gradle coordinates in Java guide pages when present.
    if let Some(java_ver) = config.get_version("java") {
        sync_java_version_in_guides(output_dir, java_ver)?;
    }

    Ok(summary)
}

fn build_tag_models(openapi: &OpenApi) -> Result<Vec<TagDocModel>> {
    let grouped = extract_operations_by_tag(openapi)?;
    let mut tags: Vec<TagDocModel> = grouped
        .into_iter()
        .map(|(tag_words, groups)| {
            let kebab_slug = Casing::Kebab.convert_words(&tag_words);
            let snake_name = Casing::Snake.convert_words(&tag_words);
            let camel_name = Casing::Camel.convert_words(&tag_words);
            let pascal_name = Casing::Pascal.convert_words(&tag_words);
            let display_name = tag_words
                .iter()
                .map(|w| pascal_case(w))
                .collect::<Vec<_>>()
                .join(" ");

            let mut operations: Vec<OperationDocModel> = groups
                .into_iter()
                .map(|g| build_operation_model(&pascal_name, g))
                .collect();
            operations.sort_by(|a, b| {
                a.py_method
                    .cmp(&b.py_method)
                    .then_with(|| a.info.path.cmp(&b.info.path))
                    .then_with(|| a.info.method.cmp(&b.info.method))
            });

            TagDocModel {
                kebab_slug,
                snake_name,
                camel_name,
                pascal_name,
                display_name,
                operations,
            }
        })
        .collect();

    tags.sort_by(|a, b| a.kebab_slug.cmp(&b.kebab_slug));
    Ok(tags)
}

fn build_operation_model(pascal_tag: &str, group: OperationGroup) -> OperationDocModel {
    let op_words = group.metadata.normalized_operation_id;
    let class_name = Casing::Pascal.convert_words(&op_words);
    let py_method = Casing::Snake.convert_words(&op_words);
    let ts_method = Casing::Camel.convert_words(&op_words);
    let java_method = java_field_ident(&ts_method);

    let is_streaming = group.operation.is_streaming;
    let params_snake = ParameterInfo::from_openapi_parameters(&group.raw_parameters, Casing::Snake)
        .unwrap_or_default();
    let params_camel = ParameterInfo::from_openapi_parameters(&group.raw_parameters, Casing::Camel)
        .unwrap_or_default();

    let is_paginated = !is_streaming
        && params_snake.iter().any(|p| {
            p.location == "query"
                && (p.original_name == "pagination_token" || p.original_name == "next_token")
        });

    let csharp_method = if is_streaming {
        format!("{class_name}Stream")
    } else {
        format!("{class_name}Async")
    };
    let csharp_pages_method = is_paginated.then(|| format!("{class_name}Pages"));
    let java_pages_method = is_paginated.then(|| format!("{java_method}Pages"));

    // TypeScript StreamClient treats streaming endpoints and explicit stream paths as EventDrivenStream.
    let is_ts_stream_method = is_streaming
        || (pascal_tag == "Stream"
            && (group.operation.path.contains("/stream")
                || group.operation.path.contains("/sample")
                || group.operation.path.contains("/firehose")
                || group.operation.path.contains("/sample10"))
            && !group.operation.path.contains("/rules"));

    let (body_schema, body_required, body_is_binary) = extract_body_schema(&group.operation);
    let (response_schema, response_is_binary) = extract_response_schema(&group.operation);
    let auth_kind = detect_auth_kind(&group.operation);

    OperationDocModel {
        info: group.operation,
        op_words,
        class_name,
        py_method,
        ts_method,
        java_method,
        csharp_method,
        csharp_pages_method,
        java_pages_method,
        params_snake,
        params_camel,
        body_schema,
        body_required,
        body_is_binary,
        response_schema,
        response_is_binary,
        is_paginated,
        is_ts_stream_method,
        auth_kind,
    }
}

fn sort_json_keys(val: Json) -> Json {
    match val {
        Json::Object(map) => {
            let mut entries: Vec<(String, Json)> = map
                .into_iter()
                .map(|(k, v)| (k, sort_json_keys(v)))
                .collect();
            entries.sort_by(|(a, _), (b, _)| a.cmp(b));
            let mut sorted = JsonMap::new();
            for (k, v) in entries {
                sorted.insert(k, v);
            }
            Json::Object(sorted)
        }
        Json::Array(arr) => Json::Array(arr.into_iter().map(sort_json_keys).collect()),
        other => other,
    }
}

fn extract_body_schema(op: &OperationInfo) -> (Option<Json>, bool, bool) {
    let Some(body) = &op.request_body else {
        return (None, false, false);
    };
    let required = body.required.unwrap_or(false);
    if let Some(media) = body
        .content
        .get("application/json")
        .or_else(|| body.content.get("multipart/form-data"))
    {
        let schema = serde_json::to_value(&media.schema).ok().map(sort_json_keys);
        return (schema, required, false);
    }
    if let Some(media) = body.content.get("application/octet-stream") {
        let schema = serde_json::to_value(&media.schema).ok().map(sort_json_keys);
        return (schema, required, true);
    }
    (None, required, false)
}

fn extract_response_schema(op: &OperationInfo) -> (Option<Json>, bool) {
    for code in ["200", "201"] {
        if let Some(resp) = op.responses.get(code)
            && let Some(content) = &resp.content
        {
            if let Some(media) = content.get("application/json") {
                return (
                    serde_json::to_value(&media.schema).ok().map(sort_json_keys),
                    false,
                );
            }
            if content.contains_key("application/octet-stream") {
                return (None, true);
            }
        }
    }
    (None, false)
}

fn detect_auth_kind(op: &OperationInfo) -> AuthKind {
    match &op.security {
        Some(reqs) if reqs.is_empty() => AuthKind::None,
        Some(reqs) => {
            let allows_bearer = reqs.iter().any(|r| r.0.contains_key("BearerToken"));
            if allows_bearer {
                AuthKind::Bearer
            } else {
                AuthKind::AccessToken
            }
        }
        None => AuthKind::Bearer,
    }
}

fn build_code_samples_overlay(tags: &[TagDocModel], config: &XdkConfig) -> Json {
    let mut all_ops: Vec<(&TagDocModel, &OperationDocModel)> = tags
        .iter()
        .flat_map(|t| t.operations.iter().map(move |op| (t, op)))
        .collect();
    all_ops.sort_by(|(_, a), (_, b)| {
        a.info
            .path
            .cmp(&b.info.path)
            .then_with(|| a.info.method.cmp(&b.info.method))
    });

    let actions: Vec<Json> = all_ops
        .into_iter()
        .map(|(tag, op)| {
            let escaped_path = op.info.path.replace('\\', "\\\\").replace('\'', "\\'");
            let target = format!(
                "$.paths['{}'].{}",
                escaped_path,
                op.info.method.to_lowercase()
            );
            let samples = vec![
                CodeSampleEntry {
                    lang: "python".to_string(),
                    label: SdkDocLang::Python.overlay_label().to_string(),
                    source: render_python_snippet(tag, op),
                },
                CodeSampleEntry {
                    lang: "typescript".to_string(),
                    label: SdkDocLang::TypeScript.overlay_label().to_string(),
                    source: render_typescript_snippet(tag, op),
                },
                CodeSampleEntry {
                    lang: "java".to_string(),
                    label: SdkDocLang::Java.overlay_label().to_string(),
                    source: render_java_snippet(tag, op),
                },
                CodeSampleEntry {
                    lang: "csharp".to_string(),
                    label: SdkDocLang::CSharp.overlay_label().to_string(),
                    source: render_csharp_snippet(tag, op),
                },
                CodeSampleEntry {
                    lang: "bash".to_string(),
                    label: "xurl".to_string(),
                    source: render_xurl_snippet(op),
                },
            ];

            json!({
                "target": target,
                "update": {
                    "x-codeSamples": samples
                }
            })
        })
        .collect();

    let py_v = config.get_version("python").unwrap_or("0.1.0");
    let ts_v = config.get_version("typescript").unwrap_or("0.1.0");
    let java_v = config.get_version("java").unwrap_or("0.1.0");
    let cs_v = config.get_version("csharp").unwrap_or("0.1.0");

    json!({
        "overlay": "1.1.0",
        "info": {
            "title": "X API Official XDK & xurl Code Samples",
            "version": format!("py-{py_v}_ts-{ts_v}_java-{java_v}_cs-{cs_v}")
        },
        "extends": "../openapi.json",
        "actions": actions
    })
}

fn render_snippet_for_lang(lang: SdkDocLang, tag: &TagDocModel, op: &OperationDocModel) -> String {
    match lang {
        SdkDocLang::Python => render_python_snippet(tag, op),
        SdkDocLang::TypeScript => render_typescript_snippet(tag, op),
        SdkDocLang::Java => render_java_snippet(tag, op),
        SdkDocLang::CSharp => render_csharp_snippet(tag, op),
    }
}

fn render_python_snippet(tag: &TagDocModel, op: &OperationDocModel) -> String {
    let mut lines = Vec::new();
    if op.auth_kind != AuthKind::None {
        lines.push("import os".to_string());
    }
    lines.push("from xdk import Client".to_string());

    let include_body = op.body_required || (op.info.method != "get" && op.body_schema.is_some());
    let req_model_name = format!("{}Request", op.class_name);
    if include_body && op.info.has_request_model && !op.body_is_binary {
        lines.push(format!(
            "from xdk.{}.models import {}",
            tag.snake_name, req_model_name
        ));
    }
    lines.push(String::new());

    match op.auth_kind {
        AuthKind::None => lines.push("client = Client()".to_string()),
        AuthKind::Bearer => {
            lines.push("client = Client(bearer_token=os.environ[\"X_BEARER_TOKEN\"])".to_string())
        }
        AuthKind::AccessToken => {
            lines.push("client = Client(access_token=os.environ[\"X_ACCESS_TOKEN\"])".to_string())
        }
    }
    lines.push(String::new());

    let mut call_args = Vec::new();
    for p in &op.params_snake {
        if p.location == "path" || p.required {
            let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
            call_args.push(format!(
                "{}={}",
                py_param_ident(&p.variable_name),
                json_to_python(&val)
            ));
        }
    }
    if include_body {
        if op.body_is_binary {
            call_args.push("body=b\"...\"".to_string());
        } else if let Some(schema) = &op.body_schema {
            let body_val = realistic_body_json(schema, 0);
            if op.info.has_request_model {
                call_args.push(format!(
                    "body={}",
                    render_python_model_expr(&req_model_name, schema, &body_val)
                ));
            } else {
                call_args.push(format!("body={}", json_to_python(&body_val)));
            }
        }
    }

    let args_str = format_call_args(&call_args, 4);
    let call_expr = format!("client.{}.{}({})", tag.snake_name, op.py_method, args_str);

    if op.info.is_streaming {
        lines.push(format!("for event in {call_expr}:"));
        lines.push("    print(event)".to_string());
    } else if op.is_paginated {
        lines.push(format!("for page in {call_expr}:"));
        lines.push("    print(page.data)".to_string());
    } else {
        lines.push(format!("response = {call_expr}"));
        lines.push("print(response)".to_string());
    }

    lines.join("\n")
}

fn render_typescript_snippet(tag: &TagDocModel, op: &OperationDocModel) -> String {
    let mut lines = vec![
        "import { Client } from \"@xdevplatform/xdk\";".to_string(),
        String::new(),
    ];

    match op.auth_kind {
        AuthKind::None => lines.push("const client = new Client();".to_string()),
        AuthKind::Bearer => lines.push(
            "const client = new Client({ bearerToken: process.env.X_BEARER_TOKEN });".to_string(),
        ),
        AuthKind::AccessToken => lines.push(
            "const client = new Client({ accessToken: process.env.X_ACCESS_TOKEN });".to_string(),
        ),
    }
    lines.push(String::new());

    let mut pos_args = Vec::new();
    for p in op.params_camel.iter().filter(|p| p.location == "path") {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        pos_args.push(json_to_ts(&val));
    }
    for p in op
        .params_camel
        .iter()
        .filter(|p| p.required && p.location != "path")
    {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        pos_args.push(json_to_ts(&val));
    }

    let include_optional_body =
        !op.body_required && op.info.method != "get" && op.body_schema.is_some();
    if op.body_required {
        if op.body_is_binary {
            pos_args.push("new Uint8Array()".to_string());
        } else if let Some(schema) = &op.body_schema {
            let body_val = realistic_body_json(schema, 0);
            pos_args.push(json_to_ts(&body_val));
        }
    } else if include_optional_body && let Some(schema) = &op.body_schema {
        let body_val = realistic_body_json(schema, 0);
        pos_args.push(format!("{{ body: {} }}", json_to_ts(&body_val)));
    }

    let args_str = format_call_args(&pos_args, 2);
    let call_expr = format!(
        "await client.{}.{}({})",
        tag.camel_name, op.ts_method, args_str
    );

    if op.is_ts_stream_method {
        lines.push(format!("const stream = {call_expr};"));
        lines.push("for await (const event of stream) {".to_string());
        lines.push("  console.log(event);".to_string());
        lines.push("}".to_string());
    } else {
        lines.push(format!("const response = {call_expr};"));
        lines.push("console.log(response);".to_string());
    }

    lines.join("\n")
}

fn render_java_snippet(tag: &TagDocModel, op: &OperationDocModel) -> String {
    let mut imports = BTreeSet::new();
    imports.insert("com.x.xdk.XClient".to_string());

    let mut pos_args = Vec::new();
    for p in op.params_camel.iter().filter(|p| p.location == "path") {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        pos_args.push(json_to_java(&val, &mut imports));
    }
    for p in op
        .params_camel
        .iter()
        .filter(|p| p.required && p.location != "path")
    {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        pos_args.push(json_to_java(&val, &mut imports));
    }

    let include_optional_body =
        !op.body_required && op.info.method != "get" && op.body_schema.is_some();
    if op.body_required {
        if op.body_is_binary {
            pos_args.push("new byte[0]".to_string());
        } else if let Some(schema) = &op.body_schema {
            pos_args.push(render_java_body_expr(schema, &mut imports));
        }
    } else if include_optional_body && let Some(schema) = &op.body_schema {
        let client_cls = format!("{}Client", tag.pascal_name);
        imports.insert(format!("com.x.xdk.clients.{client_cls}"));
        let body_expr = render_java_body_expr(schema, &mut imports);
        pos_args.push(format!(
            "{client_cls}.{}Options.builder().body({body_expr})",
            op.class_name
        ));
    }

    let mut lines: Vec<String> = imports
        .into_iter()
        .map(|i| format!("import {i};"))
        .collect();
    lines.push(String::new());

    match op.auth_kind {
        AuthKind::None => lines.push("XClient client = XClient.builder().build();".to_string()),
        AuthKind::Bearer => {
            lines.push("XClient client = XClient.builder()".to_string());
            lines.push("    .bearerToken(System.getenv(\"X_BEARER_TOKEN\"))".to_string());
            lines.push("    .build();".to_string());
        }
        AuthKind::AccessToken => {
            lines.push("XClient client = XClient.builder()".to_string());
            lines.push("    .accessToken(System.getenv(\"X_ACCESS_TOKEN\"))".to_string());
            lines.push("    .build();".to_string());
        }
    }
    lines.push(String::new());

    let args_str = format_call_args(&pos_args, 4);
    if op.info.is_streaming {
        lines.push(format!(
            "try (var stream = client.{}().{}({})) {{",
            tag.camel_name, op.java_method, args_str
        ));
        lines.push("    for (var event : stream) {".to_string());
        lines.push("        System.out.println(event);".to_string());
        lines.push("    }".to_string());
        lines.push("}".to_string());
    } else if let Some(pages_method) = &op.java_pages_method {
        lines.push(format!(
            "for (var page : client.{}().{}({})) {{",
            tag.camel_name, pages_method, args_str
        ));
        lines.push("    System.out.println(page);".to_string());
        lines.push("}".to_string());
    } else {
        lines.push(format!(
            "var response = client.{}().{}({});",
            tag.camel_name, op.java_method, args_str
        ));
        lines.push("System.out.println(response);".to_string());
    }

    lines.join("\n")
}

fn render_csharp_snippet(tag: &TagDocModel, op: &OperationDocModel) -> String {
    let mut usings = BTreeSet::new();
    if op.auth_kind != AuthKind::None {
        usings.insert("System".to_string());
    }
    usings.insert("Xdk".to_string());

    let mut pos_args = Vec::new();
    for p in op.params_camel.iter().filter(|p| p.location == "path") {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        pos_args.push(json_to_csharp(&val, &mut usings));
    }
    for p in op
        .params_camel
        .iter()
        .filter(|p| p.required && p.location != "path")
    {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        pos_args.push(json_to_csharp(&val, &mut usings));
    }

    let include_optional_body =
        !op.body_required && op.info.method != "get" && op.body_schema.is_some();
    if op.body_required {
        if op.body_is_binary {
            usings.insert("System".to_string());
            pos_args.push("Array.Empty<byte>()".to_string());
        } else if let Some(schema) = &op.body_schema {
            pos_args.push(render_csharp_body_expr(schema, &mut usings));
        }
    } else if include_optional_body && let Some(schema) = &op.body_schema {
        usings.insert("Xdk.Clients".to_string());
        let body_expr = render_csharp_body_expr(schema, &mut usings);
        pos_args.push(format!(
            "new {}Client.{}Options {{ Body = {} }}",
            tag.pascal_name, op.class_name, body_expr
        ));
    }

    let mut lines: Vec<String> = usings.into_iter().map(|u| format!("using {u};")).collect();
    lines.push(String::new());

    match op.auth_kind {
        AuthKind::None => {
            lines.push("using var client = new XClient(new XClientOptions());".to_string())
        }
        AuthKind::Bearer => {
            lines.push("using var client = new XClient(new XClientOptions".to_string());
            lines.push("{".to_string());
            lines.push(
                "    BearerToken = Environment.GetEnvironmentVariable(\"X_BEARER_TOKEN\"),"
                    .to_string(),
            );
            lines.push("});".to_string());
        }
        AuthKind::AccessToken => {
            lines.push("using var client = new XClient(new XClientOptions".to_string());
            lines.push("{".to_string());
            lines.push(
                "    AccessToken = Environment.GetEnvironmentVariable(\"X_ACCESS_TOKEN\"),"
                    .to_string(),
            );
            lines.push("});".to_string());
        }
    }
    lines.push(String::new());

    let args_str = format_call_args(&pos_args, 4);
    if op.info.is_streaming {
        lines.push(format!(
            "await using var stream = await client.{}.{}({});",
            tag.pascal_name, op.csharp_method, args_str
        ));
        lines.push("await foreach (var item in stream)".to_string());
        lines.push("{".to_string());
        lines.push("    Console.WriteLine(item);".to_string());
        lines.push("}".to_string());
    } else if let Some(pages_method) = &op.csharp_pages_method {
        lines.push(format!(
            "await foreach (var page in client.{}.{}({}))",
            tag.pascal_name, pages_method, args_str
        ));
        lines.push("{".to_string());
        lines.push("    Console.WriteLine(page);".to_string());
        lines.push("}".to_string());
    } else {
        lines.push(format!(
            "var response = await client.{}.{}({});",
            tag.pascal_name, op.csharp_method, args_str
        ));
        lines.push("Console.WriteLine(response);".to_string());
    }

    lines.join("\n")
}

fn render_xurl_snippet(op: &OperationDocModel) -> String {
    let mut resolved_path = op.info.path.clone();
    for p in op.params_snake.iter().filter(|p| p.location == "path") {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        let text = json_scalar_to_query_string(&val);
        resolved_path = resolved_path.replace(&format!("{{{}}}", p.original_name), &text);
    }

    let mut query_pairs = Vec::new();
    for p in op
        .params_snake
        .iter()
        .filter(|p| p.required && p.location == "query")
    {
        let val = realistic_param_json(&p.original_name, &op.info.path, p.schema.as_ref());
        let encoded = json_scalar_to_query_string(&val)
            .replace(' ', "%20")
            .replace(':', "%3A");
        query_pairs.push(format!("{}={}", p.original_name, encoded));
    }

    let full_url = if query_pairs.is_empty() {
        resolved_path
    } else {
        format!("{resolved_path}?{}", query_pairs.join("&"))
    };
    let quoted_url = if full_url.contains('?') || full_url.contains('&') {
        format!("\"{full_url}\"")
    } else {
        full_url
    };

    let method_upper = op.info.method.to_uppercase();
    let mut parts = vec!["xurl".to_string()];
    if method_upper != "GET" {
        parts.push(format!("-X {method_upper}"));
    }
    if op.info.is_streaming {
        parts.push("-s".to_string());
    }
    parts.push(quoted_url);

    let include_body = op.body_required || (op.info.method != "get" && op.body_schema.is_some());
    if include_body
        && !op.body_is_binary
        && let Some(schema) = &op.body_schema
    {
        let body_val = realistic_body_json(schema, 0);
        if let Ok(compact) = serde_json::to_string(&body_val) {
            let single_quote_safe = compact.replace('\'', "'\\''");
            parts.push(format!("\\\n  -d '{single_quote_safe}'"));
        }
    }

    parts.join(" ")
}

fn render_language_reference_overview(
    lang: SdkDocLang,
    version: &str,
    tags: &[TagDocModel],
) -> String {
    let mut out = String::new();
    let lang_name = lang.display_name();
    let slug = lang.slug();
    let main_client_name = match lang {
        SdkDocLang::Python | SdkDocLang::TypeScript => "Client",
        SdkDocLang::Java | SdkDocLang::CSharp => "XClient",
    };

    out.push_str("---\n");
    out.push_str(&format!("title: \"{lang_name} XDK API Reference\"\n"));
    out.push_str("sidebarTitle: \"Overview\"\n");
    out.push_str(&format!(
        "description: \"Complete API reference for the official {lang_name} XDK ({pkg} v{version}) across all X API v2 resource clients.\"\n",
        pkg = lang.package_name()
    ));
    out.push_str("---\n\n");

    out.push_str(&format!(
        "The official **{lang_name} XDK** (`{pkg}`, `v{version}`) provides typed resource clients, authentication helpers, automatic pagination, and real-time streaming for the X API v2.\n\n",
        pkg = lang.package_name()
    ));

    out.push_str("<CardGroup cols={2}>\n");
    out.push_str(&format!(
        "  <Card title=\"{reg} Package\" icon=\"box\" href=\"{url}\">\n    Install `{pkg}` (`v{version}`) — requires {rt}.\n  </Card>\n",
        reg = lang.registry_name(),
        url = lang.registry_url(),
        pkg = lang.package_name(),
        rt = lang.runtime_requirement()
    ));
    out.push_str(&format!(
        "  <Card title=\"GitHub Repository\" icon=\"github\" href=\"{repo}\">\n    Source code, release notes, and issue tracker for `{pkg}`.\n  </Card>\n",
        repo = lang.repo_url(),
        pkg = lang.package_name()
    ));
    out.push_str("</CardGroup>\n\n");

    out.push_str("## Installation\n\n");
    let install_fence = match lang {
        SdkDocLang::Java => "kotlin",
        _ => "bash",
    };
    out.push_str(&format!(
        "```{install_fence}\n{}\n```\n\n",
        lang.install_command(version)
    ));

    out.push_str(&format!("## `{main_client_name}` Initialization\n\n"));
    match lang {
        SdkDocLang::Python => {
            out.push_str("```python\nimport os\nfrom xdk import Client\n\nclient = Client(bearer_token=os.environ[\"X_BEARER_TOKEN\"])\n```\n\n");
            out.push_str("<ResponseField name=\"bearer_token\" type=\"Optional[str]\">\n  App-only OAuth 2.0 Bearer Token for public read and search endpoints.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"access_token\" type=\"Optional[str]\">\n  OAuth 2.0 user-context access token for endpoints acting on behalf of a user.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"auth\" type=\"Optional[OAuth1]\">\n  Configured `OAuth1` instance for OAuth 1.0a HMAC-SHA1 user-context signing.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"base_url\" type=\"str\" default=\"https://api.x.com\">\n  Base URL for X API requests.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"timeout\" type=\"Optional[float]\">\n  Per-request HTTP timeout in seconds.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"max_retries\" type=\"int\" default=\"0\">\n  Maximum retry attempts for transient network or 5xx failures.\n</ResponseField>\n\n");
        }
        SdkDocLang::TypeScript => {
            out.push_str("```typescript\nimport { Client } from \"@xdevplatform/xdk\";\n\nconst client = new Client({ bearerToken: process.env.X_BEARER_TOKEN });\n```\n\n");
            out.push_str("<ResponseField name=\"bearerToken\" type=\"string\">\n  App-only OAuth 2.0 Bearer Token for public read and search endpoints.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"accessToken\" type=\"string\">\n  OAuth 2.0 user-context access token for endpoints acting on behalf of a user.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"oauth1\" type=\"OAuth1\">\n  Configured `OAuth1` signer for OAuth 1.0a user-context requests.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"baseUrl\" type=\"string\" default=\"https://api.x.com\">\n  Base URL for X API requests.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"timeout\" type=\"number\">\n  Request timeout in milliseconds.\n</ResponseField>\n\n");
        }
        SdkDocLang::Java => {
            out.push_str("```java\nimport com.x.xdk.XClient;\n\nXClient client = XClient.builder()\n    .bearerToken(System.getenv(\"X_BEARER_TOKEN\"))\n    .build();\n```\n\n");
            out.push_str("<ResponseField name=\"bearerToken(String)\" type=\"XClient.Builder\">\n  Configures an OAuth 2.0 Bearer Token for app-only requests.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"accessToken(String)\" type=\"XClient.Builder\">\n  Configures an OAuth 2.0 user-context access token.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"oauth2(OAuth2Pkce)\" type=\"XClient.Builder\">\n  Attaches an `OAuth2Pkce` manager for automatic token refresh.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"oauth1(OAuth1)\" type=\"XClient.Builder\">\n  Attaches an `OAuth1` HMAC-SHA1 signer for OAuth 1.0a user-context requests.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"baseUrl(String)\" type=\"XClient.Builder\" default=\"https://api.x.com\">\n  Overrides the X API base URL.\n</ResponseField>\n\n");
        }
        SdkDocLang::CSharp => {
            out.push_str("```csharp\nusing System;\nusing Xdk;\n\nusing var client = new XClient(new XClientOptions\n{\n    BearerToken = Environment.GetEnvironmentVariable(\"X_BEARER_TOKEN\"),\n});\n```\n\n");
            out.push_str("<ResponseField name=\"BearerToken\" type=\"string?\">\n  OAuth 2.0 Bearer Token for app-only endpoints.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"AccessToken\" type=\"string?\">\n  OAuth 2.0 user-context access token.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"OAuth2\" type=\"OAuth2Pkce?\">\n  `OAuth2Pkce` instance supporting PKCE code exchange and token refresh.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"OAuth1\" type=\"OAuth1?\">\n  `OAuth1` instance for OAuth 1.0a HMAC-SHA1 signing.\n</ResponseField>\n");
            out.push_str("<ResponseField name=\"BaseUrl\" type=\"string\" default=\"https://api.x.com\">\n  Base URL for X API requests (`XClient` implements `IDisposable`).\n</ResponseField>\n\n");
        }
    }

    out.push_str("## Resource Clients\n\n");
    out.push_str("| Resource | Accessor | Client Class | Operations |\n");
    out.push_str("| :--- | :--- | :--- | ---: |\n");
    for tag in tags {
        let accessor = tag_accessor(lang, tag);
        let client_cls = format!("{}Client", tag.pascal_name);
        out.push_str(&format!(
            "| [{}](/xdks/{slug}/reference/clients/{kebab}) | `{accessor}` | `{client_cls}` | {} |\n",
            tag.display_name,
            tag.operations.len(),
            kebab = tag.kebab_slug,
        ));
    }

    out
}

fn render_tag_client_mdx(lang: SdkDocLang, _version: &str, tag: &TagDocModel) -> String {
    let mut out = String::new();
    let lang_name = lang.display_name();
    let client_cls = format!("{}Client", tag.pascal_name);
    let accessor = tag_accessor(lang, tag);

    out.push_str("---\n");
    out.push_str(&format!(
        "title: {}\n",
        yaml_quote(&format!("{client_cls} ({lang_name} XDK)"))
    ));
    out.push_str(&format!(
        "sidebarTitle: {}\n",
        yaml_quote(&tag.display_name)
    ));
    out.push_str(&format!(
        "description: {}\n",
        yaml_quote(&format!(
            "{lang_name} XDK {client_cls} reference — {} methods for X API v2 {} endpoints.",
            tag.operations.len(),
            tag.display_name
        ))
    ));
    out.push_str("---\n\n");

    out.push_str(&format!(
        "Access **{}** endpoints via `{accessor}` (`{client_cls}`).\n\n",
        tag.display_name
    ));

    out.push_str("## Methods\n\n");
    out.push_str("| Method | Endpoint | Behavior | Summary |\n");
    out.push_str("| :--- | :--- | :--- | :--- |\n");
    for op in &tag.operations {
        let m_name = method_name_for_lang(lang, op);
        let anchor = method_anchor_slug(m_name);
        let behavior =
            if op.info.is_streaming || (lang == SdkDocLang::TypeScript && op.is_ts_stream_method) {
                "Streaming"
            } else if op.is_paginated {
                "Paginated"
            } else {
                "Standard"
            };
        let summary_text = op
            .info
            .summary
            .as_deref()
            .unwrap_or("")
            .replace('|', "\\|")
            .replace('\n', " ");
        let summary_escaped = escape_mdx_prose(&summary_text);
        out.push_str(&format!(
            "| [`{m_name}`](#{anchor}) | `{method} {path}` | {behavior} | {summary_escaped} |\n",
            method = op.info.method.to_uppercase(),
            path = op.info.path,
        ));
    }
    out.push('\n');

    for op in &tag.operations {
        let m_name = method_name_for_lang(lang, op);
        out.push_str(&format!("## `{m_name}`\n\n"));

        let method_upper = op.info.method.to_uppercase();
        let badge_color = match method_upper.as_str() {
            "GET" => "blue",
            "POST" => "green",
            "PUT" | "PATCH" => "orange",
            "DELETE" => "red",
            _ => "gray",
        };
        out.push_str(&format!(
            "<Badge color=\"{badge_color}\">{method_upper}</Badge> `{}`",
            op.info.path
        ));
        if op.info.is_streaming || (lang == SdkDocLang::TypeScript && op.is_ts_stream_method) {
            out.push_str(" <Badge color=\"green\">Streaming</Badge>");
        } else if op.is_paginated {
            out.push_str(" <Badge color=\"purple\">Paginated</Badge>");
        }
        out.push_str("\n\n");

        if let Some(summary) = &op.info.summary
            && !summary.trim().is_empty()
        {
            out.push_str(&format!("**{}**\n\n", escape_mdx_prose(summary.trim())));
        }
        if let Some(desc) = &op.info.description
            && !desc.trim().is_empty()
            && op.info.summary.as_deref().map(str::trim) != Some(desc.trim())
        {
            out.push_str(&format!("{}\n\n", escape_mdx_prose(desc.trim())));
        }

        let snippet = render_snippet_for_lang(lang, tag, op);
        out.push_str(&format!(
            "```{fence}\n{snippet}\n```\n\n",
            fence = lang.code_fence_lang()
        ));

        render_operation_parameters(&mut out, lang, tag, op);

        let ret_type = return_type_for_lang(lang, op);
        out.push_str(&format!("**Returns:** `{}`", ret_type.replace('`', "")));
        if lang == SdkDocLang::Java
            && let Some(pages_m) = &op.java_pages_method
        {
            out.push_str(&format!(
                " (use `{pages_m}(...)` for automatic `Paginator<...>` iteration)"
            ));
        } else if lang == SdkDocLang::CSharp
            && let Some(pages_m) = &op.csharp_pages_method
        {
            out.push_str(&format!(
                " (use `{pages_m}(...)` for `IAsyncEnumerable` page iteration)"
            ));
        }
        out.push_str("\n\n---\n\n");
    }

    out
}

fn render_operation_parameters(
    out: &mut String,
    lang: SdkDocLang,
    tag: &TagDocModel,
    op: &OperationDocModel,
) {
    let params = match lang {
        SdkDocLang::Python => &op.params_snake,
        SdkDocLang::TypeScript | SdkDocLang::Java | SdkDocLang::CSharp => &op.params_camel,
    };

    let mut required_rows: Vec<(String, String, String)> = Vec::new();
    let mut optional_rows: Vec<(String, String, String)> = Vec::new();

    for p in params {
        let is_req = p.location == "path" || p.required;
        let p_name = param_display_name(lang, p, is_req, &op.class_name);
        let p_type = param_type_for_lang(lang, p.schema.as_ref());
        let p_desc = p
            .description
            .as_deref()
            .map(escape_mdx_prose)
            .unwrap_or_else(|| format!("`{}` ({} parameter).", p.original_name, p.location));
        if is_req {
            required_rows.push((p_name, p_type, p_desc));
        } else {
            optional_rows.push((p_name, p_type, p_desc));
        }
    }

    if op.body_schema.is_some() || op.body_is_binary {
        let body_type = body_type_for_lang(lang, op);
        let body_name = match (lang, op.body_required) {
            (SdkDocLang::CSharp, false) => "options.Body".to_string(),
            (SdkDocLang::TypeScript | SdkDocLang::Java, false) => "options.body".to_string(),
            _ => "body".to_string(),
        };
        let body_desc = op
            .body_schema
            .as_ref()
            .and_then(|s| s.get("description").and_then(|d| d.as_str()))
            .map(escape_mdx_prose)
            .unwrap_or_else(|| "Request payload.".to_string());
        if op.body_required {
            required_rows.push((body_name, body_type, body_desc));
        } else {
            optional_rows.push((body_name, body_type, body_desc));
        }
    }

    if required_rows.is_empty() && optional_rows.is_empty() {
        return;
    }

    out.push_str("### Parameters\n\n");
    for (name, ty, desc) in &required_rows {
        out.push_str(&format!(
            "<ResponseField name={} type={} required>\n  {}\n</ResponseField>\n\n",
            jsx_attr(name),
            jsx_attr(ty),
            desc
        ));
    }

    if !optional_rows.is_empty() {
        let options_title = match lang {
            SdkDocLang::Python => format!("Optional keyword arguments ({})", optional_rows.len()),
            SdkDocLang::TypeScript => format!(
                "Optional parameters ({}Options — {})",
                op.class_name,
                optional_rows.len()
            ),
            SdkDocLang::Java => format!(
                "Optional parameters ({}Client.{}Options — {})",
                tag.pascal_name,
                op.class_name,
                optional_rows.len()
            ),
            SdkDocLang::CSharp => format!(
                "Optional parameters ({}Client.{}Options — {})",
                tag.pascal_name,
                op.class_name,
                optional_rows.len()
            ),
        };
        out.push_str(&format!(
            "<Expandable title={}>\n\n",
            jsx_attr(&options_title)
        ));
        for (name, ty, desc) in &optional_rows {
            out.push_str(&format!(
                "<ResponseField name={} type={}>\n  {}\n</ResponseField>\n\n",
                jsx_attr(name),
                jsx_attr(ty),
                desc
            ));
        }
        out.push_str("</Expandable>\n\n");
    }
}

fn render_root_xdks_llms_txt(config: &XdkConfig, tags: &[TagDocModel]) -> String {
    let mut out = String::new();
    out.push_str("# X Official SDKs (XDKs)\n\n");
    out.push_str(
        "> Official, OpenAPI-generated client libraries for the X API v2 in Python, TypeScript, Java, and C# (.NET).\n\n",
    );
    out.push_str("## Official Packages\n\n");
    for lang in SdkDocLang::ALL {
        let ver = config.get_version(lang.slug()).unwrap_or("0.1.0");
        out.push_str(&format!(
            "- **{}**: `{}` (`v{ver}`, {}) — `{}` — [Index](https://docs.x.com/xdks/{}/llms.txt)\n",
            lang.display_name(),
            lang.package_name(),
            lang.runtime_requirement(),
            lang.install_command(ver),
            lang.slug(),
        ));
    }
    out.push_str("\n## Overview & Guides\n\n");
    out.push_str("- [XDKs Overview](https://docs.x.com/xdks/overview.md): Side-by-side comparison, authentication matrix, pagination, and streaming across all 4 official SDKs.\n");
    for lang in SdkDocLang::ALL {
        let s = lang.slug();
        let n = lang.display_name();
        out.push_str(&format!(
            "- [{n} Overview](https://docs.x.com/xdks/{s}/overview.md) | [Install](https://docs.x.com/xdks/{s}/install.md) | [Quickstart](https://docs.x.com/xdks/{s}/quickstart.md) | [Auth](https://docs.x.com/xdks/{s}/authentication.md) | [Pagination](https://docs.x.com/xdks/{s}/pagination.md) | [Streaming](https://docs.x.com/xdks/{s}/streaming.md) | [API Reference](https://docs.x.com/xdks/{s}/reference/overview.md)\n"
        ));
    }
    out.push_str("\n## Resource Clients (Available in All 4 XDKs)\n\n");
    for tag in tags {
        out.push_str(&format!(
            "- **{}** (`{}Client`, {} operations): [Python](https://docs.x.com/xdks/python/reference/clients/{k}.md) | [TypeScript](https://docs.x.com/xdks/typescript/reference/clients/{k}.md) | [Java](https://docs.x.com/xdks/java/reference/clients/{k}.md) | [C#](https://docs.x.com/xdks/csharp/reference/clients/{k}.md)\n",
            tag.display_name,
            tag.pascal_name,
            tag.operations.len(),
            k = tag.kebab_slug,
        ));
    }
    out
}

fn render_language_llms_txt(lang: SdkDocLang, version: &str, tags: &[TagDocModel]) -> String {
    let mut out = String::new();
    let n = lang.display_name();
    let s = lang.slug();
    out.push_str(&format!(
        "# {n} XDK (`{pkg}` v{version})\n\n",
        pkg = lang.package_name()
    ));
    out.push_str(&format!(
        "> Official {n} SDK for the X API v2 ({rt}). Install with `{}`.\n\n",
        lang.install_command(version),
        rt = lang.runtime_requirement()
    ));
    out.push_str("## Guides\n\n");
    for (page, desc) in [
        (
            "overview",
            "Architecture, capabilities, and client overview",
        ),
        ("install", "Package installation and runtime requirements"),
        (
            "quickstart",
            "First authenticated X API v2 request in under 2 minutes",
        ),
        (
            "authentication",
            "Bearer Token, OAuth 2.0 PKCE, and OAuth 1.0a user-context setup",
        ),
        (
            "pagination",
            "Automatic cursor iteration across multi-page endpoints",
        ),
        (
            "streaming",
            "Real-time event streams with reconnection and lifecycle handling",
        ),
    ] {
        out.push_str(&format!(
            "- [{n} {page}](https://docs.x.com/xdks/{s}/{page}.md): {desc}\n"
        ));
    }
    out.push_str("\n## Client Reference\n\n");
    out.push_str(&format!(
        "- [Reference Overview](https://docs.x.com/xdks/{s}/reference/overview.md): Main client options and resource client directory\n"
    ));
    for tag in tags {
        out.push_str(&format!(
            "- [`{}Client` ({})](https://docs.x.com/xdks/{s}/reference/clients/{}.md): {} methods via `{}`\n",
            tag.pascal_name,
            tag.display_name,
            tag.kebab_slug,
            tag.operations.len(),
            tag_accessor(lang, tag),
        ));
    }
    out
}

fn create_missing_endpoint_stubs(output_dir: &Path, tags: &[TagDocModel]) -> Result<Vec<PathBuf>> {
    let mut existing_ops = BTreeSet::new();
    collect_existing_openapi_frontmatter(output_dir, &mut existing_ops)?;

    let mut created = Vec::new();
    for tag in tags {
        for op in &tag.operations {
            let key = (op.info.method.to_lowercase(), op.info.path.clone());
            if existing_ops.contains(&key) {
                continue;
            }
            let slug = Casing::Kebab.convert_words(&op.op_words);
            let dir = output_dir.join("x-api").join(&tag.kebab_slug);
            fs::create_dir_all(&dir)?;
            let mut candidate = dir.join(format!("{slug}.mdx"));
            if candidate.exists() {
                candidate = dir.join(format!("{}-{slug}.mdx", op.info.method.to_lowercase()));
            }
            let stub = format!(
                "---\nopenapi: {} {}\n---\n",
                op.info.method.to_lowercase(),
                op.info.path
            );
            fs::write(&candidate, stub)?;
            existing_ops.insert(key);
            created.push(candidate);
        }
    }
    Ok(created)
}

fn collect_existing_openapi_frontmatter(
    dir: &Path,
    found: &mut BTreeSet<(String, String)>,
) -> Result<()> {
    if !dir.exists() {
        return Ok(());
    }
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        if path.is_dir() {
            let name = entry.file_name();
            let name_s = name.to_string_lossy();
            if name_s.starts_with('.') || name_s == "node_modules" || name_s == "xdks" {
                continue;
            }
            collect_existing_openapi_frontmatter(&path, found)?;
        } else if path.extension().and_then(|e| e.to_str()) == Some("mdx")
            && let Ok(content) = fs::read_to_string(&path)
            && let Some(rest) = content
                .strip_prefix("---\n")
                .or_else(|| content.strip_prefix("---\r\n"))
            && let Some((frontmatter, _)) = rest.split_once("\n---")
        {
            for line in frontmatter.lines() {
                if let Some(val) = line.trim().strip_prefix("openapi:") {
                    let parts: Vec<&str> = val
                        .trim()
                        .trim_matches('"')
                        .trim_matches('\'')
                        .split_whitespace()
                        .collect();
                    if parts.len() == 2 {
                        found.insert((parts[0].to_lowercase(), parts[1].to_string()));
                    } else if parts.len() == 3 {
                        found.insert((parts[1].to_lowercase(), parts[2].to_string()));
                    }
                }
            }
        }
    }
    Ok(())
}

fn update_docs_json(docs_json_path: &Path, tags: &[TagDocModel]) -> Result<()> {
    let raw = fs::read_to_string(docs_json_path)?;
    let mut doc: Json = serde_json::from_str(&raw).map_err(|e| {
        SdkGeneratorError::FrameworkError(format!(
            "Failed to parse {}: {e}",
            docs_json_path.display()
        ))
    })?;

    let root_obj = doc.as_object_mut().ok_or_else(|| {
        SdkGeneratorError::FrameworkError("docs.json root must be a JSON object".to_string())
    })?;

    // 1. Configure top-level `api` block for OpenAPI + XDK code samples overlay.
    let api_block = json!({
        "openapi": {
            "source": "openapi.json",
            "overlays": ["overlays/xdk-code-samples.json"]
        },
        "examples": {
            "languages": ["curl", "python", "typescript", "java", "csharp", "bash"],
            "defaults": "required"
        }
    });
    root_obj.insert("api".to_string(), api_block);

    // 2. Build the `"XDKs"` product entry with Overview + all 4 language tabs.
    let xdks_product = build_xdks_product_nav(tags);

    if let Some(products) = root_obj
        .get_mut("navigation")
        .and_then(|n| n.get_mut("products"))
        .and_then(|p| p.as_array_mut())
    {
        // Remove per-language hidden SDK products superseded by the unified "XDKs" product.
        products.retain(|p| {
            !matches!(
                p.get("product").and_then(|v| v.as_str()),
                Some("Python XDK" | "TypeScript XDK" | "Java XDK" | "C# XDK")
            )
        });

        // Update X API -> Tools & Libraries -> SDKs (XDKs) entry cards if present.
        update_x_api_tools_xdks_nav(products);

        if let Some(existing_idx) = products
            .iter()
            .position(|p| p.get("product").and_then(|v| v.as_str()) == Some("XDKs"))
        {
            products[existing_idx] = xdks_product;
        } else {
            // Insert right after "X API" so SDKs are immediately discoverable in the product switcher.
            let insert_at = products
                .iter()
                .position(|p| p.get("product").and_then(|v| v.as_str()) == Some("X API"))
                .map(|i| i + 1)
                .unwrap_or(products.len());
            products.insert(insert_at, xdks_product);
        }
    }

    // 3. Ensure redirects from older SDK reference URLs to the new client reference URLs.
    ensure_xdks_redirects(root_obj, tags);

    let mut formatted = serde_json::to_string_pretty(&doc).map_err(|e| {
        SdkGeneratorError::FrameworkError(format!("Failed to serialize docs.json: {e}"))
    })?;
    formatted.push('\n');
    fs::write(docs_json_path, formatted)?;
    Ok(())
}

fn build_xdks_product_nav(tags: &[TagDocModel]) -> Json {
    let mut tabs = vec![json!({
        "tab": "Overview",
        "pages": [
            "xdks/overview"
        ]
    })];

    for lang in SdkDocLang::ALL {
        let s = lang.slug();
        let mut ref_pages = vec![Json::String(format!("xdks/{s}/reference/overview"))];
        for tag in tags {
            ref_pages.push(Json::String(format!(
                "xdks/{s}/reference/clients/{}",
                tag.kebab_slug
            )));
        }
        tabs.push(json!({
            "tab": lang.display_name(),
            "groups": [
                {
                    "group": "Guides",
                    "pages": [
                        format!("xdks/{s}/overview"),
                        format!("xdks/{s}/install"),
                        format!("xdks/{s}/quickstart"),
                        format!("xdks/{s}/authentication"),
                        format!("xdks/{s}/pagination"),
                        format!("xdks/{s}/streaming")
                    ]
                },
                {
                    "group": "Client Reference",
                    "pages": ref_pages
                }
            ]
        }));
    }

    json!({
        "product": "XDKs",
        "description": "Official Python, TypeScript, Java, and C# SDKs",
        "icon": "cubes",
        "tabs": tabs
    })
}

fn update_x_api_tools_xdks_nav(products: &mut [Json]) {
    for prod in products.iter_mut() {
        if prod.get("product").and_then(|v| v.as_str()) != Some("X API") {
            continue;
        }
        if let Some(tabs) = prod.get_mut("tabs").and_then(|t| t.as_array_mut()) {
            for tab in tabs.iter_mut() {
                if let Some(groups) = tab.get_mut("groups").and_then(|g| g.as_array_mut()) {
                    replace_sdk_subgroup_in_groups(groups);
                }
            }
        }
    }
}

fn replace_sdk_subgroup_in_groups(groups: &mut [Json]) {
    for g in groups.iter_mut() {
        let Some(pages) = g.get_mut("pages").and_then(|p| p.as_array_mut()) else {
            continue;
        };
        for item in pages.iter_mut() {
            let is_tools_group = item
                .get("group")
                .and_then(|v| v.as_str())
                .is_some_and(|name| name == "Tools and Libraries" || name == "Tools & Libraries");
            if is_tools_group
                && let Some(tool_pages) = item.get_mut("pages").and_then(|p| p.as_array_mut())
            {
                let sdks_group = json!({
                    "group": "SDKs (XDKs)",
                    "pages": [
                        "tools/python-xdk",
                        "tools/typescript-xdk",
                        "tools/java-xdk",
                        "tools/csharp-xdk"
                    ]
                });
                if let Some(pos) = tool_pages.iter().position(|p| {
                    p.get("group")
                        .and_then(|v| v.as_str())
                        .is_some_and(|n| n.contains("SDK") || n.contains("XDK"))
                }) {
                    tool_pages[pos] = sdks_group;
                }
            }
        }
    }
}

fn ensure_xdks_redirects(root_obj: &mut JsonMap<String, Json>, tags: &[TagDocModel]) {
    let mut desired: Vec<(String, String)> = vec![
        (
            "/xdks/python/reference/index".to_string(),
            "/xdks/python/reference/overview".to_string(),
        ),
        (
            "/xdks/python/reference/modules".to_string(),
            "/xdks/python/reference/overview".to_string(),
        ),
        (
            "/xdks/python/reference/xdk".to_string(),
            "/xdks/python/reference/overview".to_string(),
        ),
        (
            "/xdks/python/reference/xdk.client".to_string(),
            "/xdks/python/reference/overview".to_string(),
        ),
        (
            "/xdks/python/reference/xdk.schemas".to_string(),
            "/xdks/python/reference/overview".to_string(),
        ),
        (
            "/xdks/python/reference/xdk.paginator".to_string(),
            "/xdks/python/pagination".to_string(),
        ),
        (
            "/xdks/python/reference/xdk.streaming".to_string(),
            "/xdks/python/streaming".to_string(),
        ),
        (
            "/xdks/python/reference/xdk.oauth1_auth".to_string(),
            "/xdks/python/authentication".to_string(),
        ),
        (
            "/xdks/python/reference/xdk.oauth2_auth".to_string(),
            "/xdks/python/authentication".to_string(),
        ),
        (
            "/xdks/typescript/reference/index".to_string(),
            "/xdks/typescript/reference/overview".to_string(),
        ),
        (
            "/xdks/typescript/reference/modules".to_string(),
            "/xdks/typescript/reference/overview".to_string(),
        ),
        (
            "/xdks/typescript/reference/classes/Client".to_string(),
            "/xdks/typescript/reference/overview".to_string(),
        ),
        (
            "/xdks/typescript/reference/classes/Paginator".to_string(),
            "/xdks/typescript/pagination".to_string(),
        ),
        (
            "/xdks/typescript/reference/classes/EventDrivenStream".to_string(),
            "/xdks/typescript/streaming".to_string(),
        ),
        (
            "/xdks/typescript/reference/classes/OAuth1".to_string(),
            "/xdks/typescript/authentication".to_string(),
        ),
        (
            "/xdks/typescript/reference/classes/OAuth2".to_string(),
            "/xdks/typescript/authentication".to_string(),
        ),
        (
            "/xdks/typescript/reference/interfaces/:slug*".to_string(),
            "/xdks/typescript/reference/overview".to_string(),
        ),
        (
            "/xdks/typescript/reference/functions/:slug*".to_string(),
            "/xdks/typescript/reference/overview".to_string(),
        ),
        (
            "/xdks/typescript/reference/variables/:slug*".to_string(),
            "/xdks/typescript/reference/overview".to_string(),
        ),
    ];

    for tag in tags {
        let py_dest = format!("/xdks/python/reference/clients/{}", tag.kebab_slug);
        desired.push((
            format!("/xdks/python/reference/xdk.{}", tag.snake_name),
            py_dest.clone(),
        ));
        desired.push((
            format!("/xdks/python/reference/xdk.{}.client", tag.snake_name),
            py_dest.clone(),
        ));
        desired.push((
            format!("/xdks/python/reference/xdk.{}.models", tag.snake_name),
            py_dest,
        ));

        let ts_dest = format!("/xdks/typescript/reference/clients/{}", tag.kebab_slug);
        desired.push((
            format!(
                "/xdks/typescript/reference/classes/{}Client",
                tag.pascal_name
            ),
            ts_dest,
        ));
    }

    let redirects_val = root_obj
        .entry("redirects".to_string())
        .or_insert_with(|| Json::Array(Vec::new()));
    let Some(redirects) = redirects_val.as_array_mut() else {
        return;
    };

    // Remove legacy redirects that shadowed live XDK pages before `/xdks/overview` existed.
    let live_xdks_routes = [
        "/xdks/overview",
        "/xdks/python/overview",
        "/xdks/typescript/overview",
        "/xdks/java/overview",
        "/xdks/csharp/overview",
    ];
    redirects.retain(|r| {
        r.get("source")
            .and_then(|v| v.as_str())
            .is_none_or(|src| !live_xdks_routes.contains(&src))
    });

    desired.insert(0, ("/xdks".to_string(), "/xdks/overview".to_string()));

    for (source, destination) in desired {
        if let Some(existing) = redirects
            .iter_mut()
            .find(|r| r.get("source").and_then(|v| v.as_str()) == Some(source.as_str()))
        {
            if let Some(obj) = existing.as_object_mut() {
                obj.insert("destination".to_string(), Json::String(destination));
            }
        } else {
            redirects.push(json!({
                "source": source,
                "destination": destination
            }));
        }
    }
}

fn sync_java_version_in_guides(output_dir: &Path, java_version: &str) -> Result<()> {
    for rel in [
        "xdks/java/install.mdx",
        "xdks/java/overview.mdx",
        "tools/java-xdk.mdx",
        "xdks/overview.mdx",
    ] {
        let path = output_dir.join(rel);
        if !path.exists() {
            continue;
        }
        let original = fs::read_to_string(&path)?;
        let updated = replace_maven_and_gradle_version(&original, java_version);
        if updated != original {
            fs::write(&path, updated)?;
        }
    }
    Ok(())
}

fn replace_maven_and_gradle_version(input: &str, java_version: &str) -> String {
    let mut out = input.to_string();
    // Sync `com.x:xdk:<ver>` occurrences.
    let prefix = "com.x:xdk:";
    let mut cursor = 0;
    while let Some(rel_idx) = out[cursor..].find(prefix) {
        let ver_start = cursor + rel_idx + prefix.len();
        let ver_end = out[ver_start..]
            .find(|c: char| !c.is_ascii_alphanumeric() && c != '.' && c != '-')
            .map(|len| ver_start + len)
            .unwrap_or(out.len());
        if ver_end > ver_start {
            out.replace_range(ver_start..ver_end, java_version);
            cursor = ver_start + java_version.len();
        } else {
            cursor = ver_start;
        }
    }
    // Sync `<artifactId>xdk</artifactId>\n  <version>...</version>` blocks.
    let marker = "<artifactId>xdk</artifactId>";
    let mut m_cursor = 0;
    while let Some(rel_idx) = out[m_cursor..].find(marker) {
        let after_marker = m_cursor + rel_idx + marker.len();
        if let Some(v_rel) = out[after_marker..].find("<version>")
            && v_rel < 40
        {
            let v_start = after_marker + v_rel + "<version>".len();
            if let Some(v_end_rel) = out[v_start..].find("</version>") {
                let v_end = v_start + v_end_rel;
                out.replace_range(v_start..v_end, java_version);
                m_cursor = v_start + java_version.len();
                continue;
            }
        }
        m_cursor = after_marker;
    }
    out
}

/// Escapes `{`, `}`, `<`, `>` outside inline backtick spans so OpenAPI descriptions
/// with path placeholders like `{id}` or `<url>` compile cleanly in Mintlify MDX.
pub fn escape_mdx_prose(text: &str) -> String {
    let normalized = text.replace("\r\n", "\n");
    let mut out = String::with_capacity(normalized.len() + 16);
    let mut in_code = false;

    for ch in normalized.chars() {
        if ch == '`' {
            in_code = !in_code;
            out.push(ch);
        } else if in_code {
            out.push(ch);
        } else {
            match ch {
                '{' => out.push_str("\\{"),
                '}' => out.push_str("\\}"),
                '<' => out.push_str("&lt;"),
                '>' => out.push_str("&gt;"),
                _ => out.push(ch),
            }
        }
    }
    out
}

fn yaml_quote(s: &str) -> String {
    serde_json::to_string(s).unwrap_or_else(|_| "\"\"".to_string())
}

fn jsx_attr(s: &str) -> String {
    if !s.contains('"') && !s.contains('\\') {
        format!("\"{s}\"")
    } else {
        let js_str = serde_json::to_string(s).unwrap_or_else(|_| "\"\"".to_string());
        format!("{{{js_str}}}")
    }
}

fn tag_accessor(lang: SdkDocLang, tag: &TagDocModel) -> String {
    match lang {
        SdkDocLang::Python => format!("client.{}", tag.snake_name),
        SdkDocLang::TypeScript => format!("client.{}", tag.camel_name),
        SdkDocLang::Java => format!("client.{}()", tag.camel_name),
        SdkDocLang::CSharp => format!("client.{}", tag.pascal_name),
    }
}

fn method_name_for_lang(lang: SdkDocLang, op: &OperationDocModel) -> &str {
    match lang {
        SdkDocLang::Python => &op.py_method,
        SdkDocLang::TypeScript => &op.ts_method,
        SdkDocLang::Java => &op.java_method,
        SdkDocLang::CSharp => &op.csharp_method,
    }
}

fn method_anchor_slug(method_name: &str) -> String {
    method_name
        .chars()
        .filter(|c| c.is_ascii_alphanumeric() || *c == '-' || *c == '_')
        .collect::<String>()
        .to_lowercase()
}

fn param_display_name(
    lang: SdkDocLang,
    p: &ParameterInfo,
    is_required: bool,
    op_class_name: &str,
) -> String {
    match (lang, is_required) {
        (SdkDocLang::Python, _) => py_param_ident(&p.variable_name),
        (SdkDocLang::TypeScript, true) => p.variable_name.clone(),
        (SdkDocLang::TypeScript, false) => format!("options.{}", p.variable_name),
        (SdkDocLang::Java, true) => java_field_ident(&p.variable_name),
        (SdkDocLang::Java, false) => format!("options.{}", java_field_ident(&p.variable_name)),
        (SdkDocLang::CSharp, true) => csharp_var_ident(&p.variable_name),
        (SdkDocLang::CSharp, false) => {
            let options_cls = format!("{op_class_name}Options");
            format!(
                "options.{}",
                csharp_prop_ident(&p.original_name, &options_cls)
            )
        }
    }
}

fn param_type_for_lang(
    lang: SdkDocLang,
    schema: Option<&openapi::RefOrValue<openapi::Schema>>,
) -> String {
    let Some(schema) = schema else {
        return match lang {
            SdkDocLang::Python => "Any".to_string(),
            SdkDocLang::TypeScript => "unknown".to_string(),
            SdkDocLang::Java => "Object".to_string(),
            SdkDocLang::CSharp => "object".to_string(),
        };
    };
    let Ok(json_schema) = serde_json::to_value(schema) else {
        return "string".to_string();
    };
    match lang {
        SdkDocLang::Python => py_type_of(&json_schema, "schemas."),
        SdkDocLang::TypeScript => ts_type_of(&json_schema, "Schemas."),
        SdkDocLang::Java => java_type_of(&json_schema, "Schemas."),
        SdkDocLang::CSharp => csharp_type_of(&json_schema, "", false),
    }
}

fn body_type_for_lang(lang: SdkDocLang, op: &OperationDocModel) -> String {
    if op.body_is_binary {
        return match lang {
            SdkDocLang::Python => "bytes".to_string(),
            SdkDocLang::TypeScript => "Uint8Array | ArrayBuffer".to_string(),
            SdkDocLang::Java => "byte[]".to_string(),
            SdkDocLang::CSharp => "byte[]".to_string(),
        };
    }
    match (lang, &op.body_schema) {
        (SdkDocLang::Python, _) if op.info.has_request_model => {
            format!("{}Request", op.class_name)
        }
        (SdkDocLang::Python, Some(s)) => py_type_of(s, "schemas."),
        (SdkDocLang::TypeScript, _) if op.info.has_request_model => {
            format!("{}Request", op.class_name)
        }
        (SdkDocLang::TypeScript, Some(s)) => ts_type_of(s, "Schemas."),
        (SdkDocLang::Java, Some(s)) => java_type_of(s, "Schemas."),
        (SdkDocLang::CSharp, Some(s)) => csharp_type_of(s, "", false),
        _ => "object".to_string(),
    }
}

fn return_type_for_lang(lang: SdkDocLang, op: &OperationDocModel) -> String {
    match lang {
        SdkDocLang::Python => {
            let inner = if op.response_is_binary {
                "bytes".to_string()
            } else if op.info.has_json_response {
                format!("{}Response", op.class_name)
            } else {
                "Dict[str, Any]".to_string()
            };
            if op.info.is_streaming {
                format!("Generator[{inner}, None, None]")
            } else if op.is_paginated {
                format!("Iterator[{inner}]")
            } else {
                inner
            }
        }
        SdkDocLang::TypeScript => {
            if op.is_ts_stream_method {
                "Promise<EventDrivenStream>".to_string()
            } else if op.response_is_binary {
                "Promise<ArrayBuffer>".to_string()
            } else if op.info.has_json_response {
                format!("Promise<{}Response>", op.class_name)
            } else {
                "Promise<Record<string, unknown>>".to_string()
            }
        }
        SdkDocLang::Java => {
            let inner = if op.response_is_binary {
                "byte[]".to_string()
            } else if let Some(s) = &op.response_schema {
                java_type_of(s, "Schemas.")
            } else {
                "JsonNode".to_string()
            };
            if op.info.is_streaming {
                format!("EventStream<{inner}>")
            } else {
                inner
            }
        }
        SdkDocLang::CSharp => {
            let inner = if op.response_is_binary {
                "byte[]".to_string()
            } else if let Some(s) = &op.response_schema {
                csharp_type_of(s, "", false)
            } else {
                "JsonElement".to_string()
            };
            if op.info.is_streaming {
                format!("Task<EventStream<{inner}>>")
            } else {
                format!("Task<{inner}>")
            }
        }
    }
}

fn py_param_ident(name: &str) -> String {
    let ident = py_field_ident(name);
    if ident.is_empty() {
        "param".to_string()
    } else {
        ident
    }
}

fn format_call_args(args: &[String], indent: usize) -> String {
    if args.is_empty() {
        return String::new();
    }
    let single_line = args.join(", ");
    if single_line.len() <= 68 && !single_line.contains('\n') {
        single_line
    } else {
        let pad = " ".repeat(indent);
        let indented: Vec<String> = args
            .iter()
            .map(|a| format!("{pad}{}", a.replace('\n', &format!("\n{pad}"))))
            .collect();
        format!("\n{}\n", indented.join(",\n"))
    }
}

fn realistic_param_json(
    name: &str,
    op_path: &str,
    schema: Option<&openapi::RefOrValue<openapi::Schema>>,
) -> Json {
    let schema_json = schema.and_then(|s| serde_json::to_value(s).ok());
    realistic_value_for_field(name, op_path, schema_json.as_ref(), 0)
}

fn realistic_value_for_field(
    name: &str,
    op_path: &str,
    schema: Option<&Json>,
    depth: usize,
) -> Json {
    if depth > 4 {
        return Json::String("example".to_string());
    }
    if let Some(s) = schema {
        if let Some(vals) = s.get("enum").and_then(|v| v.as_array())
            && let Some(first) = vals.first()
        {
            return first.clone();
        }
        match s.get("type").and_then(|t| t.as_str()) {
            Some("array") => {
                let item_schema = s.get("items");
                let singular = name.strip_suffix('s').unwrap_or(name);
                return Json::Array(vec![realistic_value_for_field(
                    singular,
                    op_path,
                    item_schema,
                    depth + 1,
                )]);
            }
            Some("integer") | Some("number") => {
                return match name {
                    "max_results" | "limit" => json!(10),
                    "woeid" => json!(1),
                    _ => json!(1),
                };
            }
            Some("boolean") => return json!(true),
            Some("object") => return realistic_body_json(s, depth + 1),
            _ => {}
        }
    }

    let lower = name.to_lowercase();
    let sample = match lower.as_str() {
        "username" => "XDevelopers",
        "query" => "from:XDevelopers",
        "granularity" => "day",
        "start_time" => "2026-01-01T00:00:00Z",
        "end_time" => "2026-01-02T00:00:00Z",
        "text" => "Hello from XDK!",
        "value" => "from:XDevelopers",
        "name" => "My List",
        "url" => "https://example.com/webhook",
        "user_id" | "source_user_id" | "target_user_id" | "participant_id" => "2244994945",
        "tweet_id" | "source_tweet_id" | "since_id" | "until_id" => "1895000000000000000",
        "list_id" => "1450000000000000000",
        "space_id" => "1YqKDqWLPPlGV",
        "media_id" | "media_key" => "3_1895000000000000000",
        "dm_conversation_id" | "conversation_id" => "1500000000000000000",
        "event_id" | "dm_event_id" => "1600000000000000000",
        "webhook_id" => "1234567890",
        "id" => {
            if op_path.contains("/users") {
                "2244994945"
            } else if op_path.contains("/lists") {
                "1450000000000000000"
            } else if op_path.contains("/spaces") {
                "1YqKDqWLPPlGV"
            } else if op_path.contains("/webhooks") {
                "1234567890"
            } else {
                "1895000000000000000"
            }
        }
        other if other.ends_with("_id") => "1895000000000000000",
        _ => "example",
    };
    Json::String(sample.to_string())
}

fn realistic_body_json(schema: &Json, depth: usize) -> Json {
    if depth > 4 {
        return json!({});
    }
    if let Some(props) = schema.get("properties").and_then(|v| v.as_object())
        && !props.is_empty()
    {
        let required: Vec<&str> = schema
            .get("required")
            .and_then(|v| v.as_array())
            .map(|arr| arr.iter().filter_map(|x| x.as_str()).collect())
            .unwrap_or_default();

        let mut map = JsonMap::new();
        for req_key in &required {
            if let Some(prop_schema) = props.get(*req_key) {
                map.insert(
                    (*req_key).to_string(),
                    realistic_value_for_field(req_key, "", Some(prop_schema), depth + 1),
                );
            }
        }

        if map.is_empty() {
            let preferred = [
                "text",
                "tweet_id",
                "target_user_id",
                "user_id",
                "list_id",
                "name",
                "url",
                "value",
                "hidden",
                "pinned",
            ];
            let chosen = preferred
                .iter()
                .copied()
                .find(|k| props.contains_key(*k))
                .or_else(|| props.keys().min().map(String::as_str));
            if let Some(key) = chosen
                && let Some(prop_schema) = props.get(key)
            {
                map.insert(
                    key.to_string(),
                    realistic_value_for_field(key, "", Some(prop_schema), depth + 1),
                );
            }
        }
        return Json::Object(map);
    }

    for key in ["oneOf", "anyOf", "allOf"] {
        if let Some(variants) = schema.get(key).and_then(|v| v.as_array())
            && let Some(first) = variants.first()
        {
            return realistic_body_json(first, depth + 1);
        }
    }

    json!({})
}

fn render_python_model_expr(model_name: &str, schema: &Json, body_val: &Json) -> String {
    let has_props = schema
        .get("properties")
        .and_then(|v| v.as_object())
        .is_some_and(|p| !p.is_empty());
    if let Some(obj) = body_val.as_object() {
        if obj.is_empty() {
            return format!("{model_name}()");
        }
        if has_props {
            let kwargs: Vec<String> = obj
                .iter()
                .map(|(k, v)| format!("{}={}", py_field_ident(k), json_to_python(v)))
                .collect();
            return format!("{model_name}({})", kwargs.join(", "));
        }
        return format!("{model_name}({})", json_to_python(body_val));
    }
    format!("{model_name}({})", json_to_python(body_val))
}

fn render_java_body_expr(schema: &Json, imports: &mut BTreeSet<String>) -> String {
    let java_ty = java_type_of(schema, "Schemas.");
    let body_val = realistic_body_json(schema, 0);
    if java_ty.starts_with("Schemas.") {
        imports.insert("com.x.xdk.Schemas".to_string());
        let mut expr = format!("new {java_ty}()");
        if let (Some(props), Some(obj)) = (
            schema.get("properties").and_then(|v| v.as_object()),
            body_val.as_object(),
        ) {
            for (k, v) in obj {
                let prop_ty = props
                    .get(k)
                    .map(|ps| java_type_of(ps, "Schemas."))
                    .unwrap_or_default();
                if matches!(
                    prop_ty.as_str(),
                    "String"
                        | "Boolean"
                        | "boolean"
                        | "Integer"
                        | "int"
                        | "Long"
                        | "long"
                        | "Double"
                        | "double"
                ) || prop_ty.starts_with("List<String>")
                {
                    let setter = java_field_ident(&snake_to_camel(k));
                    let arg = json_to_java(v, imports);
                    expr.push_str(&format!(".{setter}({arg})"));
                }
            }
        }
        return expr;
    }
    if java_ty == "JsonNode" {
        imports.insert("com.fasterxml.jackson.databind.ObjectMapper".to_string());
        let compact = serde_json::to_string(&body_val).unwrap_or_else(|_| "{}".to_string());
        let quoted = serde_json::to_string(&compact).unwrap_or_else(|_| "\"{}\"".to_string());
        return format!("new ObjectMapper().readTree({quoted})");
    }
    json_to_java(&body_val, imports)
}

fn render_csharp_body_expr(schema: &Json, usings: &mut BTreeSet<String>) -> String {
    let cs_probe = csharp_type_of(schema, "Schemas.", false);
    let body_val = realistic_body_json(schema, 0);
    if let Some(model_cls) = cs_probe.strip_prefix("Schemas.") {
        usings.insert("Xdk.Models".to_string());
        if let (Some(props), Some(obj)) = (
            schema.get("properties").and_then(|v| v.as_object()),
            body_val.as_object(),
        ) {
            let mut inits = Vec::new();
            for (k, v) in obj {
                let prop_ty = props
                    .get(k)
                    .map(|ps| csharp_type_of(ps, "", false))
                    .unwrap_or_default();
                if matches!(
                    prop_ty.as_str(),
                    "string" | "bool" | "int" | "long" | "double" | "List<string>"
                ) {
                    let prop_name = csharp_prop_ident(k, model_cls);
                    let arg = json_to_csharp(v, usings);
                    inits.push(format!("{prop_name} = {arg}"));
                }
            }
            if !inits.is_empty() {
                return format!("new {model_cls} {{ {} }}", inits.join(", "));
            }
        }
        return format!("new {model_cls}()");
    }
    if cs_probe == "JsonElement" {
        usings.insert("System.Text.Json".to_string());
        let compact = serde_json::to_string(&body_val).unwrap_or_else(|_| "{}".to_string());
        let quoted = serde_json::to_string(&compact).unwrap_or_else(|_| "\"{}\"".to_string());
        return format!("JsonDocument.Parse({quoted}).RootElement");
    }
    json_to_csharp(&body_val, usings)
}

fn json_to_python(val: &Json) -> String {
    match val {
        Json::Null => "None".to_string(),
        Json::Bool(true) => "True".to_string(),
        Json::Bool(false) => "False".to_string(),
        Json::Number(n) => n.to_string(),
        Json::String(s) => serde_json::to_string(s).unwrap_or_else(|_| "\"\"".to_string()),
        Json::Array(arr) => {
            let items: Vec<String> = arr.iter().map(json_to_python).collect();
            format!("[{}]", items.join(", "))
        }
        Json::Object(map) => {
            let entries: Vec<String> = map
                .iter()
                .map(|(k, v)| {
                    let key_q = serde_json::to_string(k).unwrap_or_else(|_| "\"\"".to_string());
                    format!("{key_q}: {}", json_to_python(v))
                })
                .collect();
            format!("{{{}}}", entries.join(", "))
        }
    }
}

fn json_to_ts(val: &Json) -> String {
    match val {
        Json::Null => "null".to_string(),
        Json::Bool(b) => b.to_string(),
        Json::Number(n) => n.to_string(),
        Json::String(s) => serde_json::to_string(s).unwrap_or_else(|_| "\"\"".to_string()),
        Json::Array(arr) => {
            let items: Vec<String> = arr.iter().map(json_to_ts).collect();
            format!("[{}]", items.join(", "))
        }
        Json::Object(map) => {
            if map.is_empty() {
                return "{}".to_string();
            }
            let entries: Vec<String> = map
                .iter()
                .map(|(k, v)| {
                    let camel = snake_to_camel(k);
                    let valid_ident = !camel.is_empty()
                        && camel
                            .chars()
                            .all(|c| c.is_ascii_alphanumeric() || c == '_' || c == '$')
                        && !camel.chars().next().unwrap().is_ascii_digit();
                    let key_repr = if valid_ident && camel == *k {
                        k.clone()
                    } else {
                        serde_json::to_string(k).unwrap_or_else(|_| "\"\"".to_string())
                    };
                    format!("{key_repr}: {}", json_to_ts(v))
                })
                .collect();
            format!("{{ {} }}", entries.join(", "))
        }
    }
}

fn json_to_java(val: &Json, imports: &mut BTreeSet<String>) -> String {
    match val {
        Json::Null => "null".to_string(),
        Json::Bool(b) => b.to_string(),
        Json::Number(n) => n.to_string(),
        Json::String(s) => serde_json::to_string(s).unwrap_or_else(|_| "\"\"".to_string()),
        Json::Array(arr) => {
            imports.insert("java.util.List".to_string());
            let items: Vec<String> = arr.iter().map(|v| json_to_java(v, imports)).collect();
            format!("List.of({})", items.join(", "))
        }
        Json::Object(map) => {
            imports.insert("java.util.Map".to_string());
            let entries: Vec<String> = map
                .iter()
                .take(5)
                .map(|(k, v)| {
                    let kq = serde_json::to_string(k).unwrap_or_else(|_| "\"\"".to_string());
                    format!("{kq}, {}", json_to_java(v, imports))
                })
                .collect();
            format!("Map.of({})", entries.join(", "))
        }
    }
}

fn json_to_csharp(val: &Json, usings: &mut BTreeSet<String>) -> String {
    match val {
        Json::Null => "null".to_string(),
        Json::Bool(b) => b.to_string(),
        Json::Number(n) => n.to_string(),
        Json::String(s) => serde_json::to_string(s).unwrap_or_else(|_| "\"\"".to_string()),
        Json::Array(arr) => {
            usings.insert("System.Collections.Generic".to_string());
            let elem_ty = match arr.first() {
                Some(Json::String(_)) | None => "string",
                Some(Json::Bool(_)) => "bool",
                Some(Json::Number(_)) => "int",
                _ => "object",
            };
            let items: Vec<String> = arr.iter().map(|v| json_to_csharp(v, usings)).collect();
            format!("new List<{elem_ty}> {{ {} }}", items.join(", "))
        }
        Json::Object(map) => {
            usings.insert("System.Collections.Generic".to_string());
            let entries: Vec<String> = map
                .iter()
                .map(|(k, v)| {
                    let kq = serde_json::to_string(k).unwrap_or_else(|_| "\"\"".to_string());
                    format!("[{kq}] = {}", json_to_csharp(v, usings))
                })
                .collect();
            format!(
                "new Dictionary<string, object?> {{ {} }}",
                entries.join(", ")
            )
        }
    }
}

fn json_scalar_to_query_string(val: &Json) -> String {
    match val {
        Json::String(s) => s.clone(),
        Json::Number(n) => n.to_string(),
        Json::Bool(b) => b.to_string(),
        Json::Array(arr) => arr
            .iter()
            .map(json_scalar_to_query_string)
            .collect::<Vec<_>>()
            .join(","),
        _ => "example".to_string(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use openapi::{OpenApiContextGuard, parse_json};
    use tempfile::TempDir;

    fn sample_config() -> XdkConfig {
        toml::from_str(
            r#"
[versions]
python = "0.11.2"
typescript = "0.7.2"
java = "0.1.2"
csharp = "0.1.2"
"#,
        )
        .unwrap()
    }

    fn sample_spec_json() -> &'static str {
        r##"{
  "openapi": "3.0.0",
  "info": { "title": "X API", "version": "2.0" },
  "components": {
    "schemas": {
      "CreatePostsRequest": {
        "type": "object",
        "properties": {
          "text": { "type": "string", "description": "Post text for {id} <mention>." }
        }
      },
      "CreatePostsResponse": {
        "type": "object",
        "properties": {
          "data": { "type": "object", "properties": { "id": { "type": "string" } } }
        }
      }
    }
  },
  "paths": {
    "/2/tweets": {
      "post": {
        "tags": ["Posts"],
        "operationId": "createPosts",
        "summary": "Creation of a Post",
        "description": "Causes the user {id} to create a Post <tag> with `{literal}`.",
        "security": [{ "OAuth2UserToken": ["tweet.write"] }],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": { "$ref": "#/components/schemas/CreatePostsRequest" }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": { "$ref": "#/components/schemas/CreatePostsResponse" }
              }
            }
          }
        }
      }
    },
    "/2/tweets/search/recent": {
      "get": {
        "tags": ["Posts"],
        "operationId": "searchPostsRecent",
        "summary": "Recent search",
        "security": [{ "BearerToken": [] }],
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "required": true,
            "schema": { "type": "string" },
            "description": "One query for matching Posts."
          },
          {
            "name": "pagination_token",
            "in": "query",
            "required": false,
            "schema": { "type": "string" }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": { "$ref": "#/components/schemas/CreatePostsResponse" }
              }
            }
          }
        }
      }
    }
  }
}"##
    }

    #[test]
    fn test_escape_mdx_prose_preserves_inline_code() {
        let input = "Lookup {id} and <woeid> while keeping `{id}` and `<T>` intact.";
        let escaped = escape_mdx_prose(input);
        assert_eq!(
            escaped,
            "Lookup \\{id\\} and &lt;woeid&gt; while keeping `{id}` and `<T>` intact."
        );
    }

    #[test]
    fn test_generate_mintlify_docs_end_to_end() {
        let _guard = OpenApiContextGuard::new();
        let spec = parse_json(sample_spec_json()).unwrap();
        let tmp = TempDir::new().unwrap();

        fs::write(
            tmp.path().join("docs.json"),
            r#"{"name": "X Docs", "navigation": {"products": [{"product": "X API", "tabs": []}]}, "redirects": [{"source": "/xdks/overview", "destination": "/tools-and-libraries"}]}"#,
        )
        .unwrap();

        let summary = generate_mintlify_docs(&spec, tmp.path(), &sample_config(), true).unwrap();

        assert_eq!(summary.tag_count, 1);
        assert_eq!(summary.operation_count, 2);
        assert!(summary.docs_json_updated);
        assert_eq!(summary.new_endpoint_stubs.len(), 2);

        let overlay_raw = fs::read_to_string(&summary.overlay_path).unwrap();
        let overlay: Json = serde_json::from_str(&overlay_raw).unwrap();
        assert_eq!(overlay["overlay"], "1.1.0");
        assert_eq!(overlay["actions"].as_array().unwrap().len(), 2);

        let samples = overlay["actions"][0]["update"]["x-codeSamples"]
            .as_array()
            .unwrap();
        assert_eq!(samples.len(), 5);
        assert!(
            samples[0]["source"]
                .as_str()
                .unwrap()
                .contains("X_ACCESS_TOKEN")
        );
        assert!(
            samples[2]["source"]
                .as_str()
                .unwrap()
                .contains("new Schemas.CreatePostsRequest().text(")
        );
        assert!(
            samples[3]["source"]
                .as_str()
                .unwrap()
                .contains("new CreatePostsRequest { Text = ")
        );
        assert!(
            samples[4]["source"]
                .as_str()
                .unwrap()
                .contains("xurl -X POST /2/tweets")
        );

        for lang in ["python", "typescript", "java", "csharp"] {
            let client_mdx = fs::read_to_string(
                tmp.path()
                    .join("xdks")
                    .join(lang)
                    .join("reference/clients/posts.mdx"),
            )
            .unwrap();
            assert!(client_mdx.contains("PostsClient"));
            assert!(client_mdx.contains("\\{id\\}"));
            assert!(client_mdx.contains("`{literal}`"));
            assert!(!client_mdx.contains("<ParamField"));
        }

        let updated_docs: Json =
            serde_json::from_str(&fs::read_to_string(tmp.path().join("docs.json")).unwrap())
                .unwrap();
        assert_eq!(
            updated_docs["api"]["openapi"]["overlays"][0],
            "overlays/xdk-code-samples.json"
        );
        let products = updated_docs["navigation"]["products"].as_array().unwrap();
        assert!(products.iter().any(|p| p["product"] == "XDKs"));
        let redirects = updated_docs["redirects"].as_array().unwrap();
        assert!(
            !redirects.iter().any(|r| r["source"] == "/xdks/overview"),
            "Stale /xdks/overview redirect should be pruned"
        );
        assert!(
            redirects
                .iter()
                .any(|r| r["source"] == "/xdks" && r["destination"] == "/xdks/overview")
        );
    }
}
