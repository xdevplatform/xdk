/**
 * Usage client for the X API.
 *
 * This module provides a client for interacting with the Usage endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  TwitterPaginator,
  TweetPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import { UsageGetResponse } from './models.js';

/**
 * Options for get method
 */
export interface UsageGetOptions {
  /** The number of days for which you need usage for. */
  days?: number;

  /** A comma separated list of Usage fields to display. */
  usagefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

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
   * Retrieves usage statistics for Posts over a specified number of days.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async get(options: UsageGetOptions = {}): Promise<UsageGetResponse> {
    // Destructure options

    const {
      days = undefined,

      usagefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/usage/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    if (days !== undefined) {
      params.append('days', String(days));
    }

    if (usagefields !== undefined) {
      usagefields.forEach(item => params.append('usage.fields', String(item)));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<UsageGetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
