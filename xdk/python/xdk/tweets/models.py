"""
Tweets models for the X API.

This module provides models for the Tweets endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for unlikePost


class UnlikePostResponse(BaseModel):
    """Response model for unlikePost"""

    data: Optional["UnlikePostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnlikePostResponseData(BaseModel):
    """Nested model for UnlikePostResponseData"""

    liked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for searchPostsRecent


class SearchPostsRecentResponse(BaseModel):
    """Response model for searchPostsRecent"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchPostsRecentResponseIncludes"] = None
    meta: Optional["SearchPostsRecentResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchPostsRecentResponseIncludes(BaseModel):
    """Nested model for SearchPostsRecentResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchPostsRecentResponseMeta(BaseModel):
    """Nested model for SearchPostsRecentResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getPostsById


class GetPostsByIdResponse(BaseModel):
    """Response model for getPostsById"""

    data: Optional["GetPostsByIdResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseData(BaseModel):
    """Nested model for GetPostsByIdResponseData"""

    attachments: Optional["GetPostsByIdResponseDataAttachments"] = None
    author_id: Optional[str] = None
    community_id: Optional[str] = None
    context_annotations: Optional[List] = None
    conversation_id: Optional[str] = None
    created_at: Optional[str] = None
    display_text_range: Optional[List] = None
    edit_controls: Optional["GetPostsByIdResponseDataEditControls"] = None
    edit_history_tweet_ids: Optional[List] = None
    entities: Optional["GetPostsByIdResponseDataEntities"] = None
    geo: Optional["GetPostsByIdResponseDataGeo"] = None
    id: Optional[str] = None
    in_reply_to_user_id: Optional[str] = None
    lang: Optional[str] = None
    non_public_metrics: Optional["GetPostsByIdResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["GetPostsByIdResponseDataNoteTweet"] = None
    organic_metrics: Optional["GetPostsByIdResponseDataOrganicMetrics"] = None
    possibly_sensitive: Optional[bool] = None
    promoted_metrics: Optional["GetPostsByIdResponseDataPromotedMetrics"] = None
    public_metrics: Optional["GetPostsByIdResponseDataPublicMetrics"] = None
    referenced_tweets: Optional[List] = None
    reply_settings: Optional[str] = None
    scopes: Optional["GetPostsByIdResponseDataScopes"] = None
    source: Optional[str] = None
    text: Optional[str] = None
    username: Optional[str] = None
    withheld: Optional["GetPostsByIdResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataAttachments(BaseModel):
    """Nested model for GetPostsByIdResponseDataAttachments"""

    media_keys: Optional[List] = None
    media_source_tweet_id: Optional[List] = None
    poll_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataEditControls(BaseModel):
    """Nested model for GetPostsByIdResponseDataEditControls"""

    editable_until: Optional[str] = None
    edits_remaining: Optional[int] = None
    is_edit_eligible: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataEntities(BaseModel):
    """Nested model for GetPostsByIdResponseDataEntities"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataGeo(BaseModel):
    """Nested model for GetPostsByIdResponseDataGeo"""

    coordinates: Optional["GetPostsByIdResponseDataGeoCoordinates"] = None
    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataGeoCoordinates(BaseModel):
    """Nested model for GetPostsByIdResponseDataGeoCoordinates"""

    coordinates: Optional[List] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataNonPublicMetrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataNonPublicMetrics"""

    impression_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataNoteTweet(BaseModel):
    """Nested model for GetPostsByIdResponseDataNoteTweet"""

    entities: Optional["GetPostsByIdResponseDataNoteTweetEntities"] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataNoteTweetEntities(BaseModel):
    """Nested model for GetPostsByIdResponseDataNoteTweetEntities"""

    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataOrganicMetrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataOrganicMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataPromotedMetrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataPromotedMetrics"""

    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataPublicMetrics(BaseModel):
    """Nested model for GetPostsByIdResponseDataPublicMetrics"""

    bookmark_count: Optional[int] = None
    impression_count: Optional[int] = None
    like_count: Optional[int] = None
    quote_count: Optional[int] = None
    reply_count: Optional[int] = None
    retweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataScopes(BaseModel):
    """Nested model for GetPostsByIdResponseDataScopes"""

    followers: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseDataWithheld(BaseModel):
    """Nested model for GetPostsByIdResponseDataWithheld"""

    copyright: Optional[bool] = None
    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdResponseIncludes(BaseModel):
    """Nested model for GetPostsByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for deletePosts


class DeletePostsResponse(BaseModel):
    """Response model for deletePosts"""

    data: Optional["DeletePostsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeletePostsResponseData(BaseModel):
    """Nested model for DeletePostsResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getListsPosts


class GetListsPostsResponse(BaseModel):
    """Response model for getListsPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetListsPostsResponseIncludes"] = None
    meta: Optional["GetListsPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetListsPostsResponseIncludes(BaseModel):
    """Nested model for GetListsPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetListsPostsResponseMeta(BaseModel):
    """Nested model for GetListsPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersPosts


class GetUsersPostsResponse(BaseModel):
    """Response model for getUsersPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersPostsResponseIncludes"] = None
    meta: Optional["GetUsersPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersPostsResponseIncludes(BaseModel):
    """Nested model for GetUsersPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersPostsResponseMeta(BaseModel):
    """Nested model for GetUsersPostsResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for getSpacesPosts


class GetSpacesPostsResponse(BaseModel):
    """Response model for getSpacesPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesPostsResponseIncludes"] = None
    meta: Optional["GetSpacesPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetSpacesPostsResponseIncludes(BaseModel):
    """Nested model for GetSpacesPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetSpacesPostsResponseMeta(BaseModel):
    """Nested model for GetSpacesPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for hidePostsReply


class HidePostsReplyRequest(BaseModel):
    """Request model for hidePostsReply"""

    hidden: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class HidePostsReplyResponse(BaseModel):
    """Response model for hidePostsReply"""

    data: Optional["HidePostsReplyResponseData"] = None

    model_config = ConfigDict(populate_by_name=True)


class HidePostsReplyResponseData(BaseModel):
    """Nested model for HidePostsReplyResponseData"""

    hidden: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersLikedPosts


class GetUsersLikedPostsResponse(BaseModel):
    """Response model for getUsersLikedPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersLikedPostsResponseIncludes"] = None
    meta: Optional["GetUsersLikedPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersLikedPostsResponseIncludes(BaseModel):
    """Nested model for GetUsersLikedPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersLikedPostsResponseMeta(BaseModel):
    """Nested model for GetUsersLikedPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for getSpacesBuyers


class GetSpacesBuyersResponse(BaseModel):
    """Response model for getSpacesBuyers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesBuyersResponseIncludes"] = None
    meta: Optional["GetSpacesBuyersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetSpacesBuyersResponseIncludes(BaseModel):
    """Nested model for GetSpacesBuyersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetSpacesBuyersResponseMeta(BaseModel):
    """Nested model for GetSpacesBuyersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getPostsByIds


class GetPostsByIdsResponse(BaseModel):
    """Response model for getPostsByIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsByIdsResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsByIdsResponseIncludes(BaseModel):
    """Nested model for GetPostsByIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


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

    model_config = ConfigDict(populate_by_name=True)


class CreatePostsResponse(BaseModel):
    """Response model for createPosts"""

    data: Optional["CreatePostsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreatePostsRequestGeo(BaseModel):
    """Nested model for CreatePostsRequestGeo"""

    place_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreatePostsRequestMedia(BaseModel):
    """Nested model for CreatePostsRequestMedia"""

    media_ids: Optional[List] = None
    tagged_user_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreatePostsRequestPoll(BaseModel):
    """Nested model for CreatePostsRequestPoll"""

    duration_minutes: Optional[int] = None
    options: Optional[List] = None
    reply_settings: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreatePostsRequestReply(BaseModel):
    """Nested model for CreatePostsRequestReply"""

    exclude_reply_user_ids: Optional[List] = None
    in_reply_to_tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreatePostsResponseData(BaseModel):
    """Nested model for CreatePostsResponseData"""

    id: Optional[str] = None
    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersTimeline


class GetUsersTimelineResponse(BaseModel):
    """Response model for getUsersTimeline"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersTimelineResponseIncludes"] = None
    meta: Optional["GetUsersTimelineResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersTimelineResponseIncludes(BaseModel):
    """Nested model for GetUsersTimelineResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersTimelineResponseMeta(BaseModel):
    """Nested model for GetUsersTimelineResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersMentions


class GetUsersMentionsResponse(BaseModel):
    """Response model for getUsersMentions"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersMentionsResponseIncludes"] = None
    meta: Optional["GetUsersMentionsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersMentionsResponseIncludes(BaseModel):
    """Nested model for GetUsersMentionsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersMentionsResponseMeta(BaseModel):
    """Nested model for GetUsersMentionsResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getInsightsHistorical


class GetInsightsHistoricalResponse(BaseModel):
    """Response model for getInsightsHistorical"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getPostsCountsRecent


class GetPostsCountsRecentResponse(BaseModel):
    """Response model for getPostsCountsRecent"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetPostsCountsRecentResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsCountsRecentResponseMeta(BaseModel):
    """Nested model for GetPostsCountsRecentResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    total_tweet_count: Optional[int] = None

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


# Models for getPostsAnalytics


class GetPostsAnalyticsResponse(BaseModel):
    """Response model for getPostsAnalytics"""

    data: Optional[List] = None
    errors: Optional[List] = None

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


# Models for getPostsQuotedPosts


class GetPostsQuotedPostsResponse(BaseModel):
    """Response model for getPostsQuotedPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsQuotedPostsResponseIncludes"] = None
    meta: Optional["GetPostsQuotedPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsQuotedPostsResponseIncludes(BaseModel):
    """Nested model for GetPostsQuotedPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsQuotedPostsResponseMeta(BaseModel):
    """Nested model for GetPostsQuotedPostsResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for getInsights28Hr


class GetInsights28HrResponse(BaseModel):
    """Response model for getInsights28Hr"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getPostsReposts


class GetPostsRepostsResponse(BaseModel):
    """Response model for getPostsReposts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsRepostsResponseIncludes"] = None
    meta: Optional["GetPostsRepostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsRepostsResponseIncludes(BaseModel):
    """Nested model for GetPostsRepostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsRepostsResponseMeta(BaseModel):
    """Nested model for GetPostsRepostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for repostPost


class RepostPostRequest(BaseModel):
    """Request model for repostPost"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class RepostPostResponse(BaseModel):
    """Response model for repostPost"""

    data: Optional["RepostPostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class RepostPostResponseData(BaseModel):
    """Nested model for RepostPostResponseData"""

    id: Optional[str] = None
    retweeted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for searchPostsAll


class SearchPostsAllResponse(BaseModel):
    """Response model for searchPostsAll"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchPostsAllResponseIncludes"] = None
    meta: Optional["SearchPostsAllResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchPostsAllResponseIncludes(BaseModel):
    """Nested model for SearchPostsAllResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchPostsAllResponseMeta(BaseModel):
    """Nested model for SearchPostsAllResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unrepostPost


class UnrepostPostResponse(BaseModel):
    """Response model for unrepostPost"""

    data: Optional["UnrepostPostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnrepostPostResponseData(BaseModel):
    """Nested model for UnrepostPostResponseData"""

    retweeted: Optional[bool] = None

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


# Models for likePost


class LikePostRequest(BaseModel):
    """Request model for likePost"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class LikePostResponse(BaseModel):
    """Response model for likePost"""

    data: Optional["LikePostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class LikePostResponseData(BaseModel):
    """Nested model for LikePostResponseData"""

    liked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getPostsCountsAll


class GetPostsCountsAllResponse(BaseModel):
    """Response model for getPostsCountsAll"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetPostsCountsAllResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsCountsAllResponseMeta(BaseModel):
    """Nested model for GetPostsCountsAllResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    total_tweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
