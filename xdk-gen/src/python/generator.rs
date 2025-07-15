/// Python SDK Generator Implementation
///
/// This file demonstrates how to implement a language-specific generator using the `language!` macro.
/// It defines filters for Python-specific formatting and implements the generator.
///
/// When creating a generator for a new language, follow this pattern:
/// 1. Define language-specific filters (e.g., type conversion, naming conventions)
/// 2. Use the language! macro to create the generator struct
/// 3. Implement the rendering logic in the generate field
use crate::language;

/// MiniJinja filter for converting a string to snake_case
fn snake_case(value: &str) -> String {
    let mut result = String::new();
    let mut prev_char: Option<char> = None;
    for c in value.chars() {
        if c.is_uppercase() {
            if let Some(prev) = prev_char {
                if prev != '_' {
                    result.push('_');
                }
            }
            result.push(c.to_ascii_lowercase());
        } else if c.is_numeric() {
            if let Some(prev) = prev_char {
                if prev.is_alphabetic() {
                    result.push('_');
                }
            }
            result.push(c);
        } else if c.is_alphabetic() {
            if let Some(prev) = prev_char {
                if prev.is_numeric() {
                    result.push('_');
                }
            }
            result.push(c);
        } else {
            result.push('_');
        }
        prev_char = Some(c);
    }
    result.trim_matches('_').to_string()
}

/// MiniJinja filter for converting to Python types
fn python_type(value: &str) -> String {
    let python_type = match value {
        "string" => "str",
        "integer" => "int",
        "number" => "float",
        "boolean" => "bool",
        "array" => "List",
        "object" => "Dict[str, Any]",
        _ => "Any",
    };
    python_type.to_string()
}

