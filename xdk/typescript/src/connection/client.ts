/**
 * Connection client for the X API.
 *
 * This module provides a client for interacting with the Connection endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  TwitterPaginator,
  TweetPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
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
   * Terminates all active streaming connections for the authenticated application.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteAll(): Promise<ConnectionDeleteAllResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/connections/all';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<ConnectionDeleteAllResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
