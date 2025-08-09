/**
 * General client for the X API.
 *
 * This module provides a client for interacting with the General endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
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
     * Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)* @param options Additional request options
     * @returns Promise with the API response
     */
  async getOpenApiSpec(
    options?: RequestOptions
  ): Promise<ApiResponse<GeneralGetOpenApiSpecResponse>> {
    const params = new URLSearchParams();

    const path = `/2/openapi.json`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<GeneralGetOpenApiSpecResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
