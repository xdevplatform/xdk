/**
 * Models for Community notes operations
 */

/**
 * Response for searchForEligiblePosts
 */
export interface CommunityNotesSearchForEligiblePostsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for deleteNotes
 */
export interface CommunityNotesDeleteNotesResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createNotes
 */
export interface CommunityNotesCreateNotesRequest {
  /** A X Community Note is a note on a Post. */
  info: Record<string, any>;
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  postId?: string;
  /** If true, the note being submitted is only for testing the capability of the bot, and won't be publicly visible. If false, the note being submitted will be a new proposed note on the product. */
  testMode?: boolean;
}

/**
 * Response for createNotes
 */
export interface CommunityNotesCreateNotesResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for searchNotesWritten
 */
export interface CommunityNotesSearchNotesWrittenResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}
