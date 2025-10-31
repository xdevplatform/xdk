/**
 * Models for community notes operations
 */

/**
 * Response for delete
 */
export interface DeleteResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for searchEligiblePosts
 */
export interface SearchEligiblePostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for evaluate
 */
export interface EvaluateRequest {
  /** Text for the community note. */
  noteText?: string;
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  postId?: string;
}

/**
 * Response for evaluate
 */
export interface EvaluateResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for create
 */
export interface CreateRequest {
  /** A X Community Note is a note on a Post. */
  info: Record<string, any>;
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  postId?: string;
  /** If true, the note being submitted is only for testing the capability of the bot, and won't be publicly visible. If false, the note being submitted will be a new proposed note on the product. */
  testMode?: boolean;
}

/**
 * Response for create
 */
export interface CreateResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for searchWritten
 */
export interface SearchWrittenResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}
