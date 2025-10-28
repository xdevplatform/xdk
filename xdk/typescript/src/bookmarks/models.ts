/**
 * Models for Bookmarks operations
 */

/**
 * Response for getUsersFolders
 */
export interface BookmarksGetUsersFoldersResponse {
  data?: Record<string, any>;
}

/**
 * Response for getUsersByFolderId
 */
export interface BookmarksGetUsersByFolderIdResponse {
  data?: Record<string, any>;
}

/**
 * Response for getUsers
 */
export interface BookmarksGetUsersResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createUsers
 */
export interface BookmarksCreateUsersRequest {
  /** Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. */
  tweetId?: string;
}

/**
 * Response for createUsers
 */
export interface BookmarksCreateUsersResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for deleteUsers
 */
export interface BookmarksDeleteUsersResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
