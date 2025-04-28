"""
Tweets models for the X API.

This module provides models for the Tweets endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for findTweetById


class find_tweet_by_id_response(BaseModel):
    """Response model for findTweetById"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for deleteTweetById


class delete_tweet_by_id_response(BaseModel):
    """Response model for deleteTweetById"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdRetweets


class users_id_retweets_request(BaseModel):
    """Request model for usersIdRetweets"""

    tweet_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "tweet_id": "1346889436626259968",
            }
        }


class users_id_retweets_response(BaseModel):
    """Response model for usersIdRetweets"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for TwentyEightHoursEngagementApi


class twenty_eight_hours_engagement_api_response(BaseModel):
    """Response model for TwentyEightHoursEngagementApi"""

    data: Optional[List] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for spaceBuyers


class space_buyers_response(BaseModel):
    """Response model for spaceBuyers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdTimeline


class users_id_timeline_response(BaseModel):
    """Response model for usersIdTimeline"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTweetsSample10Stream


class get_tweets_sample10_stream_response(BaseModel):
    """Response model for getTweetsSample10Stream"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for searchStream


class search_stream_response(BaseModel):
    """Response model for searchStream"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    matching_rules: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for spaceTweets


class space_tweets_response(BaseModel):
    """Response model for spaceTweets"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for tweetsRecentSearch


class tweets_recent_search_response(BaseModel):
    """Response model for tweetsRecentSearch"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdTweets


class users_id_tweets_response(BaseModel):
    """Response model for usersIdTweets"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for sampleStream


class sample_stream_response(BaseModel):
    """Response model for sampleStream"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for getTweetsFirehoseStreamLangJa


class get_tweets_firehose_stream_lang_ja_response(BaseModel):
    """Response model for getTweetsFirehoseStreamLangJa"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for usersIdMentions


class users_id_mentions_response(BaseModel):
    """Response model for usersIdMentions"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for tweetCountsRecentSearch


class tweet_counts_recent_search_response(BaseModel):
    """Response model for tweetCountsRecentSearch"""

    data: Optional[List] = None

    errors: Optional[List] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTweetsFirehoseStreamLangEn


class get_tweets_firehose_stream_lang_en_response(BaseModel):
    """Response model for getTweetsFirehoseStreamLangEn"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for listsIdTweets


class lists_id_tweets_response(BaseModel):
    """Response model for listsIdTweets"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findTweetsById


class find_tweets_by_id_response(BaseModel):
    """Response model for findTweetsById"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for createTweet


class create_tweet_request(BaseModel):
    """Request model for createTweet"""

    card_uri: Optional[str] = None

    community_id: Optional[str] = None

    direct_message_deep_link: Optional[str] = None

    for_super_followers_only: Optional[bool] = None

    geo: Optional[Dict[str, Any]] = None

    media: Dict[str, Any] = Field(
        description="Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.",
        default_factory=dict,
    )

    nullcast: Optional[bool] = None

    poll: Dict[str, Any] = Field(
        description="Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.",
        default_factory=dict,
    )

    quote_tweet_id: Optional[str] = None

    reply: Dict[str, Any] = Field(
        description="Tweet information of the Tweet being replied to.",
        default_factory=dict,
    )

    reply_settings: Optional[str] = None

    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "community_id": "1146654567674912769",
                "quote_tweet_id": "1346889436626259968",
                "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\u2026 https:\/\/t.co\/56a0vZUx7i",
            }
        }


# Models for usersIdLikedTweets


class users_id_liked_tweets_response(BaseModel):
    """Response model for usersIdLikedTweets"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findTweetsThatRetweetATweet


class find_tweets_that_retweet_a_tweet_response(BaseModel):
    """Response model for findTweetsThatRetweetATweet"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getRules


class get_rules_response(BaseModel):
    """Response model for getRules"""

    data: Optional[List] = None

    meta: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for addOrDeleteRules


class add_or_delete_rules_request(BaseModel):
    """Request model for addOrDeleteRules"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


class add_or_delete_rules_response(BaseModel):
    """Response model for addOrDeleteRules"""

    data: Optional[List] = None

    errors: Optional[List] = None

    meta: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTweetsFirehoseStreamLangPt


class get_tweets_firehose_stream_lang_pt_response(BaseModel):
    """Response model for getTweetsFirehoseStreamLangPt"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for hideReplyById


class hide_reply_by_id_request(BaseModel):
    """Request model for hideReplyById"""

    hidden: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


class hide_reply_by_id_response(BaseModel):
    """Response model for hideReplyById"""

    data: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for tweetsFullarchiveSearch


class tweets_fullarchive_search_response(BaseModel):
    """Response model for tweetsFullarchiveSearch"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for tweetCountsFullArchiveSearch


class tweet_counts_full_archive_search_response(BaseModel):
    """Response model for tweetCountsFullArchiveSearch"""

    data: Optional[List] = None

    errors: Optional[List] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTweetsFirehoseStream


class get_tweets_firehose_stream_response(BaseModel):
    """Response model for getTweetsFirehoseStream"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for findTweetsThatQuoteATweet


class find_tweets_that_quote_a_tweet_response(BaseModel):
    """Response model for findTweetsThatQuoteATweet"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for HistoricalEngagementApi


class historical_engagement_api_response(BaseModel):
    """Response model for HistoricalEngagementApi"""

    data: Optional[List] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTweetsFirehoseStreamLangKo


class get_tweets_firehose_stream_lang_ko_response(BaseModel):
    """Response model for getTweetsFirehoseStreamLangKo"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "author_id": "2244994945",
                    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
                    "id": "1346889436626259968",
                    "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
                    "username": "XDevelopers",
                },
            }
        }


# Models for usersIdLike


class users_id_like_request(BaseModel):
    """Request model for usersIdLike"""

    tweet_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "tweet_id": "1346889436626259968",
            }
        }


class users_id_like_response(BaseModel):
    """Response model for usersIdLike"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdUnlike


class users_id_unlike_response(BaseModel):
    """Response model for usersIdUnlike"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdUnretweets


class users_id_unretweets_response(BaseModel):
    """Response model for usersIdUnretweets"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
