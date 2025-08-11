/**
 * Community notes client for the X API.
 *
 * This module provides a client for interacting with the Community notes endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  CommunityNotesDeleteNotesResponse,
  CommunityNotesSearchNotesWrittenResponse,
  CommunityNotesSearchForEligiblePostsResponse,
  CommunityNotesCreateNotesRequest,
  CommunityNotesCreateNotesResponse,
} from './models.js';

/**
 * Client for Community notes operations
 */
export class CommunityNotesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Delete a Community Note
     * Deletes a community note.
     * @param id The community note id to delete.* @param options Additional request options
     * @returns Promise with the API response
     */
  async deleteNotes(
    options?: RequestOptions
  ): Promise<ApiResponse<CommunityNotesDeleteNotesResponse>> {
    const params = new URLSearchParams();

    const path = `/2/notes/{id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<CommunityNotesDeleteNotesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Search for Community Notes Written
     * Returns all the community notes written by the user.
     * @param testMode If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.
     * @param paginationToken Pagination token to get next set of posts eligible for notes.
     * @param maxResults Max results to return.
     * @param notefields A comma separated list of Note fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async searchNotesWritten(
    options?: RequestOptions
  ): Promise<ApiResponse<CommunityNotesSearchNotesWrittenResponse>> {
    const params = new URLSearchParams();

    const path = `/2/notes/search/notes_written`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<CommunityNotesSearchNotesWrittenResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
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
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async searchForEligiblePosts(
    options?: RequestOptions
  ): Promise<ApiResponse<CommunityNotesSearchForEligiblePostsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/notes/search/posts_eligible_for_notes`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<CommunityNotesSearchForEligiblePostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create a Community Note
     * Creates a community note endpoint for LLM use case.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createNotes(
    body?: CommunityNotesCreateNotesRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<CommunityNotesCreateNotesResponse>> {
    const params = new URLSearchParams();

    const path = `/2/notes`;

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

    return this.client.request<CommunityNotesCreateNotesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
