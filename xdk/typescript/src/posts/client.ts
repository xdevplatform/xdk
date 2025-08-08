/**
 * Posts client for the X API.
 *
 * This module provides a client for interacting with the Posts endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  PostsGetByIdsResponse,
  PostsCreateRequest,
  PostsCreateResponse,
  PostsUnrepostResponse,
  PostsGetUsersResponse,
  PostsGetUsersLikedResponse,
  PostsGetByIdResponse,
  PostsDeleteResponse,
  PostsLikeRequest,
  PostsLikeResponse,
  PostsGetRepostsResponse,
  PostsRepostRequest,
  PostsRepostResponse,
  PostsGetAnalyticsResponse,
  PostsGetUsersTimelineResponse,
  PostsUnlikeResponse,
  PostsGetInsightsHistoricalResponse,
  PostsSearchAllResponse,
  PostsGetCountsRecentResponse,
  PostsGetQuotedPostsResponse,
  PostsGetListsResponse,
  PostsGetUsersMentionsResponse,
  PostsGetCountsAllResponse,
  PostsSearchRecentResponse,
  PostsHideReplyRequest,
  PostsHideReplyResponse,
  PostsGetInsights28HrResponse
} from "./models.js";

/**
 * Client for Posts operations
 */
export class PostsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Posts by IDs
     * Retrieves details of multiple Posts by their IDs.
     * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetByIdsResponse Response data
     */
  async getByIds(
    ids: Array<any>,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetByIdsResponse> {
    let url = this.client.baseUrl + "/2/tweets";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
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

    const headers = new Headers();

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

    return responseData as PostsGetByIdsResponse;
  }

  /**
     * Create Post
     * Creates a new Post for the authenticated user.* @param body Request body* @returns PostsCreateResponse Response data
     */
  async create(body: PostsCreateRequest): Promise<Record<string, any>> {
    let url = this.client.baseUrl + "/2/tweets";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    const headers = new Headers();

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

    return responseData as PostsCreateResponse;
  }

  /**
     * Unrepost Post
     * Causes the authenticated user to unrepost a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to repost the Post.
     * @param sourceTweetId The ID of the Post that the User is requesting to unretweet.* @returns PostsUnrepostResponse Response data
     */
  async unrepost(
    id: string,
    sourceTweetId: string
  ): Promise<PostsUnrepostResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/retweets/{source_tweet_id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    url = url.replace("{source_tweet_id}", String(sourceTweetId));

    const headers = new Headers();

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

    return responseData as PostsUnrepostResponse;
  }

  /**
     * Get Posts
     * Retrieves a list of posts authored by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param sinceId The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
     * @param untilId The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param exclude The set of entities to exclude (e.g. 'replies' or 'retweets').
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetUsersResponse Response data
     */
  async getUsers(
    id: string,
    sinceId?: string,
    untilId?: string,
    maxResults?: number,
    paginationToken?: string,
    exclude?: Array<any>,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetUsersResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/tweets";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (exclude !== undefined) {
      params.set("exclude", exclude.map(String).join(","));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetUsersResponse;
  }

  /**
     * Get liked Posts
     * Retrieves a list of Posts liked by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetUsersLikedResponse Response data
     */
  async getUsersLiked(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetUsersLikedResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/liked_tweets";

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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetUsersLikedResponse;
  }

  /**
     * Get Post by ID
     * Retrieves details of a specific Post by its ID.
     * @param id A single Post ID.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetByIdResponse Response data
     */
  async getById(
    id: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetByIdResponse> {
    let url = this.client.baseUrl + "/2/tweets/{id}";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetByIdResponse;
  }

  /**
     * Delete Post
     * Deletes a specific Post by its ID, if owned by the authenticated user.
     * @param id The ID of the Post to be deleted.* @returns PostsDeleteResponse Response data
     */
  async delete(id: string): Promise<PostsDeleteResponse> {
    let url = this.client.baseUrl + "/2/tweets/{id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsDeleteResponse;
  }

  /**
     * Like Post
     * Causes the authenticated user to Like a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to like the Post.* @param body Request body* @returns PostsLikeResponse Response data
     */
  async like(id: string, body?: PostsLikeRequest): Promise<PostsLikeResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/likes";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsLikeResponse;
  }

  /**
     * Get Reposts
     * Retrieves a list of Posts that repost a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetRepostsResponse Response data
     */
  async getReposts(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetRepostsResponse> {
    let url = this.client.baseUrl + "/2/tweets/{id}/retweets";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetRepostsResponse;
  }

  /**
     * Repost Post
     * Causes the authenticated user to repost a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to repost the Post.* @param body Request body* @returns PostsRepostResponse Response data
     */
  async repost(
    id: string,
    body?: PostsRepostRequest
  ): Promise<PostsRepostResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/retweets";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsRepostResponse;
  }

  /**
     * Get Post analytics
     * Retrieves analytics data for specified Posts within a defined time range.
     * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
     * @param granularity The granularity for the search counts results.
     * @param analyticsfields A comma separated list of Analytics fields to display.* @returns PostsGetAnalyticsResponse Response data
     */
  async getAnalytics(
    ids: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    analyticsfields?: Array<any>
  ): Promise<PostsGetAnalyticsResponse> {
    let url = this.client.baseUrl + "/2/tweets/analytics";

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

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (granularity !== undefined) {
      params.set("granularity", String(granularity));
    }

    if (analyticsfields !== undefined) {
      params.set("analytics.fields", analyticsfields.map(String).join(","));
    }

    const headers = new Headers();

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

    return responseData as PostsGetAnalyticsResponse;
  }

  /**
     * Get Timeline
     * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
     * @param id The ID of the authenticated source User to list Reverse Chronological Timeline Posts of.
     * @param sinceId The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
     * @param untilId The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param exclude The set of entities to exclude (e.g. 'replies' or 'retweets').
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetUsersTimelineResponse Response data
     */
  async getUsersTimeline(
    id: string,
    sinceId?: string,
    untilId?: string,
    maxResults?: number,
    paginationToken?: string,
    exclude?: Array<any>,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetUsersTimelineResponse> {
    let url =
      this.client.baseUrl + "/2/users/{id}/timelines/reverse_chronological";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (exclude !== undefined) {
      params.set("exclude", exclude.map(String).join(","));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetUsersTimelineResponse;
  }

  /**
     * Unlike Post
     * Causes the authenticated user to Unlike a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to unlike the Post.
     * @param tweetId The ID of the Post that the User is requesting to unlike.* @returns PostsUnlikeResponse Response data
     */
  async unlike(id: string, tweetId: string): Promise<PostsUnlikeResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/likes/{tweet_id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    url = url.replace("{tweet_id}", String(tweetId));

    const headers = new Headers();

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

    return responseData as PostsUnlikeResponse;
  }

  /**
     * Get historical Post insights
     * Retrieves historical engagement metrics for specified Posts within a defined time range.
     * @param tweetIds List of PostIds for historical metrics.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
     * @param granularity granularity of metrics response.
     * @param requestedMetrics request metrics for historical request.
     * @param engagementfields A comma separated list of Engagement fields to display.* @returns PostsGetInsightsHistoricalResponse Response data
     */
  async getInsightsHistorical(
    tweetIds: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    requestedMetrics: Array<any>,
    engagementfields?: Array<any>
  ): Promise<PostsGetInsightsHistoricalResponse> {
    let url = this.client.baseUrl + "/2/insights/historical";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (tweetIds !== undefined) {
      params.set("tweet_ids", tweetIds.map(String).join(","));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (granularity !== undefined) {
      params.set("granularity", String(granularity));
    }

    if (requestedMetrics !== undefined) {
      params.set("requested_metrics", requestedMetrics.map(String).join(","));
    }

    if (engagementfields !== undefined) {
      params.set("engagement.fields", engagementfields.map(String).join(","));
    }

    const headers = new Headers();

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

    return responseData as PostsGetInsightsHistoricalResponse;
  }

  /**
     * Search all Posts
     * Retrieves Posts from the full archive matching a search query.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param maxResults The maximum number of search results to be returned by a request.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param sortOrder This order in which to return results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsSearchAllResponse Response data
     */
  async searchAll(
    query: string,
    startTime?: string,
    endTime?: string,
    sinceId?: string,
    untilId?: string,
    maxResults?: number,
    nextToken?: string,
    paginationToken?: string,
    sortOrder?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsSearchAllResponse> {
    let url = this.client.baseUrl + "/2/tweets/search/all";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.set("query", String(query));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (nextToken !== undefined) {
      params.set("next_token", String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (sortOrder !== undefined) {
      params.set("sort_order", String(sortOrder));
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

    const headers = new Headers();

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

    return responseData as PostsSearchAllResponse;
  }

  /**
     * Get count of recent Posts
     * Retrieves the count of Posts from the last 7 days matching a search query.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param granularity The granularity for the search counts results.
     * @param searchCountfields A comma separated list of SearchCount fields to display.* @returns PostsGetCountsRecentResponse Response data
     */
  async getCountsRecent(
    query: string,
    startTime?: string,
    endTime?: string,
    sinceId?: string,
    untilId?: string,
    nextToken?: string,
    paginationToken?: string,
    granularity?: string,
    searchCountfields?: Array<any>
  ): Promise<PostsGetCountsRecentResponse> {
    let url = this.client.baseUrl + "/2/tweets/counts/recent";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.set("query", String(query));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (nextToken !== undefined) {
      params.set("next_token", String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (granularity !== undefined) {
      params.set("granularity", String(granularity));
    }

    if (searchCountfields !== undefined) {
      params.set(
        "search_count.fields",
        searchCountfields.map(String).join(",")
      );
    }

    const headers = new Headers();

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

    return responseData as PostsGetCountsRecentResponse;
  }

  /**
     * Get Quoted Posts
     * Retrieves a list of Posts that quote a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results to be returned.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param exclude The set of entities to exclude (e.g. 'replies' or 'retweets').
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetQuotedPostsResponse Response data
     */
  async getQuotedPosts(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    exclude?: Array<any>,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetQuotedPostsResponse> {
    let url = this.client.baseUrl + "/2/tweets/{id}/quote_tweets";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
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

    if (exclude !== undefined) {
      params.set("exclude", exclude.map(String).join(","));
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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetQuotedPostsResponse;
  }

  /**
     * Get List Posts
     * Retrieves a list of Posts associated with a specific List by its ID.
     * @param id The ID of the List.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetListsResponse Response data
     */
  async getLists(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetListsResponse> {
    let url = this.client.baseUrl + "/2/lists/{id}/tweets";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetListsResponse;
  }

  /**
     * Get mentions
     * Retrieves a list of Posts that mention a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param sinceId The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
     * @param untilId The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsGetUsersMentionsResponse Response data
     */
  async getUsersMentions(
    id: string,
    sinceId?: string,
    untilId?: string,
    maxResults?: number,
    paginationToken?: string,
    startTime?: string,
    endTime?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsGetUsersMentionsResponse> {
    let url = this.client.baseUrl + "/2/users/{id}/mentions";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
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

    url = url.replace("{id}", String(id));

    const headers = new Headers();

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

    return responseData as PostsGetUsersMentionsResponse;
  }

  /**
     * Get count of all Posts
     * Retrieves the count of Posts matching a search query from the full archive.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param granularity The granularity for the search counts results.
     * @param searchCountfields A comma separated list of SearchCount fields to display.* @returns PostsGetCountsAllResponse Response data
     */
  async getCountsAll(
    query: string,
    startTime?: string,
    endTime?: string,
    sinceId?: string,
    untilId?: string,
    nextToken?: string,
    paginationToken?: string,
    granularity?: string,
    searchCountfields?: Array<any>
  ): Promise<PostsGetCountsAllResponse> {
    let url = this.client.baseUrl + "/2/tweets/counts/all";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.set("query", String(query));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (nextToken !== undefined) {
      params.set("next_token", String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (granularity !== undefined) {
      params.set("granularity", String(granularity));
    }

    if (searchCountfields !== undefined) {
      params.set(
        "search_count.fields",
        searchCountfields.map(String).join(",")
      );
    }

    const headers = new Headers();

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

    return responseData as PostsGetCountsAllResponse;
  }

  /**
     * Search recent Posts
     * Retrieves Posts from the last 7 days matching a search query.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param maxResults The maximum number of search results to be returned by a request.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param sortOrder This order in which to return results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns PostsSearchRecentResponse Response data
     */
  async searchRecent(
    query: string,
    startTime?: string,
    endTime?: string,
    sinceId?: string,
    untilId?: string,
    maxResults?: number,
    nextToken?: string,
    paginationToken?: string,
    sortOrder?: string,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<PostsSearchRecentResponse> {
    let url = this.client.baseUrl + "/2/tweets/search/recent";

    if (this.client.bearerToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.bearerToken}`
      );
    } else if (this.client.accessToken) {
      this.client.headers.set(
        "Authorization",
        `Bearer ${this.client.accessToken}`
      );
    }
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

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (sinceId !== undefined) {
      params.set("since_id", String(sinceId));
    }

    if (untilId !== undefined) {
      params.set("until_id", String(untilId));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (nextToken !== undefined) {
      params.set("next_token", String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (sortOrder !== undefined) {
      params.set("sort_order", String(sortOrder));
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

    const headers = new Headers();

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

    return responseData as PostsSearchRecentResponse;
  }

  /**
     * Hide reply
     * Hides or unhides a reply to a conversation owned by the authenticated user.
     * @param tweetId The ID of the reply that you want to hide or unhide.* @param body Request body* @returns PostsHideReplyResponse Response data
     */
  async hideReply(
    tweetId: string,
    body?: PostsHideReplyRequest
  ): Promise<PostsHideReplyResponse> {
    let url = this.client.baseUrl + "/2/tweets/{tweet_id}/hidden";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{tweet_id}", String(tweetId));

    const headers = new Headers();

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "PUT",
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

    return responseData as PostsHideReplyResponse;
  }

  /**
     * Get 28-hour Post insights
     * Retrieves engagement metrics for specified Posts over the last 28 hours.
     * @param tweetIds List of PostIds for 28hr metrics.
     * @param granularity granularity of metrics response.
     * @param requestedMetrics request metrics for historical request.
     * @param engagementfields A comma separated list of Engagement fields to display.* @returns PostsGetInsights28HrResponse Response data
     */
  async getInsights28Hr(
    tweetIds: Array<any>,
    granularity: string,
    requestedMetrics: Array<any>,
    engagementfields?: Array<any>
  ): Promise<PostsGetInsights28HrResponse> {
    let url = this.client.baseUrl + "/2/insights/28hr";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (tweetIds !== undefined) {
      params.set("tweet_ids", tweetIds.map(String).join(","));
    }

    if (granularity !== undefined) {
      params.set("granularity", String(granularity));
    }

    if (requestedMetrics !== undefined) {
      params.set("requested_metrics", requestedMetrics.map(String).join(","));
    }

    if (engagementfields !== undefined) {
      params.set("engagement.fields", engagementfields.map(String).join(","));
    }

    const headers = new Headers();

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

    return responseData as PostsGetInsights28HrResponse;
  }
}
