/**
 * lists client for the X API.
 *
 * This module provides a client for interacting with the lists endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetMembersResponse,
  AddMemberRequest,
  AddMemberResponse,
  GetByIdResponse,
  UpdateRequest,
  UpdateResponse,
  DeleteResponse,
  CreateRequest,
  CreateResponse,
  GetFollowersResponse,
  RemoveMemberByUserIdResponse,
  GetPostsResponse,
} from './models.js';

/**
 * Options for getMembers method
 * 
 * @public
 */
export interface GetMembersOptions {
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
}

/**
 * Options for addMember method
 * 
 * @public
 */
export interface AddMemberOptions {
  /** Request body */
  body?: AddMemberRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getById method
 * 
 * @public
 */
export interface GetByIdOptions {
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
 * Options for update method
 * 
 * @public
 */
export interface UpdateOptions {
  /** Request body */
  body?: UpdateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for create method
 * 
 * @public
 */
export interface CreateOptions {
  /** Request body */
  body?: CreateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getFollowers method
 * 
 * @public
 */
export interface GetFollowersOptions {
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
}

/**
 * Options for getPosts method
 * 
 * @public
 */
export interface GetPostsOptions {
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
}

/**
 * Client for lists operations
 * 
 * This client provides methods for interacting with the lists endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all lists related operations.
 * 
 * @category lists
 */
export class ListsClient {
  private client: Client;

  /**
     * Creates a new lists client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get List members
   * Retrieves a list of Users who are members of a specific List by its ID.


   * @param id The ID of the List.




   * @returns {Promise<GetMembersResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getMembers(
    id: string,
    options: GetMembersOptions = {}
  ): Promise<GetMembersResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

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
      ...requestOptions,
    };

    return this.client.request<GetMembersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Add List member
   * Adds a User to a specific List by its ID.


   * @param id The ID of the List for which to add a member.




   * @returns {Promise<AddMemberResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async addMember(
    id: string,
    options: AddMemberOptions = {}
  ): Promise<AddMemberResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

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
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<AddMemberResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get List by ID
   * Retrieves details of a specific List by its ID.


   * @param id The ID of the List.




   * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(
    id: string,
    options: GetByIdOptions = {}
  ): Promise<GetByIdResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      listfields = [],

      expansions = [],

      userfields = [],

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
      ...requestOptions,
    };

    return this.client.request<GetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Update List
   * Updates the details of a specific List owned by the authenticated user by its ID.


   * @param id The ID of the List to modify.




   * @returns {Promise<UpdateResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async update(
    id: string,
    options: UpdateOptions = {}
  ): Promise<UpdateResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

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
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<UpdateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete List
   * Deletes a specific List owned by the authenticated user by its ID.


   * @param id The ID of the List to delete.




   * @returns {Promise<DeleteResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id: string): Promise<DeleteResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/lists/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

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
   * Create List
   * Creates a new List for the authenticated user.



   * @returns {Promise<CreateResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(options: CreateOptions = {}): Promise<CreateResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get List followers
   * Retrieves a list of Users who follow a specific List by its ID.


   * @param id The ID of the List.




   * @returns {Promise<GetFollowersResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowers(
    id: string,
    options: GetFollowersOptions = {}
  ): Promise<GetFollowersResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

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
      ...requestOptions,
    };

    return this.client.request<GetFollowersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Remove List member
   * Removes a User from a specific List by its ID and the User’s ID.


   * @param id The ID of the List to remove a member.



   * @param userId The ID of User that will be removed from the List.




   * @returns {Promise<RemoveMemberByUserIdResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async removeMemberByUserId(
    id: string,
    userId: string
  ): Promise<RemoveMemberByUserIdResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/lists/{id}/members/{user_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{user_id}', encodeURIComponent(String(userId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<RemoveMemberByUserIdResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get List Posts
   * Retrieves a list of Posts associated with a specific List by its ID.


   * @param id The ID of the List.




   * @returns {Promise<GetPostsResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(
    id: string,
    options: GetPostsOptions = {}
  ): Promise<GetPostsResponse> {
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
      ...requestOptions,
    };

    return this.client.request<GetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