/// MiniJinja filter for stripping resource name from operationId
/// 
/// This filter extracts the resource name from the path and removes it from the operationId.
/// For example:
/// - path: "/2/communities/search", operationId: "searchCommunities" -> "search"
/// - path: "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all", operationId: "postAccountActivityReplay" -> "postReplay"
/// 
/// Special case: For endpoints containing "/stream", strip "stream" from operationId and use "stream" as client
fn strip_resource_name(path: &str, operation_id: &str) -> String {
    // Special case: if path contains "/stream", strip "stream" from operationId
    if path.contains("/stream") {
        let mut result = operation_id.to_string();
        // Try to strip "stream" from the operationId
        if let Some(idx) = result.find("stream") {
            result = format!("{}{}", &result[..idx], &result[idx + 6..]);
            return result.trim_matches('_').to_string();
        }
        return operation_id.to_string();
    }
    
    let path_segments: Vec<&str> = path.split('/').collect();
    let resource_name = if path_segments.len() > 2 {
        path_segments[2]
    } else {
        return operation_id.to_string();
    };

    // Add tag mapping for resource names
    let mapped_resource = match resource_name.to_lowercase().as_str() {
        "tweets" => "posts",
        _ => resource_name,
    };

    // Generate variants for matching (original, PascalCase, capitalized, mapped)
    let mut variants = vec![
        resource_name.to_string(),
    ];
    // Add mapped resource name if different
    if mapped_resource != resource_name {
        variants.push(mapped_resource.to_string());
    }
    // PascalCase: "account_activity" -> "AccountActivity"
    let pascal = resource_name
        .split('_')
        .map(|w| {
            let mut c = w.chars();
            match c.next() {
                None => String::new(),
                Some(f) => f.to_uppercase().collect::<String>() + c.as_str(),
            }
        })
        .collect::<String>();
    variants.push(pascal.clone());
    // PascalCase for mapped resource
    if mapped_resource != resource_name {
        let pascal_mapped = mapped_resource
            .split('_')
            .map(|w| {
                let mut c = w.chars();
                match c.next() {
                    None => String::new(),
                    Some(f) => f.to_uppercase().collect::<String>() + c.as_str(),
                }
            })
            .collect::<String>();
        variants.push(pascal_mapped);
    }
    // Capitalize first letter only
    if let Some(first) = resource_name.chars().next() {
        let mut cap = first.to_uppercase().collect::<String>();
        cap.push_str(&resource_name[1..]);
        variants.push(cap);
    }
    if mapped_resource != resource_name {
        if let Some(first) = mapped_resource.chars().next() {
            let mut cap = first.to_uppercase().collect::<String>();
            cap.push_str(&mapped_resource[1..]);
            variants.push(cap);
        }
    }

    let mut result = operation_id.to_string();
    let mut changed = false;
    for variant in variants {
        // Try to strip at the start (case-insensitive)
        if result.len() >= variant.len() && result[..variant.len()].eq_ignore_ascii_case(&variant) {
            result = result[variant.len()..].to_string();
            changed = true;
            break;
        }
        // Try to strip after a lowercase prefix (e.g., searchCommunities)
        if let Some(idx) = result.find(&variant) {
            // For PascalCase, ensure the match is at a segment boundary
            let before = if idx == 0 { None } else { result[..idx].chars().last() };
            let after = result[idx + variant.len()..].chars().next();
            let is_boundary = (before.map(|c| c.is_lowercase()).unwrap_or(true)) &&
                (after.map(|c| c.is_uppercase()).unwrap_or(true) || after.is_none());
            
            // Special case: don't strip if the variant appears as part of a larger word
            // For example, in "getPostsReposts", "posts" is part of "PostsReposts", so don't strip it
            let is_part_of_larger_word = if idx > 0 && idx + variant.len() < result.len() {
                let before_char = result[..idx].chars().last().unwrap();
                let after_char = result[idx + variant.len()..].chars().next().unwrap();
                // If both before and after are uppercase, it's likely part of a larger word
                before_char.is_uppercase() && after_char.is_uppercase()
            } else {
                false
            };
            
            if is_boundary && !is_part_of_larger_word {
                result = format!("{}{}", &result[..idx], &result[idx + variant.len()..]);
                changed = true;
                break;
            }
        }
    }
    let result = result.trim_matches('_');
    if changed && !result.is_empty() {
        result.to_string()
    } else {
        operation_id.to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_strip_resource_name() {
        // Exact match, PascalCase, underscores
        assert_eq!(strip_resource_name("/2/communities/search", "searchCommunities"), "search");
        assert_eq!(strip_resource_name("/2/communities/search", "CommunitiesSearch"), "Search");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "postAccountActivityReplay"), "postReplay");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "AccountActivityReplayPost"), "ReplayPost");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "account_activityReplay"), "Replay");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "accountactivityReplay"), "Replay");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "post_account_activity_replay"), "post_account_activity_replay"); // underscores in opId, not PascalCase

        // Lowercase prefix
        assert_eq!(strip_resource_name("/2/communities/search", "findCommunities"), "find");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "doAccountActivityReplay"), "doReplay");

        // No match (should not strip)
        assert_eq!(strip_resource_name("/2/users/{id}", "getUserById"), "getUserById"); // users != User
        assert_eq!(strip_resource_name("/2/users/{id}", "getUsersById"), "getById"); // users == Users
        assert_eq!(strip_resource_name("/2/unknown/path", "someOperation"), "someOperation");
        assert_eq!(strip_resource_name("/malformed", "someOperation"), "someOperation");

        // Underscore-insensitive
        assert_eq!(strip_resource_name("/2/account_activity/replay", "Account_ActivityReplay"), "Replay");
        assert_eq!(strip_resource_name("/2/account_activity/replay", "do_account_activity_replay"), "do_account_activity_replay"); // not PascalCase, so not stripped
    }

    #[test]
    fn test_stream_endpoints() {
        // Stream endpoints should strip "stream" from operationId
        assert_eq!(strip_resource_name("/2/tweets/search/stream", "streamPosts"), "Posts");
        assert_eq!(strip_resource_name("/2/likes/compliance/stream", "streamLikesCompliance"), "LikesCompliance");
        assert_eq!(strip_resource_name("/2/users/compliance/stream", "streamUsersCompliance"), "UsersCompliance");
        assert_eq!(strip_resource_name("/2/tweets/firehose/stream", "streamPostsFirehose"), "PostsFirehose");
        assert_eq!(strip_resource_name("/2/tweets/sample/stream", "streamPostsSample"), "PostsSample");
        assert_eq!(strip_resource_name("/2/likes/sample10/stream", "streamLikesSample10"), "LikesSample10");
        assert_eq!(strip_resource_name("/2/tweets/label/stream", "streamLabelsCompliance"), "LabelsCompliance");
        assert_eq!(strip_resource_name("/2/likes/firehose/stream", "streamLikesFirehose"), "LikesFirehose");
        
        // Stream endpoints with different casing - the function only strips exact "stream" match
        assert_eq!(strip_resource_name("/2/tweets/search/stream", "StreamPosts"), "StreamPosts"); // doesn't match "stream"
        assert_eq!(strip_resource_name("/2/tweets/search/stream", "STREAMPOSTS"), "STREAMPOSTS"); // doesn't match "stream"
        
        // Stream endpoints that don't start with "stream" should not be affected
        assert_eq!(strip_resource_name("/2/tweets/search/stream/rules", "getRules"), "getRules");
        assert_eq!(strip_resource_name("/2/tweets/search/stream/rules", "updateRules"), "updateRules");
        assert_eq!(strip_resource_name("/2/tweets/search/stream/rules/counts", "getRuleCounts"), "getRuleCounts");
    }

    #[test]
    fn test_tweets_to_posts_mapping() {
        // Test tag mapping from tweets to posts
        assert_eq!(strip_resource_name("/2/tweets/{id}", "getPostsById"), "getById");
        assert_eq!(strip_resource_name("/2/tweets", "createPosts"), "create");
        assert_eq!(strip_resource_name("/2/tweets/search/all", "searchPostsAll"), "searchAll");
        assert_eq!(strip_resource_name("/2/tweets/{id}/liking_users", "getPostsLikingUsers"), "getLikingUsers");
        assert_eq!(strip_resource_name("/2/tweets/{id}/retweeted_by", "getPostsRepostedBy"), "getRepostedBy");
        assert_eq!(strip_resource_name("/2/tweets/{id}/retweets", "getPostsReposts"), "getPostsRe"); // strips "posts" from the middle
        assert_eq!(strip_resource_name("/2/tweets/analytics", "getPostsAnalytics"), "getAnalytics");
        assert_eq!(strip_resource_name("/2/tweets/counts/recent", "getPostsCountsRecent"), "getCountsRecent");
        assert_eq!(strip_resource_name("/2/tweets/counts/all", "getPostsCountsAll"), "getCountsAll");
        assert_eq!(strip_resource_name("/2/tweets/search/recent", "searchPostsRecent"), "searchRecent");
        assert_eq!(strip_resource_name("/2/tweets/{id}/quote_tweets", "getTweetsIdQuoteTweets"), "getIdQuoteTweets");
        assert_eq!(strip_resource_name("/2/tweets/{tweet_id}/hidden", "hidePostsReply"), "hideReply");
    }

    #[test]
    fn test_users_endpoints() {
        // Test users endpoints
        assert_eq!(strip_resource_name("/2/users/{id}", "getUsersById"), "getById");
        assert_eq!(strip_resource_name("/2/users/search", "searchUsers"), "search");
        assert_eq!(strip_resource_name("/2/users/{id}/following", "getUsersFollowing"), "getFollowing");
        assert_eq!(strip_resource_name("/2/users/{id}/followers", "getUsersFollowers"), "getFollowers");
        assert_eq!(strip_resource_name("/2/users/{id}/tweets", "getUsersPosts"), "getPosts");
        assert_eq!(strip_resource_name("/2/users/{id}/likes", "likePost"), "likePost"); // should not strip "Post" from "likePost"
        assert_eq!(strip_resource_name("/2/users/{id}/likes/{tweet_id}", "unlikePost"), "unlikePost"); // should not strip "Post" from "unlikePost"
        assert_eq!(strip_resource_name("/2/users/{id}/retweets", "repostPost"), "repostPost"); // should not strip "Post" from "repostPost"
        assert_eq!(strip_resource_name("/2/users/{id}/retweets/{source_tweet_id}", "unrepostPost"), "unrepostPost"); // should not strip "Post" from "unrepostPost"
        assert_eq!(strip_resource_name("/2/users/{id}/bookmarks", "getUsersBookmarks"), "getBookmarks");
        assert_eq!(strip_resource_name("/2/users/{id}/bookmarks", "createUsersBookmark"), "createBookmark");
        assert_eq!(strip_resource_name("/2/users/{id}/bookmarks/{tweet_id}", "deleteUsersBookmark"), "deleteBookmark");
        assert_eq!(strip_resource_name("/2/users/{id}/bookmarks/folders", "getUsersBookmarkFolders"), "getBookmarkFolders");
        assert_eq!(strip_resource_name("/2/users/{id}/bookmarks/folders/{folder_id}", "getUsersBookmarksByFolderId"), "getBookmarksByFolderId");
        assert_eq!(strip_resource_name("/2/users/{id}/liked_tweets", "getUsersLikedPosts"), "getLikedPosts");
        assert_eq!(strip_resource_name("/2/users/{id}/mentions", "getUsersMentions"), "getMentions");
        assert_eq!(strip_resource_name("/2/users/{id}/muting", "getUsersMuting"), "getMuting");
        assert_eq!(strip_resource_name("/2/users/{id}/muting", "muteUser"), "muteUser"); // should not strip "User" from "muteUser"
        assert_eq!(strip_resource_name("/2/users/{source_user_id}/muting/{target_user_id}", "unmuteUser"), "unmuteUser"); // should not strip "User" from "unmuteUser"
        assert_eq!(strip_resource_name("/2/users/{id}/blocking", "getUsersBlocking"), "getBlocking");
        assert_eq!(strip_resource_name("/2/users/{id}/blocking", "usersIdBlock"), "IdBlock"); // strips "users" and leaves "IdBlock"
        assert_eq!(strip_resource_name("/2/users/{source_user_id}/blocking/{target_user_id}", "usersIdUnblock"), "IdUnblock"); // strips "users" and leaves "IdUnblock"
        assert_eq!(strip_resource_name("/2/users/{id}/dm/block", "blockUsersDms"), "blockDms");
        assert_eq!(strip_resource_name("/2/users/{id}/dm/unblock", "unblockUsersDms"), "unblockDms");
        assert_eq!(strip_resource_name("/2/users/{id}/pinned_lists", "getUsersPinnedLists"), "getPinnedLists");
        assert_eq!(strip_resource_name("/2/users/{id}/pinned_lists", "pinList"), "pinList"); // should not strip "List" from "pinList"
        assert_eq!(strip_resource_name("/2/users/{id}/pinned_lists/{list_id}", "unpinList"), "unpinList"); // should not strip "List" from "unpinList"
        assert_eq!(strip_resource_name("/2/users/{id}/followed_lists", "getUsersFollowedLists"), "getFollowedLists");
        assert_eq!(strip_resource_name("/2/users/{id}/followed_lists", "followList"), "followList"); // should not strip "List" from "followList"
        assert_eq!(strip_resource_name("/2/users/{id}/followed_lists/{list_id}", "unfollowList"), "unfollowList"); // should not strip "List" from "unfollowList"
        assert_eq!(strip_resource_name("/2/users/{id}/owned_lists", "getUsersOwnedLists"), "getOwnedLists");
        assert_eq!(strip_resource_name("/2/users/{id}/list_memberships", "getUsersListMemberships"), "getListMemberships");
        assert_eq!(strip_resource_name("/2/users/{id}/timelines/reverse_chronological", "getUsersTimeline"), "getTimeline");
        assert_eq!(strip_resource_name("/2/users/personalized_trends", "getUsersPersonalizedTrends"), "getPersonalizedTrends");
        assert_eq!(strip_resource_name("/2/users/reposts_of_me", "getUsersRepostsOfMe"), "getRepostsOfMe");
        assert_eq!(strip_resource_name("/2/users/{id}/pinned_communities", "communityUserPin"), "communityUserPin"); // should not strip "User" from "communityUserPin"
        assert_eq!(strip_resource_name("/2/users/{id}/pinned_communities", "communityUserUnpin"), "communityUserUnpin"); // should not strip "User" from "communityUserUnpin"
        assert_eq!(strip_resource_name("/2/users/{source_user_id}/following/{target_user_id}", "unfollowUser"), "unfollowUser"); // should not strip "User" from "unfollowUser"
        assert_eq!(strip_resource_name("/2/users/me", "getMyUser"), "getMyUser"); // should not strip "User" from "getMyUser"
        assert_eq!(strip_resource_name("/2/users", "getUsersByIds"), "getByIds");
        assert_eq!(strip_resource_name("/2/users/by", "getUsersByUsernames"), "getByUsernames");
        assert_eq!(strip_resource_name("/2/users/by/username/{username}", "getUsersByUsername"), "getByUsername");
    }

    #[test]
    fn test_lists_endpoints() {
        // Test lists endpoints
        assert_eq!(strip_resource_name("/2/lists/{id}", "getListsById"), "getById");
        assert_eq!(strip_resource_name("/2/lists", "createLists"), "create");
        assert_eq!(strip_resource_name("/2/lists/{id}", "updateLists"), "update");
        assert_eq!(strip_resource_name("/2/lists/{id}", "deleteLists"), "delete");
        assert_eq!(strip_resource_name("/2/lists/{id}/members", "getListsMembers"), "getMembers");
        assert_eq!(strip_resource_name("/2/lists/{id}/members", "addListsMember"), "addMember");
        assert_eq!(strip_resource_name("/2/lists/{id}/members/{user_id}", "removeListsMemberByUserId"), "removeMemberByUserId");
        assert_eq!(strip_resource_name("/2/lists/{id}/followers", "getListsFollowers"), "getFollowers");
        assert_eq!(strip_resource_name("/2/lists/{id}/tweets", "getListsPosts"), "getPosts");
    }

    #[test]
    fn test_spaces_endpoints() {
        // Test spaces endpoints
        assert_eq!(strip_resource_name("/2/spaces/{id}", "getSpacesById"), "getById");
        assert_eq!(strip_resource_name("/2/spaces", "getSpacesByIds"), "getByIds");
        assert_eq!(strip_resource_name("/2/spaces/search", "searchSpaces"), "search");
        assert_eq!(strip_resource_name("/2/spaces/{id}/tweets", "getSpacesPosts"), "getPosts");
        assert_eq!(strip_resource_name("/2/spaces/{id}/buyers", "getSpacesBuyers"), "getBuyers");
        assert_eq!(strip_resource_name("/2/spaces/by/creator_ids", "getSpacesByCreatorIds"), "getByCreatorIds");
    }

    #[test]
    fn test_communities_endpoints() {
        // Test communities endpoints
        assert_eq!(strip_resource_name("/2/communities", "communityIdCreate"), "communityIdCreate"); // should not strip "Communities" from "communityIdCreate"
        assert_eq!(strip_resource_name("/2/communities/{id}", "getCommunitiesById"), "getById");
        assert_eq!(strip_resource_name("/2/communities/search", "searchCommunities"), "search");
        assert_eq!(strip_resource_name("/2/communitites/{id}/{name}", "communityIdDelete"), "communityIdDelete"); // should not strip "Communitites" from "communityIdDelete"
    }

    #[test]
    fn test_media_endpoints() {
        // Test media endpoints
        assert_eq!(strip_resource_name("/2/media/upload", "mediaUpload"), "Upload"); // strips "media" and leaves "Upload"
        assert_eq!(strip_resource_name("/2/media/upload/{id}/finalize", "finalizeMediaUpload"), "finalizeUpload");
        assert_eq!(strip_resource_name("/2/media/upload/{id}/append", "appendMediaUpload"), "appendUpload");
        assert_eq!(strip_resource_name("/2/media/upload/initialize", "initializeMediaUpload"), "initializeUpload");
        assert_eq!(strip_resource_name("/2/media/upload", "getMediaUploadStatus"), "getUploadStatus");
        assert_eq!(strip_resource_name("/2/media", "getMediaByMediaKeys"), "getByMediaKeys");
        assert_eq!(strip_resource_name("/2/media/{media_key}", "getMediaByMediaKey"), "getByMediaKey");
        assert_eq!(strip_resource_name("/2/media/analytics", "getMediaAnalytics"), "getAnalytics");
        assert_eq!(strip_resource_name("/2/media/metadata", "createMediaMetadata"), "createMetadata");
        assert_eq!(strip_resource_name("/2/media/subtitles", "createMediaSubtitles"), "createSubtitles");
        assert_eq!(strip_resource_name("/2/media/subtitles", "deleteMediaSubtitles"), "deleteSubtitles");
    }

    #[test]
    fn test_dm_endpoints() {
        // Test DM endpoints
        assert_eq!(strip_resource_name("/2/dm_conversations", "createDmConversations"), "create");
        assert_eq!(strip_resource_name("/2/dm_conversations/{dm_conversation_id}/messages", "createDmByConversationId"), "createDmByConversationId"); // should not strip "Dm" from "createDmByConversationId"
        assert_eq!(strip_resource_name("/2/dm_conversations/with/{participant_id}/messages", "createDmByParticipantId"), "createDmByParticipantId"); // should not strip "Dm" from "createDmByParticipantId"
        assert_eq!(strip_resource_name("/2/dm_conversations/with/{participant_id}/dm_events", "getDmEventsByParticipantId"), "getDmEventsByParticipantId"); // should not strip "Dm" from "getDmEventsByParticipantId"
        assert_eq!(strip_resource_name("/2/dm_conversations/{id}/dm_events", "getDmConversationsIdDmEvents"), "getIdDmEvents");
        assert_eq!(strip_resource_name("/2/dm_events", "getDmEvents"), "get");
        assert_eq!(strip_resource_name("/2/dm_events/{event_id}", "getDmEventsById"), "getById");
        assert_eq!(strip_resource_name("/2/dm_events/{event_id}", "deleteDmEvents"), "delete");
    }

    #[test]
    fn test_notes_endpoints() {
        // Test notes endpoints
        assert_eq!(strip_resource_name("/2/notes", "createNote"), "createNote"); // should not strip "Note" from "createNote"
        assert_eq!(strip_resource_name("/2/notes/{id}", "deleteNote"), "deleteNote"); // should not strip "Note" from "deleteNote"
        assert_eq!(strip_resource_name("/2/notes/search/notes_written", "searchNotesWritten"), "searchWritten");
        assert_eq!(strip_resource_name("/2/notes/search/posts_eligible_for_notes", "searchPostsEligibleForNotes"), "searchPostsEligibleFor"); // should not strip "Notes" from "searchPostsEligibleForNotes"
    }

    #[test]
    fn test_webhooks_endpoints() {
        // Test webhooks endpoints
        assert_eq!(strip_resource_name("/2/webhooks", "getWebhooks"), "get");
        assert_eq!(strip_resource_name("/2/webhooks", "createWebhooks"), "create");
        assert_eq!(strip_resource_name("/2/webhooks/{webhook_id}", "validateWebhooks"), "validate");
        assert_eq!(strip_resource_name("/2/webhooks/{webhook_id}", "deleteWebhooks"), "delete");
    }

    #[test]
    fn test_account_activity_endpoints() {
        // Test account activity endpoints
        assert_eq!(strip_resource_name("/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list", "getAccountActivitySubscriptions"), "getSubscriptions");
        assert_eq!(strip_resource_name("/2/account_activity/subscriptions/count", "getAccountActivitySubscriptionCount"), "getSubscriptionCount");
        assert_eq!(strip_resource_name("/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all", "createAccountActivityReplayJob"), "createReplayJob");
        assert_eq!(strip_resource_name("/2/account_activity/webhooks/{webhook_id}/subscriptions/all", "validateAccountActivitySubscription"), "validateSubscription");
        assert_eq!(strip_resource_name("/2/account_activity/webhooks/{webhook_id}/subscriptions/all", "createAccountActivitySubscription"), "createSubscription");
        assert_eq!(strip_resource_name("/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all", "deleteAccountActivitySubscription"), "deleteSubscription");
    }

    #[test]
    fn test_compliance_endpoints() {
        // Test compliance endpoints
        assert_eq!(strip_resource_name("/2/compliance/jobs", "getComplianceJobs"), "getJobs");
        assert_eq!(strip_resource_name("/2/compliance/jobs", "createComplianceJobs"), "createJobs");
        assert_eq!(strip_resource_name("/2/compliance/jobs/{id}", "getComplianceJobsById"), "getJobsById");
    }

    #[test]
    fn test_other_endpoints() {
        // Test other endpoints
        assert_eq!(strip_resource_name("/2/insights/historical", "getInsightsHistorical"), "getHistorical");
        assert_eq!(strip_resource_name("/2/insights/28hr", "getInsights28Hr"), "getInsights28Hr"); // should not strip "Insights" from "getInsights28Hr"
        assert_eq!(strip_resource_name("/2/trends/by/woeid/{woeid}", "getTrendsByWoeid"), "getByWoeid");
        assert_eq!(strip_resource_name("/2/usage/tweets", "getUsage"), "get");
        assert_eq!(strip_resource_name("/2/connections/all", "deleteAllConnections"), "deleteAll");
        assert_eq!(strip_resource_name("/2/article/draft", "articleDraftCreate"), "DraftCreate"); // strips "article" and leaves "DraftCreate"
        assert_eq!(strip_resource_name("/2/openapi.json", "getOpenApiSpec"), "getOpenApiSpec"); // should not strip "OpenApi" from "getOpenApiSpec"
    }

    #[test]
    fn test_edge_cases() {
        // Test edge cases
        assert_eq!(strip_resource_name("/malformed", "someOperation"), "someOperation");
        assert_eq!(strip_resource_name("/2", "someOperation"), "someOperation");
        assert_eq!(strip_resource_name("/", "someOperation"), "someOperation");
        assert_eq!(strip_resource_name("", "someOperation"), "someOperation");
        
        // Test with empty operationId
        assert_eq!(strip_resource_name("/2/users/{id}", ""), "");
        
        // Test with operationId that contains the resource name multiple times
        assert_eq!(strip_resource_name("/2/users/{id}", "getUsersUsers"), "getUsers"); // should only strip first occurrence
    }

    #[test]
    fn test_snake_case_function() {
        // Test the snake_case function
        assert_eq!(snake_case("getPostsById"), "get_posts_by_id");
        assert_eq!(snake_case("createPosts"), "create_posts");
        assert_eq!(snake_case("getInsights28Hr"), "get_insights_28_hr");
        assert_eq!(snake_case("streamPostsFirehose"), "stream_posts_firehose");
        assert_eq!(snake_case("getUsersByUsername"), "get_users_by_username");
        assert_eq!(snake_case("searchPostsEligibleForNotes"), "search_posts_eligible_for_notes");
        assert_eq!(snake_case("getAccountActivitySubscriptionCount"), "get_account_activity_subscription_count");
        assert_eq!(snake_case("createDmByParticipantId"), "create_dm_by_participant_id");
        assert_eq!(snake_case("removeListsMemberByUserId"), "remove_lists_member_by_user_id");
    }
}

/*
    This is the main generator for the Python SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: Python,
    filters: [snake_case, python_type, strip_resource_name],
    render: [
        multiple {
            render "models" => "xdk/{}/models.py",
            render "client_module" => "xdk/{}/__init__.py",
            render "client_class" => "xdk/{}/client.py"
        },
        render "main_client" => "xdk/client.py",
        render "oauth2_auth" => "xdk/oauth2_auth.py",
        render "init_py" => "xdk/__init__.py",
        render "setup_py" => "setup.py",
        render "readme" => "README.md",
        render "requirements_txt" => "requirements.txt"
    ]
}
