"""
Auto-generated posts models for the X API.

This module provides Pydantic models for request and response data structures
for the posts endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_reposted_by


class GetRepostedByResponse(BaseModel):
    """Response model for get_reposted_by"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_counts_recent


class GetCountsRecentResponse(BaseModel):
    """Response model for get_counts_recent"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_by_id


class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for delete


class DeleteResponse(BaseModel):
    """Response model for delete"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_analytics


class GetAnalyticsResponse(BaseModel):
    """Response model for get_analytics"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for search_recent


class SearchRecentResponse(BaseModel):
    """Response model for search_recent"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_by_ids


class GetByIdsResponse(BaseModel):
    """Response model for get_by_ids"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for create


class CreateRequest(BaseModel):
    """Request model for create"""

    model_config = ConfigDict(populate_by_name=True)


class CreateResponse(BaseModel):
    """Response model for create"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_insights28hr


class GetInsights28hrResponse(BaseModel):
    """Response model for get_insights28hr"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for hide_reply


class HideReplyRequest(BaseModel):
    """Request model for hide_reply"""

    model_config = ConfigDict(populate_by_name=True)


class HideReplyResponse(BaseModel):
    """Response model for hide_reply"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for search_all


class SearchAllResponse(BaseModel):
    """Response model for search_all"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_counts_all


class GetCountsAllResponse(BaseModel):
    """Response model for get_counts_all"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_insights_historical


class GetInsightsHistoricalResponse(BaseModel):
    """Response model for get_insights_historical"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_quoted


class GetQuotedResponse(BaseModel):
    """Response model for get_quoted"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_liking_users


class GetLikingUsersResponse(BaseModel):
    """Response model for get_liking_users"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_reposts


class GetRepostsResponse(BaseModel):
    """Response model for get_reposts"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")
