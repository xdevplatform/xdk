/**
 * Models for Lists operations
 */

/**
 * Response for unpin
 */
export interface ListsUnpinResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getUsersOwned
 */
export interface ListsGetUsersOwnedResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getUsersPinned
 */
export interface ListsGetUsersPinnedResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for pin
 */
export interface ListsPinRequest {
  /** The unique identifier of this List. */
  listId?: string;
}

/**
 * Response for pin
 */
export interface ListsPinResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getUsersFollowed
 */
export interface ListsGetUsersFollowedResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for follow
 */
export interface ListsFollowRequest {
  /** The unique identifier of this List. */
  listId?: string;
}

/**
 * Response for follow
 */
export interface ListsFollowResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for addMember
 */
export interface ListsAddMemberRequest {
  /** Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  userId?: string;
}

/**
 * Response for addMember
 */
export interface ListsAddMemberResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for create
 */
export interface ListsCreateRequest {
  description?: string;
  name?: string;
  private?: boolean;
}

/**
 * Response for create
 */
export interface ListsCreateResponse {
  /** A X List is a curated group of accounts. */
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getUsersMemberships
 */
export interface ListsGetUsersMembershipsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getById
 */
export interface ListsGetByIdResponse {
  /** A X List is a curated group of accounts. */
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Request body for update
 */
export interface ListsUpdateRequest {
  description?: string;
  name?: string;
  private?: boolean;
}

/**
 * Response for update
 */
export interface ListsUpdateResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for delete
 */
export interface ListsDeleteResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for unfollow
 */
export interface ListsUnfollowResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for removeMemberByUserId
 */
export interface ListsRemoveMemberByUserIdResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
