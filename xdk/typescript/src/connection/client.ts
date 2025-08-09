/**
 * Connection client for the X API.
 *
 * This module provides a client for interacting with the Connection endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { ConnectionDeleteAllResponse } from './models.js';

/**
 * Client for Connection operations
 */
export class ConnectionClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Terminate all connections
     * Terminates all active streaming connections for the authenticated application.* @param options Additional request options
     * @returns Promise with the API response
     */
  async deleteAll(
    options?: RequestOptions
  ): Promise<ApiResponse<ConnectionDeleteAllResponse>> {
    const params = new URLSearchParams();

    const path = `/2/connections/all`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ConnectionDeleteAllResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
