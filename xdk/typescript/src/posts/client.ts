/**
 * posts client for the X API.
 *
 * This module provides a client for interacting with the posts endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetByIdResponse,
  DeleteResponse,
  GetInsightsHistoricalResponse,
  SearchAllResponse,
  GetCountsRecentResponse,
  GetRepostsResponse,
  GetQuotedResponse,
  GetByIdsResponse,
  CreateRequest,
  CreateResponse,
  SearchRecentResponse,
  GetRepostedByResponse,
  GetCountsAllResponse,
  GetInsights28hrResponse,
  GetAnalyticsResponse,
  HideReplyRequest,
  HideReplyResponse,
  GetLikingUsersResponse,
} from './models.js';

/**
 * Options for searchAll method
 */
export interface SearchAllOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getCountsRecent method
 */
export interface GetCountsRecentOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getReposts method
 */
export interface GetRepostsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getQuoted method
 */
export interface GetQuotedOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for searchRecent method
 */
export interface SearchRecentOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getRepostedBy method
 */
export interface GetRepostedByOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getCountsAll method
 */
export interface GetCountsAllOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for hideReply method
 */
export interface HideReplyOptions {
  /** Request body */
  body?: HideReplyRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getLikingUsers method
 */
export interface GetLikingUsersOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for posts operations
 * 
 * This client provides methods for interacting with the posts endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all posts related operations.
 * 
 * @category posts
 */
export class PostsClient {
  private client: Client;

  /**
     * Creates a new posts client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get Post by ID
   * Retrieves details of a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(): Promise<GetByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets/{id}';

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
   * Delete Post
   * Deletes a specific Post by its ID, if owned by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(): Promise<DeleteResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets/{id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get historical Post insights
   * Retrieves historical engagement metrics for specified Posts within a defined time range.












   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getInsightsHistorical(): Promise<GetInsightsHistoricalResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/insights/historical';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetInsightsHistoricalResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search all Posts
   * Retrieves Posts from the full archive matching a search query.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async searchAll(options: SearchAllOptions = {}): Promise<SearchAllResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/search/all';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get count of recent Posts
   * Retrieves the count of Posts from the last 7 days matching a search query.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getCountsRecent(
    options: GetCountsRecentOptions = {}
  ): Promise<GetCountsRecentResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/counts/recent';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetCountsRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Reposts
   * Retrieves a list of Posts that repost a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getReposts(
    options: GetRepostsOptions = {}
  ): Promise<GetRepostsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}/retweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetRepostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Quoted Posts
   * Retrieves a list of Posts that quote a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getQuoted(options: GetQuotedOptions = {}): Promise<GetQuotedResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}/quote_tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetQuotedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Posts by IDs
   * Retrieves details of multiple Posts by their IDs.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(): Promise<GetByIdsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets';

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
   * Create or Edit Post
   * Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.


   * @param body Request body

   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(body: CreateRequest): Promise<CreateResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search recent Posts
   * Retrieves Posts from the last 7 days matching a search query.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async searchRecent(
    options: SearchRecentOptions = {}
  ): Promise<SearchRecentResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/search/recent';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Reposted by
   * Retrieves a list of Users who reposted a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getRepostedBy(
    options: GetRepostedByOptions = {}
  ): Promise<GetRepostedByResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}/retweeted_by';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetRepostedByResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get count of all Posts
   * Retrieves the count of Posts matching a search query from the full archive.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getCountsAll(
    options: GetCountsAllOptions = {}
  ): Promise<GetCountsAllResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/counts/all';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetCountsAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get 28-hour Post insights
   * Retrieves engagement metrics for specified Posts over the last 28 hours.








   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getInsights28hr(): Promise<GetInsights28hrResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/insights/28hr';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetInsights28hrResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Post analytics
   * Retrieves analytics data for specified Posts within a defined time range.










   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getAnalytics(): Promise<GetAnalyticsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets/analytics';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Hide reply
   * Hides or unhides a reply to a conversation owned by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async hideReply(options: HideReplyOptions = {}): Promise<HideReplyResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{tweet_id}/hidden';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<HideReplyResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Liking Users
   * Retrieves a list of Users who liked a specific Post by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getLikingUsers(
    options: GetLikingUsersOptions = {}
  ): Promise<GetLikingUsersResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}/liking_users';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetLikingUsersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
