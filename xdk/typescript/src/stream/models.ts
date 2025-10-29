/**
 * Models for Stream operations
 */

/**
 * Response for postsFirehosePt
 */
export interface StreamPostsFirehosePtResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for likesSample10
 */
export interface StreamLikesSample10Response {
  /** A Like event, with the tweet author user and the tweet being liked */
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsFirehoseEn
 */
export interface StreamPostsFirehoseEnResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for usersCompliance
 * User compliance stream events.
 */
export interface StreamUsersComplianceResponse {}

/**
 * Response for likesFirehose
 */
export interface StreamLikesFirehoseResponse {
  /** A Like event, with the tweet author user and the tweet being liked */
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsCompliance
 * Tweet compliance stream events.
 */
export interface StreamPostsComplianceResponse {}

/**
 * Response for postsFirehoseJa
 */
export interface StreamPostsFirehoseJaResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getRuleCounts
 */
export interface StreamGetRuleCountsResponse {
  /** A count of user-provided stream filtering rules at the application and project levels. */
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for posts
 * A Tweet or error that can be returned by the streaming Tweet API. The values returned with a successful streamed Tweet includes the user provided rules that the Tweet matched.
 */
export interface StreamPostsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  /** The list of rules which matched the Tweet */
  matchingRules?: Array<any>;
}

/**
 * Response for getRules
 */
export interface StreamGetRulesResponse {
  data?: Array<any>;
  meta: Record<string, any>;
}

/**
 * Request body for updateRules
 */
export interface StreamUpdateRulesRequest {}

/**
 * Response for updateRules
 * A response from modifying user-specified stream filtering rules.
 */
export interface StreamUpdateRulesResponse {
  /** All user-specified stream filtering rules that were created. */
  data?: Array<any>;
  errors?: Array<any>;
  meta: Record<string, any>;
}

/**
 * Response for labelsCompliance
 * Tweet label stream events.
 */
export interface StreamLabelsComplianceResponse {}

/**
 * Response for postsSample
 */
export interface StreamPostsSampleResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsFirehose
 */
export interface StreamPostsFirehoseResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsSample10
 */
export interface StreamPostsSample10Response {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for likesCompliance
 * Likes compliance stream events.
 */
export interface StreamLikesComplianceResponse {}

/**
 * Response for postsFirehoseKo
 */
export interface StreamPostsFirehoseKoResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}
