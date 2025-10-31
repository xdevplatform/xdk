/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetByIdResponse,
  DeleteResponse,
  GetInsightsHistoricalResponse,
  SearchAllResponse,
  GetCountsRecentResponse,
  GetRepostsResponse,
  GetQuotedResponse,
  GetByIdsResponse,
  CreateResponse,
  SearchRecentResponse,
  GetRepostedByResponse,
  GetCountsAllResponse,
  GetInsights28hrResponse,
  GetAnalyticsResponse,
  HideReplyResponse,
  GetLikingUsersResponse,
} from './models.js';

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
 * Options for delete method
 */
export interface DeleteStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getInsightsHistorical method
 */
export interface GetInsightsHistoricalStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for searchAll method
 */
export interface SearchAllStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getCountsRecent method
 */
export interface GetCountsRecentStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getReposts method
 */
export interface GetRepostsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getQuoted method
 */
export interface GetQuotedStreamingOptions {
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
 * Options for create method
 */
export interface CreateStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for searchRecent method
 */
export interface SearchRecentStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getRepostedBy method
 */
export interface GetRepostedByStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getCountsAll method
 */
export interface GetCountsAllStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getInsights28hr method
 */
export interface GetInsights28hrStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getAnalytics method
 */
export interface GetAnalyticsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for hideReply method
 */
export interface HideReplyStreamingOptions {
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
 * Options for getLikingUsers method
 */
export interface GetLikingUsersStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class PostsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Post by ID
     * Retrieves details of a specific Post by its ID.
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
    let path = `/2/tweets/{id}`;

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
     * Delete Post
     * Deletes a specific Post by its ID, if owned by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async delete(options: DeleteStreamingOptions = {}): Promise<DeleteResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'delete');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{id}`;

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
    return this.client.request<DeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get historical Post insights
     * Retrieves historical engagement metrics for specified Posts within a defined time range.
     * 
     * @returns Promise with the API response
     */
  async getInsightsHistorical(
    options: GetInsightsHistoricalStreamingOptions = {}
  ): Promise<GetInsightsHistoricalResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getInsightsHistorical'
    );

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/insights/historical`;

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
    return this.client.request<GetInsightsHistoricalResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search all Posts
     * Retrieves Posts from the full archive matching a search query.
     * 
     * @returns Promise with the API response
     */
  async searchAll(
    options: SearchAllStreamingOptions = {}
  ): Promise<SearchAllResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'searchAll');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/all`;

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
    return this.client.request<SearchAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get count of recent Posts
     * Retrieves the count of Posts from the last 7 days matching a search query.
     * 
     * @returns Promise with the API response
     */
  async getCountsRecent(
    options: GetCountsRecentStreamingOptions = {}
  ): Promise<GetCountsRecentResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getCountsRecent');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/counts/recent`;

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
    return this.client.request<GetCountsRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Reposts
     * Retrieves a list of Posts that repost a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getReposts(
    options: GetRepostsStreamingOptions = {}
  ): Promise<GetRepostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getReposts');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{id}/retweets`;

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
    return this.client.request<GetRepostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Quoted Posts
     * Retrieves a list of Posts that quote a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getQuoted(
    options: GetQuotedStreamingOptions = {}
  ): Promise<GetQuotedResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getQuoted');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{id}/quote_tweets`;

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
    return this.client.request<GetQuotedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Posts by IDs
     * Retrieves details of multiple Posts by their IDs.
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
    let path = `/2/tweets`;

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
     * Create or Edit Post
     * Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.
     * 
     * @returns Promise with the API response
     */
  async create(
    body: any,
    options: CreateStreamingOptions = {}
  ): Promise<CreateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'create');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets`;

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
    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search recent Posts
     * Retrieves Posts from the last 7 days matching a search query.
     * 
     * @returns Promise with the API response
     */
  async searchRecent(
    options: SearchRecentStreamingOptions = {}
  ): Promise<SearchRecentResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'searchRecent');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/recent`;

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
    return this.client.request<SearchRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Reposted by
     * Retrieves a list of Users who reposted a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getRepostedBy(
    options: GetRepostedByStreamingOptions = {}
  ): Promise<GetRepostedByResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRepostedBy');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{id}/retweeted_by`;

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
    return this.client.request<GetRepostedByResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get count of all Posts
     * Retrieves the count of Posts matching a search query from the full archive.
     * 
     * @returns Promise with the API response
     */
  async getCountsAll(
    options: GetCountsAllStreamingOptions = {}
  ): Promise<GetCountsAllResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getCountsAll');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/counts/all`;

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
    return this.client.request<GetCountsAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get 28-hour Post insights
     * Retrieves engagement metrics for specified Posts over the last 28 hours.
     * 
     * @returns Promise with the API response
     */
  async getInsights28hr(
    options: GetInsights28hrStreamingOptions = {}
  ): Promise<GetInsights28hrResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getInsights28hr');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/insights/28hr`;

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
    return this.client.request<GetInsights28hrResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Post analytics
     * Retrieves analytics data for specified Posts within a defined time range.
     * 
     * @returns Promise with the API response
     */
  async getAnalytics(
    options: GetAnalyticsStreamingOptions = {}
  ): Promise<GetAnalyticsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getAnalytics');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/analytics`;

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
    return this.client.request<GetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Hide reply
     * Hides or unhides a reply to a conversation owned by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async hideReply(
    options: HideReplyStreamingOptions = {}
  ): Promise<HideReplyResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'hideReply');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{tweet_id}/hidden`;

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
    return this.client.request<HideReplyResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Liking Users
     * Retrieves a list of Users who liked a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getLikingUsers(
    options: GetLikingUsersStreamingOptions = {}
  ): Promise<GetLikingUsersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getLikingUsers');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{id}/liking_users`;

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
    return this.client.request<GetLikingUsersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
