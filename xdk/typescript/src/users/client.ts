/**
 * Users client for the X API.
 *
 * This module provides a client for interacting with the Users endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  UsersGetPostsLikingResponse,
  UsersGetMyResponse,
  UsersGetBlockingResponse,
  UsersGetFollowersResponse,
  UsersGetByUsernameResponse,
  UsersGetFollowingResponse,
  UsersFollowRequest,
  UsersFollowResponse,
  UsersUnmuteResponse,
  UsersGetListsMembersResponse,
  UsersGetByIdsResponse,
  UsersGetMutingResponse,
  UsersMuteRequest,
  UsersMuteResponse,
  UsersGetRepostsOfMeResponse,
  UsersSearchResponse,
  UsersBlockDmsResponse,
  UsersUnfollowResponse,
  UsersGetListsFollowersResponse,
  UsersUnblockDmsResponse,
  UsersGetPostsRepostedByResponse,
  UsersGetByIdResponse,
  UsersGetByUsernamesResponse,
} from './models.js';

/**
 * Client for Users operations
 */
export class UsersClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Liking Users
     * Retrieves a list of Users who liked a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getPostsLiking(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetPostsLikingResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/tweets/{id}/liking_users`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetPostsLikingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get my User
     * Retrieves details of the authenticated user.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getMy(
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetMyResponse>> {
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/me`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetMyResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get blocking
     * Retrieves a list of Users blocked by the specified User ID.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getBlocking(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetBlockingResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/{id}/blocking`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetBlockingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get followers
     * Retrieves a list of Users who follow a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getFollowers(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetFollowersResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/{id}/followers`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetFollowersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get User by username
     * Retrieves details of a specific User by their username.
     * @param username A username.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByUsername(
    username: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetByUsernameResponse>> {
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/by/username/{username}`.replace(
      '{username}',
      String(username)
    );

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetByUsernameResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get following
     * Retrieves a list of Users followed by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getFollowing(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetFollowingResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/{id}/following`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetFollowingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Follow User
     * Causes the authenticated user to follow a specific user by their ID.
     * @param id The ID of the authenticated source User that is requesting to follow the target User.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async follow(
    id: string,
    body?: UsersFollowRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersFollowResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/following`.replace('{id}', String(id));

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

    return this.client.request<UsersFollowResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unmute User
     * Causes the authenticated user to unmute a specific user by their ID.
     * @param sourceUserId The ID of the authenticated source User that is requesting to unmute the target User.
     * @param targetUserId The ID of the User that the source User is requesting to unmute.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unmute(
    targetUserId: string,
    sourceUserId: string,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersUnmuteResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{source_user_id}/muting/{target_user_id}`
      .replace('{source_user_id}', String(sourceUserId))
      .replace('{target_user_id}', String(targetUserId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersUnmuteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get List members
     * Retrieves a list of Users who are members of a specific List by its ID.
     * @param id The ID of the List.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getListsMembers(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetListsMembersResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/lists/{id}/members`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetListsMembersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Users by IDs
     * Retrieves details of multiple Users by their IDs.
     * @param ids A list of User IDs, comma-separated. You can specify up to 100 IDs.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByIds(
    ids: Array<any>,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetByIdsResponse>> {
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.set('ids', String(ids));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get muting
     * Retrieves a list of Users muted by the authenticated user.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getMuting(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetMutingResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/{id}/muting`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetMutingResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Mute User
     * Causes the authenticated user to mute a specific User by their ID.
     * @param id The ID of the authenticated source User that is requesting to mute the target User.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async mute(
    id: string,
    body?: UsersMuteRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersMuteResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/muting`.replace('{id}', String(id));

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

    return this.client.request<UsersMuteResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Reposts of me
     * Retrieves a list of Posts that repost content from the authenticated user.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getRepostsOfMe(
    placefields?: Array<any>,
    userfields?: Array<any>,
    pollfields?: Array<any>,
    mediafields?: Array<any>,
    tweetfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetRepostsOfMeResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (mediafields !== undefined) {
      params.set('media.fields', String(mediafields));
    }

    if (pollfields !== undefined) {
      params.set('poll.fields', String(pollfields));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (placefields !== undefined) {
      params.set('place.fields', String(placefields));
    }

    const path = `/2/users/reposts_of_me`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetRepostsOfMeResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Search Users
     * Retrieves a list of Users matching a search query.
     * @param query TThe the query string by which to query for users.
     * @param maxResults The maximum number of results.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async search(
    query: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    nextToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersSearchResponse>> {
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.set('query', String(query));
    }

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (nextToken !== undefined) {
      params.set('next_token', String(nextToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/search`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersSearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Block DMs
     * Blocks direct messages to or from a specific User by their ID for the authenticated user.
     * @param id The ID of the target User that the authenticated user requesting to block dms for.* @param options Additional request options
     * @returns Promise with the API response
     */
  async blockDms(
    id: string,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersBlockDmsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/dm/block`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersBlockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unfollow User
     * Causes the authenticated user to unfollow a specific user by their ID.
     * @param sourceUserId The ID of the authenticated source User that is requesting to unfollow the target User.
     * @param targetUserId The ID of the User that the source User is requesting to unfollow.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unfollow(
    targetUserId: string,
    sourceUserId: string,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersUnfollowResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{source_user_id}/following/{target_user_id}`
      .replace('{source_user_id}', String(sourceUserId))
      .replace('{target_user_id}', String(targetUserId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersUnfollowResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get List followers
     * Retrieves a list of Users who follow a specific List by its ID.
     * @param id The ID of the List.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getListsFollowers(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetListsFollowersResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/lists/{id}/followers`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetListsFollowersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unblock DMs
     * Unblocks direct messages to or from a specific User by their ID for the authenticated user.
     * @param id The ID of the target User that the authenticated user requesting to unblock dms for.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unblockDms(
    id: string,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersUnblockDmsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/dm/unblock`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersUnblockDmsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Reposted by
     * Retrieves a list of Users who reposted a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getPostsRepostedBy(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetPostsRepostedByResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/tweets/{id}/retweeted_by`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetPostsRepostedByResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get User by ID
     * Retrieves details of a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getById(
    id: string,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetByIdResponse>> {
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/{id}`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Users by usernames
     * Retrieves details of multiple Users by their usernames.
     * @param usernames A list of usernames, comma-separated.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByUsernames(
    usernames: Array<any>,
    tweetfields?: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<UsersGetByUsernamesResponse>> {
    const params = new URLSearchParams();

    if (usernames !== undefined) {
      params.set('usernames', String(usernames));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/users/by`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsersGetByUsernamesResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
