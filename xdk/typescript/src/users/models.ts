/**
 * Models for Users operations
 */

/**
 * Response for getBookmarkFolders
 */
export interface UsersGetBookmarkFoldersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for deleteBookmark
 */
export interface UsersDeleteBookmarkResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getMentions
 */
export interface UsersGetMentionsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getPosts
 */
export interface UsersGetPostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getFollowing
 */
export interface UsersGetFollowingResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for follow
 */
export interface UsersFollowRequest {
  /** Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  targetUserId?: string;
}

/**
 * Response for follow
 */
export interface UsersFollowResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unmute
 */
export interface UsersUnmuteResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getBookmarksByFolderId
 */
export interface UsersGetBookmarksByFolderIdResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getLikedPosts
 */
export interface UsersGetLikedPostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for unrepostPost
 */
export interface UsersUnrepostPostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unfollow
 */
export interface UsersUnfollowResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getFollowers
 */
export interface UsersGetFollowersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getBlocking
 */
export interface UsersGetBlockingResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for repostPost
 */
export interface UsersRepostPostRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for repostPost
 */
export interface UsersRepostPostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getPinnedLists
 */
export interface UsersGetPinnedListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for pinList
 */
export interface UsersPinListRequest {
  /** The unique identifier of this List. */
  listId?: string;
}

/**
 * Response for pinList
 */
export interface UsersPinListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getByIds
 */
export interface UsersGetByIdsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getByUsername
 */
export interface UsersGetByUsernameResponse {
  /** The X User object. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getListMemberships
 */
export interface UsersGetListMembershipsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getOwnedLists
 */
export interface UsersGetOwnedListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for blockDms
 */
export interface UsersBlockDmsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getFollowedLists
 */
export interface UsersGetFollowedListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for followList
 */
export interface UsersFollowListRequest {
  /** The unique identifier of this List. */
  listId?: string;
}

/**
 * Response for followList
 */
export interface UsersFollowListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unfollowList
 */
export interface UsersUnfollowListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for likePost
 */
export interface UsersLikePostRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for likePost
 */
export interface UsersLikePostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getTimeline
 */
export interface UsersGetTimelineResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for search
 */
export interface UsersSearchResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for unblockDms
 */
export interface UsersUnblockDmsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unpinList
 */
export interface UsersUnpinListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getMe
 */
export interface UsersGetMeResponse {
  /** The X User object. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getBookmarks
 */
export interface UsersGetBookmarksResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createBookmark
 */
export interface UsersCreateBookmarkRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for createBookmark
 */
export interface UsersCreateBookmarkResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getRepostsOfMe
 */
export interface UsersGetRepostsOfMeResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for unlikePost
 */
export interface UsersUnlikePostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getById
 */
export interface UsersGetByIdResponse {
  /** The X User object. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getByUsernames
 */
export interface UsersGetByUsernamesResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getMuting
 */
export interface UsersGetMutingResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for mute
 */
export interface UsersMuteRequest {
  /** Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  targetUserId?: string;
}

/**
 * Response for mute
 */
export interface UsersMuteResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
