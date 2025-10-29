/**
 * Lists client for the X API.
 *
 * This module provides a client for interacting with the Lists endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  ListsGetFollowersResponse,
  ListsGetMembersResponse,
  ListsAddMemberRequest,
  ListsAddMemberResponse,
  ListsGetPostsResponse,
  ListsGetByIdResponse,
  ListsUpdateRequest,
  ListsUpdateResponse,
  ListsDeleteResponse,
  ListsRemoveMemberByUserIdResponse,
  ListsCreateRequest,
  ListsCreateResponse,
} from './models.js';

/**
 * Options for getFollowers method
 */
export interface ListsGetFollowersOptions {
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
 * Options for getMembers method
 */
export interface ListsGetMembersOptions {
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
 * Options for addMember method
 */
export interface ListsAddMemberOptions {
  /** Request body */
  body?: ListsAddMemberRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getPosts method
 */
export interface ListsGetPostsOptions {
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
export interface ListsGetByIdOptions {
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
 */
export interface ListsUpdateOptions {
  /** Request body */
  body?: ListsUpdateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for create method
 */
export interface ListsCreateOptions {
  /** Request body */
  body?: ListsCreateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Lists operations
 * 
 * This client provides methods for interacting with the Lists endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Lists related operations.
 * 
 * @category Lists
 */
export class ListsClient {
  private client: Client;

  /**
     * Creates a new Lists client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Add List member
   * Adds a User to a specific List by its ID.


   * @param id The ID of the List for which to add a member.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async addMember(
    id: string,
    options: ListsAddMemberOptions = {}
  ): Promise<ListsAddMemberResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

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

    return this.client.request<ListsAddMemberResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get List by ID
   * Retrieves details of a specific List by its ID.


   * @param id The ID of the List.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(
    id: string,
    options: ListsGetByIdOptions = {}
  ): Promise<ListsGetByIdResponse> {
    // Destructure options

    const {
      listfields = [],

      expansions = [],

      userfields = [],

      requestOptions: requestOptions = {},
    } = options;

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

    return this.client.request<ListsGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Update List
   * Updates the details of a specific List owned by the authenticated user by its ID.


   * @param id The ID of the List to modify.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async update(
    id: string,
    options: ListsUpdateOptions = {}
  ): Promise<ListsUpdateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

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

    return this.client.request<ListsUpdateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete List
   * Deletes a specific List owned by the authenticated user by its ID.


   * @param id The ID of the List to delete.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id: string): Promise<ListsDeleteResponse> {
    // Destructure options

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

    return this.client.request<ListsDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Remove List member
   * Removes a User from a specific List by its ID and the User’s ID.


   * @param id The ID of the List to remove a member.



   * @param userId The ID of User that will be removed from the List.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async removeMemberByUserId(
    id: string,
    userId: string
  ): Promise<ListsRemoveMemberByUserIdResponse> {
    // Destructure options

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

    return this.client.request<ListsRemoveMemberByUserIdResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create List
   * Creates a new List for the authenticated user.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(options: ListsCreateOptions = {}): Promise<ListsCreateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/lists';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<ListsCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get List followers
   * Retrieves a list of Users who follow a specific List by its ID.
   * Returns a paginator for automatic pagination through all results.


   * @param id The ID of the List.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getFollowers(
    id: string,
    options: ListsGetFollowersOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/followers';

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
        ...requestOptions,
      };

      const response = await this.client.request<ListsGetFollowersResponse>(
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
   * Get List members
   * Retrieves a list of Users who are members of a specific List by its ID.
   * Returns a paginator for automatic pagination through all results.


   * @param id The ID of the List.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getMembers(
    id: string,
    options: ListsGetMembersOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/members';

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
        ...requestOptions,
      };

      const response = await this.client.request<ListsGetMembersResponse>(
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
   * Get List Posts
   * Retrieves a list of Posts associated with a specific List by its ID.
   * Returns a paginator for automatic pagination through all results.


   * @param id The ID of the List.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getPosts(
    id: string,
    options: ListsGetPostsOptions = {}
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

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/tweets';

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
        ...requestOptions,
      };

      const response = await this.client.request<ListsGetPostsResponse>(
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
}
