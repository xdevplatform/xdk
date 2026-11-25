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

    def test_dropping_a_schema_altogether_is_breaking(self) -> None:
        old = base_spec()
        old["paths"]["/2/tweets/{id}"]["get"]["requestBody"] = {
            "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Tweet"}}}
        }

        def op(spec: dict) -> dict:
            return spec["paths"]["/2/tweets/{id}"]["get"]

        expected = {
            "request body": "Removed schema at `GET /2/tweets/{id} requestBody(application/json)`",
            "response": "Removed schema at `GET /2/tweets/{id} response[200](application/json)`",
            "parameter": "Removed schema at `GET /2/tweets/{id} param `tweet.fields``",
        }
        for case, message in expected.items():
            with self.subTest(case=case):
                new = copy.deepcopy(old)
                if case == "request body":
                    del op(new)["requestBody"]["content"]["application/json"]["schema"]
                elif case == "response":
                    del op(new)["responses"]["200"]["content"]["application/json"]["schema"]
                else:
                    del op(new)["parameters"][1]["schema"]
                res = cod.classify_diff(old, new)
                self.assertEqual(res["change_level"], "breaking")
                self.assertEqual(res["breaking_changes"], [message])

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


def shared_spec() -> dict:
    """base_spec() plus operations that only reach shared components through `$ref`."""
    spec = base_spec()
    spec["components"]["parameters"] = {
        "TweetFieldsParameter": {
            "name": "tweet.fields",
            "in": "query",
            "description": "Fields to return.",
            "required": False,
            "schema": {
                "type": "array",
                "items": {"type": "string", "enum": ["created_at", "author_id"]},
            },
        }
    }
    spec["components"]["requestBodies"] = {
        "TweetCreate": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {"text": {"type": "string"}, "lang": {"type": "string"}},
                    }
                }
            }
        }
    }
    spec["components"]["responses"] = {
        "TweetList": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {"count": {"type": "integer"}, "next": {"type": "string"}},
                    }
                }
            },
        },
        "Problem": {
            "description": "Error",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {"detail": {"type": "string"}, "type": {"type": "string"}},
                    }
                }
            },
        },
    }
    shared_param = {"$ref": "#/components/parameters/TweetFieldsParameter"}
    spec["paths"]["/2/tweets"] = {
        "get": {
            "operationId": "findTweets",
            "tags": ["Posts"],
            "parameters": [shared_param],
            "responses": {
                "200": {"$ref": "#/components/responses/TweetList"},
                "default": {"$ref": "#/components/responses/Problem"},
            },
        },
        "post": {
            "operationId": "createTweet",
            "tags": ["Posts"],
            "parameters": [shared_param],
            "requestBody": {"$ref": "#/components/requestBodies/TweetCreate"},
            "responses": {"default": {"$ref": "#/components/responses/Problem"}},
        },
    }
    return spec


