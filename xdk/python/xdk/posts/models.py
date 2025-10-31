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
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetRepostedByResponseIncludes"] =None
    meta: Optional["GetRepostedByResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetRepostedByResponseIncludes(BaseModel):
    """Nested model for GetRepostedByResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)






class GetRepostedByResponseMeta(BaseModel):
    """Nested model for GetRepostedByResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for get_counts_recent








class GetCountsRecentResponse(BaseModel):
    """Response model for get_counts_recent"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    meta: Optional["GetCountsRecentResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetCountsRecentResponseMeta(BaseModel):
    """Nested model for GetCountsRecentResponseMeta"""
    newest_id:Optional[str] =None
    next_token:Optional[str] =None
    oldest_id:Optional[str] =None
    total_tweet_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for get_analytics








class GetAnalyticsResponse(BaseModel):
    """Response model for get_analytics"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)





























# Models for get_insights_historical








class GetInsightsHistoricalResponse(BaseModel):
    """Response model for get_insights_historical"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)





























# Models for search_recent








class SearchRecentResponse(BaseModel):
    """Response model for search_recent"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["SearchRecentResponseIncludes"] =None
    meta: Optional["SearchRecentResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class SearchRecentResponseIncludes(BaseModel):
    """Nested model for SearchRecentResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)






class SearchRecentResponseMeta(BaseModel):
    """Nested model for SearchRecentResponseMeta"""
    newest_id:Optional[str] =None
    next_token:Optional[str] =None
    oldest_id:Optional[str] =None
    result_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for get_insights28hr








class GetInsights28hrResponse(BaseModel):
    """Response model for get_insights28hr"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)





























# Models for get_by_id








class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""
    
    data: Optional["GetByIdResponseData"] =None
    errors: Optional[List] =None
    includes: Optional["GetByIdResponseIncludes"] =None
    

    model_config = ConfigDict(populate_by_name=True)


















class GetByIdResponseData(BaseModel):
    """Nested model for GetByIdResponseData"""
    attachments: Optional["GetByIdResponseDataAttachments"] = None
    author_id:Optional[str] =None
    community_id:Optional[str] =None
    context_annotations:Optional[List] =None
    conversation_id:Optional[str] =None
    created_at:Optional[str] =None
    display_text_range:Optional[List] =None
    edit_controls: Optional["GetByIdResponseDataEditControls"] = None
    edit_history_tweet_ids:Optional[List] =None
    entities: Optional["GetByIdResponseDataEntities"] = None
    geo: Optional["GetByIdResponseDataGeo"] = None
    id:Optional[str] =None
    in_reply_to_user_id:Optional[str] =None
    lang:Optional[str] =None
    non_public_metrics: Optional["GetByIdResponseDataNonPublicMetrics"] = None
    note_tweet: Optional["GetByIdResponseDataNoteTweet"] = None
    organic_metrics: Optional["GetByIdResponseDataOrganicMetrics"] = None
    possibly_sensitive:Optional[bool] =None
    promoted_metrics: Optional["GetByIdResponseDataPromotedMetrics"] = None
    public_metrics: Optional["GetByIdResponseDataPublicMetrics"] = None
    referenced_tweets:Optional[List] =None
    reply_settings:Optional[str] =None
    scopes: Optional["GetByIdResponseDataScopes"] = None
    source:Optional[str] =None
    suggested_source_links:Optional[List] =None
    text:Optional[str] =None
    username:Optional[str] =None
    withheld: Optional["GetByIdResponseDataWithheld"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataAttachments(BaseModel):
    """Nested model for GetByIdResponseDataAttachments"""
    media_keys:Optional[List] =None
    media_source_tweet_id:Optional[List] =None
    poll_ids:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataEditControls(BaseModel):
    """Nested model for GetByIdResponseDataEditControls"""
    editable_until:Optional[str] =None
    edits_remaining:Optional[int] =None
    is_edit_eligible:Optional[bool] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataEntities(BaseModel):
    """Nested model for GetByIdResponseDataEntities"""
    annotations:Optional[List] =None
    cashtags:Optional[List] =None
    hashtags:Optional[List] =None
    mentions:Optional[List] =None
    urls:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataGeo(BaseModel):
    """Nested model for GetByIdResponseDataGeo"""
    coordinates: Optional["GetByIdResponseDataGeoCoordinates"] = None
    place_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataGeoCoordinates(BaseModel):
    """Nested model for GetByIdResponseDataGeoCoordinates"""
    coordinates:Optional[List] =None
    type:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataNonPublicMetrics(BaseModel):
    """Nested model for GetByIdResponseDataNonPublicMetrics"""
    impression_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataNoteTweet(BaseModel):
    """Nested model for GetByIdResponseDataNoteTweet"""
    entities: Optional["GetByIdResponseDataNoteTweetEntities"] = None
    text:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataNoteTweetEntities(BaseModel):
    """Nested model for GetByIdResponseDataNoteTweetEntities"""
    cashtags:Optional[List] =None
    hashtags:Optional[List] =None
    mentions:Optional[List] =None
    urls:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataOrganicMetrics(BaseModel):
    """Nested model for GetByIdResponseDataOrganicMetrics"""
    impression_count:Optional[int] =None
    like_count:Optional[int] =None
    reply_count:Optional[int] =None
    retweet_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataPromotedMetrics(BaseModel):
    """Nested model for GetByIdResponseDataPromotedMetrics"""
    impression_count:Optional[int] =None
    like_count:Optional[int] =None
    reply_count:Optional[int] =None
    retweet_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataPublicMetrics(BaseModel):
    """Nested model for GetByIdResponseDataPublicMetrics"""
    bookmark_count:Optional[int] =None
    impression_count:Optional[int] =None
    like_count:Optional[int] =None
    quote_count:Optional[int] =None
    reply_count:Optional[int] =None
    retweet_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataScopes(BaseModel):
    """Nested model for GetByIdResponseDataScopes"""
    followers:Optional[bool] =None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseDataWithheld(BaseModel):
    """Nested model for GetByIdResponseDataWithheld"""
    copyright:Optional[bool] =None
    country_codes:Optional[List] =None
    scope:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)









class GetByIdResponseIncludes(BaseModel):
    """Nested model for GetByIdResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for delete








class DeleteResponse(BaseModel):
    """Response model for delete"""
    
    data: Optional["DeleteResponseData"] =Field(default_factory=dict)
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)


















class DeleteResponseData(BaseModel):
    """Nested model for DeleteResponseData"""
    deleted:Optional[bool] =None

    model_config = ConfigDict(populate_by_name=True)














# Models for get_by_ids








class GetByIdsResponse(BaseModel):
    """Response model for get_by_ids"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetByIdsResponseIncludes"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetByIdsResponseIncludes(BaseModel):
    """Nested model for GetByIdsResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for create

class CreateRequest(BaseModel):
    """Request model for create"""
    
    card_uri: Optional[str] =None
    community_id: Optional[str] =None
    direct_message_deep_link: Optional[str] =None
    edit_options: Optional["CreateRequestEditOptions"] =Field(description="Options for editing an existing Post. When provided, this request will edit the specified Post instead of creating a new one.",default_factory=dict)
    for_super_followers_only: Optional[bool] =None
    geo: Optional["CreateRequestGeo"] =None
    media: Optional["CreateRequestMedia"] =Field(description="Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.",default_factory=dict)
    nullcast: Optional[bool] =None
    poll: Optional["CreateRequestPoll"] =Field(description="Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.",default_factory=dict)
    quote_tweet_id: Optional[str] =None
    reply: Optional["CreateRequestReply"] =Field(description="Tweet information of the Tweet being replied to.",default_factory=dict)
    reply_settings: Optional[str] =None
    share_with_followers: Optional[bool] =None
    text: Optional[str] =None
    

    model_config = ConfigDict(populate_by_name=True)








class CreateResponse(BaseModel):
    """Response model for create"""
    
    data: Optional["CreateResponseData"] =Field(default_factory=dict)
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)






















class CreateRequestEditOptions(BaseModel):
    """Nested model for CreateRequestEditOptions"""
    previous_post_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)









class CreateRequestGeo(BaseModel):
    """Nested model for CreateRequestGeo"""
    place_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)






class CreateRequestMedia(BaseModel):
    """Nested model for CreateRequestMedia"""
    media_ids:Optional[List] =None
    tagged_user_ids:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)









class CreateRequestPoll(BaseModel):
    """Nested model for CreateRequestPoll"""
    duration_minutes:Optional[int] =None
    options:Optional[List] =None
    reply_settings:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)









class CreateRequestReply(BaseModel):
    """Nested model for CreateRequestReply"""
    exclude_reply_user_ids:Optional[List] =None
    in_reply_to_tweet_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)




























class CreateResponseData(BaseModel):
    """Nested model for CreateResponseData"""
    id:Optional[str] =None
    text:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)














# Models for get_counts_all








class GetCountsAllResponse(BaseModel):
    """Response model for get_counts_all"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    meta: Optional["GetCountsAllResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetCountsAllResponseMeta(BaseModel):
    """Nested model for GetCountsAllResponseMeta"""
    newest_id:Optional[str] =None
    next_token:Optional[str] =None
    oldest_id:Optional[str] =None
    total_tweet_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for get_quoted








class GetQuotedResponse(BaseModel):
    """Response model for get_quoted"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetQuotedResponseIncludes"] =None
    meta: Optional["GetQuotedResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetQuotedResponseIncludes(BaseModel):
    """Nested model for GetQuotedResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)






class GetQuotedResponseMeta(BaseModel):
    """Nested model for GetQuotedResponseMeta"""
    next_token:Optional[str] =None
    result_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for get_liking_users








class GetLikingUsersResponse(BaseModel):
    """Response model for get_liking_users"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetLikingUsersResponseIncludes"] =None
    meta: Optional["GetLikingUsersResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetLikingUsersResponseIncludes(BaseModel):
    """Nested model for GetLikingUsersResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)






