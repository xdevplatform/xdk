/**
 * users client for the X API.
 *
 * This module provides a client for interacting with the users endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetOwnedListsResponse,
  BlockDmsResponse,
  GetLikedPostsResponse,
  UnrepostPostResponse,
  GetMentionsResponse,
  UnfollowUserResponse,
  UnblockDmsResponse,
  GetByIdsResponse,
  UnmuteUserResponse,
  GetFollowingResponse,
  FollowUserRequest,
  FollowUserResponse,
  GetBookmarkFoldersResponse,
  GetBookmarksByFolderIdResponse,
  GetPostsResponse,
  GetListMembershipsResponse,
  UnfollowListResponse,
  GetRepostsOfMeResponse,
  GetBlockingResponse,
  SearchResponse,
  GetFollowersResponse,
  GetMeResponse,
  GetByIdResponse,
  GetByUsernamesResponse,
  GetByUsernameResponse,
  GetTimelineResponse,
  DeleteBookmarkResponse,
  GetPinnedListsResponse,
  PinListRequest,
  PinListResponse,
  UnpinListResponse,
  GetFollowedListsResponse,
  FollowListRequest,
  FollowListResponse,
  RepostPostRequest,
  RepostPostResponse,
  LikePostRequest,
  LikePostResponse,
  GetMutingResponse,
  MuteUserRequest,
  MuteUserResponse,
  GetBookmarksResponse,
  CreateBookmarkRequest,
  CreateBookmarkResponse,
  UnlikePostResponse,
} from './models.js';

/**
 * Options for getOwnedLists method
 * 
 * @public
 */
export interface GetOwnedListsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getLikedPosts method
 * 
 * @public
 */
export interface GetLikedPostsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getMentions method
 * 
 * @public
 */
export interface GetMentionsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowing method
 * 
 * @public
 */
export interface GetFollowingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for followUser method
 * 
 * @public
 */
export interface FollowUserOptions {
  /** Request body */
  body?: FollowUserRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getBookmarkFolders method
 * 
 * @public
 */
export interface GetBookmarkFoldersOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getPosts method
 * 
 * @public
 */
export interface GetPostsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getListMemberships method
 * 
 * @public
 */
export interface GetListMembershipsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getRepostsOfMe method
 * 
 * @public
 */
export interface GetRepostsOfMeOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getBlocking method
 * 
 * @public
 */
export interface GetBlockingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for search method
 * 
 * @public
 */
export interface SearchOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowers method
 * 
 * @public
 */
export interface GetFollowersOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getTimeline method
 * 
 * @public
 */
export interface GetTimelineOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowedLists method
 * 
 * @public
 */
export interface GetFollowedListsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for followList method
 * 
 * @public
 */
export interface FollowListOptions {
  /** Request body */
  body?: FollowListRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for repostPost method
 * 
 * @public
 */
export interface RepostPostOptions {
  /** Request body */
  body?: RepostPostRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for likePost method
 * 
 * @public
 */
export interface LikePostOptions {
  /** Request body */
  body?: LikePostRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getMuting method
 * 
 * @public
 */
export interface GetMutingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for muteUser method
 * 
 * @public
 */
export interface MuteUserOptions {
  /** Request body */
  body?: MuteUserRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getBookmarks method
 * 
 * @public
 */
export interface GetBookmarksOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for users operations
 * 
 * This client provides methods for interacting with the users endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all users related operations.
 * 
 * @category users
 */
export class UsersClient {
  private client: Client;

