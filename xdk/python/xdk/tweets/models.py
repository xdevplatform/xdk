"""
Tweets models for the X API.

This module provides models for the Tweets endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


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


# Models for searchPostsRecent


class SearchPostsRecentResponse(BaseModel):
    """Response model for searchPostsRecent"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchPostsRecentResponseIncludes"] = None
    meta: Optional["SearchPostsRecentResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchPostsRecentResponseIncludes(BaseModel):
    """Nested model for SearchPostsRecentResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchPostsRecentResponseMeta(BaseModel):
    """Nested model for SearchPostsRecentResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for getInsightsHistorical


class GetInsightsHistoricalResponse(BaseModel):
    """Response model for getInsightsHistorical"""

    data: Optional[List] = None
    errors: Optional[List] = None

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


# Models for getUsersLikedPosts


class GetUsersLikedPostsResponse(BaseModel):
    """Response model for getUsersLikedPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersLikedPostsResponseIncludes"] = None
    meta: Optional["GetUsersLikedPostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersLikedPostsResponseIncludes(BaseModel):
    """Nested model for GetUsersLikedPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersLikedPostsResponseMeta(BaseModel):
    """Nested model for GetUsersLikedPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersPosts


class GetUsersPostsResponse(BaseModel):
    """Response model for getUsersPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersPostsResponseIncludes"] = None
    meta: Optional["GetUsersPostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersPostsResponseIncludes(BaseModel):
    """Nested model for GetUsersPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersPostsResponseMeta(BaseModel):
    """Nested model for GetUsersPostsResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for getPostsById


class GetPostsByIdResponse(BaseModel):
    """Response model for getPostsById"""

    data: Optional["GetPostsByIdResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsByIdResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseData(BaseModel):
    """Nested model for GetPostsByIdResponseData"""

    attachments: Optional["GetPostsByIdResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["GetPostsByIdResponseDataEdit_controls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["GetPostsByIdResponseDataEntities"] = None
    geo: Optional["GetPostsByIdResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["GetPostsByIdResponseDataNon_public_metrics"] = None
    note_tweet: Optional["GetPostsByIdResponseDataNote_tweet"] = None
    organic_metrics: Optional["GetPostsByIdResponseDataOrganic_metrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["GetPostsByIdResponseDataPromoted_metrics"] = None
    public_metrics: Optional["GetPostsByIdResponseDataPublic_metrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["GetPostsByIdResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["GetPostsByIdResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataAttachments(BaseModel):
    """Nested model for GetPostsByIdResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataEdit_controls(BaseModel):
    """Nested model for GetPostsByIdResponseDataEdit_controls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataEntities(BaseModel):
    """Nested model for GetPostsByIdResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataGeo(BaseModel):
    """Nested model for GetPostsByIdResponseDataGeo"""

    coordinates: Optional["GetPostsByIdResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataGeoCoordinates(BaseModel):
    """Nested model for GetPostsByIdResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataNon_public_metrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataNon_public_metrics"""

    impression_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataNote_tweet(BaseModel):
    """Nested model for GetPostsByIdResponseDataNote_tweet"""

    entities: Optional["GetPostsByIdResponseDataNote_tweetEntities"] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataNote_tweetEntities(BaseModel):
    """Nested model for GetPostsByIdResponseDataNote_tweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataOrganic_metrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataOrganic_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataPromoted_metrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataPromoted_metrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataPublic_metrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataPublic_metrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataScopes(BaseModel):
    """Nested model for GetPostsByIdResponseDataScopes"""

    followers: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseDataWithheld(BaseModel):
    """Nested model for GetPostsByIdResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdResponseIncludes(BaseModel):
    """Nested model for GetPostsByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deletePosts


class DeletePostsResponse(BaseModel):
    """Response model for deletePosts"""

    data: Optional["DeletePostsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeletePostsResponseData(BaseModel):
    """Nested model for DeletePostsResponseData"""

    deleted: Optional[bool] = None

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


# Models for getPostsReposts


class GetPostsRepostsResponse(BaseModel):
    """Response model for getPostsReposts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsRepostsResponseIncludes"] = None
    meta: Optional["GetPostsRepostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsRepostsResponseIncludes(BaseModel):
    """Nested model for GetPostsRepostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsRepostsResponseMeta(BaseModel):
    """Nested model for GetPostsRepostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsAnalytics


class GetPostsAnalyticsResponse(BaseModel):
    """Response model for getPostsAnalytics"""

    data: Optional[List] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for repostPost


class RepostPostRequest(BaseModel):
    """Request model for repostPost"""

    tweet_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class RepostPostResponse(BaseModel):
    """Response model for repostPost"""

    data: Optional["RepostPostResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class RepostPostResponseData(BaseModel):
    """Nested model for RepostPostResponseData"""

    id: Optional[str] = None
    retweeted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesPosts


class GetSpacesPostsResponse(BaseModel):
    """Response model for getSpacesPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesPostsResponseIncludes"] = None
    meta: Optional["GetSpacesPostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesPostsResponseIncludes(BaseModel):
    """Nested model for GetSpacesPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesPostsResponseMeta(BaseModel):
    """Nested model for GetSpacesPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsCountsRecent


class GetPostsCountsRecentResponse(BaseModel):
    """Response model for getPostsCountsRecent"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetPostsCountsRecentResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsCountsRecentResponseMeta(BaseModel):
    """Nested model for GetPostsCountsRecentResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    total_tweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unrepostPost


class UnrepostPostResponse(BaseModel):
    """Response model for unrepostPost"""

    data: Optional["UnrepostPostResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnrepostPostResponseData(BaseModel):
    """Nested model for UnrepostPostResponseData"""

    retweeted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getListsPosts


class GetListsPostsResponse(BaseModel):
    """Response model for getListsPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetListsPostsResponseIncludes"] = None
    meta: Optional["GetListsPostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetListsPostsResponseIncludes(BaseModel):
    """Nested model for GetListsPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetListsPostsResponseMeta(BaseModel):
    """Nested model for GetListsPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsCountsAll


class GetPostsCountsAllResponse(BaseModel):
    """Response model for getPostsCountsAll"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetPostsCountsAllResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsCountsAllResponseMeta(BaseModel):
    """Nested model for GetPostsCountsAllResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    total_tweet_count: Optional[int] = None

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


# Models for searchPostsAll


class SearchPostsAllResponse(BaseModel):
    """Response model for searchPostsAll"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchPostsAllResponseIncludes"] = None
    meta: Optional["SearchPostsAllResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchPostsAllResponseIncludes(BaseModel):
    """Nested model for SearchPostsAllResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchPostsAllResponseMeta(BaseModel):
    """Nested model for SearchPostsAllResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for getSpacesBuyers


class GetSpacesBuyersResponse(BaseModel):
    """Response model for getSpacesBuyers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesBuyersResponseIncludes"] = None
    meta: Optional["GetSpacesBuyersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesBuyersResponseIncludes(BaseModel):
    """Nested model for GetSpacesBuyersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesBuyersResponseMeta(BaseModel):
    """Nested model for GetSpacesBuyersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unlikePost


class UnlikePostResponse(BaseModel):
    """Response model for unlikePost"""

    data: Optional["UnlikePostResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnlikePostResponseData(BaseModel):
    """Nested model for UnlikePostResponseData"""

    liked: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersTimeline


class GetUsersTimelineResponse(BaseModel):
    """Response model for getUsersTimeline"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersTimelineResponseIncludes"] = None
    meta: Optional["GetUsersTimelineResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersTimelineResponseIncludes(BaseModel):
    """Nested model for GetUsersTimelineResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersTimelineResponseMeta(BaseModel):
    """Nested model for GetUsersTimelineResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for likePost


class LikePostRequest(BaseModel):
    """Request model for likePost"""

    tweet_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class LikePostResponse(BaseModel):
    """Response model for likePost"""

    data: Optional["LikePostResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class LikePostResponseData(BaseModel):
    """Nested model for LikePostResponseData"""

    liked: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsQuotedPosts


class GetPostsQuotedPostsResponse(BaseModel):
    """Response model for getPostsQuotedPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsQuotedPostsResponseIncludes"] = None
    meta: Optional["GetPostsQuotedPostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsQuotedPostsResponseIncludes(BaseModel):
    """Nested model for GetPostsQuotedPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsQuotedPostsResponseMeta(BaseModel):
    """Nested model for GetPostsQuotedPostsResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsByIds


class GetPostsByIdsResponse(BaseModel):
    """Response model for getPostsByIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsByIdsResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsByIdsResponseIncludes(BaseModel):
    """Nested model for GetPostsByIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createPosts


class CreatePostsRequest(BaseModel):
    """Request model for createPosts"""

    card_uri: Optional[str] = None
    community_id: Optional[str] = None
    direct_message_deep_link: Optional[str] = None
    for_super_followers_only: Optional[bool] = None
    geo: Optional["CreatePostsRequestGeo"] = None
    media: Optional["CreatePostsRequestMedia"] = Field(
        description="Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.",
        default_factory=dict,
    )
    nullcast: Optional[bool] = None
    poll: Optional["CreatePostsRequestPoll"] = Field(
        description="Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.",
        default_factory=dict,
    )
    quote_tweet_id: Optional[str] = None
    reply: Optional["CreatePostsRequestReply"] = Field(
        description="Tweet information of the Tweet being replied to.",
        default_factory=dict,
    )
    reply_settings: Optional[str] = None
    share_with_followers: Optional[bool] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatePostsResponse(BaseModel):
    """Response model for createPosts"""

    data: Optional["CreatePostsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatePostsRequestGeo(BaseModel):
    """Nested model for CreatePostsRequestGeo"""

    place_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatePostsRequestMedia(BaseModel):
    """Nested model for CreatePostsRequestMedia"""

    media_ids: Optional[List] = None
    tagged_user_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatePostsRequestPoll(BaseModel):
    """Nested model for CreatePostsRequestPoll"""

    duration_minutes: Optional[int] = None
    options: Optional[List] = None
    reply_settings: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatePostsRequestReply(BaseModel):
    """Nested model for CreatePostsRequestReply"""

    exclude_reply_user_ids: Optional[List] = None
    in_reply_to_tweet_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatePostsResponseData(BaseModel):
    """Nested model for CreatePostsResponseData"""

    id: Optional[str] = None
    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for hidePostsReply


class HidePostsReplyRequest(BaseModel):
    """Request model for hidePostsReply"""

    hidden: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class HidePostsReplyResponse(BaseModel):
    """Response model for hidePostsReply"""

    data: Optional["HidePostsReplyResponseData"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class HidePostsReplyResponseData(BaseModel):
    """Nested model for HidePostsReplyResponseData"""

    hidden: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getInsights28Hr


class GetInsights28HrResponse(BaseModel):
    """Response model for getInsights28Hr"""

    data: Optional[List] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersMentions


class GetUsersMentionsResponse(BaseModel):
    """Response model for getUsersMentions"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersMentionsResponseIncludes"] = None
    meta: Optional["GetUsersMentionsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersMentionsResponseIncludes(BaseModel):
    """Nested model for GetUsersMentionsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersMentionsResponseMeta(BaseModel):
    """Nested model for GetUsersMentionsResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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
