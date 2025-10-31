/**
 * Models for posts operations
 */

/**
 * Response for getById
 */
export interface GetByIdResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for delete
 */
export interface DeleteResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getInsightsHistorical
 */
export interface GetInsightsHistoricalResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Response for searchAll
 */
export interface SearchAllResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getCountsRecent
 */
export interface GetCountsRecentResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getReposts
 */
export interface GetRepostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getQuoted
 */
export interface GetQuotedResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
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
 * Request body for create
 */
export interface CreateRequest {
  /** Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link. */
  cardUri?: string;
  /** The unique identifier of this Community. */
  communityId?: string;
  /** Link to take the conversation from the public timeline to a private Direct Message. */
  directMessageDeepLink?: string;
  /** Options for editing an existing Post. When provided, this request will edit the specified Post instead of creating a new one. */
  editOptions: Record<string, any>;
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
export interface CreateResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for searchRecent
 */
export interface SearchRecentResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getRepostedBy
 */
export interface GetRepostedByResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getCountsAll
 */
export interface GetCountsAllResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getInsights28hr
 */
export interface GetInsights28hrResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Response for getAnalytics
 */
export interface GetAnalyticsResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Request body for hideReply
 */
export interface HideReplyRequest {
  hidden?: boolean;
}

/**
 * Response for hideReply
 */
export interface HideReplyResponse {
  data?: Record<string, any>;
}

/**
 * Response for getLikingUsers
 */
export interface GetLikingUsersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}
