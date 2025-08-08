/**
 * Users client for the X API.
 *
 * This module provides a client for interacting with the Users endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  UsersUnfollowResponse,
  UsersUnblockDmsResponse,
  UsersGetBlockingResponse,
  UsersGetByUsernameResponse,
  UsersGetByIdsResponse,
  UsersGetByUsernamesResponse,
  UsersGetByIdResponse,
  UsersUnmuteResponse,
  UsersGetMutingResponse,
  UsersMuteRequest,
  UsersMuteResponse,
  UsersGetFollowersResponse,
  UsersGetMyResponse,
  UsersSearchResponse,
  UsersGetFollowingResponse,
  UsersFollowRequest,
  UsersFollowResponse,
  UsersGetPostsLikingResponse,
  UsersGetListsMembersResponse,
  UsersGetListsFollowersResponse,
  UsersGetPostsRepostedByResponse,
  UsersGetRepostsOfMeResponse,
  UsersBlockDmsResponse
} from "./models.js";

/**
 * Client for Users operations
 */
export class UsersClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Unfollow User
     * Causes the authenticated user to unfollow a specific user by their ID.
     * @param sourceUserId The ID of the authenticated source User that is requesting to unfollow the target User.
     * @param targetUserId The ID of the User that the source User is requesting to unfollow.* @returns UsersUnfollowResponse Response data
     */
  async unfollow(
    sourceUserId: string,
    targetUserId: string
  ): Promise<UsersUnfollowResponse> {
    let url =
      this.client.baseUrl +
      "/2/users/{source_user_id}/following/{target_user_id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{source_user_id}", String(sourceUserId));

    url = url.replace("{target_user_id}", String(targetUserId));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "DELETE",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersUnfollowResponse;
  }

  /**
     * Unblock DMs
     * Unblocks direct messages to or from a specific User by their ID for the authenticated user.
     * @param id The ID of the target User that the authenticated user requesting to unblock dms for.* @returns UsersUnblockDmsResponse Response data
     */
  async unblockDms(id: string): Promise<UsersUnblockDmsResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/dm/unblock";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersUnblockDmsResponse;
  }

  /**
     * Get blocking
     * Retrieves a list of Users blocked by the specified User ID.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetBlockingResponse Response data
     */
  async getBlocking(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetBlockingResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/blocking";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetBlockingResponse;
  }

  /**
     * Get User by username
     * Retrieves details of a specific User by their username.
     * @param username A username.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetByUsernameResponse Response data
     */
  async getByUsername(
    username: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetByUsernameResponse> {
    let url = this.client.baseUrl + "/2/users/by/username/{username}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{username}", String(username));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetByUsernameResponse;
  }

  /**
     * Get Users by IDs
     * Retrieves details of multiple Users by their IDs.
     * @param ids A list of User IDs, comma-separated. You can specify up to 100 IDs.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetByIdsResponse Response data
     */
  async getByIds(
    ids: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetByIdsResponse> {
    let url = this.client.baseUrl + "/2/users";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.set("ids", ids.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetByIdsResponse;
  }

  /**
     * Get Users by usernames
     * Retrieves details of multiple Users by their usernames.
     * @param usernames A list of usernames, comma-separated.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetByUsernamesResponse Response data
     */
  async getByUsernames(
    usernames: Array<any>,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetByUsernamesResponse> {
    let url = this.client.baseUrl + "/2/users/by";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (usernames !== undefined) {
      params.set("usernames", usernames.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetByUsernamesResponse;
  }

  /**
     * Get User by ID
     * Retrieves details of a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetByIdResponse Response data
     */
  async getById(
    id: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetByIdResponse> {
    let url = this.client.baseUrl + "/2/users/{id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetByIdResponse;
  }

  /**
     * Unmute User
     * Causes the authenticated user to unmute a specific user by their ID.
     * @param sourceUserId The ID of the authenticated source User that is requesting to unmute the target User.
     * @param targetUserId The ID of the User that the source User is requesting to unmute.* @returns UsersUnmuteResponse Response data
     */
  async unmute(
    sourceUserId: string,
    targetUserId: string
  ): Promise<UsersUnmuteResponse> {
    let url =
      this.client.baseUrl + "/2/users/{source_user_id}/muting/{target_user_id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{source_user_id}", String(sourceUserId));

    url = url.replace("{target_user_id}", String(targetUserId));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "DELETE",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersUnmuteResponse;
  }

  /**
     * Get muting
     * Retrieves a list of Users muted by the authenticated user.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetMutingResponse Response data
     */
  async getMuting(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetMutingResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/muting";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetMutingResponse;
  }

  /**
     * Mute User
     * Causes the authenticated user to mute a specific User by their ID.
     * @param id The ID of the authenticated source User that is requesting to mute the target User.* @param body Request body* @returns UsersMuteResponse Response data
     */
  async mute(id: string, body?: UsersMuteRequest): Promise<UsersMuteResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/muting";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersMuteResponse;
  }

  /**
     * Get followers
     * Retrieves a list of Users who follow a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetFollowersResponse Response data
     */
  async getFollowers(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetFollowersResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/followers";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetFollowersResponse;
  }

  /**
     * Get my User
     * Retrieves details of the authenticated user.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetMyResponse Response data
     */
  async getMy(
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetMyResponse> {
    let url = this.client.baseUrl + "/2/users/me";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetMyResponse;
  }

  /**
     * Search Users
     * Retrieves a list of Users matching a search query.
     * @param query TThe the query string by which to query for users.
     * @param maxResults The maximum number of results.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersSearchResponse Response data
     */
  async search(
    query: string,
    maxResults?: number,
    nextToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersSearchResponse> {
    let url = this.client.baseUrl + "/2/users/search";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.set("query", String(query));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (nextToken !== undefined) {
      params.set("next_token", String(nextToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersSearchResponse;
  }

  /**
     * Get following
     * Retrieves a list of Users followed by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetFollowingResponse Response data
     */
  async getFollowing(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetFollowingResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/following";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetFollowingResponse;
  }

  /**
     * Follow User
     * Causes the authenticated user to follow a specific user by their ID.
     * @param id The ID of the authenticated source User that is requesting to follow the target User.* @param body Request body* @returns UsersFollowResponse Response data
     */
  async follow(
    id: string,
    body?: UsersFollowRequest
  ): Promise<UsersFollowResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/following";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersFollowResponse;
  }

  /**
     * Get Liking Users
     * Retrieves a list of Users who liked a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetPostsLikingResponse Response data
     */
  async getPostsLiking(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetPostsLikingResponse> {
    let url = this.client.baseUrl + "/2/tweets/{id}/liking_users";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetPostsLikingResponse;
  }

  /**
     * Get List members
     * Retrieves a list of Users who are members of a specific List by its ID.
     * @param id The ID of the List.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetListsMembersResponse Response data
     */
  async getListsMembers(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetListsMembersResponse> {
    let url = this.client.baseUrl + "/2/lists/{id}/members";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetListsMembersResponse;
  }

  /**
     * Get List followers
     * Retrieves a list of Users who follow a specific List by its ID.
     * @param id The ID of the List.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetListsFollowersResponse Response data
     */
  async getListsFollowers(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetListsFollowersResponse> {
    let url = this.client.baseUrl + "/2/lists/{id}/followers";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetListsFollowersResponse;
  }

  /**
     * Get Reposted by
     * Retrieves a list of Users who reposted a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns UsersGetPostsRepostedByResponse Response data
     */
  async getPostsRepostedBy(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<UsersGetPostsRepostedByResponse> {
    let url = this.client.baseUrl + "/2/tweets/{id}/retweeted_by";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetPostsRepostedByResponse;
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
     * @param placefields A comma separated list of Place fields to display.* @returns UsersGetRepostsOfMeResponse Response data
     */
  async getRepostsOfMe(
    maxResults?: number,
    paginationToken?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<UsersGetRepostsOfMeResponse> {
    let url = this.client.baseUrl + "/2/users/reposts_of_me";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (pollfields !== undefined) {
      params.set("poll.fields", pollfields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (placefields !== undefined) {
      params.set("place.fields", placefields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersGetRepostsOfMeResponse;
  }

  /**
     * Block DMs
     * Blocks direct messages to or from a specific User by their ID for the authenticated user.
     * @param id The ID of the target User that the authenticated user requesting to block dms for.* @returns UsersBlockDmsResponse Response data
     */
  async blockDms(id: string): Promise<UsersBlockDmsResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/dm/block";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as UsersBlockDmsResponse;
  }
}
