"""
Users models for the X API.

This module provides models for the Users endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for getPostsLikingUsers








class GetpostslikingusersResponse(BaseModel):
    """Response model for getPostsLikingUsers"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetpostslikingusersResponseIncludes"] =None
    meta: Optional["GetpostslikingusersResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetpostslikingusersResponseIncludes(BaseModel):
    """Nested model for GetpostslikingusersResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetpostslikingusersResponseMeta(BaseModel):
    """Nested model for GetpostslikingusersResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for blockUsersDms








class BlockusersdmsResponse(BaseModel):
    """Response model for blockUsersDms"""
    
    data: Optional["BlockusersdmsResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class BlockusersdmsResponseData(BaseModel):
    """Nested model for BlockusersdmsResponseData"""
    blocked:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for unfollowUser








class UnfollowuserResponse(BaseModel):
    """Response model for unfollowUser"""
    
    data: Optional["UnfollowuserResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class UnfollowuserResponseData(BaseModel):
    """Nested model for UnfollowuserResponseData"""
    following:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for getUsersByIds








class GetusersbyidsResponse(BaseModel):
    """Response model for getUsersByIds"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersbyidsResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersbyidsResponseIncludes(BaseModel):
    """Nested model for GetusersbyidsResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersByUsernames








class GetusersbyusernamesResponse(BaseModel):
    """Response model for getUsersByUsernames"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersbyusernamesResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersbyusernamesResponseIncludes(BaseModel):
    """Nested model for GetusersbyusernamesResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getPostsRepostedBy








class GetpostsrepostedbyResponse(BaseModel):
    """Response model for getPostsRepostedBy"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetpostsrepostedbyResponseIncludes"] =None
    meta: Optional["GetpostsrepostedbyResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetpostsrepostedbyResponseIncludes(BaseModel):
    """Nested model for GetpostsrepostedbyResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetpostsrepostedbyResponseMeta(BaseModel):
    """Nested model for GetpostsrepostedbyResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for searchUsers








class SearchusersResponse(BaseModel):
    """Response model for searchUsers"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["SearchusersResponseIncludes"] =None
    meta: Optional["SearchusersResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class SearchusersResponseIncludes(BaseModel):
    """Nested model for SearchusersResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class SearchusersResponseMeta(BaseModel):
    """Nested model for SearchusersResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersBlocking








class GetusersblockingResponse(BaseModel):
    """Response model for getUsersBlocking"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersblockingResponseIncludes"] =None
    meta: Optional["GetusersblockingResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersblockingResponseIncludes(BaseModel):
    """Nested model for GetusersblockingResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetusersblockingResponseMeta(BaseModel):
    """Nested model for GetusersblockingResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for unmuteUser








class UnmuteuserResponse(BaseModel):
    """Response model for unmuteUser"""
    
    data: Optional["UnmuteuserResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class UnmuteuserResponseData(BaseModel):
    """Nested model for UnmuteuserResponseData"""
    muting:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for getUsersById








class GetusersbyidResponse(BaseModel):
    """Response model for getUsersById"""
    
    data: Optional["GetusersbyidResponseData"] =Field(description="The X User object.",default_factory=dict)
    errors: Optional[List] =None
    includes: Optional["GetusersbyidResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetusersbyidResponseData(BaseModel):
    """Nested model for GetusersbyidResponseData"""
    affiliation: Optional["GetusersbyidResponseDataAffiliation"] = None
    connection_status:Optional[List] =None
    created_at:Optional[str] =None
    description:Optional[str] =None
    entities: Optional["GetusersbyidResponseDataEntities"] = None
    id:Optional[str] =None
    location:Optional[str] =None
    most_recent_tweet_id:Optional[str] =None
    name:Optional[str] =None
    pinned_tweet_id:Optional[str] =None
    profile_banner_url:Optional[str] =None
    profile_image_url:Optional[str] =None
    protected:Optional[bool] =None
    public_metrics: Optional["GetusersbyidResponseDataPublicMetrics"] = None
    receives_your_dm:Optional[bool] =None
    subscription_type:Optional[str] =None
    url:Optional[str] =None
    username:Optional[str] =None
    verified:Optional[bool] =None
    verified_type:Optional[str] =None
    withheld: Optional["GetusersbyidResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyidResponseDataAffiliation(BaseModel):
    """Nested model for GetusersbyidResponseDataAffiliation"""
    badge_url:Optional[str] =None
    description:Optional[str] =None
    url:Optional[str] =None
    user_id:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyidResponseDataEntities(BaseModel):
    """Nested model for GetusersbyidResponseDataEntities"""
    description: Optional["GetusersbyidResponseDataEntitiesDescription"] = None
    url: Optional["GetusersbyidResponseDataEntitiesUrl"] = None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyidResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetusersbyidResponseDataEntitiesDescription"""
    annotations:Optional[List] =None
    cashtags:Optional[List] =None
    hashtags:Optional[List] =None
    mentions:Optional[List] =None
    urls:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyidResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetusersbyidResponseDataEntitiesUrl"""
    urls:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyidResponseDataPublicMetrics(BaseModel):
    """Nested model for GetusersbyidResponseDataPublicMetrics"""
    followers_count:Optional[int] =None
    following_count:Optional[int] =None
    like_count:Optional[int] =None
    listed_count:Optional[int] =None
    tweet_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyidResponseDataWithheld(BaseModel):
    """Nested model for GetusersbyidResponseDataWithheld"""
    country_codes:Optional[List] =None
    scope:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









class GetusersbyidResponseIncludes(BaseModel):
    """Nested model for GetusersbyidResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getMyUser








class GetmyuserResponse(BaseModel):
    """Response model for getMyUser"""
    
    data: Optional["GetmyuserResponseData"] =Field(description="The X User object.",default_factory=dict)
    errors: Optional[List] =None
    includes: Optional["GetmyuserResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetmyuserResponseData(BaseModel):
    """Nested model for GetmyuserResponseData"""
    affiliation: Optional["GetmyuserResponseDataAffiliation"] = None
    connection_status:Optional[List] =None
    created_at:Optional[str] =None
    description:Optional[str] =None
    entities: Optional["GetmyuserResponseDataEntities"] = None
    id:Optional[str] =None
    location:Optional[str] =None
    most_recent_tweet_id:Optional[str] =None
    name:Optional[str] =None
    pinned_tweet_id:Optional[str] =None
    profile_banner_url:Optional[str] =None
    profile_image_url:Optional[str] =None
    protected:Optional[bool] =None
    public_metrics: Optional["GetmyuserResponseDataPublicMetrics"] = None
    receives_your_dm:Optional[bool] =None
    subscription_type:Optional[str] =None
    url:Optional[str] =None
    username:Optional[str] =None
    verified:Optional[bool] =None
    verified_type:Optional[str] =None
    withheld: Optional["GetmyuserResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetmyuserResponseDataAffiliation(BaseModel):
    """Nested model for GetmyuserResponseDataAffiliation"""
    badge_url:Optional[str] =None
    description:Optional[str] =None
    url:Optional[str] =None
    user_id:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetmyuserResponseDataEntities(BaseModel):
    """Nested model for GetmyuserResponseDataEntities"""
    description: Optional["GetmyuserResponseDataEntitiesDescription"] = None
    url: Optional["GetmyuserResponseDataEntitiesUrl"] = None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetmyuserResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetmyuserResponseDataEntitiesDescription"""
    annotations:Optional[List] =None
    cashtags:Optional[List] =None
    hashtags:Optional[List] =None
    mentions:Optional[List] =None
    urls:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetmyuserResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetmyuserResponseDataEntitiesUrl"""
    urls:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetmyuserResponseDataPublicMetrics(BaseModel):
    """Nested model for GetmyuserResponseDataPublicMetrics"""
    followers_count:Optional[int] =None
    following_count:Optional[int] =None
    like_count:Optional[int] =None
    listed_count:Optional[int] =None
    tweet_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetmyuserResponseDataWithheld(BaseModel):
    """Nested model for GetmyuserResponseDataWithheld"""
    country_codes:Optional[List] =None
    scope:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









class GetmyuserResponseIncludes(BaseModel):
    """Nested model for GetmyuserResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersFollowing








class GetusersfollowingResponse(BaseModel):
    """Response model for getUsersFollowing"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersfollowingResponseIncludes"] =None
    meta: Optional["GetusersfollowingResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersfollowingResponseIncludes(BaseModel):
    """Nested model for GetusersfollowingResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetusersfollowingResponseMeta(BaseModel):
    """Nested model for GetusersfollowingResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for followUser

class FollowuserRequest(BaseModel):
    """Request model for followUser"""
    
    target_user_id: Optional[str] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class FollowuserResponse(BaseModel):
    """Response model for followUser"""
    
    data: Optional["FollowuserResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True





























class FollowuserResponseData(BaseModel):
    """Nested model for FollowuserResponseData"""
    following:Optional[bool] =None
    pending_follow:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for getListsFollowers








class GetlistsfollowersResponse(BaseModel):
    """Response model for getListsFollowers"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetlistsfollowersResponseIncludes"] =None
    meta: Optional["GetlistsfollowersResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetlistsfollowersResponseIncludes(BaseModel):
    """Nested model for GetlistsfollowersResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetlistsfollowersResponseMeta(BaseModel):
    """Nested model for GetlistsfollowersResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getListsMembers








class GetlistsmembersResponse(BaseModel):
    """Response model for getListsMembers"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetlistsmembersResponseIncludes"] =None
    meta: Optional["GetlistsmembersResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetlistsmembersResponseIncludes(BaseModel):
    """Nested model for GetlistsmembersResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetlistsmembersResponseMeta(BaseModel):
    """Nested model for GetlistsmembersResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersFollowers








class GetusersfollowersResponse(BaseModel):
    """Response model for getUsersFollowers"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersfollowersResponseIncludes"] =None
    meta: Optional["GetusersfollowersResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersfollowersResponseIncludes(BaseModel):
    """Nested model for GetusersfollowersResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetusersfollowersResponseMeta(BaseModel):
    """Nested model for GetusersfollowersResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersRepostsOfMe








class GetusersrepostsofmeResponse(BaseModel):
    """Response model for getUsersRepostsOfMe"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersrepostsofmeResponseIncludes"] =None
    meta: Optional["GetusersrepostsofmeResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersrepostsofmeResponseIncludes(BaseModel):
    """Nested model for GetusersrepostsofmeResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetusersrepostsofmeResponseMeta(BaseModel):
    """Nested model for GetusersrepostsofmeResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersByUsername








class GetusersbyusernameResponse(BaseModel):
    """Response model for getUsersByUsername"""
    
    data: Optional["GetusersbyusernameResponseData"] =Field(description="The X User object.",default_factory=dict)
    errors: Optional[List] =None
    includes: Optional["GetusersbyusernameResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetusersbyusernameResponseData(BaseModel):
    """Nested model for GetusersbyusernameResponseData"""
    affiliation: Optional["GetusersbyusernameResponseDataAffiliation"] = None
    connection_status:Optional[List] =None
    created_at:Optional[str] =None
    description:Optional[str] =None
    entities: Optional["GetusersbyusernameResponseDataEntities"] = None
    id:Optional[str] =None
    location:Optional[str] =None
    most_recent_tweet_id:Optional[str] =None
    name:Optional[str] =None
    pinned_tweet_id:Optional[str] =None
    profile_banner_url:Optional[str] =None
    profile_image_url:Optional[str] =None
    protected:Optional[bool] =None
    public_metrics: Optional["GetusersbyusernameResponseDataPublicMetrics"] = None
    receives_your_dm:Optional[bool] =None
    subscription_type:Optional[str] =None
    url:Optional[str] =None
    username:Optional[str] =None
    verified:Optional[bool] =None
    verified_type:Optional[str] =None
    withheld: Optional["GetusersbyusernameResponseDataWithheld"] = None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyusernameResponseDataAffiliation(BaseModel):
    """Nested model for GetusersbyusernameResponseDataAffiliation"""
    badge_url:Optional[str] =None
    description:Optional[str] =None
    url:Optional[str] =None
    user_id:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyusernameResponseDataEntities(BaseModel):
    """Nested model for GetusersbyusernameResponseDataEntities"""
    description: Optional["GetusersbyusernameResponseDataEntitiesDescription"] = None
    url: Optional["GetusersbyusernameResponseDataEntitiesUrl"] = None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyusernameResponseDataEntitiesDescription(BaseModel):
    """Nested model for GetusersbyusernameResponseDataEntitiesDescription"""
    annotations:Optional[List] =None
    cashtags:Optional[List] =None
    hashtags:Optional[List] =None
    mentions:Optional[List] =None
    urls:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyusernameResponseDataEntitiesUrl(BaseModel):
    """Nested model for GetusersbyusernameResponseDataEntitiesUrl"""
    urls:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyusernameResponseDataPublicMetrics(BaseModel):
    """Nested model for GetusersbyusernameResponseDataPublicMetrics"""
    followers_count:Optional[int] =None
    following_count:Optional[int] =None
    like_count:Optional[int] =None
    listed_count:Optional[int] =None
    tweet_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


class GetusersbyusernameResponseDataWithheld(BaseModel):
    """Nested model for GetusersbyusernameResponseDataWithheld"""
    country_codes:Optional[List] =None
    scope:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









class GetusersbyusernameResponseIncludes(BaseModel):
    """Nested model for GetusersbyusernameResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersMuting








class GetusersmutingResponse(BaseModel):
    """Response model for getUsersMuting"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersmutingResponseIncludes"] =None
    meta: Optional["GetusersmutingResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersmutingResponseIncludes(BaseModel):
    """Nested model for GetusersmutingResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetusersmutingResponseMeta(BaseModel):
    """Nested model for GetusersmutingResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for muteUser

class MuteuserRequest(BaseModel):
    """Request model for muteUser"""
    
    target_user_id: Optional[str] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class MuteuserResponse(BaseModel):
    """Response model for muteUser"""
    
    data: Optional["MuteuserResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True





























class MuteuserResponseData(BaseModel):
    """Nested model for MuteuserResponseData"""
    muting:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for unblockUsersDms








class UnblockusersdmsResponse(BaseModel):
    """Response model for unblockUsersDms"""
    
    data: Optional["UnblockusersdmsResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class UnblockusersdmsResponseData(BaseModel):
    """Nested model for UnblockusersdmsResponseData"""
    blocked:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True












  