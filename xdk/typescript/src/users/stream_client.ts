/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  UnmuteUserResponse,
  UnlikePostResponse,
  GetLikedPostsResponse,
  GetPostsResponse,
  GetPinnedListsResponse,
  PinListResponse,
  GetOwnedListsResponse,
  GetListMembershipsResponse,
  RepostPostResponse,
  GetTimelineResponse,
  GetFollowersResponse,
  GetMentionsResponse,
  GetBookmarkFoldersResponse,
  BlockDmsResponse,
  SearchResponse,
  GetByUsernamesResponse,
  UnfollowUserResponse,
  UnpinListResponse,
  GetBlockingResponse,
  UnrepostPostResponse,
  DeleteBookmarkResponse,
  GetBookmarksByFolderIdResponse,
  GetFollowingResponse,
  FollowUserResponse,
  GetBookmarksResponse,
  CreateBookmarkResponse,
  GetByIdsResponse,
  LikePostResponse,
  GetByIdResponse,
  GetByUsernameResponse,
  GetMeResponse,
  GetRepostsOfMeResponse,
  UnblockDmsResponse,
  UnfollowListResponse,
  GetFollowedListsResponse,
  FollowListResponse,
  GetMutingResponse,
  MuteUserResponse,
} from './models.js';

/**
 * Options for unmuteUser method
 */
export interface UnmuteUserStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for unlikePost method
 */
export interface UnlikePostStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getLikedPosts method
 */
export interface GetLikedPostsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getPosts method
 */
export interface GetPostsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getPinnedLists method
 */
export interface GetPinnedListsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for pinList method
 */
export interface PinListStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getOwnedLists method
 */
export interface GetOwnedListsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getListMemberships method
 */
export interface GetListMembershipsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for repostPost method
 */
export interface RepostPostStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getTimeline method
 */
export interface GetTimelineStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getFollowers method
 */
export interface GetFollowersStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getMentions method
 */
export interface GetMentionsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getBookmarkFolders method
 */
export interface GetBookmarkFoldersStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for blockDms method
 */
export interface BlockDmsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for search method
 */
export interface SearchStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getByUsernames method
 */
export interface GetByUsernamesStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for unfollowUser method
 */
export interface UnfollowUserStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for unpinList method
 */
export interface UnpinListStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getBlocking method
 */
export interface GetBlockingStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for unrepostPost method
 */
export interface UnrepostPostStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for deleteBookmark method
 */
export interface DeleteBookmarkStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getBookmarksByFolderId method
 */
export interface GetBookmarksByFolderIdStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getFollowing method
 */
export interface GetFollowingStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for followUser method
 */
export interface FollowUserStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getBookmarks method
 */
export interface GetBookmarksStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createBookmark method
 */
export interface CreateBookmarkStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getByIds method
 */
export interface GetByIdsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for likePost method
 */
export interface LikePostStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getById method
 */
export interface GetByIdStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getByUsername method
 */
export interface GetByUsernameStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getMe method
 */
export interface GetMeStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getRepostsOfMe method
 */
export interface GetRepostsOfMeStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for unblockDms method
 */
export interface UnblockDmsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for unfollowList method
 */
export interface UnfollowListStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getFollowedLists method
 */
export interface GetFollowedListsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for followList method
 */
export interface FollowListStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getMuting method
 */
export interface GetMutingStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for muteUser method
 */
