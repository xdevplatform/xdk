/**
 * trends client for the X API.
 *
 * This module provides a client for interacting with the trends endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import { GetPersonalizedResponse, GetByWoeidResponse } from './models.js';

/**
 * Options for getByWoeid method
 * 
 * @public
 */
export interface GetByWoeidOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for trends operations
 * 
 * This client provides methods for interacting with the trends endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all trends related operations.
 * 
 * @category trends
 */
export class TrendsClient {
  private client: Client;

  /**
     * Creates a new trends client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get personalized Trends
   * Retrieves personalized trending topics for the authenticated user.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPersonalized(): Promise<GetPersonalizedResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/users/personalized_trends';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetPersonalizedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Trends by WOEID
   * Retrieves trending topics for a specific location identified by its WOEID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByWoeid(
    options: GetByWoeidOptions = {}
  ): Promise<GetByWoeidResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/trends/by/woeid/{woeid}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetByWoeidResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
