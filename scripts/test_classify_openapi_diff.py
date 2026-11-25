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
                "User": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "id": {"type": "string"},
                        "description": {
                            "type": "string",
                            "description": "The user's profile bio.",
                        },
                        "title": {"type": "string"},
                    },
                },
                "Place": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                },
                "Tweet": {
                    "type": "object",
                    "required": ["id", "text"],
                    "properties": {
                        "id": {"type": "string"},
                        "text": {"type": "string"},
                        "lang": {"type": "string", "enum": ["en", "es"]},
                        "author": {"$ref": "#/components/schemas/User"},
                        "metrics": {
                            "type": "object",
                            "properties": {
                                "like_count": {"type": "integer", "format": "int32"},
                            },
                        },
                    },
                },
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
        new["components"]["schemas"]["User"]["properties"]["description"][
            "description"
        ] = "Updated bio doc prose only"
        res = cod.classify_diff(old, new)
        self.assertFalse(res["changed"])
        self.assertEqual(res["change_level"], "none")

    def test_properties_named_description_or_title_are_not_stripped(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        del new["components"]["schemas"]["User"]["properties"]["description"]
        new["components"]["schemas"]["User"]["properties"]["title"]["type"] = "integer"
        res = cod.classify_diff(old, new)
        self.assertTrue(res["changed"])
        self.assertEqual(res["change_level"], "breaking")
        self.assertTrue(
            any("Removed property `User.description`" in m for m in res["breaking_changes"])
        )
        self.assertTrue(
            any("Type changed at `User.title`" in m for m in res["breaking_changes"])
        )

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
        bumps = cod.compute_sdk_bumps(
            res["change_level"], {"python": "1.2.0", "java": "0.1.2"}
        )
        self.assertEqual(bumps["python"], "minor")
        self.assertEqual(bumps["java"], "minor")

    def test_removed_endpoint_is_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/users/me"] = {
            "get": {
                "operationId": "getMe",
                "tags": ["Users"],
                "responses": {"200": {"description": "OK"}},
            }
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

    def test_newly_required_schema_property_is_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["components"]["schemas"]["Tweet"]["required"].append("lang")
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertTrue(
            any("Property `Tweet.lang` became required" in m for m in res["breaking_changes"])
        )

    def test_array_items_enum_removal_is_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        new["paths"]["/2/tweets/{id}"]["get"]["parameters"][1]["schema"]["items"][
            "enum"
        ].remove("author_id")
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertTrue(
            any("Removed enum value(s)" in m and "tweet.fields" in m for m in res["breaking_changes"])
        )

    def test_nested_format_nullable_ref_and_enum_presence_changes_are_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        # Nested format change
        new["components"]["schemas"]["Tweet"]["properties"]["metrics"]["properties"][
            "like_count"
        ]["format"] = "int64"
        # Nullable change
        new["components"]["schemas"]["Tweet"]["properties"]["text"]["nullable"] = True
        # $ref target change
        new["components"]["schemas"]["Tweet"]["properties"]["author"][
            "$ref"
        ] = "#/components/schemas/Place"
        # Enum constraint removed
        del new["components"]["schemas"]["Tweet"]["properties"]["lang"]["enum"]
        # Enum constraint added
        new["components"]["schemas"]["User"]["properties"]["id"]["enum"] = ["1", "2"]

        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        joined = "\n".join(res["breaking_changes"])
        self.assertIn("Format changed at `Tweet.metrics.like_count`", joined)
        self.assertIn("Nullability changed at `Tweet.text`", joined)
        self.assertIn("Schema reference changed at `Tweet.author`", joined)
        self.assertIn("Removed enum constraint at `Tweet.lang`", joined)
        self.assertIn("Added enum constraint at `User.id`", joined)

    def test_inline_request_response_and_composition_breaking_changes(self) -> None:
        old = base_spec()
        old["paths"]["/2/inline"] = {
            "post": {
                "operationId": "createInline",
                "tags": ["Posts"],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {"a": {"type": "string"}, "b": {"type": "string"}},
                            }
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "oneOf": [
                                        {"$ref": "#/components/schemas/User"},
                                        {"$ref": "#/components/schemas/Place"},
                                    ]
                                }
                            }
                        },
                    }
                },
            }
        }
        new = copy.deepcopy(old)
        del new["paths"]["/2/inline"]["post"]["requestBody"]["content"][
            "application/json"
        ]["schema"]["properties"]["b"]
        new["paths"]["/2/inline"]["post"]["responses"]["200"]["content"][
            "application/json"
        ]["schema"]["oneOf"].pop()

        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        joined = "\n".join(res["breaking_changes"])
        self.assertIn("Removed property `POST /2/inline requestBody(application/json).b`", joined)
        self.assertIn("Removed `oneOf` variant `#/components/schemas/Place`", joined)

    def test_operation_id_removed_or_added_and_tag_change_are_breaking(self) -> None:
        old = base_spec()
        new = copy.deepcopy(old)
        del new["paths"]["/2/tweets/{id}"]["get"]["operationId"]
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
