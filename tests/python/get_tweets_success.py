import pytest
import json
import os
from pathlib import Path
from xdk import Client

# Global flag for verbose output
VERBOSE = False

def get_bearer_token():
    xurl_path = Path.home() / '.xurl'
    if not xurl_path.exists():
        raise FileNotFoundError("~/.xurl file not found")
    
    with open(xurl_path) as f:
        data = json.load(f)
        # Get the first OAuth2 token's access token
        bearer_token = data.get('bearer_token', {})
        if not bearer_token:
            raise ValueError("No bearer token found in ~/.xurl")
        return bearer_token.get('bearer')

def test_get_tweets():
    # Initialize the main client with bearer token from ~/.xurl
    bearer_token = get_bearer_token()
    client = Client(
        base_url="https://api.twitter.com",
        bearer_token=bearer_token
    )
    
    # The tweets client is already initialized as part of the main client
    tweets_client = client.tweets
    
    # Test fetching tweets by ID
    tweet_ids = ["20", "53"]  # Replace with actual tweet IDs
    response = tweets_client.find_tweets_by_id(
        ids=tweet_ids,
        tweet_fields=["text", "created_at"],
        expansions=["author_id"],
        user_fields=["username", "name"]
    )
    # Assert that we got a response
    assert response is not None
    if VERBOSE:
        print("\nTweets by ID Response:")
        print(response.model_dump_json(indent=2))
    
    # Test searching recent tweets
    search_response = tweets_client.tweets_recent_search(
        query="python",
        max_results=10,
        tweet_fields=["text", "created_at"],
        expansions=["author_id"],
        user_fields=["username", "name"]
    )
    
    # Assert that we got a response
    assert search_response is not None
    if VERBOSE:
        print("\nRecent Search Response:")
        print(search_response.model_dump_json(indent=2))
    
    # Test getting user tweets
    user_tweets = tweets_client.users_id_tweets(
        id="44196397",
        max_results=10,
        tweet_fields=["text", "created_at"],
        expansions=["author_id"],
        user_fields=["username", "name"]
    )
    
    # Assert that we got a response
    assert user_tweets is not None
    if VERBOSE:
        print("\nUser Tweets Response:")
        print(user_tweets.model_dump_json(indent=2))

if __name__ == "__main__":
    pytest.main([__file__])
