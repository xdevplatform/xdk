/**
 * Models for Posts operations
 */

/**
 * Response for getById
 */
export interface PostsGetByIdResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for delete
 */
export interface PostsDeleteResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for searchRecent
 */
export interface PostsSearchRecentResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getQuotedPosts
 */
export interface PostsGetQuotedPostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getByIds
 */
export interface PostsGetByIdsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Request body for create
 */
export interface PostsCreateRequest {
  /** Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link. */
  cardUri?: string;
  /** The unique identifier of this Community. */
  communityId?: string;
  /** Link to take the conversation from the public timeline to a private Direct Message. */
  directMessageDeepLink?: string;
  /** Exclusive Tweet for super followers. */
  forSuperFollowersOnly?: boolean;
  /** Place ID being attached to the Tweet for geo location. */
  geo?: Record<string, any>;
  /** Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI. */
  media: Record<string, any>;
  /** Nullcasted (promoted-only) Posts do not appear in the public timeline and are not served to followers. */
  nullcast?: boolean;
  /** Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI. */
  poll: Record<string, any>;
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  quoteTweetId?: string;
  /** Tweet information of the Tweet being replied to. */
  reply: Record<string, any>;
  /** Settings to indicate who can reply to the Tweet. */
  replySettings?: string;
  /** Share community post with followers too. */
  shareWithFollowers?: boolean;
  /** The content of the Tweet. */
  text?: string;
}

/**
 * Response for create
 */
export interface PostsCreateResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getReposts
 */
export interface PostsGetRepostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getUsersMentions
 */
export interface PostsGetUsersMentionsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getInsightsHistorical
 */
export interface PostsGetInsightsHistoricalResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Response for getUsersTimeline
 */
export interface PostsGetUsersTimelineResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getInsights28Hr
 */
export interface PostsGetInsights28HrResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Response for searchAll
 */
export interface PostsSearchAllResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getUsersLiked
 */
export interface PostsGetUsersLikedResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for like
 */
export interface PostsLikeRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for like
 */
export interface PostsLikeResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for repost
 */
export interface PostsRepostRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for repost
 */
export interface PostsRepostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getUsers
 */
export interface PostsGetUsersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getLists
 */
export interface PostsGetListsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getCountsRecent
 */
export interface PostsGetCountsRecentResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Request body for hideReply
 */
export interface PostsHideReplyRequest {
  hidden?: boolean;
}

/**
 * Response for hideReply
 */
export interface PostsHideReplyResponse {
  data?: Record<string, any>;
}

/**
 * Response for getCountsAll
 */
export interface PostsGetCountsAllResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getAnalytics
 */
export interface PostsGetAnalyticsResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Response for unlike
 */
export interface PostsUnlikeResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unrepost
 */
export interface PostsUnrepostResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