class SharedComponentTests(unittest.TestCase):
    """Changes to `$ref`-ed parameters, request bodies and responses leave operations untouched."""

    def test_shared_parameter_items_enum_removal_is_breaking_and_reported_once(self) -> None:
        old = shared_spec()
        new = copy.deepcopy(old)
        new["components"]["parameters"]["TweetFieldsParameter"]["schema"]["items"]["enum"].remove(
            "author_id"
        )
        # One of the two referencing operations also changes on its own.
        new["paths"]["/2/tweets"]["get"]["parameters"].append(
            {"name": "max_results", "in": "query", "schema": {"type": "integer"}}
        )
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertEqual(
            res["breaking_changes"],
            [
                "Removed enum value(s) at `#/components/parameters/TweetFieldsParameter"
                ' param `tweet.fields`[]`: "author_id"'
            ],
        )
        self.assertIn("Updated shared parameter `TweetFieldsParameter`", res["schema_changes"])

    def test_shared_parameter_required_type_and_rename_are_breaking(self) -> None:
        old = shared_spec()

        new = copy.deepcopy(old)
        new["components"]["parameters"]["TweetFieldsParameter"]["required"] = True
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertIn("became required", "\n".join(res["breaking_changes"]))

        new = copy.deepcopy(old)
        new["components"]["parameters"]["TweetFieldsParameter"]["schema"] = {"type": "string"}
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertIn("Type changed", "\n".join(res["breaking_changes"]))

        new = copy.deepcopy(old)
        new["components"]["parameters"]["TweetFieldsParameter"]["name"] = "post.fields"
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertIn("`tweet.fields` to query `post.fields`", "\n".join(res["breaking_changes"]))

    def test_shared_parameter_additive_and_doc_only_changes_are_not_breaking(self) -> None:
        old = shared_spec()

        new = copy.deepcopy(old)
        new["components"]["parameters"]["TweetFieldsParameter"]["schema"]["items"]["enum"].append(
            "lang"
        )
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "patch")
        self.assertEqual(res["breaking_changes"], [])
        self.assertEqual(res["schema_changes"], ["Updated shared parameter `TweetFieldsParameter`"])

        new = copy.deepcopy(old)
        new["components"]["parameters"]["TweetFieldsParameter"]["description"] = "Reworded."
        new["components"]["responses"]["TweetList"]["description"] = "Reworded."
        res = cod.classify_diff(old, new)
        self.assertFalse(res["changed"])

    def test_shared_request_body_change_is_breaking(self) -> None:
        old = shared_spec()
        new = copy.deepcopy(old)
        body = new["components"]["requestBodies"]["TweetCreate"]
        del body["content"]["application/json"]["schema"]["properties"]["lang"]
        body["required"] = True
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        joined = "\n".join(res["breaking_changes"])
        self.assertIn(
            "Removed property `#/components/requestBodies/TweetCreate(application/json).lang`",
            joined,
        )
        self.assertIn(
            "Request body became required on `#/components/requestBodies/TweetCreate`", joined
        )

    def test_shared_success_response_change_is_breaking_but_error_response_is_not(self) -> None:
        old = shared_spec()

        new = copy.deepcopy(old)
        del new["components"]["responses"]["TweetList"]["content"]["application/json"]["schema"][
            "properties"
        ]["next"]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertEqual(
            res["breaking_changes"],
            ["Removed property `#/components/responses/TweetList(application/json).next`"],
        )

        # `Problem` is only ever used as a non-2xx response, which SDK return types ignore.
        new = copy.deepcopy(old)
        del new["components"]["responses"]["Problem"]["content"]["application/json"]["schema"][
            "properties"
        ]["type"]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "patch")
        self.assertEqual(res["breaking_changes"], [])

    def test_switching_between_shared_and_inline_definitions(self) -> None:
        old = shared_spec()
        shared = old["components"]["parameters"]["TweetFieldsParameter"]

        # Inlining an identical definition changes nothing the SDKs can see.
        new = copy.deepcopy(old)
        new["paths"]["/2/tweets"]["get"]["parameters"] = [copy.deepcopy(shared)]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["breaking_changes"], [])

        # Inlining a narrower definition is still caught on the operation itself.
        new = copy.deepcopy(old)
        narrower = copy.deepcopy(shared)
        narrower["schema"]["items"]["enum"].remove("author_id")
        new["paths"]["/2/tweets"]["get"]["parameters"] = [narrower]
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertIn("GET /2/tweets param `tweet.fields`[]", "\n".join(res["breaking_changes"]))


