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
  GetPostsResponse,
  GetFollowersResponse,
  GetMembersResponse,
  AddMemberRequest,
  AddMemberResponse,
  GetByIdResponse,
  UpdateRequest,
  UpdateResponse,
  DeleteResponse,
  RemoveMemberByUserIdResponse,
  CreateRequest,
  CreateResponse,
} from './models.js';

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
 * Options for getFollowers method
 * 
 * @public
 */
export interface GetFollowersOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getMembers method
 * 
 * @public
 */
export interface GetMembersOptions {
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
   * Get List Posts
   * Retrieves a list of Posts associated with a specific List by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(options: GetPostsOptions = {}): Promise<GetPostsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/tweets';

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
   * Get List followers
   * Retrieves a list of Users who follow a specific List by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getFollowers(
    options: GetFollowersOptions = {}
  ): Promise<GetFollowersResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/followers';

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
   * Get List members
   * Retrieves a list of Users who are members of a specific List by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getMembers(
    options: GetMembersOptions = {}
  ): Promise<GetMembersResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/members';

    // Build query parameters
    const params = new URLSearchParams();

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




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async addMember(options: AddMemberOptions = {}): Promise<AddMemberResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}/members';

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




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(): Promise<GetByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/lists/{id}';

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
   * Update List
   * Updates the details of a specific List owned by the authenticated user by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async update(options: UpdateOptions = {}): Promise<UpdateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/lists/{id}';

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




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(): Promise<DeleteResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/lists/{id}';

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
   * Remove List member
   * Removes a User from a specific List by its ID and the User’s ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async removeMemberByUserId(): Promise<RemoveMemberByUserIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/lists/{id}/members/{user_id}';

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
   * Create List
   * Creates a new List for the authenticated user.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(options: CreateOptions = {}): Promise<CreateResponse> {
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

    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
