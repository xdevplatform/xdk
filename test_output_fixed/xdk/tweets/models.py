"""
Tweets models for the X API.

This module provides models for the Tweets endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for streamPostsFirehose








class 2_tweets_firehose_stream_response(BaseModel):
    """Response model for streamPostsFirehose"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsReposts








class 2_tweets_id_retweets_response(BaseModel):
    """Response model for getPostsReposts"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersTimeline








class 2_users_id_timelines_reverse_chronological_response(BaseModel):
    """Response model for getUsersTimeline"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsSample








class 2_tweets_sample_stream_response(BaseModel):
    """Response model for streamPostsSample"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for likePost

class 2_users_id_likes_request(BaseModel):
    """Request model for likePost"""
    
    
    
    
    
    
    tweet_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_likes_response(BaseModel):
    """Response model for likePost"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsAnalytics








class 2_tweets_analytics_response(BaseModel):
    """Response model for getPostsAnalytics"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsFirehoseKo








class 2_tweets_firehose_stream_lang_ko_response(BaseModel):
    """Response model for streamPostsFirehoseKo"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unlikePost








class 2_users_id_likes_tweet_id_response(BaseModel):
    """Response model for unlikePost"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsSample10








class 2_tweets_sample10_stream_response(BaseModel):
    """Response model for streamPostsSample10"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPosts








class 2_tweets_search_stream_response(BaseModel):
    """Response model for streamPosts"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    matching_rules: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsFirehoseEn








class 2_tweets_firehose_stream_lang_en_response(BaseModel):
    """Response model for streamPostsFirehoseEn"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getTweetsIdQuoteTweets








class 2_tweets_id_quote_tweets_response(BaseModel):
    """Response model for getTweetsIdQuoteTweets"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getSpacesPosts








class 2_spaces_id_tweets_response(BaseModel):
    """Response model for getSpacesPosts"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsByIds








class 2_tweets_response(BaseModel):
    """Response model for getPostsByIds"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createPosts

class 2_tweets_request(BaseModel):
    """Request model for createPosts"""
    
    
    
    
    
    
    card_uri: Optional[str] = None
    
    community_id: Optional[str] = None
    
    direct_message_deep_link: Optional[str] = None
    
    for_super_followers_only: Optional[bool] = None
    
    geo: Optional[Dict[str, Any]] = None
    
    media: Dict[str, Any] = Field(description="Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.", default_factory=dict)
    
    nullcast: Optional[bool] = None
    
    poll: Dict[str, Any] = Field(description="Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.", default_factory=dict)
    
    quote_tweet_id: Optional[str] = None
    
    reply: Dict[str, Any] = Field(description="Tweet information of the Tweet being replied to.", default_factory=dict)
    
    reply_settings: Optional[str] = None
    
    text: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_tweets_response(BaseModel):
    """Response model for createPosts"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unrepostPost








class 2_users_id_retweets_source_tweet_id_response(BaseModel):
    """Response model for unrepostPost"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchPostsAll








class 2_tweets_search_all_response(BaseModel):
    """Response model for searchPostsAll"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsFirehoseJa








class 2_tweets_firehose_stream_lang_ja_response(BaseModel):
    """Response model for streamPostsFirehoseJa"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getRules








class 2_tweets_search_stream_rules_response(BaseModel):
    """Response model for getRules"""
    
    
    data: Optional[List] = None
    
    meta: Dict[str, Any] = Field(default_factory=dict)
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for updateRules

class 2_tweets_search_stream_rules_request(BaseModel):
    """Request model for updateRules"""
    
    
    
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_tweets_search_stream_rules_response(BaseModel):
    """Response model for updateRules"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Dict[str, Any] = Field(default_factory=dict)
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getListsPosts








class 2_lists_id_tweets_response(BaseModel):
    """Response model for getListsPosts"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getInsightsHistorical








class 2_insights_historical_response(BaseModel):
    """Response model for getInsightsHistorical"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersLikedPosts








class 2_users_id_liked_tweets_response(BaseModel):
    """Response model for getUsersLikedPosts"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsById








class 2_tweets_id_response(BaseModel):
    """Response model for getPostsById"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deletePosts








class 2_tweets_id_response(BaseModel):
    """Response model for deletePosts"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for hidePostsReply

class 2_tweets_tweet_id_hidden_request(BaseModel):
    """Request model for hidePostsReply"""
    
    
    
    
    
    
    hidden: Optional[bool] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_tweets_tweet_id_hidden_response(BaseModel):
    """Response model for hidePostsReply"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsCountsAll








class 2_tweets_counts_all_response(BaseModel):
    """Response model for getPostsCountsAll"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsCountsRecent








class 2_tweets_counts_recent_response(BaseModel):
    """Response model for getPostsCountsRecent"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersMentions








class 2_users_id_mentions_response(BaseModel):
    """Response model for getUsersMentions"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for repostPost

class 2_users_id_retweets_request(BaseModel):
    """Request model for repostPost"""
    
    
    
    
    
    
    tweet_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_retweets_response(BaseModel):
    """Response model for repostPost"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchPostsRecent








class 2_tweets_search_recent_response(BaseModel):
    """Response model for searchPostsRecent"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsFirehosePt








class 2_tweets_firehose_stream_lang_pt_response(BaseModel):
    """Response model for streamPostsFirehosePt"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getSpacesBuyers








class 2_spaces_id_buyers_response(BaseModel):
    """Response model for getSpacesBuyers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getInsights28Hr








class 2_insights_28hr_response(BaseModel):
    """Response model for getInsights28Hr"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersPosts








class 2_users_id_tweets_response(BaseModel):
    """Response model for getUsersPosts"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 