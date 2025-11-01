/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetPostsResponse,
  RemoveMemberByUserIdResponse,
  GetByIdResponse,
  UpdateResponse,
  DeleteResponse,
  CreateResponse,
  GetFollowersResponse,
  GetMembersResponse,
  AddMemberResponse,
} from './models.js';

/**
 * Options for getPosts method
 * 
 * @public
 */
export interface GetPostsStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: any;

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
 * Options for removeMemberByUserId method
 * 
 * @public
 */
export interface RemoveMemberByUserIdStreamingOptions {
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
  /** A comma separated list of List fields to display. */
  listfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for update method
 * 
 * @public
 */
export interface UpdateStreamingOptions {
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
 * Options for delete method
 * 
 * @public
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
 * Options for create method
 * 
 * @public
 */
export interface CreateStreamingOptions {
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
 * Options for getFollowers method
 * 
 * @public
 */
export interface GetFollowersStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: any;

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
 * Options for getMembers method
 * 
 * @public
 */
export interface GetMembersStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: any;

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
 * Options for addMember method
 * 
 * @public
 */
export interface AddMemberStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class ListsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get List Posts
     * Retrieves a list of Posts associated with a specific List by its ID.
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

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getPosts');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

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
    let path = '/2/lists/{id}/tweets';

    path = path.replace('{id}', encodeURIComponent(String(id)));

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
     * Remove List member
     * Removes a User from a specific List by its ID and the User’s ID.
     * 
     * @returns Promise with the API response
     */
  async removeMemberByUserId(
    id: string,
    userId: string,
    options: RemoveMemberByUserIdStreamingOptions = {}
  ): Promise<RemoveMemberByUserIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'removeMemberByUserId'
    );

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}/members/{user_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{user_id}', encodeURIComponent(String(userId)));

    // Build query parameters
    const params = new URLSearchParams();

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
    return this.client.request<RemoveMemberByUserIdResponse>(
      'DELETE',
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
    options: GetByIdStreamingOptions = {}
  ): Promise<GetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      listfields = [],

      expansions = [],

      userfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}';

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
     * Update List
     * Updates the details of a specific List owned by the authenticated user by its ID.
     * 
     * @returns Promise with the API response
     */
  async update(
    id: string,
    options: UpdateStreamingOptions = {}
  ): Promise<UpdateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'update');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<UpdateResponse>(
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
  async delete(
    id: string,
    options: DeleteStreamingOptions = {}
  ): Promise<DeleteResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'delete');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

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
    return this.client.request<DeleteResponse>(
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
  async create(options: CreateStreamingOptions = {}): Promise<CreateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'create');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get List followers
     * Retrieves a list of Users who follow a specific List by its ID.
     * 
     * @returns Promise with the API response
     */
  async getFollowers(
    id: string,
    options: GetFollowersStreamingOptions = {}
  ): Promise<GetFollowersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getFollowers');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}/followers';

    path = path.replace('{id}', encodeURIComponent(String(id)));

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
    return this.client.request<GetFollowersResponse>(
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
    options: GetMembersStreamingOptions = {}
  ): Promise<GetMembersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getMembers');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}/members';

    path = path.replace('{id}', encodeURIComponent(String(id)));

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
    return this.client.request<GetMembersResponse>(
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
    options: AddMemberStreamingOptions = {}
  ): Promise<AddMemberResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'addMember');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists/{id}/members';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<AddMemberResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
