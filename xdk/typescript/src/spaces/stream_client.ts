/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  SpacesGetByCreatorIdsResponse,
  SpacesGetBuyersResponse,
  SpacesGetPostsResponse,
  SpacesGetByIdResponse,
  SpacesGetByIdsResponse,
  SpacesSearchResponse,
} from './models.js';

/**
 * Options for getByCreatorIds method
 */
export interface SpacesGetByCreatorIdsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getBuyers method
 */
export interface SpacesGetBuyersStreamingOptions {
  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getPosts method
 */
export interface SpacesGetPostsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getById method
 */
export interface SpacesGetByIdStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getByIds method
 */
export interface SpacesGetByIdsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for search method
 */
export interface SpacesSearchStreamingOptions {
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
    options: SpacesGetByCreatorIdsStreamingOptions = {}
  ): Promise<SpacesGetByCreatorIdsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByCreatorIds');

    // Destructure options with defaults

    const {
      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (userIds !== undefined) {
      params.append('user_ids', String(userIds));
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

    // Build path parameters
    let path = `/2/spaces/by/creator_ids`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<SpacesGetByCreatorIdsResponse>(
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
    options: SpacesGetBuyersStreamingOptions = {}
  ): Promise<SpacesGetBuyersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getBuyers');

    // Destructure options with defaults

    const {
      paginationToken = undefined,

      maxResults = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/spaces/{id}/buyers`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<SpacesGetBuyersResponse>(
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
    options: SpacesGetPostsStreamingOptions = {}
  ): Promise<SpacesGetPostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getPosts');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/spaces/{id}/tweets`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<SpacesGetPostsResponse>(
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
    options: SpacesGetByIdStreamingOptions = {}
  ): Promise<SpacesGetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options with defaults

    const {
      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/spaces/{id}`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<SpacesGetByIdResponse>(
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
    options: SpacesGetByIdsStreamingOptions = {}
  ): Promise<SpacesGetByIdsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByIds');

    // Destructure options with defaults

    const {
      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.append('ids', String(ids));
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

    // Build path parameters
    let path = `/2/spaces`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<SpacesGetByIdsResponse>(
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
    options: SpacesSearchStreamingOptions = {}
  ): Promise<SpacesSearchResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'search');

    // Destructure options with defaults

    const {
      state = undefined,

      maxResults = undefined,

      spacefields = [],

      expansions = [],

      userfields = [],

      topicfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.append('query', String(query));
    }

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

    // Build path parameters
    let path = `/2/spaces/search`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<SpacesSearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
