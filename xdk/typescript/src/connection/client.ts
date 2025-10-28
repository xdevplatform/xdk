/**
 * Connection client for the X API.
 *
 * This module provides a client for interacting with the Connection endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import { ConnectionDeleteAllResponse } from './models.js';

/**
 * Client for Connection operations
 * 
 * This client provides methods for interacting with the Connection endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Connection related operations.
 * 
 * @category Connection
 */
export class ConnectionClient {
  private client: Client;

  /**
     * Creates a new Connection client instance
     * 
     * @param client - The main X API client instance
     */
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
