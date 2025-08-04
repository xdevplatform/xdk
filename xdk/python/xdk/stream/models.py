"""
Stream models for the X API.

This module provides models for the Stream endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for streamLikesFirehose


class StreamLikesFirehoseResponse(BaseModel):
    """Response model for streamLikesFirehose"""

    data: Optional["StreamLikesFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamLikesFirehoseResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamLikesFirehoseResponseData(BaseModel):
    """Nested model for StreamLikesFirehoseResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamLikesFirehoseResponseIncludes(BaseModel):
    """Nested model for StreamLikesFirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamLikesCompliance


class StreamLikesComplianceResponse(BaseModel):
    """Response model for streamLikesCompliance"""

    data: Optional[Dict[str, Any]] = Field(default=None)
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsFirehosePt


class StreamPostsFirehosePtResponse(BaseModel):
    """Response model for streamPostsFirehosePt"""

    data: Optional["StreamPostsFirehosePtResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehosePtResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseData(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseData"""

    attachments: Optional["StreamPostsFirehosePtResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehosePtResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehosePtResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehosePtResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehosePtResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehosePtResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsFirehosePtResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehosePtResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehosePtResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehosePtResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehosePtResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehosePtResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataNoteTweet"""

    entities: Optional["StreamPostsFirehosePtResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehosePtResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsCompliance


class StreamPostsComplianceResponse(BaseModel):
    """Response model for streamPostsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet compliance data.")
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsFirehoseJa


class StreamPostsFirehoseJaResponse(BaseModel):
    """Response model for streamPostsFirehoseJa"""

    data: Optional["StreamPostsFirehoseJaResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseJaResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseData"""

    attachments: Optional["StreamPostsFirehoseJaResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseJaResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseJaResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseJaResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseJaResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseJaResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseJaResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseJaResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehoseJaResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseJaResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseJaResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseJaResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataNoteTweet"""

    entities: Optional["StreamPostsFirehoseJaResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseJaResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsFirehoseEn


class StreamPostsFirehoseEnResponse(BaseModel):
    """Response model for streamPostsFirehoseEn"""

    data: Optional["StreamPostsFirehoseEnResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseEnResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseData"""

    attachments: Optional["StreamPostsFirehoseEnResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseEnResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseEnResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseEnResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseEnResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseEnResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseEnResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseEnResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehoseEnResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseEnResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseEnResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseEnResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataNoteTweet"""

    entities: Optional["StreamPostsFirehoseEnResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseEnResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsSample


class StreamPostsSampleResponse(BaseModel):
    """Response model for streamPostsSample"""

    data: Optional["StreamPostsSampleResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsSampleResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseData(BaseModel):
    """Nested model for StreamPostsSampleResponseData"""

    attachments: Optional["StreamPostsSampleResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsSampleResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsSampleResponseDataEntities"] = None
    geo: Optional["StreamPostsSampleResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreamPostsSampleResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["StreamPostsSampleResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsSampleResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsSampleResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreamPostsSampleResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsSampleResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsSampleResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsSampleResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsSampleResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataEntities(BaseModel):
    """Nested model for StreamPostsSampleResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataGeo(BaseModel):
    """Nested model for StreamPostsSampleResponseDataGeo"""

    coordinates: Optional["StreamPostsSampleResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsSampleResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsSampleResponseDataNoteTweet"""

    entities: Optional["StreamPostsSampleResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsSampleResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataScopes(BaseModel):
    """Nested model for StreamPostsSampleResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsSampleResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSampleResponseIncludes(BaseModel):
    """Nested model for StreamPostsSampleResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getRules


class GetRulesResponse(BaseModel):
    """Response model for getRules"""

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


# Models for updateRules


class UpdateRulesRequest(BaseModel):
    """Request model for updateRules"""

    add: Optional[List] = Field(default=None)
    delete: Optional[Dict[str, Any]] = Field(
        default=None,
        description="IDs and values of all deleted user-specified stream filtering rules.",
    )

    model_config = ConfigDict(populate_by_name=True)


class UpdateRulesResponse(BaseModel):
    """Response model for updateRules"""

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


# Models for streamUsersCompliance


class StreamUsersComplianceResponse(BaseModel):
    """Response model for streamUsersCompliance"""

    data: Optional[Any] = Field(default=None, description="User compliance data.")
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsFirehoseKo


class StreamPostsFirehoseKoResponse(BaseModel):
    """Response model for streamPostsFirehoseKo"""

    data: Optional["StreamPostsFirehoseKoResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseKoResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseData"""

    attachments: Optional["StreamPostsFirehoseKoResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseKoResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseKoResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseKoResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseKoResponseDataNonPublicMetrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseKoResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseKoResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseKoResponseDataPromotedMetrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehoseKoResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseKoResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseKoResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseKoResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataNoteTweet"""

    entities: Optional["StreamPostsFirehoseKoResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseKoResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getRuleCounts


class GetRuleCountsResponse(BaseModel):
    """Response model for getRuleCounts"""

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


# Models for streamPostsFirehose


class StreamPostsFirehoseResponse(BaseModel):
    """Response model for streamPostsFirehose"""

    data: Optional["StreamPostsFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseResponseData"""

    attachments: Optional["StreamPostsFirehoseResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreamPostsFirehoseResponseDataNonPublicMetrics"] = (
        None
    )
    note_tweet: Optional["StreamPostsFirehoseResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreamPostsFirehoseResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataNoteTweet"""

    entities: Optional["StreamPostsFirehoseResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsFirehoseResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPostsSample10


class StreamPostsSample10Response(BaseModel):
    """Response model for streamPostsSample10"""

    data: Optional["StreamPostsSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsSample10ResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseData(BaseModel):
    """Nested model for StreamPostsSample10ResponseData"""

    attachments: Optional["StreamPostsSample10ResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsSample10ResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsSample10ResponseDataEntities"] = None
    geo: Optional["StreamPostsSample10ResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreamPostsSample10ResponseDataNonPublicMetrics"] = (
        None
    )
    note_tweet: Optional["StreamPostsSample10ResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsSample10ResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsSample10ResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreamPostsSample10ResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsSample10ResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsSample10ResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataEntities(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataGeo(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataGeo"""

    coordinates: Optional["StreamPostsSample10ResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataNoteTweet"""

    entities: Optional["StreamPostsSample10ResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataScopes(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsSample10ResponseIncludes(BaseModel):
    """Nested model for StreamPostsSample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamLikesSample10


class StreamLikesSample10Response(BaseModel):
    """Response model for streamLikesSample10"""

    data: Optional["StreamLikesSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamLikesSample10ResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamLikesSample10ResponseData(BaseModel):
    """Nested model for StreamLikesSample10ResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamLikesSample10ResponseIncludes(BaseModel):
    """Nested model for StreamLikesSample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for streamLabelsCompliance


class StreamLabelsComplianceResponse(BaseModel):
    """Response model for streamLabelsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet label data.")
    errors: Optional[List] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


# Models for streamPosts


class StreamPostsResponse(BaseModel):
    """Response model for streamPosts"""

    data: Optional["StreamPostsResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsResponseIncludes"] = None
    matching_rules: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseData(BaseModel):
    """Nested model for StreamPostsResponseData"""

    attachments: Optional["StreamPostsResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsResponseDataEntities"] = None
    geo: Optional["StreamPostsResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreamPostsResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["StreamPostsResponseDataNoteTweet"] = None
    organic_metrics: Optional["StreamPostsResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsResponseDataPromotedMetrics"] = None
    public_metrics: Optional["StreamPostsResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataEditControls(BaseModel):
    """Nested model for StreamPostsResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataEntities(BaseModel):
    """Nested model for StreamPostsResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataGeo(BaseModel):
    """Nested model for StreamPostsResponseDataGeo"""

    coordinates: Optional["StreamPostsResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataNonPublicMetrics(BaseModel):
    """Nested model for StreamPostsResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataNoteTweet(BaseModel):
    """Nested model for StreamPostsResponseDataNoteTweet"""

    entities: Optional["StreamPostsResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataNoteTweetEntities(BaseModel):
    """Nested model for StreamPostsResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataOrganicMetrics(BaseModel):
    """Nested model for StreamPostsResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataPromotedMetrics(BaseModel):
    """Nested model for StreamPostsResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataPublicMetrics(BaseModel):
    """Nested model for StreamPostsResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataScopes(BaseModel):
    """Nested model for StreamPostsResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class StreamPostsResponseIncludes(BaseModel):
    """Nested model for StreamPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)
