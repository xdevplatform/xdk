/**
 * Spaces client for the X API.
 *
 * This module provides a client for interacting with the Spaces endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  SpacesGetByCreatorIdsResponse,
  SpacesGetPostsResponse,
  SpacesGetByIdResponse,
  SpacesGetBuyersResponse,
  SpacesGetByIdsResponse,
  SpacesSearchResponse
} from "./models.js";

/**
 * Client for Spaces operations
 */
export class SpacesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Spaces by creator IDs
     * Retrieves details of Spaces created by specified User IDs.
     * @param userIds The IDs of Users to search through.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @returns SpacesGetByCreatorIdsResponse Response data
     */
  async getByCreatorIds(
    userIds: Array<any>,
    spacefields?: Array<any>,
    expansions?: Array<any>,
    userfields?: Array<any>,
    topicfields?: Array<any>
  ): Promise<SpacesGetByCreatorIdsResponse> {
    let url = this.client.baseUrl + "/2/spaces/by/creator_ids";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (userIds !== undefined) {
      params.set("user_ids", userIds.map(String).join(","));
    }

    if (spacefields !== undefined) {
      params.set("space.fields", spacefields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (topicfields !== undefined) {
      params.set("topic.fields", topicfields.map(String).join(","));
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

    return responseData as SpacesGetByCreatorIdsResponse;
  }

  /**
     * Get Space Posts
     * Retrieves a list of Posts shared in a specific Space by its ID.
     * @param id The ID of the Space to be retrieved.
     * @param maxResults The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns SpacesGetPostsResponse Response data
     */
  async getPosts(
    id: string,
    maxResults?: number,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<SpacesGetPostsResponse> {
    let url = this.client.baseUrl + "/2/spaces/{id}/tweets";

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

    return responseData as SpacesGetPostsResponse;
  }

  /**
     * Get space by ID
     * Retrieves details of a specific space by its ID.
     * @param id The ID of the Space to be retrieved.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @returns SpacesGetByIdResponse Response data
     */
  async getById(
    id: string,
    spacefields?: Array<any>,
    expansions?: Array<any>,
    userfields?: Array<any>,
    topicfields?: Array<any>
  ): Promise<SpacesGetByIdResponse> {
    let url = this.client.baseUrl + "/2/spaces/{id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (spacefields !== undefined) {
      params.set("space.fields", spacefields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (topicfields !== undefined) {
      params.set("topic.fields", topicfields.map(String).join(","));
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

    return responseData as SpacesGetByIdResponse;
  }

  /**
     * Get Space ticket buyers
     * Retrieves a list of Users who purchased tickets to a specific Space by its ID.
     * @param id The ID of the Space to be retrieved.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param maxResults The maximum number of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns SpacesGetBuyersResponse Response data
     */
  async getBuyers(
    id: string,
    paginationToken?: string,
    maxResults?: number,
    userfields?: Array<any>,
    expansions?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<SpacesGetBuyersResponse> {
    let url = this.client.baseUrl + "/2/spaces/{id}/buyers";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
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

    return responseData as SpacesGetBuyersResponse;
  }

  /**
     * Get Spaces by IDs
     * Retrieves details of multiple Spaces by their IDs.
     * @param ids The list of Space IDs to return.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @returns SpacesGetByIdsResponse Response data
     */
  async getByIds(
    ids: Array<any>,
    spacefields?: Array<any>,
    expansions?: Array<any>,
    userfields?: Array<any>,
    topicfields?: Array<any>
  ): Promise<SpacesGetByIdsResponse> {
    let url = this.client.baseUrl + "/2/spaces";

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

    if (spacefields !== undefined) {
      params.set("space.fields", spacefields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (topicfields !== undefined) {
      params.set("topic.fields", topicfields.map(String).join(","));
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

    return responseData as SpacesGetByIdsResponse;
  }

  /**
     * Search Spaces
     * Retrieves a list of Spaces matching the specified search query.
     * @param query The search query.
     * @param state The state of Spaces to search for.
     * @param maxResults The number of results to return.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @returns SpacesSearchResponse Response data
     */
  async search(
    query: string,
    state?: string,
    maxResults?: number,
    spacefields?: Array<any>,
    expansions?: Array<any>,
    userfields?: Array<any>,
    topicfields?: Array<any>
  ): Promise<SpacesSearchResponse> {
    let url = this.client.baseUrl + "/2/spaces/search";

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

    if (state !== undefined) {
      params.set("state", String(state));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (spacefields !== undefined) {
      params.set("space.fields", spacefields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (topicfields !== undefined) {
      params.set("topic.fields", topicfields.map(String).join(","));
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

    return responseData as SpacesSearchResponse;
  }
}