class CycleSafetyTests(unittest.TestCase):
    def cyclic_spec(self) -> dict:
        spec = base_spec()
        schemas = spec["components"]["schemas"]
        schemas["Node"] = {
            "type": "object",
            "properties": {
                "value": {"type": "string"},
                "next": {"$ref": "#/components/schemas/Node"},
                "children": {"type": "array", "items": {"$ref": "#/components/schemas/Node"}},
                "owner": {"$ref": "#/components/schemas/Owner"},
            },
        }
        schemas["Owner"] = {
            "allOf": [
                {"$ref": "#/components/schemas/User"},
                {"type": "object", "properties": {"root": {"$ref": "#/components/schemas/Node"}}},
            ]
        }
        # Alias loops are invalid OpenAPI, but must not hang or crash the release job.
        schemas["LoopA"] = {"$ref": "#/components/schemas/LoopB"}
        schemas["LoopB"] = {"$ref": "#/components/schemas/LoopA"}
        spec["components"]["parameters"] = {
            "Loop": {"$ref": "#/components/parameters/Loop"},
        }
        spec["paths"]["/2/nodes"] = {
            "get": {
                "operationId": "getNodes",
                "tags": ["Nodes"],
                "parameters": [{"$ref": "#/components/parameters/Loop"}],
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Node"}
                            }
                        },
                    }
                },
            }
        }
        return spec

    def test_recursive_schemas_terminate_and_report_each_change_once(self) -> None:
        old = self.cyclic_spec()
        self.assertFalse(cod.classify_diff(old, copy.deepcopy(old))["changed"])

        new = copy.deepcopy(old)
        del new["components"]["schemas"]["Node"]["properties"]["value"]
        new["components"]["schemas"]["Owner"]["allOf"][1]["properties"]["root"] = {
            "$ref": "#/components/schemas/User"
        }
        new["components"]["schemas"]["LoopB"] = {"type": "string"}
        res = cod.classify_diff(old, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertEqual(
            sum("Removed property `Node.value`" in m for m in res["breaking_changes"]), 1
        )
        self.assertIn("Schema reference changed at `Owner.root`", "\n".join(res["breaking_changes"]))


REAL_SPEC_PATH = Path(__file__).resolve().parent.parent / "specs" / "openapi.json"


@unittest.skipUnless(REAL_SPEC_PATH.is_file(), "specs/openapi.json is not checked out")
class RealSpecTests(unittest.TestCase):
    """Guard against false positives and regressions on the committed X API spec."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.spec = cod.load_json(REAL_SPEC_PATH)

    def mutated(self) -> dict:
        return copy.deepcopy(self.spec)

    def test_unchanged_spec_is_not_a_release(self) -> None:
        res = cod.classify_diff(self.spec, self.mutated())
        self.assertFalse(res["changed"])
        self.assertEqual(res["breaking_changes"], [])

    def test_doc_only_edits_everywhere_are_not_a_release(self) -> None:
        new = self.mutated()
        new["info"]["version"] = "999.0"

        def reword(node: object, in_name_map: bool = False) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    if not in_name_map and key in ("description", "summary") and isinstance(value, str):
                        node[key] = value + " (reworded)"
                    elif not in_name_map and key in ("example", "examples", "default", "enum"):
                        continue
                    else:
                        reword(value, not in_name_map and key in cod.MAP_CONTAINER_KEYS)
            elif isinstance(node, list):
                for item in node:
                    reword(item)

        reword(new["paths"], in_name_map=True)
        for section in ("schemas", "parameters"):
            reword(new["components"][section], in_name_map=True)
        self.assertNotEqual(new["paths"], self.spec["paths"])
        res = cod.classify_diff(self.spec, new)
        self.assertFalse(res["changed"])

    def test_fields_named_like_doc_keywords_are_real_properties(self) -> None:
        for schema, field in (("User", "description"), ("List", "description"), ("Space", "title")):
            with self.subTest(schema=schema, field=field):
                self.assertIn(field, self.spec["components"]["schemas"][schema]["properties"])
                view = cod.structural_view(self.spec)
                self.assertIn(field, view["components"]["schemas"][schema]["properties"])

                new = self.mutated()
                del new["components"]["schemas"][schema]["properties"][field]
                res = cod.classify_diff(self.spec, new)
                self.assertEqual(res["change_level"], "breaking")
                self.assertEqual(res["breaking_changes"], [f"Removed property `{schema}.{field}`"])

                new = self.mutated()
                new["components"]["schemas"][schema]["properties"][field]["type"] = "integer"
                res = cod.classify_diff(self.spec, new)
                self.assertEqual(res["change_level"], "breaking")

    def test_removed_fields_parameter_enum_value_is_breaking_and_reported_once(self) -> None:
        for name in ("PostFieldsParameter", "UserFieldsParameter"):
            with self.subTest(parameter=name):
                new = self.mutated()
                values = new["components"]["parameters"][name]["schema"]["items"]["enum"]
                removed = values.pop(0)
                res = cod.classify_diff(self.spec, new)
                self.assertEqual(res["change_level"], "breaking")
                self.assertEqual(len(res["breaking_changes"]), 1)
                self.assertIn(f'"{removed}"', res["breaking_changes"][0])
                self.assertIn(name, res["breaking_changes"][0])

    def test_added_fields_parameter_enum_value_is_patch(self) -> None:
        new = self.mutated()
        new["components"]["parameters"]["PostFieldsParameter"]["schema"]["items"]["enum"].append(
            "brand_new_field"
        )
        res = cod.classify_diff(self.spec, new)
        self.assertEqual(res["change_level"], "patch")
        self.assertEqual(res["breaking_changes"], [])

    def test_newly_required_property_is_breaking(self) -> None:
        new = self.mutated()
        user = new["components"]["schemas"]["User"]
        self.assertNotIn("description", user.get("required", []))
        user.setdefault("required", []).append("description")
        res = cod.classify_diff(self.spec, new)
        self.assertEqual(res["change_level"], "breaking")
        self.assertEqual(res["breaking_changes"], ["Property `User.description` became required"])


if __name__ == "__main__":
    unittest.main()
