/**
 * Users client for the X API.
 *
 * This module provides a client for interacting with the Users endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import {
  UsersGetBookmarkFoldersResponse,
  UsersDeleteBookmarkResponse,
  UsersGetMentionsResponse,
  UsersGetPostsResponse,
  UsersGetFollowingResponse,
  UsersFollowRequest,
  UsersFollowResponse,
  UsersUnmuteResponse,
  UsersGetBookmarksByFolderIdResponse,
  UsersGetLikedPostsResponse,
  UsersUnrepostPostResponse,
  UsersUnfollowResponse,
  UsersGetFollowersResponse,
  UsersGetBlockingResponse,
  UsersRepostPostRequest,
  UsersRepostPostResponse,
  UsersGetPinnedListsResponse,
  UsersPinListRequest,
  UsersPinListResponse,
  UsersGetByIdsResponse,
  UsersGetByUsernameResponse,
  UsersGetListMembershipsResponse,
  UsersGetOwnedListsResponse,
  UsersBlockDmsResponse,
  UsersGetFollowedListsResponse,
  UsersFollowListRequest,
  UsersFollowListResponse,
  UsersUnfollowListResponse,
  UsersLikePostRequest,
  UsersLikePostResponse,
  UsersGetTimelineResponse,
  UsersSearchResponse,
  UsersUnblockDmsResponse,
  UsersUnpinListResponse,
  UsersGetMeResponse,
  UsersGetBookmarksResponse,
  UsersCreateBookmarkRequest,
  UsersCreateBookmarkResponse,
  UsersGetRepostsOfMeResponse,
  UsersUnlikePostResponse,
  UsersGetByIdResponse,
  UsersGetByUsernamesResponse,
  UsersGetMutingResponse,
  UsersMuteRequest,
  UsersMuteResponse,
} from './models.js';

/**
 * Options for getBookmarkFolders method
 */
export interface UsersGetBookmarkFoldersOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getMentions method
 */
export interface UsersGetMentionsOptions {
  /** The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified. */
  sinceId?: string;

  /** The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified. */
  untilId?: string;

  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified. */
  endTime?: string;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getPosts method
 */
export interface UsersGetPostsOptions {
  /** The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified. */
  sinceId?: string;

  /** The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified. */
  untilId?: string;

  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** The set of entities to exclude (e.g. 'replies' or 'retweets'). */
  exclude?: Array<any>;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified. */
  endTime?: string;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowing method
 */
export interface UsersGetFollowingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for follow method
 */
export interface UsersFollowOptions {
  /** Request body */
  body?: UsersFollowRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getLikedPosts method
 */
export interface UsersGetLikedPostsOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowers method
 */
export interface UsersGetFollowersOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getBlocking method
 */
export interface UsersGetBlockingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for repostPost method
 */
export interface UsersRepostPostOptions {
  /** Request body */
  body?: UsersRepostPostRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getPinnedLists method
 */
export interface UsersGetPinnedListsOptions {
  /** A comma separated list of List fields to display. */
  listfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByIds method
 */
export interface UsersGetByIdsOptions {
  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByUsername method
 */
export interface UsersGetByUsernameOptions {
  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getListMemberships method
 */
export interface UsersGetListMembershipsOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of List fields to display. */
  listfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getOwnedLists method
 */
export interface UsersGetOwnedListsOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of List fields to display. */
  listfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowedLists method
 */
export interface UsersGetFollowedListsOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of List fields to display. */
  listfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for followList method
 */
export interface UsersFollowListOptions {
  /** Request body */
  body?: UsersFollowListRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for likePost method
 */
export interface UsersLikePostOptions {
  /** Request body */
  body?: UsersLikePostRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getTimeline method
 */
export interface UsersGetTimelineOptions {
  /** The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified. */
  sinceId?: string;

  /** The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified. */
  untilId?: string;

  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** The set of entities to exclude (e.g. 'replies' or 'retweets'). */
  exclude?: Array<any>;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified. */
  endTime?: string;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for search method
 */
export interface UsersSearchOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getMe method
 */
export interface UsersGetMeOptions {
  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getBookmarks method
 */
export interface UsersGetBookmarksOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getRepostsOfMe method
 */
export interface UsersGetRepostsOfMeOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getById method
 */
export interface UsersGetByIdOptions {
  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByUsernames method
 */
export interface UsersGetByUsernamesOptions {
  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getMuting method
 */
export interface UsersGetMutingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for mute method
 */
export interface UsersMuteOptions {
  /** Request body */
  body?: UsersMuteRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Users operations
 * 
 * This client provides methods for interacting with the Users endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Users related operations.
 * 
 * @category Users
 */
export class UsersClient {
  private client: Client;

