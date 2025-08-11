/**
 * Lists client for the X API.
 *
 * This module provides a client for interacting with the Lists endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  ListsGetUsersOwnedResponse,
  ListsAddMemberRequest,
  ListsAddMemberResponse,
  ListsGetUsersFollowedResponse,
  ListsFollowRequest,
  ListsFollowResponse,
  ListsUnfollowResponse,
  ListsUnpinResponse,
  ListsGetUsersMembershipsResponse,
  ListsCreateRequest,
  ListsCreateResponse,
  ListsGetByIdResponse,
  ListsUpdateRequest,
  ListsUpdateResponse,
  ListsDeleteResponse,
  ListsRemoveMemberByUserIdResponse,
  ListsGetUsersPinnedResponse,
  ListsPinRequest,
  ListsPinResponse,
} from './models.js';

/**
 * Client for Lists operations
 */
export class ListsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get owned Lists
     * Retrieves a list of Lists owned by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param listfields A comma separated list of List fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersOwned(
    id: any,
    maxResults?: any,
    paginationToken?: any,
    listfields?: any,
    expansions?: any,
    userfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsGetUsersOwnedResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (listfields !== undefined) {
      params.set('list.fields', String(listfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    const path = `/2/users/{id}/owned_lists`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsGetUsersOwnedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Add List member
     * Adds a User to a specific List by its ID.
     * @param id The ID of the List for which to add a member.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async addMember(
    id: any,
    body?: ListsAddMemberRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsAddMemberResponse>> {
    const params = new URLSearchParams();

    const path = `/2/lists/{id}/members`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<ListsAddMemberResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get followed Lists
     * Retrieves a list of Lists followed by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param listfields A comma separated list of List fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersFollowed(
    id: any,
    maxResults?: any,
    paginationToken?: any,
    listfields?: any,
    expansions?: any,
    userfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsGetUsersFollowedResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (listfields !== undefined) {
      params.set('list.fields', String(listfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    const path = `/2/users/{id}/followed_lists`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsGetUsersFollowedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Follow List
     * Causes the authenticated user to follow a specific List by its ID.
     * @param id The ID of the authenticated source User that will follow the List.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async follow(
    id: any,
    body?: ListsFollowRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsFollowResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/followed_lists`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<ListsFollowResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unfollow List
     * Causes the authenticated user to unfollow a specific List by its ID.
     * @param id The ID of the authenticated source User that will unfollow the List.
     * @param listId The ID of the List to unfollow.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unfollow(
    id: any,
    listId: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsUnfollowResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/followed_lists/{list_id}`
      .replace('{id}', String(id))
      .replace('{list_id}', String(listId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsUnfollowResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unpin List
     * Causes the authenticated user to unpin a specific List by its ID.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param listId The ID of the List to unpin.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unpin(
    id: any,
    listId: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsUnpinResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/pinned_lists/{list_id}`
      .replace('{id}', String(id))
      .replace('{list_id}', String(listId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsUnpinResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get List memberships
     * Retrieves a list of Lists that a specific User is a member of by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param listfields A comma separated list of List fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersMemberships(
    id: any,
    maxResults?: any,
    paginationToken?: any,
    listfields?: any,
    expansions?: any,
    userfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsGetUsersMembershipsResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (listfields !== undefined) {
      params.set('list.fields', String(listfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    const path = `/2/users/{id}/list_memberships`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsGetUsersMembershipsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create List
     * Creates a new List for the authenticated user.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async create(
    body?: ListsCreateRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsCreateResponse>> {
    const params = new URLSearchParams();

    const path = `/2/lists`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<ListsCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get List by ID
     * Retrieves details of a specific List by its ID.
     * @param id The ID of the List.
     * @param listfields A comma separated list of List fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getById(
    id: any,
    listfields?: any,
    expansions?: any,
    userfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsGetByIdResponse>> {
    const params = new URLSearchParams();

    if (listfields !== undefined) {
      params.set('list.fields', String(listfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    const path = `/2/lists/{id}`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Update List
     * Updates the details of a specific List owned by the authenticated user by its ID.
     * @param id The ID of the List to modify.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async update(
    id: any,
    body?: ListsUpdateRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsUpdateResponse>> {
    const params = new URLSearchParams();

    const path = `/2/lists/{id}`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<ListsUpdateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete List
     * Deletes a specific List owned by the authenticated user by its ID.
     * @param id The ID of the List to delete.* @param options Additional request options
     * @returns Promise with the API response
     */
  async delete(
    id: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsDeleteResponse>> {
    const params = new URLSearchParams();

    const path = `/2/lists/{id}`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Remove List member
     * Removes a User from a specific List by its ID and the User’s ID.
     * @param id The ID of the List to remove a member.
     * @param userId The ID of User that will be removed from the List.* @param options Additional request options
     * @returns Promise with the API response
     */
  async removeMemberByUserId(
    id: any,
    userId: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsRemoveMemberByUserIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/lists/{id}/members/{user_id}`
      .replace('{id}', String(id))
      .replace('{user_id}', String(userId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsRemoveMemberByUserIdResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get pinned Lists
     * Retrieves a list of Lists pinned by the authenticated user.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param listfields A comma separated list of List fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersPinned(
    id: any,
    listfields?: any,
    expansions?: any,
    userfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsGetUsersPinnedResponse>> {
    const params = new URLSearchParams();

    if (listfields !== undefined) {
      params.set('list.fields', String(listfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    const path = `/2/users/{id}/pinned_lists`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ListsGetUsersPinnedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Pin List
     * Causes the authenticated user to pin a specific List by its ID.
     * @param id The ID of the authenticated source User that will pin the List.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async pin(
    id: any,
    body?: ListsPinRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<ListsPinResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/pinned_lists`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<ListsPinResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
