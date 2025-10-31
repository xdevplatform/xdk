/**
 * Models for users operations
 */

/**
 * Response for unmuteUser
 */
export interface UnmuteUserResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unlikePost
 */
export interface UnlikePostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getLikedPosts
 */
export interface GetLikedPostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getPosts
 */
export interface GetPostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getPinnedLists
 */
export interface GetPinnedListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for pinList
 */
export interface PinListRequest {
  /** The unique identifier of this List. */
  listId?: string;
}

/**
 * Response for pinList
 */
export interface PinListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getOwnedLists
 */
export interface GetOwnedListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getListMemberships
 */
export interface GetListMembershipsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for repostPost
 */
export interface RepostPostRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for repostPost
 */
export interface RepostPostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getTimeline
 */
export interface GetTimelineResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getFollowers
 */
export interface GetFollowersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getMentions
 */
export interface GetMentionsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getBookmarkFolders
 */
export interface GetBookmarkFoldersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for blockDms
 */
export interface BlockDmsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for search
 */
export interface SearchResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getByUsernames
 */
export interface GetByUsernamesResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for unfollowUser
 */
export interface UnfollowUserResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unpinList
 */
export interface UnpinListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getBlocking
 */
export interface GetBlockingResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for unrepostPost
 */
export interface UnrepostPostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for deleteBookmark
 */
export interface DeleteBookmarkResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getBookmarksByFolderId
 */
export interface GetBookmarksByFolderIdResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getFollowing
 */
export interface GetFollowingResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for followUser
 */
export interface FollowUserRequest {
  /** Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  targetUserId?: string;
}

/**
 * Response for followUser
 */
export interface FollowUserResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getBookmarks
 */
export interface GetBookmarksResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createBookmark
 */
export interface CreateBookmarkRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for createBookmark
 */
export interface CreateBookmarkResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getByIds
 */
export interface GetByIdsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Request body for likePost
 */
export interface LikePostRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for likePost
 */
export interface LikePostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getById
 */
export interface GetByIdResponse {
  /** The X User object. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getByUsername
 */
export interface GetByUsernameResponse {
  /** The X User object. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getMe
 */
export interface GetMeResponse {
  /** The X User object. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getRepostsOfMe
 */
export interface GetRepostsOfMeResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for unblockDms
 */
export interface UnblockDmsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unfollowList
 */
export interface UnfollowListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getFollowedLists
 */
export interface GetFollowedListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for followList
 */
export interface FollowListRequest {
  /** The unique identifier of this List. */
  listId?: string;
}

/**
 * Response for followList
 */
export interface FollowListResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getMuting
 */
export interface GetMutingResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for muteUser
 */
export interface MuteUserRequest {
  /** Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  targetUserId?: string;
}

/**
 * Response for muteUser
 */
export interface MuteUserResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
