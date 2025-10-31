/**
 * general client for the X API.
 *
 * This module provides a client for interacting with the general endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import { GetOpenApiSpecResponse } from './models.js';

/**
 * Client for general operations
 * 
 * This client provides methods for interacting with the general endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all general related operations.
 * 
 * @category general
 */
export class GeneralClient {
  private client: Client;

  /**
     * Creates a new general client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get OpenAPI Spec.
   * Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getOpenApiSpec(): Promise<GetOpenApiSpecResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/openapi.json';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetOpenApiSpecResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
