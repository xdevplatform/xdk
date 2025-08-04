"""
Auto-generated pagination tests for Usage client.

This module contains tests that validate pagination functionality
using the Cursor class for methods that support pagination.

Generated automatically - do not edit manually.
"""

import pytest
from unittest.mock import Mock, patch
from xdk.usage.client import UsageClient
from xdk import Client, Cursor, cursor, PaginationError


class TestUsagePagination:
    """Test pagination functionality for UsageClient."""
    
    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.usage_client = getattr(self.client, "usage")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_non_paginatable_method_raises_error(self):
        """Test that non-paginatable methods raise PaginationError."""
        
        # Create a mock method that doesn't support pagination
        def non_paginatable_method(id: str) -> dict:
            return {"id": id}
        
        with pytest.raises(PaginationError):
            cursor(non_paginatable_method)
        
        def non_paginatable_method(id: str) -> dict:
            return {"id": id}
        
        with pytest.raises(PaginationError):
            cursor(non_paginatable_method)
    
    def test_cursor_class_functionality(self):
        """Test basic Cursor class functionality."""
        
        # Test that Cursor can be imported and instantiated
        from xdk.paginator import Cursor
        assert Cursor is not None
        
        # Test cursor factory function
        from xdk.paginator import cursor as cursor_factory
        assert cursor_factory is not None
    
    
    def test_pagination_edge_cases(self):
        """Test pagination edge cases."""
        
        with patch.object(self.client, 'session') as mock_session:
            # Test empty response
            empty_response = Mock()
            empty_response.status_code = 200
            empty_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0}
            }
            empty_response.raise_for_status.return_value = None
            mock_session.get.return_value = empty_response
            
            # Pick first paginatable method for testing
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    