  /**
     * Creates a new users client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get owned Lists
   * Retrieves a list of Lists owned by a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getOwnedLists(
    options: GetOwnedListsOptions = {}
  ): Promise<GetOwnedListsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/owned_lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetOwnedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Block DMs
   * Blocks direct messages to or from a specific User by their ID for the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async blockDms(): Promise<BlockDmsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/dm/block';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<BlockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get liked Posts
   * Retrieves a list of Posts liked by a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getLikedPosts(
    options: GetLikedPostsOptions = {}
  ): Promise<GetLikedPostsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/liked_tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetLikedPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unrepost Post
   * Causes the authenticated user to unrepost a specific Post by its ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unrepostPost(): Promise<UnrepostPostResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/retweets/{source_tweet_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnrepostPostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get mentions
   * Retrieves a list of Posts that mention a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getMentions(
    options: GetMentionsOptions = {}
  ): Promise<GetMentionsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/mentions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetMentionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unfollow User
   * Causes the authenticated user to unfollow a specific user by their ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unfollowUser(): Promise<UnfollowUserResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{source_user_id}/following/{target_user_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnfollowUserResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unblock DMs
   * Unblocks direct messages to or from a specific User by their ID for the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unblockDms(): Promise<UnblockDmsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/dm/unblock';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnblockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Users by IDs
   * Retrieves details of multiple Users by their IDs.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(): Promise<GetByIdsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unmute User
   * Causes the authenticated user to unmute a specific user by their ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unmuteUser(): Promise<UnmuteUserResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{source_user_id}/muting/{target_user_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnmuteUserResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get following
   * Retrieves a list of Users followed by a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowing(
    options: GetFollowingOptions = {}
  ): Promise<GetFollowingResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/following';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetFollowingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Follow User
   * Causes the authenticated user to follow a specific user by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async followUser(
    options: FollowUserOptions = {}
  ): Promise<FollowUserResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/following';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<FollowUserResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Bookmark folders
   * Retrieves a list of Bookmark folders created by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarkFolders(
    options: GetBookmarkFoldersOptions = {}
  ): Promise<GetBookmarkFoldersResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/folders';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetBookmarkFoldersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Bookmarks by folder ID
   * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarksByFolderId(): Promise<GetBookmarksByFolderIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/folders/{folder_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetBookmarksByFolderIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Posts
   * Retrieves a list of posts authored by a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(options: GetPostsOptions = {}): Promise<GetPostsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get List memberships
   * Retrieves a list of Lists that a specific User is a member of by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getListMemberships(
    options: GetListMembershipsOptions = {}
  ): Promise<GetListMembershipsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/list_memberships';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetListMembershipsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unfollow List
   * Causes the authenticated user to unfollow a specific List by its ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unfollowList(): Promise<UnfollowListResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists/{list_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnfollowListResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Reposts of me
   * Retrieves a list of Posts that repost content from the authenticated user.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getRepostsOfMe(
    options: GetRepostsOfMeOptions = {}
  ): Promise<GetRepostsOfMeResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/reposts_of_me';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetRepostsOfMeResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get blocking
   * Retrieves a list of Users blocked by the specified User ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getBlocking(
    options: GetBlockingOptions = {}
  ): Promise<GetBlockingResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/blocking';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetBlockingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search Users
   * Retrieves a list of Users matching a search query.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async search(options: SearchOptions = {}): Promise<SearchResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/search';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get followers
   * Retrieves a list of Users who follow a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowers(
    options: GetFollowersOptions = {}
  ): Promise<GetFollowersResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/followers';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetFollowersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get my User
   * Retrieves details of the authenticated user.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getMe(): Promise<GetMeResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/me';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetMeResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get User by ID
   * Retrieves details of a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(): Promise<GetByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Users by usernames
   * Retrieves details of multiple Users by their usernames.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByUsernames(): Promise<GetByUsernamesResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/by';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByUsernamesResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get User by username
   * Retrieves details of a specific User by their username.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByUsername(): Promise<GetByUsernameResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/by/username/{username}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByUsernameResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Timeline
   * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getTimeline(
    options: GetTimelineOptions = {}
  ): Promise<GetTimelineResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/timelines/reverse_chronological';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetTimelineResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete Bookmark
   * Removes a Post from the authenticated user’s Bookmarks by its ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteBookmark(): Promise<DeleteBookmarkResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/{tweet_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DeleteBookmarkResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get pinned Lists
   * Retrieves a list of Lists pinned by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPinnedLists(): Promise<GetPinnedListsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/pinned_lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetPinnedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Pin List
   * Causes the authenticated user to pin a specific List by its ID.




   * @param body Request body

   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async pinList(body: PinListRequest): Promise<PinListResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/pinned_lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<PinListResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unpin List
   * Causes the authenticated user to unpin a specific List by its ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unpinList(): Promise<UnpinListResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/pinned_lists/{list_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnpinListResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get followed Lists
   * Retrieves a list of Lists followed by a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowedLists(
    options: GetFollowedListsOptions = {}
  ): Promise<GetFollowedListsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetFollowedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Follow List
   * Causes the authenticated user to follow a specific List by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async followList(
    options: FollowListOptions = {}
  ): Promise<FollowListResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<FollowListResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Repost Post
   * Causes the authenticated user to repost a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async repostPost(
    options: RepostPostOptions = {}
  ): Promise<RepostPostResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/retweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<RepostPostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Like Post
   * Causes the authenticated user to Like a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async likePost(options: LikePostOptions = {}): Promise<LikePostResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/likes';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<LikePostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get muting
   * Retrieves a list of Users muted by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getMuting(options: GetMutingOptions = {}): Promise<GetMutingResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/muting';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetMutingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Mute User
   * Causes the authenticated user to mute a specific User by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async muteUser(options: MuteUserOptions = {}): Promise<MuteUserResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/muting';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MuteUserResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Bookmarks
   * Retrieves a list of Posts bookmarked by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getBookmarks(
    options: GetBookmarksOptions = {}
  ): Promise<GetBookmarksResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetBookmarksResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create Bookmark
   * Adds a post to the authenticated user’s bookmarks.




   * @param body Request body

   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createBookmark(
    body: CreateBookmarkRequest
  ): Promise<CreateBookmarkResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<CreateBookmarkResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Unlike Post
   * Causes the authenticated user to Unlike a specific Post by its ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async unlikePost(): Promise<UnlikePostResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/likes/{tweet_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<UnlikePostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
