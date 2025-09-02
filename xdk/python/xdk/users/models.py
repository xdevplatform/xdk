"""
Auto-generated users models for the X API.

This module provides Pydantic models for request and response data structures
for the users endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_list_memberships


class GetListMembershipsResponse(BaseModel):
    """Response model for get_list_memberships"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetListMembershipsResponseIncludes"] = None
    meta: Optional["GetListMembershipsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetListMembershipsResponseIncludes(BaseModel):
    """Nested model for GetListMembershipsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetListMembershipsResponseMeta(BaseModel):
    """Nested model for GetListMembershipsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for search


class SearchResponse(BaseModel):
    """Response model for search"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchResponseIncludes"] = None
    meta: Optional["SearchResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchResponseIncludes(BaseModel):
    """Nested model for SearchResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchResponseMeta(BaseModel):
    """Nested model for SearchResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for like_post


class LikePostRequest(BaseModel):
    """Request model for like_post"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class LikePostResponse(BaseModel):
    """Response model for like_post"""

    data: Optional["LikePostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class LikePostResponseData(BaseModel):
    """Nested model for LikePostResponseData"""

    liked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_blocking


class GetBlockingResponse(BaseModel):
    """Response model for get_blocking"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetBlockingResponseIncludes"] = None
    meta: Optional["GetBlockingResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBlockingResponseIncludes(BaseModel):
    """Nested model for GetBlockingResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBlockingResponseMeta(BaseModel):
    """Nested model for GetBlockingResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unrepost_post


class UnrepostPostResponse(BaseModel):
    """Response model for unrepost_post"""

    data: Optional["UnrepostPostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnrepostPostResponseData(BaseModel):
    """Nested model for UnrepostPostResponseData"""

    retweeted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_liked_posts


class GetLikedPostsResponse(BaseModel):
    """Response model for get_liked_posts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetLikedPostsResponseIncludes"] = None
    meta: Optional["GetLikedPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetLikedPostsResponseIncludes(BaseModel):
    """Nested model for GetLikedPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetLikedPostsResponseMeta(BaseModel):
    """Nested model for GetLikedPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_ids


class GetByIdsResponse(BaseModel):
    """Response model for get_by_ids"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetByIdsResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdsResponseIncludes(BaseModel):
    """Nested model for GetByIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_id


class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""

    data: Optional["GetByIdResponseData"] = Field(
        description="The X User object.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseData(BaseModel):
    """Nested model for GetByIdResponseData"""

    affiliation: Optional["GetByIdResponseDataAffiliation"] = None
    connection_status: Optional[List] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    entities: Optional["GetByIdResponseDataEntities"] = None
    id: Optional[str] = None
    location: Optional[str] = None
    most_recent_tweet_id: Optional[str] = None
    name: Optional[str] = None
    pinned_tweet_id: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_image_url: Optional[str] = None
    protected: Optional[bool] = None
    public_metrics: Optional["GetByIdResponseDataPublicMetrics"] = None
    receives_your_dm: Optional[bool] = None
    subscription_type: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None
    verified: Optional[bool] = None
    verified_type: Optional[str] = None
    withheld: Optional["GetByIdResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataAffiliation(BaseModel):
    """Nested model for GetByIdResponseDataAffiliation"""

    badge_url: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataEntities(BaseModel):
    """Nested model for GetByIdResponseDataEntities"""

    description: Optional["GetByIdResponseDataEntitiesDescription"] = None
    url: Optional["GetByIdResponseDataEntitiesUrl"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetByIdResponseDataEntitiesDescription"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetByIdResponseDataEntitiesUrl"""

    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataPublicMetrics(BaseModel):
    """Nested model for GetByIdResponseDataPublicMetrics"""

    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    like_count: Optional[int] = None
    listed_count: Optional[int] = None
    tweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataWithheld(BaseModel):
    """Nested model for GetByIdResponseDataWithheld"""

    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseIncludes(BaseModel):
    """Nested model for GetByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_username


class GetByUsernameResponse(BaseModel):
    """Response model for get_by_username"""

    data: Optional["GetByUsernameResponseData"] = Field(
        description="The X User object.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetByUsernameResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseData(BaseModel):
    """Nested model for GetByUsernameResponseData"""

    affiliation: Optional["GetByUsernameResponseDataAffiliation"] = None
    connection_status: Optional[List] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    entities: Optional["GetByUsernameResponseDataEntities"] = None
    id: Optional[str] = None
    location: Optional[str] = None
    most_recent_tweet_id: Optional[str] = None
    name: Optional[str] = None
    pinned_tweet_id: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_image_url: Optional[str] = None
    protected: Optional[bool] = None
    public_metrics: Optional["GetByUsernameResponseDataPublicMetrics"] = None
    receives_your_dm: Optional[bool] = None
    subscription_type: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None
    verified: Optional[bool] = None
    verified_type: Optional[str] = None
    withheld: Optional["GetByUsernameResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseDataAffiliation(BaseModel):
    """Nested model for GetByUsernameResponseDataAffiliation"""

    badge_url: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseDataEntities(BaseModel):
    """Nested model for GetByUsernameResponseDataEntities"""

    description: Optional["GetByUsernameResponseDataEntitiesDescription"] = None
    url: Optional["GetByUsernameResponseDataEntitiesUrl"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetByUsernameResponseDataEntitiesDescription"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetByUsernameResponseDataEntitiesUrl"""

    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseDataPublicMetrics(BaseModel):
    """Nested model for GetByUsernameResponseDataPublicMetrics"""

    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    like_count: Optional[int] = None
    listed_count: Optional[int] = None
    tweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseDataWithheld(BaseModel):
    """Nested model for GetByUsernameResponseDataWithheld"""

    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernameResponseIncludes(BaseModel):
    """Nested model for GetByUsernameResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_bookmarks


class GetBookmarksResponse(BaseModel):
    """Response model for get_bookmarks"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetBookmarksResponseIncludes"] = None
    meta: Optional["GetBookmarksResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBookmarksResponseIncludes(BaseModel):
    """Nested model for GetBookmarksResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBookmarksResponseMeta(BaseModel):
    """Nested model for GetBookmarksResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_bookmark


class CreateBookmarkRequest(BaseModel):
    """Request model for create_bookmark"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateBookmarkResponse(BaseModel):
    """Response model for create_bookmark"""

    data: Optional["CreateBookmarkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateBookmarkResponseData(BaseModel):
    """Nested model for CreateBookmarkResponseData"""

    bookmarked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_muting


class GetMutingResponse(BaseModel):
    """Response model for get_muting"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetMutingResponseIncludes"] = None
    meta: Optional["GetMutingResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMutingResponseIncludes(BaseModel):
    """Nested model for GetMutingResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMutingResponseMeta(BaseModel):
    """Nested model for GetMutingResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for mute_user


class MuteUserRequest(BaseModel):
    """Request model for mute_user"""

    target_user_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class MuteUserResponse(BaseModel):
    """Response model for mute_user"""

    data: Optional["MuteUserResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class MuteUserResponseData(BaseModel):
    """Nested model for MuteUserResponseData"""

    muting: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_bookmark_folders


class GetBookmarkFoldersResponse(BaseModel):
    """Response model for get_bookmark_folders"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetBookmarkFoldersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBookmarkFoldersResponseMeta(BaseModel):
    """Nested model for GetBookmarkFoldersResponseMeta"""

    next_token: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unfollow_list


class UnfollowListResponse(BaseModel):
    """Response model for unfollow_list"""

    data: Optional["UnfollowListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnfollowListResponseData(BaseModel):
    """Nested model for UnfollowListResponseData"""

    following: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unfollow_user


class UnfollowUserResponse(BaseModel):
    """Response model for unfollow_user"""

    data: Optional["UnfollowUserResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnfollowUserResponseData(BaseModel):
    """Nested model for UnfollowUserResponseData"""

    following: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unlike_post


class UnlikePostResponse(BaseModel):
    """Response model for unlike_post"""

    data: Optional["UnlikePostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnlikePostResponseData(BaseModel):
    """Nested model for UnlikePostResponseData"""

    liked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_following


class GetFollowingResponse(BaseModel):
    """Response model for get_following"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetFollowingResponseIncludes"] = None
    meta: Optional["GetFollowingResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowingResponseIncludes(BaseModel):
    """Nested model for GetFollowingResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowingResponseMeta(BaseModel):
    """Nested model for GetFollowingResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for follow_user


class FollowUserRequest(BaseModel):
    """Request model for follow_user"""

    target_user_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class FollowUserResponse(BaseModel):
    """Response model for follow_user"""

    data: Optional["FollowUserResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class FollowUserResponseData(BaseModel):
    """Nested model for FollowUserResponseData"""

    following: Optional[bool] = None
    pending_follow: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for repost_post


class RepostPostRequest(BaseModel):
    """Request model for repost_post"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class RepostPostResponse(BaseModel):
    """Response model for repost_post"""

    data: Optional["RepostPostResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class RepostPostResponseData(BaseModel):
    """Nested model for RepostPostResponseData"""

    id: Optional[str] = None
    retweeted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_timeline


class GetTimelineResponse(BaseModel):
    """Response model for get_timeline"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetTimelineResponseIncludes"] = None
    meta: Optional["GetTimelineResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetTimelineResponseIncludes(BaseModel):
    """Nested model for GetTimelineResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetTimelineResponseMeta(BaseModel):
    """Nested model for GetTimelineResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unmute_user


class UnmuteUserResponse(BaseModel):
    """Response model for unmute_user"""

    data: Optional["UnmuteUserResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnmuteUserResponseData(BaseModel):
    """Nested model for UnmuteUserResponseData"""

    muting: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete_bookmark


class DeleteBookmarkResponse(BaseModel):
    """Response model for delete_bookmark"""

    data: Optional["DeleteBookmarkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteBookmarkResponseData(BaseModel):
    """Nested model for DeleteBookmarkResponseData"""

    bookmarked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_usernames


class GetByUsernamesResponse(BaseModel):
    """Response model for get_by_usernames"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetByUsernamesResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByUsernamesResponseIncludes(BaseModel):
    """Nested model for GetByUsernamesResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_reposts_of_me


class GetRepostsOfMeResponse(BaseModel):
    """Response model for get_reposts_of_me"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetRepostsOfMeResponseIncludes"] = None
    meta: Optional["GetRepostsOfMeResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetRepostsOfMeResponseIncludes(BaseModel):
    """Nested model for GetRepostsOfMeResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetRepostsOfMeResponseMeta(BaseModel):
    """Nested model for GetRepostsOfMeResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_mentions


class GetMentionsResponse(BaseModel):
    """Response model for get_mentions"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetMentionsResponseIncludes"] = None
    meta: Optional["GetMentionsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMentionsResponseIncludes(BaseModel):
    """Nested model for GetMentionsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMentionsResponseMeta(BaseModel):
    """Nested model for GetMentionsResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_owned_lists


class GetOwnedListsResponse(BaseModel):
    """Response model for get_owned_lists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetOwnedListsResponseIncludes"] = None
    meta: Optional["GetOwnedListsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetOwnedListsResponseIncludes(BaseModel):
    """Nested model for GetOwnedListsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetOwnedListsResponseMeta(BaseModel):
    """Nested model for GetOwnedListsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_posts


class GetPostsResponse(BaseModel):
    """Response model for get_posts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsResponseIncludes"] = None
    meta: Optional["GetPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsResponseIncludes(BaseModel):
    """Nested model for GetPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsResponseMeta(BaseModel):
    """Nested model for GetPostsResponseMeta"""

    newest_id: Optional[str] = None
    next_token: Optional[str] = None
    oldest_id: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_me


class GetMeResponse(BaseModel):
    """Response model for get_me"""

    data: Optional["GetMeResponseData"] = Field(
        description="The X User object.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetMeResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseData(BaseModel):
    """Nested model for GetMeResponseData"""

    affiliation: Optional["GetMeResponseDataAffiliation"] = None
    connection_status: Optional[List] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    entities: Optional["GetMeResponseDataEntities"] = None
    id: Optional[str] = None
    location: Optional[str] = None
    most_recent_tweet_id: Optional[str] = None
    name: Optional[str] = None
    pinned_tweet_id: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_image_url: Optional[str] = None
    protected: Optional[bool] = None
    public_metrics: Optional["GetMeResponseDataPublicMetrics"] = None
    receives_your_dm: Optional[bool] = None
    subscription_type: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None
    verified: Optional[bool] = None
    verified_type: Optional[str] = None
    withheld: Optional["GetMeResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseDataAffiliation(BaseModel):
    """Nested model for GetMeResponseDataAffiliation"""

    badge_url: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseDataEntities(BaseModel):
    """Nested model for GetMeResponseDataEntities"""

    description: Optional["GetMeResponseDataEntitiesDescription"] = None
    url: Optional["GetMeResponseDataEntitiesUrl"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetMeResponseDataEntitiesDescription"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetMeResponseDataEntitiesUrl"""

    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseDataPublicMetrics(BaseModel):
    """Nested model for GetMeResponseDataPublicMetrics"""

    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    like_count: Optional[int] = None
    listed_count: Optional[int] = None
    tweet_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseDataWithheld(BaseModel):
    """Nested model for GetMeResponseDataWithheld"""

    country_codes: Optional[List] = None
    scope: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMeResponseIncludes(BaseModel):
    """Nested model for GetMeResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_bookmarks_by_folder_id


class GetBookmarksByFolderIdResponse(BaseModel):
    """Response model for get_bookmarks_by_folder_id"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetBookmarksByFolderIdResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBookmarksByFolderIdResponseMeta(BaseModel):
    """Nested model for GetBookmarksByFolderIdResponseMeta"""

    next_token: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unblock_dms


class UnblockDmsResponse(BaseModel):
    """Response model for unblock_dms"""

    data: Optional["UnblockDmsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnblockDmsResponseData(BaseModel):
    """Nested model for UnblockDmsResponseData"""

    blocked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_followed_lists


class GetFollowedListsResponse(BaseModel):
    """Response model for get_followed_lists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetFollowedListsResponseIncludes"] = None
    meta: Optional["GetFollowedListsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowedListsResponseIncludes(BaseModel):
    """Nested model for GetFollowedListsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowedListsResponseMeta(BaseModel):
    """Nested model for GetFollowedListsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for follow_list


class FollowListRequest(BaseModel):
    """Request model for follow_list"""

    list_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class FollowListResponse(BaseModel):
    """Response model for follow_list"""

    data: Optional["FollowListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class FollowListResponseData(BaseModel):
    """Nested model for FollowListResponseData"""

    following: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_followers


class GetFollowersResponse(BaseModel):
    """Response model for get_followers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetFollowersResponseIncludes"] = None
    meta: Optional["GetFollowersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowersResponseIncludes(BaseModel):
    """Nested model for GetFollowersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowersResponseMeta(BaseModel):
    """Nested model for GetFollowersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_pinned_lists


class GetPinnedListsResponse(BaseModel):
    """Response model for get_pinned_lists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPinnedListsResponseIncludes"] = None
    meta: Optional["GetPinnedListsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPinnedListsResponseIncludes(BaseModel):
    """Nested model for GetPinnedListsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPinnedListsResponseMeta(BaseModel):
    """Nested model for GetPinnedListsResponseMeta"""

    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for pin_list


class PinListRequest(BaseModel):
    """Request model for pin_list"""

    list_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PinListResponse(BaseModel):
    """Response model for pin_list"""

    data: Optional["PinListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PinListResponseData(BaseModel):
    """Nested model for PinListResponseData"""

    pinned: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for block_dms


class BlockDmsResponse(BaseModel):
    """Response model for block_dms"""

    data: Optional["BlockDmsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class BlockDmsResponseData(BaseModel):
    """Nested model for BlockDmsResponseData"""

    blocked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unpin_list


class UnpinListResponse(BaseModel):
    """Response model for unpin_list"""

    data: Optional["UnpinListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnpinListResponseData(BaseModel):
    """Nested model for UnpinListResponseData"""

    pinned: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
