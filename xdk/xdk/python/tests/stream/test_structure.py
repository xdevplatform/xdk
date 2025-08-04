"""
Auto-generated structural tests for Stream client.

This module contains tests that validate the structure and API surface
of the Stream client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.stream.client import StreamClient
from xdk import Client


class TestStreamStructure:
    """Test the structure of StreamClient."""
    
    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.stream_client = getattr(self.client, "stream")
    
    def test_client_exists(self):
        """Test that StreamClient class exists and is importable."""
        assert StreamClient is not None
        assert hasattr(StreamClient, '__name__')
        assert StreamClient.__name__ == "StreamClient"
    
    def test_client_initialization(self):
        """Test that StreamClient can be initialized properly."""
        assert self.stream_client is not None
        assert isinstance(self.stream_client, StreamClient)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_stream_posts_firehose_ko_exists(self):
        """Test that stream_posts_firehose_ko method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_firehose_ko", None)
        assert method is not None, f"Method stream_posts_firehose_ko does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_ko is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_firehose_ko should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_firehose_ko"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_firehose_ko_return_annotation(self):
        """Test that stream_posts_firehose_ko has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_firehose_ko")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_firehose_ko should have return type annotation"
    
    
    
    
    def test_stream_likes_firehose_exists(self):
        """Test that stream_likes_firehose method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_likes_firehose", None)
        assert method is not None, f"Method stream_likes_firehose does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_likes_firehose is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_likes_firehose should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_likes_firehose"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_likes_firehose_return_annotation(self):
        """Test that stream_likes_firehose has proper return type annotation."""
        method = getattr(StreamClient, "stream_likes_firehose")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_likes_firehose should have return type annotation"
    
    
    
    
    def test_stream_posts_exists(self):
        """Test that stream_posts method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts", None)
        assert method is not None, f"Method stream_posts does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_return_annotation(self):
        """Test that stream_posts has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts should have return type annotation"
    
    
    
    
    def test_stream_likes_sample10_exists(self):
        """Test that stream_likes_sample10 method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_likes_sample10", None)
        assert method is not None, f"Method stream_likes_sample10 does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_likes_sample10 is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_likes_sample10 should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_likes_sample10"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_likes_sample10_return_annotation(self):
        """Test that stream_likes_sample10 has proper return type annotation."""
        method = getattr(StreamClient, "stream_likes_sample10")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_likes_sample10 should have return type annotation"
    
    
    
    
    def test_stream_posts_firehose_ja_exists(self):
        """Test that stream_posts_firehose_ja method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_firehose_ja", None)
        assert method is not None, f"Method stream_posts_firehose_ja does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_ja is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_firehose_ja should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_firehose_ja"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_firehose_ja_return_annotation(self):
        """Test that stream_posts_firehose_ja has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_firehose_ja")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_firehose_ja should have return type annotation"
    
    
    
    
    def test_stream_posts_firehose_en_exists(self):
        """Test that stream_posts_firehose_en method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_firehose_en", None)
        assert method is not None, f"Method stream_posts_firehose_en does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_en is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_firehose_en should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_firehose_en"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_firehose_en_return_annotation(self):
        """Test that stream_posts_firehose_en has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_firehose_en")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_firehose_en should have return type annotation"
    
    
    
    
    def test_get_rule_counts_exists(self):
        """Test that get_rule_counts method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "get_rule_counts", None)
        assert method is not None, f"Method get_rule_counts does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"get_rule_counts is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_rule_counts should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_rule_counts"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_rule_counts_return_annotation(self):
        """Test that get_rule_counts has proper return type annotation."""
        method = getattr(StreamClient, "get_rule_counts")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_rule_counts should have return type annotation"
    
    
    
    
    def test_stream_labels_compliance_exists(self):
        """Test that stream_labels_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_labels_compliance", None)
        assert method is not None, f"Method stream_labels_compliance does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_labels_compliance is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_labels_compliance should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_labels_compliance"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_labels_compliance_return_annotation(self):
        """Test that stream_labels_compliance has proper return type annotation."""
        method = getattr(StreamClient, "stream_labels_compliance")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_labels_compliance should have return type annotation"
    
    
    
    
    def test_stream_posts_firehose_exists(self):
        """Test that stream_posts_firehose method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_firehose", None)
        assert method is not None, f"Method stream_posts_firehose does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_firehose is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_firehose should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_firehose"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_firehose_return_annotation(self):
        """Test that stream_posts_firehose has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_firehose")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_firehose should have return type annotation"
    
    
    
    
    def test_stream_posts_sample_exists(self):
        """Test that stream_posts_sample method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_sample", None)
        assert method is not None, f"Method stream_posts_sample does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_sample is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_sample should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_sample"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_sample_return_annotation(self):
        """Test that stream_posts_sample has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_sample")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_sample should have return type annotation"
    
    
    
    
    def test_stream_posts_firehose_pt_exists(self):
        """Test that stream_posts_firehose_pt method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_firehose_pt", None)
        assert method is not None, f"Method stream_posts_firehose_pt does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_pt is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_firehose_pt should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_firehose_pt"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_firehose_pt_return_annotation(self):
        """Test that stream_posts_firehose_pt has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_firehose_pt")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_firehose_pt should have return type annotation"
    
    
    
    
    def test_stream_posts_compliance_exists(self):
        """Test that stream_posts_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_compliance", None)
        assert method is not None, f"Method stream_posts_compliance does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_compliance is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_compliance should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_compliance"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_compliance_return_annotation(self):
        """Test that stream_posts_compliance has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_compliance")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_compliance should have return type annotation"
    
    
    
    
    def test_stream_posts_sample10_exists(self):
        """Test that stream_posts_sample10 method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_posts_sample10", None)
        assert method is not None, f"Method stream_posts_sample10 does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_posts_sample10 is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts_sample10 should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_posts_sample10"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_posts_sample10_return_annotation(self):
        """Test that stream_posts_sample10 has proper return type annotation."""
        method = getattr(StreamClient, "stream_posts_sample10")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_posts_sample10 should have return type annotation"
    
    
    
    
    def test_stream_likes_compliance_exists(self):
        """Test that stream_likes_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_likes_compliance", None)
        assert method is not None, f"Method stream_likes_compliance does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_likes_compliance is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_likes_compliance should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_likes_compliance"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_likes_compliance_return_annotation(self):
        """Test that stream_likes_compliance has proper return type annotation."""
        method = getattr(StreamClient, "stream_likes_compliance")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_likes_compliance should have return type annotation"
    
    
    
    
    def test_stream_users_compliance_exists(self):
        """Test that stream_users_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "stream_users_compliance", None)
        assert method is not None, f"Method stream_users_compliance does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"stream_users_compliance is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_users_compliance should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "partition",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from stream_users_compliance"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "backfill_minutes",
            
            "start_time",
            
            "end_time",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_stream_users_compliance_return_annotation(self):
        """Test that stream_users_compliance has proper return type annotation."""
        method = getattr(StreamClient, "stream_users_compliance")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method stream_users_compliance should have return type annotation"
    
    
    
    
    def test_get_rules_exists(self):
        """Test that get_rules method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "get_rules", None)
        assert method is not None, f"Method get_rules does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"get_rules is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_rules should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_rules"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "ids",
            
            "max_results",
            
            "pagination_token",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_rules_return_annotation(self):
        """Test that get_rules has proper return type annotation."""
        method = getattr(StreamClient, "get_rules")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_rules should have return type annotation"
    
    
    def test_get_rules_pagination_params(self):
        """Test that get_rules has pagination parameters."""
        method = getattr(StreamClient, "get_rules")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method get_rules should have pagination parameters"
    
    
    
    def test_update_rules_exists(self):
        """Test that update_rules method exists with correct signature."""
        # Check method exists
        method = getattr(StreamClient, "update_rules", None)
        assert method is not None, f"Method update_rules does not exist on StreamClient"
        
        # Check method is callable
        assert callable(method), f"update_rules is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"update_rules should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from update_rules"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "dry_run",
            
            "delete_all",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_update_rules_return_annotation(self):
        """Test that update_rules has proper return type annotation."""
        method = getattr(StreamClient, "update_rules")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method update_rules should have return type annotation"
    
    
    
    
    
    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            
            "stream_posts_firehose_ko",
            
            "stream_likes_firehose",
            
            "stream_posts",
            
            "stream_likes_sample10",
            
            "stream_posts_firehose_ja",
            
            "stream_posts_firehose_en",
            
            "get_rule_counts",
            
            "stream_labels_compliance",
            
            "stream_posts_firehose",
            
            "stream_posts_sample",
            
            "stream_posts_firehose_pt",
            
            "stream_posts_compliance",
            
            "stream_posts_sample10",
            
            "stream_likes_compliance",
            
            "stream_users_compliance",
            
            "get_rules",
            
            "update_rules",
            
        ]
        
        client_methods = [name for name in dir(StreamClient) 
                         if not name.startswith('_') and callable(getattr(StreamClient, name))]
        
        for expected_method in expected_methods:
            assert expected_method in client_methods, \
                f"Expected method '{expected_method}' not found on StreamClient"
    
    def test_no_unexpected_public_methods(self):
        """Test that no unexpected public methods exist (helps catch API drift)."""
        expected_methods = set([
            
            "stream_posts_firehose_ko",
            
            "stream_likes_firehose",
            
            "stream_posts",
            
            "stream_likes_sample10",
            
            "stream_posts_firehose_ja",
            
            "stream_posts_firehose_en",
            
            "get_rule_counts",
            
            "stream_labels_compliance",
            
            "stream_posts_firehose",
            
            "stream_posts_sample",
            
            "stream_posts_firehose_pt",
            
            "stream_posts_compliance",
            
            "stream_posts_sample10",
            
            "stream_likes_compliance",
            
            "stream_users_compliance",
            
            "get_rules",
            
            "update_rules",
            
        ])
        
        actual_methods = set([name for name in dir(StreamClient) 
                            if not name.startswith('_') and callable(getattr(StreamClient, name))])
        
        # Remove standard methods that might be inherited
        standard_methods = {'__init__'}
        actual_methods = actual_methods - standard_methods
        
        unexpected_methods = actual_methods - expected_methods
        
        # This is a warning, not a failure, since new methods might be added
        if unexpected_methods:
            print(f"Warning: Unexpected methods found on StreamClient: {unexpected_methods}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_imports_work(self):
        """Test that all expected imports work correctly."""
        expected_imports = [
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            "typing",
            
            "requests",
            
            "pydantic",
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        ]
        
        for import_name in expected_imports:
            try:
                __import__(import_name)
            except ImportError as e:
                pytest.fail(f"Expected import '{import_name}' failed: {e}")