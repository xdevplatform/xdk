#!/usr/bin/env python3
"""Unit tests for scripts/classify_openapi_diff.py."""

from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import classify_openapi_diff as cod  # noqa: E402


def base_spec() -> dict:
    return {
        "openapi": "3.0.0",
        "info": {"title": "X API v2", "version": "2.175"},
        "paths": {
            "/2/tweets/{id}": {
                "get": {
                    "operationId": "findTweetById",
                    "tags": ["Posts"],
                    "summary": "Get Post by ID",
                    "description": "Returns a single Post.",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "tweet.fields",
                            "in": "query",
                            "required": False,
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "string",
                                    "enum": ["created_at", "author_id"],
                                },
                            },
                        },
                    ],
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Tweet"}
                                }
                            },
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "Tweet": {
                    "type": "object",
                    "required": ["id", "text"],
                    "properties": {
                        "id": {"type": "string"},
                        "text": {"type": "string"},
                        "lang": {"type": "string", "enum": ["en", "es"]},
                    },
                }
            }
        },
    }


class ClassifyOpenApiDiffTests(unittest.TestCase):
    def test_identical_specs_no_release(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        res = cod.classify_diff(old, new)
        self.assertFalse(res["changed"])
        self.assertEqual(res["change_level"], "none")
        bumps = cod.compute_sdk_bumps(res["change_level"], {"python": "0.11.2"})
        self.assertEqual(bumps["python"], "none")

    def test_doc_only_and_version_bump_ignored(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["info"]["version"] = "2.176"
        new["paths"]["/2/tweets/{id}"]["get"]["description"] = "Updated prose!"
        new["paths"]["/2/tweets/{id}"]["get"]["summary"] = "New summary"
        new["paths"]["/2/tweets/{id}"]["get"]["x-custom"] = {"foo": "bar"}
        new["components"]["schemas"]["Tweet"]["description"] = "A post object"
        res = cod.classify_diff(old, new)
        self.assertFalse(res["changed"])
        self.assertEqual(res["change_level"], "none")

    def test_shuffled_security_scopes_required_enum_and_params_ignored(self) -> None:
        old = base_spec()
        old["paths"]["/2/tweets/{id}"]["get"]["security"] = [
            {"OAuth2UserToken": ["tweet.read", "users.read", "tweet.write"]},
            {"BearerToken": []},
        ]
        new = copy.deepcopy(old)
        new["paths"]["/2/tweets/{id}"]["get"]["security"] = [
            {"BearerToken": []},
            {"OAuth2UserToken": ["users.read", "tweet.write", "tweet.read"]},
        ]
        new["paths"]["/2/tweets/{id}"]["get"]["parameters"].reverse()
        new["components"]["schemas"]["Tweet"]["required"].reverse()
        new["components"]["schemas"]["Tweet"]["properties"]["lang"]["enum"].reverse()
        res = cod.classify_diff(old, new)
        self.assertFalse(res["changed"])
        self.assertEqual(res["change_level"], "none")

    def test_additive_optional_param_and_property_is_patch(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/tweets/{id}"]["get"]["parameters"].append(
            {
                "name": "expansions",
                "in": "query",
                "required": False,
                "schema": {"type": "string"},
            }
        )
        new["components"]["schemas"]["Tweet"]["properties"]["note"] = {"type": "string"}
        new["components"]["schemas"]["Tweet"]["properties"]["lang"]["enum"].append("fr")
        res = cod.classify_diff(old, new)
        self.assertTrue(res["changed"])
        self.assertEqual(res["change_level"], "patch")
        bumps = cod.compute_sdk_bumps(res["change_level"], {"python": "0.11.2"})
        self.assertEqual(bumps["python"], "patch")

    def test_new_endpoint_is_feature_minor(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/posts/drafts"] = {
            "post": {
                "operationId": "createPostDraft",
                "tags": ["Posts"],
                "responses": {"201": {"description": "Created"}},
            }
        }
        res = cod.classify_diff(old, new)
        self.assertTrue(res["changed"])
        self.assertEqual(res["change_level"], "feature")
        self.assertEqual(res["added_endpoints"], ["`POST /2/posts/drafts`"])
        bumps = cod.compute_sdk_bumps(res["change_level"], {"python": "1.2.0", "java": "0.1.2"})
        self.assertEqual(bumps["python"], "minor")
        self.assertEqual(bumps["java"], "minor")

    def test_removed_endpoint_is_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/users/me"] = {
            "get": {"operationId": "getMe", "tags": ["Users"], "responses": {"200": {"description": "OK"}}}
        }
        del new["paths"]["/2/tweets/{id}"]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertTrue(any("Removed endpoint" in msg for msg in res["breaking_changes"]))

        bumps = cod.compute_sdk_bumps(
            res["change_level"],
            {"python": "0.11.2", "typescript": "1.0.0", "java": "0.1.2", "csharp": "2.3.4"},
        )
        self.assertEqual(bumps["python"], "minor")
        self.assertEqual(bumps["java"], "minor")
        self.assertEqual(bumps["typescript"], "major")
        self.assertEqual(bumps["csharp"], "major")

    def test_newly_required_param_and_removed_property_are_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/tweets/{id}"]["get"]["parameters"][1]["required"] = True
        del new["components"]["schemas"]["Tweet"]["properties"]["text"]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertTrue(any("became required" in msg for msg in res["breaking_changes"]))
        self.assertTrue(any("Removed property `Tweet.text`" in msg for msg in res["breaking_changes"]))

    def test_operation_id_and_tag_change_are_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/tweets/{id}"]["get"]["operationId"] = "getPostById"
        new["paths"]["/2/tweets/{id}"]["get"]["tags"] = ["Media"]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertEqual(len(res["breaking_changes"]), 2)

    def test_validate_rejects_truncated_spec(self) -> None:
        with self.assertRaises(ValueError):
            cod.validate_openapi_spec({"openapi": "3.0.0", "paths": {}}, "live", min_paths=50)

    def test_read_sdk_versions_from_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "xdk-config.toml"
            cfg.write_text(
                '[versions]\npython = "0.11.2"\ntypescript = "0.7.2"\njava = "0.1.2"\ncsharp = "1.0.0"\n',
                encoding="utf-8",
            )
            versions = cod.read_sdk_versions(cfg)
            self.assertEqual(versions["python"], "0.11.2")
            self.assertEqual(versions["csharp"], "1.0.0")


if __name__ == "__main__":
    unittest.main()
