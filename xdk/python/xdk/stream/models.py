"""
Stream models for the X API.

This module provides models for the Stream endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for streamLabelsCompliance


class StreamLabelsComplianceResponse(BaseModel):
    """Response model for streamLabelsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet label data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getRules


class GetRulesResponse(BaseModel):
    """Response model for getRules"""

    data: Optional[List] = None
    meta: Optional["GetRulesResponseMeta"] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetRulesResponseMeta(BaseModel):
    """Nested model for GetRulesResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None
    sent: Optional[str] = None
    summary: Any = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for updateRules


class UpdateRulesRequest(BaseModel):
    """Request model for updateRules"""

    add: Optional[List] = Field(default=None)
    delete: Optional[Dict[str, Any]] = Field(
        default=None,
        description="IDs and values of all deleted user-specified stream filtering rules.",
    )

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UpdateRulesResponse(BaseModel):
    """Response model for updateRules"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["UpdateRulesResponseMeta"] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UpdateRulesResponseMeta(BaseModel):
    """Nested model for UpdateRulesResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None
    sent: Optional[str] = None
    summary: Any = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsSample10


class StreamPostsSample10Response(BaseModel):
    """Response model for streamPostsSample10"""

    data: Optional["StreamPostsSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsSample10ResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseData(BaseModel):
    """Nested model for StreamPostsSample10ResponseData"""

    attachments: Optional["StreamPostsSample10ResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsSample10ResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsSample10ResponseDataEntities"] = None
    geo: Optional["StreamPostsSample10ResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsSample10ResponseDataNon_public_metrics"
    ] = None
    note_tweet: Optional["StreamPostsSample10ResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsSample10ResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsSample10ResponseDataPromoted_metrics"] = None
    public_metrics: Optional["StreamPostsSample10ResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsSample10ResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsSample10ResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataEntities(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataGeo(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataGeo"""

    coordinates: Optional["StreamPostsSample10ResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataNote_tweet"""

    entities: Optional["StreamPostsSample10ResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataScopes(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsSample10ResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSample10ResponseIncludes(BaseModel):
    """Nested model for StreamPostsSample10ResponseIncludes"""

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


class StreamPostsComplianceResponse(BaseModel):
    """Response model for streamPostsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesFirehose


class StreamLikesFirehoseResponse(BaseModel):
    """Response model for streamLikesFirehose"""

    data: Optional["StreamLikesFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamLikesFirehoseResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesFirehoseResponseData(BaseModel):
    """Nested model for StreamLikesFirehoseResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesFirehoseResponseIncludes(BaseModel):
    """Nested model for StreamLikesFirehoseResponseIncludes"""

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


class StreamUsersComplianceResponse(BaseModel):
    """Response model for streamUsersCompliance"""

    data: Optional[Any] = Field(default=None, description="User compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehosePt


class StreamPostsFirehosePtResponse(BaseModel):
    """Response model for streamPostsFirehosePt"""

    data: Optional["StreamPostsFirehosePtResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehosePtResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseData(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseData"""

    attachments: Optional["StreamPostsFirehosePtResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehosePtResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehosePtResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehosePtResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehosePtResponseDataNon_public_metrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehosePtResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsFirehosePtResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehosePtResponseDataPromoted_metrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehosePtResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehosePtResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehosePtResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehosePtResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataNote_tweet"""

    entities: Optional["StreamPostsFirehosePtResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehosePtResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehosePtResponseIncludes"""

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


class StreamPostsSampleResponse(BaseModel):
    """Response model for streamPostsSample"""

    data: Optional["StreamPostsSampleResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsSampleResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseData(BaseModel):
    """Nested model for StreamPostsSampleResponseData"""

    attachments: Optional["StreamPostsSampleResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsSampleResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsSampleResponseDataEntities"] = None
    geo: Optional["StreamPostsSampleResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreamPostsSampleResponseDataNon_public_metrics"] = (
        None
    )
    note_tweet: Optional["StreamPostsSampleResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsSampleResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsSampleResponseDataPromoted_metrics"] = None
    public_metrics: Optional["StreamPostsSampleResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsSampleResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsSampleResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsSampleResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsSampleResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataEntities(BaseModel):
    """Nested model for StreamPostsSampleResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataGeo(BaseModel):
    """Nested model for StreamPostsSampleResponseDataGeo"""

    coordinates: Optional["StreamPostsSampleResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsSampleResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsSampleResponseDataNote_tweet"""

    entities: Optional["StreamPostsSampleResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsSampleResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsSampleResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataScopes(BaseModel):
    """Nested model for StreamPostsSampleResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsSampleResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsSampleResponseIncludes(BaseModel):
    """Nested model for StreamPostsSampleResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehose


class StreamPostsFirehoseResponse(BaseModel):
    """Response model for streamPostsFirehose"""

    data: Optional["StreamPostsFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseResponseData"""

    attachments: Optional["StreamPostsFirehoseResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseResponseDataNon_public_metrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseResponseDataPromoted_metrics"] = None
    public_metrics: Optional["StreamPostsFirehoseResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataNote_tweet"""

    entities: Optional["StreamPostsFirehoseResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesCompliance


class StreamLikesComplianceResponse(BaseModel):
    """Response model for streamLikesCompliance"""

    data: Optional[Dict[str, Any]] = Field(default=None)
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehoseEn


class StreamPostsFirehoseEnResponse(BaseModel):
    """Response model for streamPostsFirehoseEn"""

    data: Optional["StreamPostsFirehoseEnResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseEnResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseData"""

    attachments: Optional["StreamPostsFirehoseEnResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseEnResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseEnResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseEnResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseEnResponseDataNon_public_metrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseEnResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseEnResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseEnResponseDataPromoted_metrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehoseEnResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseEnResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseEnResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseEnResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataNote_tweet"""

    entities: Optional["StreamPostsFirehoseEnResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseEnResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseEnResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesSample10


class StreamLikesSample10Response(BaseModel):
    """Response model for streamLikesSample10"""

    data: Optional["StreamLikesSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamLikesSample10ResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesSample10ResponseData(BaseModel):
    """Nested model for StreamLikesSample10ResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesSample10ResponseIncludes(BaseModel):
    """Nested model for StreamLikesSample10ResponseIncludes"""

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


class StreamPostsFirehoseKoResponse(BaseModel):
    """Response model for streamPostsFirehoseKo"""

    data: Optional["StreamPostsFirehoseKoResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseKoResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseData"""

    attachments: Optional["StreamPostsFirehoseKoResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseKoResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseKoResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseKoResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseKoResponseDataNon_public_metrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseKoResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseKoResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseKoResponseDataPromoted_metrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehoseKoResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseKoResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseKoResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseKoResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataNote_tweet"""

    entities: Optional["StreamPostsFirehoseKoResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseKoResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseKoResponseIncludes"""

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


class GetRuleCountsResponse(BaseModel):
    """Response model for getRuleCounts"""

    data: Optional["GetRuleCountsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetRuleCountsResponseData(BaseModel):
    """Nested model for GetRuleCountsResponseData"""

    all_project_client_apps: Optional[List] = None
    cap_per_client_app: Optional[int] = None
    cap_per_project: Optional[int] = None
    client_app_rules_count: Optional[
        "GetRuleCountsResponseDataClient_app_rules_count"
    ] = None
    project_rules_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetRuleCountsResponseDataClient_app_rules_count(BaseModel):
    """Nested model for GetRuleCountsResponseDataClient_app_rules_count"""

    client_app_id: Optional[str] = None
    rule_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsFirehoseJa


class StreamPostsFirehoseJaResponse(BaseModel):
    """Response model for streamPostsFirehoseJa"""

    data: Optional["StreamPostsFirehoseJaResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsFirehoseJaResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseData(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseData"""

    attachments: Optional["StreamPostsFirehoseJaResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsFirehoseJaResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsFirehoseJaResponseDataEntities"] = None
    geo: Optional["StreamPostsFirehoseJaResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional[
        "StreamPostsFirehoseJaResponseDataNon_public_metrics"
    ] = None
    note_tweet: Optional["StreamPostsFirehoseJaResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsFirehoseJaResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsFirehoseJaResponseDataPromoted_metrics"] = (
        None
    )
    public_metrics: Optional["StreamPostsFirehoseJaResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsFirehoseJaResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsFirehoseJaResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataEntities(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataGeo(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataGeo"""

    coordinates: Optional["StreamPostsFirehoseJaResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataNote_tweet"""

    entities: Optional["StreamPostsFirehoseJaResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataScopes(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsFirehoseJaResponseIncludes(BaseModel):
    """Nested model for StreamPostsFirehoseJaResponseIncludes"""

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


class StreamPostsResponse(BaseModel):
    """Response model for streamPosts"""

    data: Optional["StreamPostsResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamPostsResponseIncludes"] = None
    matching_rules: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseData(BaseModel):
    """Nested model for StreamPostsResponseData"""

    attachments: Optional["StreamPostsResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["StreamPostsResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["StreamPostsResponseDataEntities"] = None
    geo: Optional["StreamPostsResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["StreamPostsResponseDataNon_public_metrics"] = None
    note_tweet: Optional["StreamPostsResponseDataNote_tweet"] = None
    organic_metrics: Optional["StreamPostsResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["StreamPostsResponseDataPromoted_metrics"] = None
    public_metrics: Optional["StreamPostsResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["StreamPostsResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["StreamPostsResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataAttachments(BaseModel):
    """Nested model for StreamPostsResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataEdit_controls(BaseModel):
    """Nested model for StreamPostsResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataEntities(BaseModel):
    """Nested model for StreamPostsResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataGeo(BaseModel):
    """Nested model for StreamPostsResponseDataGeo"""

    coordinates: Optional["StreamPostsResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataGeoCoordinates(BaseModel):
    """Nested model for StreamPostsResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataNon_public_metrics(BaseModel):
    """Nested model for StreamPostsResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataNote_tweet(BaseModel):
    """Nested model for StreamPostsResponseDataNote_tweet"""

    entities: Optional["StreamPostsResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataNote_tweetEntities(BaseModel):
    """Nested model for StreamPostsResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataOrganic_metrics(BaseModel):
    """Nested model for StreamPostsResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataPromoted_metrics(BaseModel):
    """Nested model for StreamPostsResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataPublic_metrics(BaseModel):
    """Nested model for StreamPostsResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataScopes(BaseModel):
    """Nested model for StreamPostsResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseDataWithheld(BaseModel):
    """Nested model for StreamPostsResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamPostsResponseIncludes(BaseModel):
    """Nested model for StreamPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
