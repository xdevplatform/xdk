/**
 * Community notes client for the X API.
 *
 * This module provides a client for interacting with the Community notes endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  CommunityNotesSearchForEligiblePostsResponse,
  CommunityNotesDeleteNotesResponse,
  CommunityNotesSearchNotesWrittenResponse,
  CommunityNotesCreateNotesRequest,
  CommunityNotesCreateNotesResponse
} from "./models.js";

/**
 * Client for Community notes operations
 */
export class CommunityNotesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Search for Posts Eligible for Community Notes
     * Returns all the posts that are eligible for community notes.
     * @param testMode If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.
     * @param paginationToken Pagination token to get next set of posts eligible for notes.
     * @param maxResults Max results to return.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @returns CommunityNotesSearchForEligiblePostsResponse Response data
     */
  async searchForEligiblePosts(
    testMode: boolean,
    paginationToken?: string,
    maxResults?: number,
    tweetfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    pollfields?: Array<any>,
    userfields?: Array<any>,
    placefields?: Array<any>
  ): Promise<CommunityNotesSearchForEligiblePostsResponse> {
    let url = this.client.baseUrl + "/2/notes/search/posts_eligible_for_notes";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (testMode !== undefined) {
      params.set("test_mode", String(testMode));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

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

    return responseData as CommunityNotesSearchForEligiblePostsResponse;
  }

  /**
     * Delete a Community Note
     * Deletes a community note.
     * @param id The community note id to delete.* @returns CommunityNotesDeleteNotesResponse Response data
     */
  async deleteNotes(id: string): Promise<CommunityNotesDeleteNotesResponse> {
    let url = this.client.baseUrl + "/2/notes/{id}";

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

    return responseData as CommunityNotesDeleteNotesResponse;
  }

  /**
     * Search for Community Notes Written
     * Returns all the community notes written by the user.
     * @param testMode If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.
     * @param paginationToken Pagination token to get next set of posts eligible for notes.
     * @param maxResults Max results to return.
     * @param notefields A comma separated list of Note fields to display.* @returns CommunityNotesSearchNotesWrittenResponse Response data
     */
  async searchNotesWritten(
    testMode: boolean,
    paginationToken?: string,
    maxResults?: number,
    notefields?: Array<any>
  ): Promise<CommunityNotesSearchNotesWrittenResponse> {
    let url = this.client.baseUrl + "/2/notes/search/notes_written";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (testMode !== undefined) {
      params.set("test_mode", String(testMode));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (notefields !== undefined) {
      params.set("note.fields", notefields.map(String).join(","));
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

    return responseData as CommunityNotesSearchNotesWrittenResponse;
  }

  /**
     * Create a Community Note
     * Creates a community note endpoint for LLM use case.* @param body Request body* @returns CommunityNotesCreateNotesResponse Response data
     */
  async createNotes(
    body?: CommunityNotesCreateNotesRequest
  ): Promise<CommunityNotesCreateNotesResponse> {
    let url = this.client.baseUrl + "/2/notes";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

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

    return responseData as CommunityNotesCreateNotesResponse;
  }
}
