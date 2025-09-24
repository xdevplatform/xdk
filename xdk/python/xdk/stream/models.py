"""
Auto-generated stream models for the X API.

This module provides Pydantic models for request and response data structures
for the stream endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for posts_firehose_ko


class PostsFirehoseKoResponse(BaseModel):
    """Response model for posts_firehose_ko"""

    data: Optional["PostsFirehoseKoResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsFirehoseKoResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseData(BaseModel):
    """Nested model for PostsFirehoseKoResponseData"""

    attachments: Optional["PostsFirehoseKoResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsFirehoseKoResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsFirehoseKoResponseDataEntities"] = None
    geo: Optional["PostsFirehoseKoResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsFirehoseKoResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsFirehoseKoResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsFirehoseKoResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsFirehoseKoResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsFirehoseKoResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsFirehoseKoResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsFirehoseKoResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataAttachments(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataEditControls(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataEntities(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataGeo(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataGeo"""

    coordinates: Optional["PostsFirehoseKoResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataNoteTweet(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataNoteTweet"""

    entities: Optional["PostsFirehoseKoResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataScopes(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseDataWithheld(BaseModel):
    """Nested model for PostsFirehoseKoResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseKoResponseIncludes(BaseModel):
    """Nested model for PostsFirehoseKoResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_rule_counts


class GetRuleCountsResponse(BaseModel):
    """Response model for get_rule_counts"""

    data: Optional["GetRuleCountsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetRuleCountsResponseData(BaseModel):
    """Nested model for GetRuleCountsResponseData"""

    all_project_client_apps: Optional[List] = None
    cap_per_client_app: Optional[int] = None
    cap_per_project: Optional[int] = None
    client_app_rules_count: Optional["GetRuleCountsResponseDataClientAppRulesCount"] = (
        None
    )
    project_rules_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetRuleCountsResponseDataClientAppRulesCount(BaseModel):
    """Nested model for GetRuleCountsResponseDataClientAppRulesCount"""

    client_app_id: Optional[str] = None
    rule_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_sample


class PostsSampleResponse(BaseModel):
    """Response model for posts_sample"""

    data: Optional["PostsSampleResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsSampleResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseData(BaseModel):
    """Nested model for PostsSampleResponseData"""

    attachments: Optional["PostsSampleResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsSampleResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsSampleResponseDataEntities"] = None
    geo: Optional["PostsSampleResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsSampleResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsSampleResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsSampleResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsSampleResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsSampleResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsSampleResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsSampleResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataAttachments(BaseModel):
    """Nested model for PostsSampleResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataEditControls(BaseModel):
    """Nested model for PostsSampleResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataEntities(BaseModel):
    """Nested model for PostsSampleResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataGeo(BaseModel):
    """Nested model for PostsSampleResponseDataGeo"""

    coordinates: Optional["PostsSampleResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsSampleResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsSampleResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataNoteTweet(BaseModel):
    """Nested model for PostsSampleResponseDataNoteTweet"""

    entities: Optional["PostsSampleResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsSampleResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsSampleResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsSampleResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsSampleResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataScopes(BaseModel):
    """Nested model for PostsSampleResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseDataWithheld(BaseModel):
    """Nested model for PostsSampleResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSampleResponseIncludes(BaseModel):
    """Nested model for PostsSampleResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_firehose_pt


class PostsFirehosePtResponse(BaseModel):
    """Response model for posts_firehose_pt"""

    data: Optional["PostsFirehosePtResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsFirehosePtResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseData(BaseModel):
    """Nested model for PostsFirehosePtResponseData"""

    attachments: Optional["PostsFirehosePtResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsFirehosePtResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsFirehosePtResponseDataEntities"] = None
    geo: Optional["PostsFirehosePtResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsFirehosePtResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsFirehosePtResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsFirehosePtResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsFirehosePtResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsFirehosePtResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsFirehosePtResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsFirehosePtResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataAttachments(BaseModel):
    """Nested model for PostsFirehosePtResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataEditControls(BaseModel):
    """Nested model for PostsFirehosePtResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataEntities(BaseModel):
    """Nested model for PostsFirehosePtResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataGeo(BaseModel):
    """Nested model for PostsFirehosePtResponseDataGeo"""

    coordinates: Optional["PostsFirehosePtResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsFirehosePtResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsFirehosePtResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataNoteTweet(BaseModel):
    """Nested model for PostsFirehosePtResponseDataNoteTweet"""

    entities: Optional["PostsFirehosePtResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsFirehosePtResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsFirehosePtResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsFirehosePtResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsFirehosePtResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataScopes(BaseModel):
    """Nested model for PostsFirehosePtResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseDataWithheld(BaseModel):
    """Nested model for PostsFirehosePtResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehosePtResponseIncludes(BaseModel):
    """Nested model for PostsFirehosePtResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for labels_compliance


class LabelsComplianceResponse(BaseModel):
    """Response model for labels_compliance"""

    data: Optional[Any] = Field(default=None, description="Tweet label data.")
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_firehose_en


class PostsFirehoseEnResponse(BaseModel):
    """Response model for posts_firehose_en"""

    data: Optional["PostsFirehoseEnResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsFirehoseEnResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseData(BaseModel):
    """Nested model for PostsFirehoseEnResponseData"""

    attachments: Optional["PostsFirehoseEnResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsFirehoseEnResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsFirehoseEnResponseDataEntities"] = None
    geo: Optional["PostsFirehoseEnResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsFirehoseEnResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsFirehoseEnResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsFirehoseEnResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsFirehoseEnResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsFirehoseEnResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsFirehoseEnResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsFirehoseEnResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataAttachments(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataEditControls(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataEntities(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataGeo(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataGeo"""

    coordinates: Optional["PostsFirehoseEnResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataNoteTweet(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataNoteTweet"""

    entities: Optional["PostsFirehoseEnResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataScopes(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseDataWithheld(BaseModel):
    """Nested model for PostsFirehoseEnResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseEnResponseIncludes(BaseModel):
    """Nested model for PostsFirehoseEnResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_rules


class GetRulesResponse(BaseModel):
    """Response model for get_rules"""

    data: Optional[List] = None
    meta: Optional["GetRulesResponseMeta"] = Field(default_factory=dict)

    model_config = ConfigDict(populate_by_name=True)


class GetRulesResponseMeta(BaseModel):
    """Nested model for GetRulesResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None
    sent: Optional[str] = None
    summary: Any = None

    model_config = ConfigDict(populate_by_name=True)


# Models for update_rules


class UpdateRulesRequest(BaseModel):
    """Request model for update_rules"""

    add: Optional[List] = Field(default=None)
    delete: Optional[Dict[str, Any]] = Field(
        default=None,
        description="IDs and values of all deleted user-specified stream filtering rules.",
    )

    model_config = ConfigDict(populate_by_name=True)


class UpdateRulesResponse(BaseModel):
    """Response model for update_rules"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["UpdateRulesResponseMeta"] = Field(default_factory=dict)

    model_config = ConfigDict(populate_by_name=True)


class UpdateRulesResponseMeta(BaseModel):
    """Nested model for UpdateRulesResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None
    sent: Optional[str] = None
    summary: Any = None

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_sample10


class PostsSample10Response(BaseModel):
    """Response model for posts_sample10"""

    data: Optional["PostsSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsSample10ResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseData(BaseModel):
    """Nested model for PostsSample10ResponseData"""

    attachments: Optional["PostsSample10ResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsSample10ResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsSample10ResponseDataEntities"] = None
    geo: Optional["PostsSample10ResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsSample10ResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsSample10ResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsSample10ResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsSample10ResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsSample10ResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsSample10ResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsSample10ResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataAttachments(BaseModel):
    """Nested model for PostsSample10ResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataEditControls(BaseModel):
    """Nested model for PostsSample10ResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataEntities(BaseModel):
    """Nested model for PostsSample10ResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataGeo(BaseModel):
    """Nested model for PostsSample10ResponseDataGeo"""

    coordinates: Optional["PostsSample10ResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsSample10ResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsSample10ResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataNoteTweet(BaseModel):
    """Nested model for PostsSample10ResponseDataNoteTweet"""

    entities: Optional["PostsSample10ResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsSample10ResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsSample10ResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsSample10ResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsSample10ResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataScopes(BaseModel):
    """Nested model for PostsSample10ResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseDataWithheld(BaseModel):
    """Nested model for PostsSample10ResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsSample10ResponseIncludes(BaseModel):
    """Nested model for PostsSample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_compliance


class PostsComplianceResponse(BaseModel):
    """Response model for posts_compliance"""

    data: Optional[Any] = Field(default=None, description="Tweet compliance data.")
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_firehose


class PostsFirehoseResponse(BaseModel):
    """Response model for posts_firehose"""

    data: Optional["PostsFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsFirehoseResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseData(BaseModel):
    """Nested model for PostsFirehoseResponseData"""

    attachments: Optional["PostsFirehoseResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsFirehoseResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsFirehoseResponseDataEntities"] = None
    geo: Optional["PostsFirehoseResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsFirehoseResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsFirehoseResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsFirehoseResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsFirehoseResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsFirehoseResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsFirehoseResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsFirehoseResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataAttachments(BaseModel):
    """Nested model for PostsFirehoseResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataEditControls(BaseModel):
    """Nested model for PostsFirehoseResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataEntities(BaseModel):
    """Nested model for PostsFirehoseResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataGeo(BaseModel):
    """Nested model for PostsFirehoseResponseDataGeo"""

    coordinates: Optional["PostsFirehoseResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsFirehoseResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataNoteTweet(BaseModel):
    """Nested model for PostsFirehoseResponseDataNoteTweet"""

    entities: Optional["PostsFirehoseResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsFirehoseResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsFirehoseResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsFirehoseResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataScopes(BaseModel):
    """Nested model for PostsFirehoseResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseDataWithheld(BaseModel):
    """Nested model for PostsFirehoseResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseResponseIncludes(BaseModel):
    """Nested model for PostsFirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for users_compliance


class UsersComplianceResponse(BaseModel):
    """Response model for users_compliance"""

    data: Optional[Any] = Field(default=None, description="User compliance data.")
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for posts_firehose_ja


class PostsFirehoseJaResponse(BaseModel):
    """Response model for posts_firehose_ja"""

    data: Optional["PostsFirehoseJaResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsFirehoseJaResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseData(BaseModel):
    """Nested model for PostsFirehoseJaResponseData"""

    attachments: Optional["PostsFirehoseJaResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsFirehoseJaResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsFirehoseJaResponseDataEntities"] = None
    geo: Optional["PostsFirehoseJaResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsFirehoseJaResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsFirehoseJaResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsFirehoseJaResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsFirehoseJaResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsFirehoseJaResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsFirehoseJaResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsFirehoseJaResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataAttachments(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataEditControls(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataEntities(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataGeo(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataGeo"""

    coordinates: Optional["PostsFirehoseJaResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataNoteTweet(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataNoteTweet"""

    entities: Optional["PostsFirehoseJaResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataScopes(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseDataWithheld(BaseModel):
    """Nested model for PostsFirehoseJaResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsFirehoseJaResponseIncludes(BaseModel):
    """Nested model for PostsFirehoseJaResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for posts


class PostsResponse(BaseModel):
    """Response model for posts"""

    data: Optional["PostsResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["PostsResponseIncludes"] = None
    matching_rules: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseData(BaseModel):
    """Nested model for PostsResponseData"""

    attachments: Optional["PostsResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["PostsResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["PostsResponseDataEntities"] = None
    geo: Optional["PostsResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["PostsResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["PostsResponseDataNoteTweet"] = None
    organic_metrics: Optional["PostsResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["PostsResponseDataPromotedMetrics"] = None
    public_metrics: Optional["PostsResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["PostsResponseDataScopes"] = None
    source: Optional[str] = None
    suggested_source_links: Optional[List] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["PostsResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataAttachments(BaseModel):
    """Nested model for PostsResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataEditControls(BaseModel):
    """Nested model for PostsResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataEntities(BaseModel):
    """Nested model for PostsResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataGeo(BaseModel):
    """Nested model for PostsResponseDataGeo"""

    coordinates: Optional["PostsResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataGeoCoordinates(BaseModel):
    """Nested model for PostsResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataNonPublicMetrics(BaseModel):
    """Nested model for PostsResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataNoteTweet(BaseModel):
    """Nested model for PostsResponseDataNoteTweet"""

    entities: Optional["PostsResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataNoteTweetEntities(BaseModel):
    """Nested model for PostsResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataOrganicMetrics(BaseModel):
    """Nested model for PostsResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataPromotedMetrics(BaseModel):
    """Nested model for PostsResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataPublicMetrics(BaseModel):
    """Nested model for PostsResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataScopes(BaseModel):
    """Nested model for PostsResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseDataWithheld(BaseModel):
    """Nested model for PostsResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PostsResponseIncludes(BaseModel):
    """Nested model for PostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for likes_firehose


class LikesFirehoseResponse(BaseModel):
    """Response model for likes_firehose"""

    data: Optional["LikesFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["LikesFirehoseResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class LikesFirehoseResponseData(BaseModel):
    """Nested model for LikesFirehoseResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class LikesFirehoseResponseIncludes(BaseModel):
    """Nested model for LikesFirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for likes_compliance


class LikesComplianceResponse(BaseModel):
    """Response model for likes_compliance"""

    data: Optional[Dict[str, Any]] = Field(default=None)
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for likes_sample10


class LikesSample10Response(BaseModel):
    """Response model for likes_sample10"""

    data: Optional["LikesSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["LikesSample10ResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class LikesSample10ResponseData(BaseModel):
    """Nested model for LikesSample10ResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class LikesSample10ResponseIncludes(BaseModel):
    """Nested model for LikesSample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)
