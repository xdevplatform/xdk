/**
 * Communities client for the X API.
 *
 * This module provides a client for interacting with the Communities endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  CommunitiesGetByIdResponse,
  CommunitiesSearchResponse,
} from './models.js';

/**
 * Client for Communities operations
 */
export class CommunitiesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Community by ID
     * Retrieves details of a specific Community by its ID.
     * @param id The ID of the Community.
     * @param communityfields A comma separated list of Community fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getById(
    options?: RequestOptions
  ): Promise<ApiResponse<CommunitiesGetByIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/communities/{id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<CommunitiesGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Search Communities
     * Retrieves a list of Communities matching the specified search query.
     * @param query Query to search communities.
     * @param maxResults The maximum number of search results to be returned by a request.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param communityfields A comma separated list of Community fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async search(
    options?: RequestOptions
  ): Promise<ApiResponse<CommunitiesSearchResponse>> {
    const params = new URLSearchParams();

    const path = `/2/communities/search`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<CommunitiesSearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
