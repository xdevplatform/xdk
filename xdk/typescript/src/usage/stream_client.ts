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
 * 
 * @public
 */
export interface GetStreamingOptions {
  /** The number of days for which you need usage for. */
  days?: number;

  /** A comma separated list of Usage fields to display. */
  usagefields?: Array<any>;

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

    // Destructure options (exclude path parameters, they're already function params)

    const {
      days = undefined,

      usagefields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/usage/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    if (days !== undefined) {
      params.append('days', String(days));
    }

    if (usagefields !== undefined) {
      params.append('usage.fields', usagefields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
