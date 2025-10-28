/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  ListsGetFollowersResponse,
  ListsGetMembersResponse,
  ListsAddMemberResponse,
  ListsGetPostsResponse,
  ListsGetByIdResponse,
  ListsUpdateResponse,
  ListsDeleteResponse,
  ListsRemoveMemberByUserIdResponse,
  ListsCreateResponse,
} from './models.js';

/**
 * Options for getFollowers method
 */
export interface ListsGetFollowersStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getMembers method
 */
export interface ListsGetMembersStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for addMember method
 */
export interface ListsAddMemberStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getPosts method
 */
export interface ListsGetPostsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getById method
 */
export interface ListsGetByIdStreamingOptions {
  /** A comma separated list of List fields to display. */
  listfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for update method
 */
export interface ListsUpdateStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for create method
 */
export interface ListsCreateStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class ListsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get List followers
     * Retrieves a list of Users who follow a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async getFollowers(
    id: string,
    options: ListsGetFollowersStreamingOptions = {}
  ): Promise<ListsGetFollowersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getFollowers');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/lists/{id}/followers`;

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
    return this.client.request<ListsGetFollowersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get List members
     * Retrieves a list of Users who are members of a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async getMembers(
    id: string,
    options: ListsGetMembersStreamingOptions = {}
  ): Promise<ListsGetMembersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getMembers');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/lists/{id}/members`;

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
    return this.client.request<ListsGetMembersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Add List member
     * Adds a User to a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async addMember(
    id: string,
    options: ListsAddMemberStreamingOptions = {}
  ): Promise<ListsAddMemberResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'addMember');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/lists/{id}/members`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<ListsAddMemberResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get List Posts
     * Retrieves a list of Posts associated with a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async getPosts(
    id: string,
    options: ListsGetPostsStreamingOptions = {}
  ): Promise<ListsGetPostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getPosts');

    // Destructure options with defaults

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

    // Build path parameters
    let path = `/2/lists/{id}/tweets`;

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
    return this.client.request<ListsGetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get List by ID
     * Retrieves details of a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async getById(
    id: string,
    options: ListsGetByIdStreamingOptions = {}
  ): Promise<ListsGetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options with defaults

    const {
      listfields = [],

      expansions = [],

      userfields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/lists/{id}`;

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
    return this.client.request<ListsGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Update List
     * Updates the details of a specific List owned by the authenticated user by its ID.
     * 
     * @returns Promise with the API response
     */
  async update(
    id: string,
    options: ListsUpdateStreamingOptions = {}
  ): Promise<ListsUpdateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'update');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/lists/{id}`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<ListsUpdateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete List
     * Deletes a specific List owned by the authenticated user by its ID.
     * 
     * @returns Promise with the API response
     */
  async delete(id: string): Promise<ListsDeleteResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'delete');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/lists/{id}`;

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
    return this.client.request<ListsDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Remove List member
     * Removes a User from a specific List by its ID and the User’s ID.
     * 
     * @returns Promise with the API response
     */
  async removeMemberByUserId(
    id: string,
    userId: string
  ): Promise<ListsRemoveMemberByUserIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'removeMemberByUserId'
    );

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/lists/{id}/members/{user_id}`;

    path = path.replace(`{${'id'}}`, String(id));

    path = path.replace(`{${'user_id'}}`, String(userId));

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
    return this.client.request<ListsRemoveMemberByUserIdResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create List
     * Creates a new List for the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async create(
    options: ListsCreateStreamingOptions = {}
  ): Promise<ListsCreateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'create');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/lists`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<ListsCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
