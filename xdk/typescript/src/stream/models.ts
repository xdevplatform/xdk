/**
 * Models for stream operations
 */

/**
 * Response for postsSample
 */
export interface PostsSampleResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsSample10
 */
export interface PostsSample10Response {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getRuleCounts
 */
export interface GetRuleCountsResponse {
  /** A count of user-provided stream filtering rules at the application and project levels. */
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for postsFirehoseEn
 */
export interface PostsFirehoseEnResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for posts
 * A Tweet or error that can be returned by the streaming Tweet API. The values returned with a successful streamed Tweet includes the user provided rules that the Tweet matched.
 */
export interface PostsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  /** The list of rules which matched the Tweet */
  matchingRules?: Array<any>;
}

/**
 * Response for likesSample10
 */
export interface LikesSample10Response {
  /** A Like event, with the tweet author user and the tweet being liked */
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsFirehoseKo
 */
export interface PostsFirehoseKoResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsCompliance
 * Tweet compliance stream events.
 */
export interface PostsComplianceResponse {}

/**
 * Response for usersCompliance
 * User compliance stream events.
 */
export interface UsersComplianceResponse {}

/**
 * Response for postsFirehoseJa
 */
export interface PostsFirehoseJaResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for getRules
 */
export interface GetRulesResponse {
  data?: Array<any>;
  meta: Record<string, any>;
}

/**
 * Request body for updateRules
 */
export interface UpdateRulesRequest {}

/**
 * Response for updateRules
 * A response from modifying user-specified stream filtering rules.
 */
export interface UpdateRulesResponse {
  /** All user-specified stream filtering rules that were created. */
  data?: Array<any>;
  errors?: Array<any>;
  meta: Record<string, any>;
}

/**
 * Response for postsFirehosePt
 */
export interface PostsFirehosePtResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for likesFirehose
 */
export interface LikesFirehoseResponse {
  /** A Like event, with the tweet author user and the tweet being liked */
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for postsFirehose
 */
export interface PostsFirehoseResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for likesCompliance
 * Likes compliance stream events.
 */
export interface LikesComplianceResponse {}

/**
 * Response for labelsCompliance
 * Tweet label stream events.
 */
export interface LabelsComplianceResponse {}
