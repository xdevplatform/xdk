/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import { GetResponse } from './models.js';

/**
 * Options for get method
 */
export interface GetStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class UsageClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get usage
     * Retrieves usage statistics for Posts over a specified number of days.
     * 
     * @returns Promise with the API response
     */
  async get(options: GetStreamingOptions = {}): Promise<GetResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'get');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/usage/tweets`;

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
    return this.client.request<GetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