class GetLikingUsersResponseMeta(BaseModel):
    """Nested model for GetLikingUsersResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for search_all








class SearchAllResponse(BaseModel):
    """Response model for search_all"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["SearchAllResponseIncludes"] =None
    meta: Optional["SearchAllResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class SearchAllResponseIncludes(BaseModel):
    """Nested model for SearchAllResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)






class SearchAllResponseMeta(BaseModel):
    """Nested model for SearchAllResponseMeta"""
    newest_id:Optional[str] =None
    next_token:Optional[str] =None
    oldest_id:Optional[str] =None
    result_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for hide_reply

class HideReplyRequest(BaseModel):
    """Request model for hide_reply"""
    
    hidden: Optional[bool] =None
    

    model_config = ConfigDict(populate_by_name=True)








class HideReplyResponse(BaseModel):
    """Response model for hide_reply"""
    
    data: Optional["HideReplyResponseData"] =None
    

    model_config = ConfigDict(populate_by_name=True)





























class HideReplyResponseData(BaseModel):
    """Nested model for HideReplyResponseData"""
    hidden:Optional[bool] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for get_reposts








class GetRepostsResponse(BaseModel):
    """Response model for get_reposts"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetRepostsResponseIncludes"] =None
    meta: Optional["GetRepostsResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetRepostsResponseIncludes(BaseModel):
    """Nested model for GetRepostsResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    model_config = ConfigDict(populate_by_name=True)






class GetRepostsResponseMeta(BaseModel):
    """Nested model for GetRepostsResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)









  