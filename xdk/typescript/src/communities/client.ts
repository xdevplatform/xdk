/**
 * Communities client for the X API.
 *
 * This module provides a client for interacting with the Communities endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  CommunitiesSearchResponse,
  CommunitiesGetByIdResponse,
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
    query: string,
    communityfields?: Array<any>,
    paginationToken?: string,
    nextToken?: string,
    maxResults?: number,
    options?: RequestOptions
  ): Promise<ApiResponse<CommunitiesSearchResponse>> {
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

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (communityfields !== undefined) {
      params.set('community.fields', String(communityfields));
    }

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

  /**
     * Get Community by ID
     * Retrieves details of a specific Community by its ID.
     * @param id The ID of the Community.
     * @param communityfields A comma separated list of Community fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getById(
    id: string,
    communityfields?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<CommunitiesGetByIdResponse>> {
    const params = new URLSearchParams();

    if (communityfields !== undefined) {
      params.set('community.fields', String(communityfields));
    }

    const path = `/2/communities/{id}`.replace('{id}', String(id));

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
}
