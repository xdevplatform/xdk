"""
Stream models for the X API.

This module provides models for the Stream endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for streamPostsFirehose


class StreampostsfirehoseResponse(BaseModel):
    """Response model for streamPostsFirehose"""

    data: Optional["StreampostsfirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostsfirehoseResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseData(BaseModel):
    """Nested model for StreampostsfirehoseResponseData"""

    attachments: Optional["StreampostsfirehoseResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostsfirehoseResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostsfirehoseResponseDataEntities"] = None
    geo: Optional["StreampostsfirehoseResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreampostsfirehoseResponseDataNonPublicMetrics"] = (
        None
    )
    note_tweet: Optional["StreampostsfirehoseResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostsfirehoseResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostsfirehoseResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreampostsfirehoseResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostsfirehoseResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostsfirehoseResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataAttachments(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataEditControls(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataEntities(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataGeo(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataGeo"""

    coordinates: Optional["StreampostsfirehoseResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataNoteTweet"""

    entities: Optional["StreampostsfirehoseResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataScopes(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseDataWithheld(BaseModel):
    """Nested model for StreampostsfirehoseResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseResponseIncludes(BaseModel):
    """Nested model for StreampostsfirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsCompliance


class StreampostscomplianceResponse(BaseModel):
    """Response model for streamPostsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehoseEn


class StreampostsfirehoseenResponse(BaseModel):
    """Response model for streamPostsFirehoseEn"""

    data: Optional["StreampostsfirehoseenResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostsfirehoseenResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseData(BaseModel):
    """Nested model for StreampostsfirehoseenResponseData"""

    attachments: Optional["StreampostsfirehoseenResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostsfirehoseenResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostsfirehoseenResponseDataEntities"] = None
    geo: Optional["StreampostsfirehoseenResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreampostsfirehoseenResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreampostsfirehoseenResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostsfirehoseenResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostsfirehoseenResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreampostsfirehoseenResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostsfirehoseenResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostsfirehoseenResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataAttachments(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataEditControls(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataEntities(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataGeo(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataGeo"""

    coordinates: Optional["StreampostsfirehoseenResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataNoteTweet"""

    entities: Optional["StreampostsfirehoseenResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataScopes(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseDataWithheld(BaseModel):
    """Nested model for StreampostsfirehoseenResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseenResponseIncludes(BaseModel):
    """Nested model for StreampostsfirehoseenResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsSample


class StreampostssampleResponse(BaseModel):
    """Response model for streamPostsSample"""

    data: Optional["StreampostssampleResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostssampleResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseData(BaseModel):
    """Nested model for StreampostssampleResponseData"""

    attachments: Optional["StreampostssampleResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostssampleResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostssampleResponseDataEntities"] = None
    geo: Optional["StreampostssampleResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreampostssampleResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["StreampostssampleResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostssampleResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostssampleResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreampostssampleResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostssampleResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostssampleResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataAttachments(BaseModel):
    """Nested model for StreampostssampleResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataEditControls(BaseModel):
    """Nested model for StreampostssampleResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataEntities(BaseModel):
    """Nested model for StreampostssampleResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataGeo(BaseModel):
    """Nested model for StreampostssampleResponseDataGeo"""

    coordinates: Optional["StreampostssampleResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostssampleResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostssampleResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostssampleResponseDataNoteTweet"""

    entities: Optional["StreampostssampleResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostssampleResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostssampleResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostssampleResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostssampleResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataScopes(BaseModel):
    """Nested model for StreampostssampleResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseDataWithheld(BaseModel):
    """Nested model for StreampostssampleResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostssampleResponseIncludes(BaseModel):
    """Nested model for StreampostssampleResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPosts


class StreampostsResponse(BaseModel):
    """Response model for streamPosts"""

    data: Optional["StreampostsResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostsResponseIncludes"] = None
    matching_rules: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseData(BaseModel):
    """Nested model for StreampostsResponseData"""

    attachments: Optional["StreampostsResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostsResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostsResponseDataEntities"] = None
    geo: Optional["StreampostsResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreampostsResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["StreampostsResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostsResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostsResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreampostsResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostsResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostsResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataAttachments(BaseModel):
    """Nested model for StreampostsResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataEditControls(BaseModel):
    """Nested model for StreampostsResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataEntities(BaseModel):
    """Nested model for StreampostsResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataGeo(BaseModel):
    """Nested model for StreampostsResponseDataGeo"""

    coordinates: Optional["StreampostsResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostsResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostsResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostsResponseDataNoteTweet"""

    entities: Optional["StreampostsResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostsResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostsResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostsResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostsResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataScopes(BaseModel):
    """Nested model for StreampostsResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseDataWithheld(BaseModel):
    """Nested model for StreampostsResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsResponseIncludes(BaseModel):
    """Nested model for StreampostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getRuleCounts


class GetrulecountsResponse(BaseModel):
    """Response model for getRuleCounts"""

    data: Optional["GetrulecountsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetrulecountsResponseData(BaseModel):
    """Nested model for GetrulecountsResponseData"""

    all_project_client_apps: Optional[List] = None
    cap_per_client_app: Optional[int] = None
    cap_per_project: Optional[int] = None
    client_app_rules_count: Optional["GetrulecountsResponseDataClientAppRulesCount"] = (
        None
    )
    project_rules_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetrulecountsResponseDataClientAppRulesCount(BaseModel):
    """Nested model for GetrulecountsResponseDataClientAppRulesCount"""

    client_app_id: Optional[str] = None
    rule_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesSample10


class Streamlikessample10Response(BaseModel):
    """Response model for streamLikesSample10"""

    data: Optional["Streamlikessample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["Streamlikessample10ResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streamlikessample10ResponseData(BaseModel):
    """Nested model for Streamlikessample10ResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streamlikessample10ResponseIncludes(BaseModel):
    """Nested model for Streamlikessample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehoseKo


class StreampostsfirehosekoResponse(BaseModel):
    """Response model for streamPostsFirehoseKo"""

    data: Optional["StreampostsfirehosekoResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostsfirehosekoResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseData(BaseModel):
    """Nested model for StreampostsfirehosekoResponseData"""

    attachments: Optional["StreampostsfirehosekoResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostsfirehosekoResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostsfirehosekoResponseDataEntities"] = None
    geo: Optional["StreampostsfirehosekoResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreampostsfirehosekoResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreampostsfirehosekoResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostsfirehosekoResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostsfirehosekoResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreampostsfirehosekoResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostsfirehosekoResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostsfirehosekoResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataAttachments(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataEditControls(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataEntities(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataGeo(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataGeo"""

    coordinates: Optional["StreampostsfirehosekoResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataNoteTweet"""

    entities: Optional["StreampostsfirehosekoResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataScopes(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseDataWithheld(BaseModel):
    """Nested model for StreampostsfirehosekoResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosekoResponseIncludes(BaseModel):
    """Nested model for StreampostsfirehosekoResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehoseJa


class StreampostsfirehosejaResponse(BaseModel):
    """Response model for streamPostsFirehoseJa"""

    data: Optional["StreampostsfirehosejaResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostsfirehosejaResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseData(BaseModel):
    """Nested model for StreampostsfirehosejaResponseData"""

    attachments: Optional["StreampostsfirehosejaResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostsfirehosejaResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostsfirehosejaResponseDataEntities"] = None
    geo: Optional["StreampostsfirehosejaResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreampostsfirehosejaResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreampostsfirehosejaResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostsfirehosejaResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostsfirehosejaResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreampostsfirehosejaResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostsfirehosejaResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostsfirehosejaResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataAttachments(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataEditControls(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataEntities(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataGeo(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataGeo"""

    coordinates: Optional["StreampostsfirehosejaResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataNoteTweet"""

    entities: Optional["StreampostsfirehosejaResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataScopes(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseDataWithheld(BaseModel):
    """Nested model for StreampostsfirehosejaResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehosejaResponseIncludes(BaseModel):
    """Nested model for StreampostsfirehosejaResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamUsersCompliance


class StreamuserscomplianceResponse(BaseModel):
    """Response model for streamUsersCompliance"""

    data: Optional[Any] = Field(default=None, description="User compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLabelsCompliance


class StreamlabelscomplianceResponse(BaseModel):
    """Response model for streamLabelsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet label data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesFirehose


class StreamlikesfirehoseResponse(BaseModel):
    """Response model for streamLikesFirehose"""

    data: Optional["StreamlikesfirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamlikesfirehoseResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamlikesfirehoseResponseData(BaseModel):
    """Nested model for StreamlikesfirehoseResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamlikesfirehoseResponseIncludes(BaseModel):
    """Nested model for StreamlikesfirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getRules


class GetrulesResponse(BaseModel):
    """Response model for getRules"""

    data: Optional[List] = None
    meta: Optional["GetrulesResponseMeta"] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetrulesResponseMeta(BaseModel):
    """Nested model for GetrulesResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None
    sent: Optional[str] = None
    summary: Any = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for updateRules


class UpdaterulesRequest(BaseModel):
    """Request model for updateRules"""

    add: Optional[List] = Field(default=None)
    delete: Optional[Dict[str, Any]] = Field(
        default=None,
        description="IDs and values of all deleted user-specified stream filtering rules.",
    )

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UpdaterulesResponse(BaseModel):
    """Response model for updateRules"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["UpdaterulesResponseMeta"] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UpdaterulesResponseMeta(BaseModel):
    """Nested model for UpdaterulesResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None
    sent: Optional[str] = None
    summary: Any = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesCompliance


class StreamlikescomplianceResponse(BaseModel):
    """Response model for streamLikesCompliance"""

    data: Optional[Dict[str, Any]] = Field(default=None)
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsSample10


class Streampostssample10Response(BaseModel):
    """Response model for streamPostsSample10"""

    data: Optional["Streampostssample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["Streampostssample10ResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseData(BaseModel):
    """Nested model for Streampostssample10ResponseData"""

    attachments: Optional["Streampostssample10ResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["Streampostssample10ResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["Streampostssample10ResponseDataEntities"] = None
    geo: Optional["Streampostssample10ResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["Streampostssample10ResponseDataNonPublicMetrics"] = (
        None
    )
    note_tweet: Optional["Streampostssample10ResponseDataNoteTweet"] = None
    organic_metrics: Optional["Streampostssample10ResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["Streampostssample10ResponseDataPromotedMetrics"] = None
    public_metrics: Optional["Streampostssample10ResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["Streampostssample10ResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["Streampostssample10ResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataAttachments(BaseModel):
    """Nested model for Streampostssample10ResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataEditControls(BaseModel):
    """Nested model for Streampostssample10ResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataEntities(BaseModel):
    """Nested model for Streampostssample10ResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataGeo(BaseModel):
    """Nested model for Streampostssample10ResponseDataGeo"""

    coordinates: Optional["Streampostssample10ResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataGeoCoordinates(BaseModel):
    """Nested model for Streampostssample10ResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataNonPublicMetrics(BaseModel):
    """Nested model for Streampostssample10ResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataNoteTweet(BaseModel):
    """Nested model for Streampostssample10ResponseDataNoteTweet"""

    entities: Optional["Streampostssample10ResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataNoteTweetEntities(BaseModel):
    """Nested model for Streampostssample10ResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataOrganicMetrics(BaseModel):
    """Nested model for Streampostssample10ResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataPromotedMetrics(BaseModel):
    """Nested model for Streampostssample10ResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataPublicMetrics(BaseModel):
    """Nested model for Streampostssample10ResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataScopes(BaseModel):
    """Nested model for Streampostssample10ResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseDataWithheld(BaseModel):
    """Nested model for Streampostssample10ResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class Streampostssample10ResponseIncludes(BaseModel):
    """Nested model for Streampostssample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehosePt


class StreampostsfirehoseptResponse(BaseModel):
    """Response model for streamPostsFirehosePt"""

    data: Optional["StreampostsfirehoseptResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreampostsfirehoseptResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseData(BaseModel):
    """Nested model for StreampostsfirehoseptResponseData"""

    attachments: Optional["StreampostsfirehoseptResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreampostsfirehoseptResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreampostsfirehoseptResponseDataEntities"] = None
    geo: Optional["StreampostsfirehoseptResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreampostsfirehoseptResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreampostsfirehoseptResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreampostsfirehoseptResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreampostsfirehoseptResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreampostsfirehoseptResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreampostsfirehoseptResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreampostsfirehoseptResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataAttachments(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataEditControls(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataEntities(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataGeo(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataGeo"""

    coordinates: Optional["StreampostsfirehoseptResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataNoteTweet(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataNoteTweet"""

    entities: Optional["StreampostsfirehoseptResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataPublicMetrics(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataScopes(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseDataWithheld(BaseModel):
    """Nested model for StreampostsfirehoseptResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreampostsfirehoseptResponseIncludes(BaseModel):
    """Nested model for StreampostsfirehoseptResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