export interface MuteUserStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class UsersClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Unmute User
     * Causes the authenticated user to unmute a specific user by their ID.
     * 
     * @returns Promise with the API response
     */
  async unmuteUser(
    options: UnmuteUserStreamingOptions = {}
  ): Promise<UnmuteUserResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unmuteUser');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{source_user_id}/muting/{target_user_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnmuteUserResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Unlike Post
     * Causes the authenticated user to Unlike a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async unlikePost(
    options: UnlikePostStreamingOptions = {}
  ): Promise<UnlikePostResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unlikePost');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/likes/{tweet_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnlikePostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get liked Posts
     * Retrieves a list of Posts liked by a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getLikedPosts(
    options: GetLikedPostsStreamingOptions = {}
  ): Promise<GetLikedPostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getLikedPosts');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/liked_tweets`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetLikedPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Posts
     * Retrieves a list of posts authored by a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getPosts(
    options: GetPostsStreamingOptions = {}
  ): Promise<GetPostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getPosts');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/tweets`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get pinned Lists
     * Retrieves a list of Lists pinned by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getPinnedLists(
    options: GetPinnedListsStreamingOptions = {}
  ): Promise<GetPinnedListsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getPinnedLists');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/pinned_lists`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetPinnedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Pin List
     * Causes the authenticated user to pin a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async pinList(
    body: any,
    options: PinListStreamingOptions = {}
  ): Promise<PinListResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'pinList');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/pinned_lists`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<PinListResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get owned Lists
     * Retrieves a list of Lists owned by a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getOwnedLists(
    options: GetOwnedListsStreamingOptions = {}
  ): Promise<GetOwnedListsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getOwnedLists');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/owned_lists`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetOwnedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get List memberships
     * Retrieves a list of Lists that a specific User is a member of by their ID.
     * 
     * @returns Promise with the API response
     */
  async getListMemberships(
    options: GetListMembershipsStreamingOptions = {}
  ): Promise<GetListMembershipsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getListMemberships');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/list_memberships`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetListMembershipsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Repost Post
     * Causes the authenticated user to repost a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async repostPost(
    options: RepostPostStreamingOptions = {}
  ): Promise<RepostPostResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'repostPost');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/retweets`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<RepostPostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Timeline
     * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
     * 
     * @returns Promise with the API response
     */
  async getTimeline(
    options: GetTimelineStreamingOptions = {}
  ): Promise<GetTimelineResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getTimeline');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/timelines/reverse_chronological`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetTimelineResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get followers
     * Retrieves a list of Users who follow a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getFollowers(
    options: GetFollowersStreamingOptions = {}
  ): Promise<GetFollowersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getFollowers');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/followers`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetFollowersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get mentions
     * Retrieves a list of Posts that mention a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getMentions(
    options: GetMentionsStreamingOptions = {}
  ): Promise<GetMentionsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getMentions');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/mentions`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetMentionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Bookmark folders
     * Retrieves a list of Bookmark folders created by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getBookmarkFolders(
    options: GetBookmarkFoldersStreamingOptions = {}
  ): Promise<GetBookmarkFoldersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getBookmarkFolders');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/bookmarks/folders`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetBookmarkFoldersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Block DMs
     * Blocks direct messages to or from a specific User by their ID for the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async blockDms(
    options: BlockDmsStreamingOptions = {}
  ): Promise<BlockDmsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'blockDms');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/dm/block`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<BlockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search Users
     * Retrieves a list of Users matching a search query.
     * 
     * @returns Promise with the API response
     */
  async search(options: SearchStreamingOptions = {}): Promise<SearchResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'search');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/search`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<SearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Users by usernames
     * Retrieves details of multiple Users by their usernames.
     * 
     * @returns Promise with the API response
     */
  async getByUsernames(
    options: GetByUsernamesStreamingOptions = {}
  ): Promise<GetByUsernamesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByUsernames');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/by`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetByUsernamesResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Unfollow User
     * Causes the authenticated user to unfollow a specific user by their ID.
     * 
     * @returns Promise with the API response
     */
  async unfollowUser(
    options: UnfollowUserStreamingOptions = {}
  ): Promise<UnfollowUserResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unfollowUser');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{source_user_id}/following/{target_user_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnfollowUserResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Unpin List
     * Causes the authenticated user to unpin a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async unpinList(
    options: UnpinListStreamingOptions = {}
  ): Promise<UnpinListResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unpinList');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/pinned_lists/{list_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnpinListResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get blocking
     * Retrieves a list of Users blocked by the specified User ID.
     * 
     * @returns Promise with the API response
     */
  async getBlocking(
    options: GetBlockingStreamingOptions = {}
  ): Promise<GetBlockingResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getBlocking');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/blocking`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetBlockingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Unrepost Post
     * Causes the authenticated user to unrepost a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async unrepostPost(
    options: UnrepostPostStreamingOptions = {}
  ): Promise<UnrepostPostResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unrepostPost');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/retweets/{source_tweet_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnrepostPostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete Bookmark
     * Removes a Post from the authenticated user’s Bookmarks by its ID.
     * 
     * @returns Promise with the API response
     */
  async deleteBookmark(
    options: DeleteBookmarkStreamingOptions = {}
  ): Promise<DeleteBookmarkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteBookmark');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/bookmarks/{tweet_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<DeleteBookmarkResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Bookmarks by folder ID
     * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getBookmarksByFolderId(
    options: GetBookmarksByFolderIdStreamingOptions = {}
  ): Promise<GetBookmarksByFolderIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getBookmarksByFolderId'
    );

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/bookmarks/folders/{folder_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetBookmarksByFolderIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get following
     * Retrieves a list of Users followed by a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getFollowing(
    options: GetFollowingStreamingOptions = {}
  ): Promise<GetFollowingResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getFollowing');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/following`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetFollowingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Follow User
     * Causes the authenticated user to follow a specific user by their ID.
     * 
     * @returns Promise with the API response
     */
  async followUser(
    options: FollowUserStreamingOptions = {}
  ): Promise<FollowUserResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'followUser');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/following`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<FollowUserResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Bookmarks
     * Retrieves a list of Posts bookmarked by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getBookmarks(
    options: GetBookmarksStreamingOptions = {}
  ): Promise<GetBookmarksResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getBookmarks');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/bookmarks`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetBookmarksResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create Bookmark
     * Adds a post to the authenticated user’s bookmarks.
     * 
     * @returns Promise with the API response
     */
  async createBookmark(
    body: any,
    options: CreateBookmarkStreamingOptions = {}
  ): Promise<CreateBookmarkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createBookmark');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/bookmarks`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<CreateBookmarkResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Users by IDs
     * Retrieves details of multiple Users by their IDs.
     * 
     * @returns Promise with the API response
     */
  async getByIds(
    options: GetByIdsStreamingOptions = {}
  ): Promise<GetByIdsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByIds');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Like Post
     * Causes the authenticated user to Like a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async likePost(
    options: LikePostStreamingOptions = {}
  ): Promise<LikePostResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likePost');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/likes`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<LikePostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get User by ID
     * Retrieves details of a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getById(
    options: GetByIdStreamingOptions = {}
  ): Promise<GetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get User by username
     * Retrieves details of a specific User by their username.
     * 
     * @returns Promise with the API response
     */
  async getByUsername(
    options: GetByUsernameStreamingOptions = {}
  ): Promise<GetByUsernameResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByUsername');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/by/username/{username}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetByUsernameResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get my User
     * Retrieves details of the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getMe(options: GetMeStreamingOptions = {}): Promise<GetMeResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getMe');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/me`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetMeResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Reposts of me
     * Retrieves a list of Posts that repost content from the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getRepostsOfMe(
    options: GetRepostsOfMeStreamingOptions = {}
  ): Promise<GetRepostsOfMeResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRepostsOfMe');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/reposts_of_me`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetRepostsOfMeResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Unblock DMs
     * Unblocks direct messages to or from a specific User by their ID for the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async unblockDms(
    options: UnblockDmsStreamingOptions = {}
  ): Promise<UnblockDmsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unblockDms');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/dm/unblock`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnblockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Unfollow List
     * Causes the authenticated user to unfollow a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async unfollowList(
    options: UnfollowListStreamingOptions = {}
  ): Promise<UnfollowListResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'unfollowList');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/followed_lists/{list_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<UnfollowListResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get followed Lists
     * Retrieves a list of Lists followed by a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async getFollowedLists(
    options: GetFollowedListsStreamingOptions = {}
  ): Promise<GetFollowedListsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getFollowedLists');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/followed_lists`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetFollowedListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Follow List
     * Causes the authenticated user to follow a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async followList(
    options: FollowListStreamingOptions = {}
  ): Promise<FollowListResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'followList');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/followed_lists`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<FollowListResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get muting
     * Retrieves a list of Users muted by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getMuting(
    options: GetMutingStreamingOptions = {}
  ): Promise<GetMutingResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getMuting');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/muting`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetMutingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Mute User
     * Causes the authenticated user to mute a specific User by their ID.
     * 
     * @returns Promise with the API response
     */
  async muteUser(
    options: MuteUserStreamingOptions = {}
  ): Promise<MuteUserResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'muteUser');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/users/{id}/muting`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<MuteUserResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
