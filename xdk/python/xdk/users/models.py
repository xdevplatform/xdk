"""
Users models for the X API.

This module provides models for the Users endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getListsFollowers


class GetListsFollowersResponse(BaseModel):
    """Response model for getListsFollowers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetListsFollowersResponseIncludes"] = None
    meta: Optional["GetListsFollowersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetListsFollowersResponseIncludes(BaseModel):
    """Nested model for GetListsFollowersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetListsFollowersResponseMeta(BaseModel):
    """Nested model for GetListsFollowersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersByIds


class GetUsersByIdsResponse(BaseModel):
    """Response model for getUsersByIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersByIdsResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdsResponseIncludes(BaseModel):
    """Nested model for GetUsersByIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unblockUsersDms


class UnblockUsersDmsResponse(BaseModel):
    """Response model for unblockUsersDms"""

    data: Optional["UnblockUsersDmsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnblockUsersDmsResponseData(BaseModel):
    """Nested model for UnblockUsersDmsResponseData"""

    blocked: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersBlocking


class GetUsersBlockingResponse(BaseModel):
    """Response model for getUsersBlocking"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersBlockingResponseIncludes"] = None
    meta: Optional["GetUsersBlockingResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersBlockingResponseIncludes(BaseModel):
    """Nested model for GetUsersBlockingResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersBlockingResponseMeta(BaseModel):
    """Nested model for GetUsersBlockingResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersById


class GetUsersByIdResponse(BaseModel):
    """Response model for getUsersById"""

    data: Optional["GetUsersByIdResponseData"] = Field(
        description="The X User object.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetUsersByIdResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseData(BaseModel):
    """Nested model for GetUsersByIdResponseData"""

    affiliation: Optional["GetUsersByIdResponseDataAffiliation"] = None
    connection_status: Optional[List] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    entities: Optional["GetUsersByIdResponseDataEntities"] = None
    id: Optional[str] = None
    location: Optional[str] = None
    most_recent_tweet_id: Optional[str] = None
    name: Optional[str] = None
    pinned_tweet_id: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_image_url: Optional[str] = None
    protected: Optional[bool] = None
    public_metrics: Optional["GetUsersByIdResponseDataPublic_metrics"] = None
    receives_your_dm: Optional[bool] = None
    subscription_type: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None
    verified: Optional[bool] = None
    verified_type: Optional[str] = None
    withheld: Optional["GetUsersByIdResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseDataAffiliation(BaseModel):
    """Nested model for GetUsersByIdResponseDataAffiliation"""

    badge_url: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseDataEntities(BaseModel):
    """Nested model for GetUsersByIdResponseDataEntities"""

    description: Optional["GetUsersByIdResponseDataEntitiesDescription"] = None
    url: Optional["GetUsersByIdResponseDataEntitiesUrl"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetUsersByIdResponseDataEntitiesDescription"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetUsersByIdResponseDataEntitiesUrl"""

    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseDataPublic_metrics(BaseModel):
    """Nested model for GetUsersByIdResponseDataPublic_metrics"""

    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    like_count: Optional[int] = None
    listed_count: Optional[int] = None
    tweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseDataWithheld(BaseModel):
    """Nested model for GetUsersByIdResponseDataWithheld"""

    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByIdResponseIncludes(BaseModel):
    """Nested model for GetUsersByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsRepostedBy


class GetPostsRepostedByResponse(BaseModel):
    """Response model for getPostsRepostedBy"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsRepostedByResponseIncludes"] = None
    meta: Optional["GetPostsRepostedByResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsRepostedByResponseIncludes(BaseModel):
    """Nested model for GetPostsRepostedByResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsRepostedByResponseMeta(BaseModel):
    """Nested model for GetPostsRepostedByResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unfollowUser


class UnfollowUserResponse(BaseModel):
    """Response model for unfollowUser"""

    data: Optional["UnfollowUserResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnfollowUserResponseData(BaseModel):
    """Nested model for UnfollowUserResponseData"""

    following: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersRepostsOfMe


class GetUsersRepostsOfMeResponse(BaseModel):
    """Response model for getUsersRepostsOfMe"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersRepostsOfMeResponseIncludes"] = None
    meta: Optional["GetUsersRepostsOfMeResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersRepostsOfMeResponseIncludes(BaseModel):
    """Nested model for GetUsersRepostsOfMeResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersRepostsOfMeResponseMeta(BaseModel):
    """Nested model for GetUsersRepostsOfMeResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for blockUsersDms


class BlockUsersDmsResponse(BaseModel):
    """Response model for blockUsersDms"""

    data: Optional["BlockUsersDmsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class BlockUsersDmsResponseData(BaseModel):
    """Nested model for BlockUsersDmsResponseData"""

    blocked: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getListsMembers


class GetListsMembersResponse(BaseModel):
    """Response model for getListsMembers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetListsMembersResponseIncludes"] = None
    meta: Optional["GetListsMembersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetListsMembersResponseIncludes(BaseModel):
    """Nested model for GetListsMembersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetListsMembersResponseMeta(BaseModel):
    """Nested model for GetListsMembersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getPostsLikingUsers


class GetPostsLikingUsersResponse(BaseModel):
    """Response model for getPostsLikingUsers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsLikingUsersResponseIncludes"] = None
    meta: Optional["GetPostsLikingUsersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsLikingUsersResponseIncludes(BaseModel):
    """Nested model for GetPostsLikingUsersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetPostsLikingUsersResponseMeta(BaseModel):
    """Nested model for GetPostsLikingUsersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMyUser


class GetMyUserResponse(BaseModel):
    """Response model for getMyUser"""

    data: Optional["GetMyUserResponseData"] = Field(
        description="The X User object.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetMyUserResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseData(BaseModel):
    """Nested model for GetMyUserResponseData"""

    affiliation: Optional["GetMyUserResponseDataAffiliation"] = None
    connection_status: Optional[List] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    entities: Optional["GetMyUserResponseDataEntities"] = None
    id: Optional[str] = None
    location: Optional[str] = None
    most_recent_tweet_id: Optional[str] = None
    name: Optional[str] = None
    pinned_tweet_id: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_image_url: Optional[str] = None
    protected: Optional[bool] = None
    public_metrics: Optional["GetMyUserResponseDataPublic_metrics"] = None
    receives_your_dm: Optional[bool] = None
    subscription_type: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None
    verified: Optional[bool] = None
    verified_type: Optional[str] = None
    withheld: Optional["GetMyUserResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseDataAffiliation(BaseModel):
    """Nested model for GetMyUserResponseDataAffiliation"""

    badge_url: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseDataEntities(BaseModel):
    """Nested model for GetMyUserResponseDataEntities"""

    description: Optional["GetMyUserResponseDataEntitiesDescription"] = None
    url: Optional["GetMyUserResponseDataEntitiesUrl"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetMyUserResponseDataEntitiesDescription"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetMyUserResponseDataEntitiesUrl"""

    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseDataPublic_metrics(BaseModel):
    """Nested model for GetMyUserResponseDataPublic_metrics"""

    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    like_count: Optional[int] = None
    listed_count: Optional[int] = None
    tweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseDataWithheld(BaseModel):
    """Nested model for GetMyUserResponseDataWithheld"""

    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMyUserResponseIncludes(BaseModel):
    """Nested model for GetMyUserResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for searchUsers


class SearchUsersResponse(BaseModel):
    """Response model for searchUsers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchUsersResponseIncludes"] = None
    meta: Optional["SearchUsersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchUsersResponseIncludes(BaseModel):
    """Nested model for SearchUsersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchUsersResponseMeta(BaseModel):
    """Nested model for SearchUsersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersByUsername


class GetUsersByUsernameResponse(BaseModel):
    """Response model for getUsersByUsername"""

    data: Optional["GetUsersByUsernameResponseData"] = Field(
        description="The X User object.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetUsersByUsernameResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseData(BaseModel):
    """Nested model for GetUsersByUsernameResponseData"""

    affiliation: Optional["GetUsersByUsernameResponseDataAffiliation"] = None
    connection_status: Optional[List] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    entities: Optional["GetUsersByUsernameResponseDataEntities"] = None
    id: Optional[str] = None
    location: Optional[str] = None
    most_recent_tweet_id: Optional[str] = None
    name: Optional[str] = None
    pinned_tweet_id: Optional[str] = None
    profile_banner_url: Optional[str] = None
    profile_image_url: Optional[str] = None
    protected: Optional[bool] = None
    public_metrics: Optional["GetUsersByUsernameResponseDataPublic_metrics"] = None
    receives_your_dm: Optional[bool] = None
    subscription_type: Optional[str] = None
    url: Optional[str] = None
    username: Optional[str] = None
    verified: Optional[bool] = None
    verified_type: Optional[str] = None
    withheld: Optional["GetUsersByUsernameResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseDataAffiliation(BaseModel):
    """Nested model for GetUsersByUsernameResponseDataAffiliation"""

    badge_url: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    user_id: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseDataEntities(BaseModel):
    """Nested model for GetUsersByUsernameResponseDataEntities"""

    description: Optional["GetUsersByUsernameResponseDataEntitiesDescription"] = None
    url: Optional["GetUsersByUsernameResponseDataEntitiesUrl"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetUsersByUsernameResponseDataEntitiesDescription"""

    annotations: Optional[List] = None
    cashtags: Optional[List] = None
    hashtags: Optional[List] = None
    mentions: Optional[List] = None
    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetUsersByUsernameResponseDataEntitiesUrl"""

    urls: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseDataPublic_metrics(BaseModel):
    """Nested model for GetUsersByUsernameResponseDataPublic_metrics"""

    followers_count: Optional[int] = None
    following_count: Optional[int] = None
    like_count: Optional[int] = None
    listed_count: Optional[int] = None
    tweet_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseDataWithheld(BaseModel):
    """Nested model for GetUsersByUsernameResponseDataWithheld"""

    country_codes: Optional[List] = None
    scope: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernameResponseIncludes(BaseModel):
    """Nested model for GetUsersByUsernameResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersMuting


class GetUsersMutingResponse(BaseModel):
    """Response model for getUsersMuting"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersMutingResponseIncludes"] = None
    meta: Optional["GetUsersMutingResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersMutingResponseIncludes(BaseModel):
    """Nested model for GetUsersMutingResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersMutingResponseMeta(BaseModel):
    """Nested model for GetUsersMutingResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for muteUser


class MuteUserRequest(BaseModel):
    """Request model for muteUser"""

    target_user_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MuteUserResponse(BaseModel):
    """Response model for muteUser"""

    data: Optional["MuteUserResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MuteUserResponseData(BaseModel):
    """Nested model for MuteUserResponseData"""

    muting: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersByUsernames


class GetUsersByUsernamesResponse(BaseModel):
    """Response model for getUsersByUsernames"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersByUsernamesResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersByUsernamesResponseIncludes(BaseModel):
    """Nested model for GetUsersByUsernamesResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersFollowers


class GetUsersFollowersResponse(BaseModel):
    """Response model for getUsersFollowers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersFollowersResponseIncludes"] = None
    meta: Optional["GetUsersFollowersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersFollowersResponseIncludes(BaseModel):
    """Nested model for GetUsersFollowersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersFollowersResponseMeta(BaseModel):
    """Nested model for GetUsersFollowersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersFollowing


class GetUsersFollowingResponse(BaseModel):
    """Response model for getUsersFollowing"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersFollowingResponseIncludes"] = None
    meta: Optional["GetUsersFollowingResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersFollowingResponseIncludes(BaseModel):
    """Nested model for GetUsersFollowingResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsersFollowingResponseMeta(BaseModel):
    """Nested model for GetUsersFollowingResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for followUser


class FollowUserRequest(BaseModel):
    """Request model for followUser"""

    target_user_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FollowUserResponse(BaseModel):
    """Response model for followUser"""

    data: Optional["FollowUserResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FollowUserResponseData(BaseModel):
    """Nested model for FollowUserResponseData"""

    following: Optional[bool] = None
    pending_follow: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unmuteUser


class UnmuteUserResponse(BaseModel):
    """Response model for unmuteUser"""

    data: Optional["UnmuteUserResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnmuteUserResponseData(BaseModel):
    """Nested model for UnmuteUserResponseData"""

    muting: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
