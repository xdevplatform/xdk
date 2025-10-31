/**
 * usage client for the X API.
 *
 * This module provides a client for interacting with the usage endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import { GetResponse } from './models.js';

/**
 * Options for get method
 * 
 * @public
 */
export interface GetOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for usage operations
 * 
 * This client provides methods for interacting with the usage endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all usage related operations.
 * 
 * @category usage
 */
export class UsageClient {
  private client: Client;

  /**
     * Creates a new usage client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get usage
   * Retrieves usage statistics for Posts over a specified number of days.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async get(options: GetOptions = {}): Promise<GetResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/usage/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