  /**
     * Creates a new Users client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Delete Bookmark
   * Removes a Post from the authenticated user’s Bookmarks by its ID.
   * @param id The ID of the authenticated source User whose bookmark is to be removed.
   * @param tweetId The ID of the Post that the source User is removing from bookmarks.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteBookmark(
    id: string,
    tweetId: string
  ): Promise<UsersDeleteBookmarkResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/{tweet_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{tweet_id}', encodeURIComponent(String(tweetId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersDeleteBookmarkResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Follow User
   * Causes the authenticated user to follow a specific user by their ID.
   * @param id The ID of the authenticated source User that is requesting to follow the target User.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async follow(
    id: string,
    options: UsersFollowOptions = {}
  ): Promise<UsersFollowResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/following';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<UsersFollowResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unmute User
   * Causes the authenticated user to unmute a specific user by their ID.
   * @param sourceUserId The ID of the authenticated source User that is requesting to unmute the target User.
   * @param targetUserId The ID of the User that the source User is requesting to unmute.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unmute(
    sourceUserId: string,
    targetUserId: string
  ): Promise<UsersUnmuteResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{source_user_id}/muting/{target_user_id}';

    path = path.replace(
      '{source_user_id}',
      encodeURIComponent(String(sourceUserId))
    );

    path = path.replace(
      '{target_user_id}',
      encodeURIComponent(String(targetUserId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnmuteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Bookmarks by folder ID
   * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
   * @param id The ID of the authenticated source User for whom to return results.
   * @param folderId The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarksByFolderId(
    id: string,
    folderId: string
  ): Promise<UsersGetBookmarksByFolderIdResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/folders/{folder_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{folder_id}', encodeURIComponent(String(folderId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersGetBookmarksByFolderIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unrepost Post
   * Causes the authenticated user to unrepost a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to repost the Post.
   * @param sourceTweetId The ID of the Post that the User is requesting to unretweet.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unrepostPost(
    id: string,
    sourceTweetId: string
  ): Promise<UsersUnrepostPostResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/retweets/{source_tweet_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace(
      '{source_tweet_id}',
      encodeURIComponent(String(sourceTweetId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnrepostPostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unfollow User
   * Causes the authenticated user to unfollow a specific user by their ID.
   * @param sourceUserId The ID of the authenticated source User that is requesting to unfollow the target User.
   * @param targetUserId The ID of the User that the source User is requesting to unfollow.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unfollow(
    sourceUserId: string,
    targetUserId: string
  ): Promise<UsersUnfollowResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{source_user_id}/following/{target_user_id}';

    path = path.replace(
      '{source_user_id}',
      encodeURIComponent(String(sourceUserId))
    );

    path = path.replace(
      '{target_user_id}',
      encodeURIComponent(String(targetUserId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnfollowResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Repost Post
   * Causes the authenticated user to repost a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to repost the Post.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async repostPost(
    id: string,
    options: UsersRepostPostOptions = {}
  ): Promise<UsersRepostPostResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/retweets';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<UsersRepostPostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get pinned Lists
   * Retrieves a list of Lists pinned by the authenticated user.
   * @param id The ID of the authenticated source User for whom to return results.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPinnedLists(
    id: string,
    options: UsersGetPinnedListsOptions = {}
  ): Promise<UsersGetPinnedListsResponse> {
    // Destructure options

    const {
      listfields = [],

      expansions = [],

      userfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/pinned_lists';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (listfields !== undefined) {
      params.append('list.fields', listfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsersGetPinnedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Pin List
   * Causes the authenticated user to pin a specific List by its ID.
   * @param id The ID of the authenticated source User that will pin the List.* @param body Request body
* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async pinList(
    id: string,
    body: UsersPinListRequest
  ): Promise<UsersPinListResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/pinned_lists';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<UsersPinListResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Users by IDs
   * Retrieves details of multiple Users by their IDs.
   * @param ids A list of User IDs, comma-separated. You can specify up to 100 IDs.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(
    ids: Array<any>,
    options: UsersGetByIdsOptions = {}
  ): Promise<UsersGetByIdsResponse> {
    // Destructure options

    const {
      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users';

    // Build query parameters
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.append('ids', ids.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsersGetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get User by username
   * Retrieves details of a specific User by their username.
   * @param username A username.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByUsername(
    username: string,
    options: UsersGetByUsernameOptions = {}
  ): Promise<UsersGetByUsernameResponse> {
    // Destructure options

    const {
      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/by/username/{username}';

    path = path.replace('{username}', encodeURIComponent(String(username)));

    // Build query parameters
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsersGetByUsernameResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Block DMs
   * Blocks direct messages to or from a specific User by their ID for the authenticated user.
   * @param id The ID of the target User that the authenticated user requesting to block dms for.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async blockDms(id: string): Promise<UsersBlockDmsResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/dm/block';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersBlockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Follow List
   * Causes the authenticated user to follow a specific List by its ID.
   * @param id The ID of the authenticated source User that will follow the List.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async followList(
    id: string,
    options: UsersFollowListOptions = {}
  ): Promise<UsersFollowListResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<UsersFollowListResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unfollow List
   * Causes the authenticated user to unfollow a specific List by its ID.
   * @param id The ID of the authenticated source User that will unfollow the List.
   * @param listId The ID of the List to unfollow.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unfollowList(
    id: string,
    listId: string
  ): Promise<UsersUnfollowListResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists/{list_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{list_id}', encodeURIComponent(String(listId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnfollowListResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Like Post
   * Causes the authenticated user to Like a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to like the Post.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async likePost(
    id: string,
    options: UsersLikePostOptions = {}
  ): Promise<UsersLikePostResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/likes';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<UsersLikePostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unblock DMs
   * Unblocks direct messages to or from a specific User by their ID for the authenticated user.
   * @param id The ID of the target User that the authenticated user requesting to unblock dms for.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unblockDms(id: string): Promise<UsersUnblockDmsResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/dm/unblock';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnblockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unpin List
   * Causes the authenticated user to unpin a specific List by its ID.
   * @param id The ID of the authenticated source User for whom to return results.
   * @param listId The ID of the List to unpin.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unpinList(id: string, listId: string): Promise<UsersUnpinListResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/pinned_lists/{list_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{list_id}', encodeURIComponent(String(listId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnpinListResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get my User
   * Retrieves details of the authenticated user.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getMe(options: UsersGetMeOptions = {}): Promise<UsersGetMeResponse> {
    // Destructure options

    const {
      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/me';

    // Build query parameters
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsersGetMeResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create Bookmark
   * Adds a post to the authenticated user’s bookmarks.
   * @param id The ID of the authenticated source User for whom to add bookmarks.* @param body Request body
* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createBookmark(
    id: string,
    body: UsersCreateBookmarkRequest
  ): Promise<UsersCreateBookmarkResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<UsersCreateBookmarkResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unlike Post
   * Causes the authenticated user to Unlike a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to unlike the Post.
   * @param tweetId The ID of the Post that the User is requesting to unlike.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unlikePost(
    id: string,
    tweetId: string
  ): Promise<UsersUnlikePostResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/likes/{tweet_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{tweet_id}', encodeURIComponent(String(tweetId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UsersUnlikePostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get User by ID
   * Retrieves details of a specific User by their ID.
   * @param id The ID of the User to lookup.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(
    id: string,
    options: UsersGetByIdOptions = {}
  ): Promise<UsersGetByIdResponse> {
    // Destructure options

    const {
      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsersGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Users by usernames
   * Retrieves details of multiple Users by their usernames.
   * @param usernames A list of usernames, comma-separated.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByUsernames(
    usernames: Array<any>,
    options: UsersGetByUsernamesOptions = {}
  ): Promise<UsersGetByUsernamesResponse> {
    // Destructure options

    const {
      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/by';

    // Build query parameters
    const params = new URLSearchParams();

    if (usernames !== undefined) {
      params.append('usernames', usernames.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsersGetByUsernamesResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Mute User
   * Causes the authenticated user to mute a specific User by their ID.
   * @param id The ID of the authenticated source User that is requesting to mute the target User.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async mute(
    id: string,
    options: UsersMuteOptions = {}
  ): Promise<UsersMuteResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/muting';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<UsersMuteResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Bookmark folders
   * Retrieves a list of Bookmark folders created by the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getBookmarkFolders(
    id: string,
    options: UsersGetBookmarkFoldersOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/folders';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<
        UsersGetBookmarkFoldersResponse
      >(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get mentions
   * Retrieves a list of Posts that mention a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getMentions(
    id: string,
    options: UsersGetMentionsOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      sinceId = undefined,

      untilId = undefined,

      maxResults = undefined,

      paginationToken = undefined,

      startTime = undefined,

      endTime = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/mentions';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (sinceId !== undefined) {
        params.append('since_id', String(sinceId));
      }

      if (untilId !== undefined) {
        params.append('until_id', String(untilId));
      }

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (startTime !== undefined) {
        params.append('start_time', String(startTime));
      }

      if (endTime !== undefined) {
        params.append('end_time', String(endTime));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetMentionsResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Posts
   * Retrieves a list of posts authored by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getPosts(
    id: string,
    options: UsersGetPostsOptions = {}
  ): Promise<PostPaginator> {
    // Destructure options

    const {
      sinceId = undefined,

      untilId = undefined,

      maxResults = undefined,

      paginationToken = undefined,

      exclude = [],

      startTime = undefined,

      endTime = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/tweets';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (sinceId !== undefined) {
        params.append('since_id', String(sinceId));
      }

      if (untilId !== undefined) {
        params.append('until_id', String(untilId));
      }

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (exclude !== undefined) {
        params.append('exclude', exclude.join(','));
      }

      if (startTime !== undefined) {
        params.append('start_time', String(startTime));
      }

      if (endTime !== undefined) {
        params.append('end_time', String(endTime));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetPostsResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get following
   * Retrieves a list of Users followed by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getFollowing(
    id: string,
    options: UsersGetFollowingOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/following';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetFollowingResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get liked Posts
   * Retrieves a list of Posts liked by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getLikedPosts(
    id: string,
    options: UsersGetLikedPostsOptions = {}
  ): Promise<PostPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/liked_tweets';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetLikedPostsResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get followers
   * Retrieves a list of Users who follow a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getFollowers(
    id: string,
    options: UsersGetFollowersOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/followers';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetFollowersResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get blocking
   * Retrieves a list of Users blocked by the specified User ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getBlocking(
    id: string,
    options: UsersGetBlockingOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/blocking';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetBlockingResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get List memberships
   * Retrieves a list of Lists that a specific User is a member of by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getListMemberships(
    id: string,
    options: UsersGetListMembershipsOptions = {}
  ): Promise<ListPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      listfields = [],

      expansions = [],

      userfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/list_memberships';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (listfields !== undefined) {
        params.append('list.fields', listfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<
        UsersGetListMembershipsResponse
      >(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new ListPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get owned Lists
   * Retrieves a list of Lists owned by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getOwnedLists(
    id: string,
    options: UsersGetOwnedListsOptions = {}
  ): Promise<ListPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      listfields = [],

      expansions = [],

      userfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/owned_lists';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (listfields !== undefined) {
        params.append('list.fields', listfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetOwnedListsResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new ListPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get followed Lists
   * Retrieves a list of Lists followed by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getFollowedLists(
    id: string,
    options: UsersGetFollowedListsOptions = {}
  ): Promise<ListPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      listfields = [],

      expansions = [],

      userfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (listfields !== undefined) {
        params.append('list.fields', listfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetFollowedListsResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new ListPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Timeline
   * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getTimeline(
    id: string,
    options: UsersGetTimelineOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      sinceId = undefined,

      untilId = undefined,

      maxResults = undefined,

      paginationToken = undefined,

      exclude = [],

      startTime = undefined,

      endTime = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/timelines/reverse_chronological';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (sinceId !== undefined) {
        params.append('since_id', String(sinceId));
      }

      if (untilId !== undefined) {
        params.append('until_id', String(untilId));
      }

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (exclude !== undefined) {
        params.append('exclude', exclude.join(','));
      }

      if (startTime !== undefined) {
        params.append('start_time', String(startTime));
      }

      if (endTime !== undefined) {
        params.append('end_time', String(endTime));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetTimelineResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Search Users
   * Retrieves a list of Users matching a search query.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async search(
    query: string,
    options: UsersSearchOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      nextToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/search';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (query !== undefined) {
        params.append('query', String(query));
      }

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (nextToken !== undefined) {
        params.append('next_token', String(nextToken));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('next_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersSearchResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Bookmarks
   * Retrieves a list of Posts bookmarked by the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getBookmarks(
    id: string,
    options: UsersGetBookmarksOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetBookmarksResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Reposts of me
   * Retrieves a list of Posts that repost content from the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getRepostsOfMe(
    options: UsersGetRepostsOfMeOptions = {}
  ): Promise<PostPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/reposts_of_me';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetRepostsOfMeResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get muting
   * Retrieves a list of Users muted by the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getMuting(
    id: string,
    options: UsersGetMutingOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/muting';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<UsersGetMutingResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }
}
