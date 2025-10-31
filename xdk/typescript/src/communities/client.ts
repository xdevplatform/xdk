/**
 * communities client for the X API.
 *
 * This module provides a client for interacting with the communities endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import { SearchResponse, GetByIdResponse } from './models.js';

/**
 * Options for search method
 */
export interface SearchOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for communities operations
 * 
 * This client provides methods for interacting with the communities endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all communities related operations.
 * 
 * @category communities
 */
export class CommunitiesClient {
  private client: Client;

  /**
     * Creates a new communities client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Search Communities
   * Retrieves a list of Communities matching the specified search query.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async search(options: SearchOptions = {}): Promise<SearchResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/communities/search';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Community by ID
   * Retrieves details of a specific Community by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(): Promise<GetByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/communities/{id}';

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
}
