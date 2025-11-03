/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetByCreatorIdsResponse,
  GetPostsResponse,
  GetByIdsResponse,
  GetByIdResponse,
  GetBuyersResponse,
  SearchResponse,
} from './models.js';

/**
 * Options for getByCreatorIds method
 * 
 * @public
 */
export interface GetByCreatorIdsStreamingOptions {
  /** A comma separated list of Space fields to display. */
  spacefields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Topic fields to display. */
  topicfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getPosts method
 * 
 * @public
 */
export interface GetPostsStreamingOptions {
  /** The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100. */
  maxResults?: number;

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
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getByIds method
 * 
 * @public
 */
export interface GetByIdsStreamingOptions {
  /** A comma separated list of Space fields to display. */
  spacefields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Topic fields to display. */
  topicfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getById method
 * 
 * @public
 */
export interface GetByIdStreamingOptions {
  /** A comma separated list of Space fields to display. */
  spacefields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Topic fields to display. */
  topicfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getBuyers method
 * 
 * @public
 */
export interface GetBuyersStreamingOptions {
  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: any;

  /** The maximum number of results. */
  maxResults?: number;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for search method
 * 
 * @public
 */
export interface SearchStreamingOptions {
  /** The state of Spaces to search for. */
  state?: string;

  /** The number of results to return. */
  maxResults?: number;

  /** A comma separated list of Space fields to display. */
  spacefields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Topic fields to display. */
  topicfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class SpacesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Spaces by creator IDs
     * Retrieves details of Spaces created by specified User IDs.
     * 
     * @returns Promise with the API response
     */
  async getByCreatorIds(
    userIds: Array<any>,
    options: GetByCreatorIdsStreamingOptions = {}
  ): Promise<GetByCreatorIdsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByCreatorIds');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/spaces/by/creator_ids';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('user_ids', userIds.join(','));

    if (spacefields !== undefined) {
      params.append('space.fields', spacefields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (topicfields !== undefined) {
      params.append('topic.fields', topicfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetByCreatorIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Space Posts
     * Retrieves a list of Posts shared in a specific Space by its ID.
     * 
     * @returns Promise with the API response
     */
  async getPosts(
    id: string,
    options: GetPostsStreamingOptions = {}
  ): Promise<GetPostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getPosts');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/spaces/{id}/tweets';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Spaces by IDs
     * Retrieves details of multiple Spaces by their IDs.
     * 
     * @returns Promise with the API response
     */
  async getByIds(
    ids: Array<any>,
    options: GetByIdsStreamingOptions = {}
  ): Promise<GetByIdsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByIds');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/spaces';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('ids', ids.join(','));

    if (spacefields !== undefined) {
      params.append('space.fields', spacefields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (topicfields !== undefined) {
      params.append('topic.fields', topicfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get space by ID
     * Retrieves details of a specific space by its ID.
     * 
     * @returns Promise with the API response
     */
  async getById(
    id: string,
    options: GetByIdStreamingOptions = {}
  ): Promise<GetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/spaces/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (spacefields !== undefined) {
      params.append('space.fields', spacefields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (topicfields !== undefined) {
      params.append('topic.fields', topicfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Space ticket buyers
     * Retrieves a list of Users who purchased tickets to a specific Space by its ID.
     * 
     * @returns Promise with the API response
     */
  async getBuyers(
    id: string,
    options: GetBuyersStreamingOptions = {}
  ): Promise<GetBuyersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getBuyers');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      paginationToken = undefined,

      maxResults = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/spaces/{id}/buyers';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetBuyersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search Spaces
     * Retrieves a list of Spaces matching the specified search query.
     * 
     * @returns Promise with the API response
     */
  async search(
    query: string,
    options: SearchStreamingOptions = {}
  ): Promise<SearchResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'search');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      state = undefined,

      maxResults = undefined,

      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/spaces/search';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('query', String(query));

    if (state !== undefined) {
      params.append('state', String(state));
    }

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (spacefields !== undefined) {
      params.append('space.fields', spacefields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (topicfields !== undefined) {
      params.append('topic.fields', topicfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<SearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
