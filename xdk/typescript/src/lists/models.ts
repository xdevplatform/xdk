/**
 * Models for lists operations
 */

/**
 * Response for getById
 */
export interface GetByIdResponse {
  /** A X List is a curated group of accounts. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Request body for update
 */
export interface UpdateRequest {
  description?: string;
  name?: string;
  private?: boolean;
}

/**
 * Response for update
 */
export interface UpdateResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for delete
 */
export interface DeleteResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
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
 * Response for removeMemberByUserId
 */
export interface RemoveMemberByUserIdResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getMembers
 */
export interface GetMembersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for addMember
 */
export interface AddMemberRequest {
  /** Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  userId?: string;
}

/**
 * Response for addMember
 */
export interface AddMemberResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for create
 */
export interface CreateRequest {
  description?: string;
  name?: string;
  private?: boolean;
}

/**
 * Response for create
 */
export interface CreateResponse {
  /** A X List is a curated group of accounts. */
  data: Record<string, any>;
  errors?: Array<any>;
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
