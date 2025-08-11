/**
 * Usage client for the X API.
 *
 * This module provides a client for interacting with the Usage endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { UsageGetResponse } from './models.js';

/**
 * Client for Usage operations
 */
export class UsageClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get usage
     * Retrieves usage statistics for Posts over a specified number of days.
     * @param days The number of days for which you need usage for.
     * @param usagefields A comma separated list of Usage fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async get(options?: RequestOptions): Promise<ApiResponse<UsageGetResponse>> {
    const params = new URLSearchParams();

    const path = `/2/usage/tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<UsageGetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
