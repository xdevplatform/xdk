/**
 * General client for the X API.
 *
 * This module provides a client for interacting with the General endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  TwitterPaginator,
  TweetPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import { GeneralGetOpenApiSpecResponse } from './models.js';

/**
 * Client for General operations
 */
export class GeneralClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get OpenAPI Spec.
   * Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getOpenApiSpec(): Promise<GeneralGetOpenApiSpecResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/openapi.json';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GeneralGetOpenApiSpecResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
