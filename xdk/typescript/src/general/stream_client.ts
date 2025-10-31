/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import { GetOpenApiSpecResponse } from './models.js';

/**
 * Options for getOpenApiSpec method
 */
export interface GetOpenApiSpecStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class GeneralClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get OpenAPI Spec.
     * Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
     * 
     * @returns Promise with the API response
     */
  async getOpenApiSpec(
    options: GetOpenApiSpecStreamingOptions = {}
  ): Promise<GetOpenApiSpecResponse> {
    // Validate authentication requirements

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/openapi.json`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetOpenApiSpecResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
