/**
 * activity client for the X API.
 *
 * This module provides a client for interacting with the activity endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  UpdateSubscriptionRequest,
  UpdateSubscriptionResponse,
  DeleteSubscriptionResponse,
  GetSubscriptionsResponse,
  CreateSubscriptionRequest,
  CreateSubscriptionResponse,
  StreamResponse,
} from './models.js';

/**
 * Options for updateSubscription method
 */
export interface UpdateSubscriptionOptions {
  /** Request body */
  body?: UpdateSubscriptionRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createSubscription method
 */
export interface CreateSubscriptionOptions {
  /** Request body */
  body?: CreateSubscriptionRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for stream method
 */
export interface StreamOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for activity operations
 * 
 * This client provides methods for interacting with the activity endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all activity related operations.
 * 
 * @category activity
 */
export class ActivityClient {
  private client: Client;

  /**
     * Creates a new activity client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Update X activity subscription
   * Updates a subscription for an X activity event




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async updateSubscription(
    options: UpdateSubscriptionOptions = {}
  ): Promise<UpdateSubscriptionResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/activity/subscriptions/{subscription_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<UpdateSubscriptionResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Deletes X activity subscription
   * Deletes a subscription for an X activity event




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubscription(): Promise<DeleteSubscriptionResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/activity/subscriptions/{subscription_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DeleteSubscriptionResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get X activity subscriptions
   * Get a list of active subscriptions for XAA


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptions(): Promise<GetSubscriptionsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/activity/subscriptions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetSubscriptionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create X activity subscription
   * Creates a subscription for an X activity event


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createSubscription(
    options: CreateSubscriptionOptions = {}
  ): Promise<CreateSubscriptionResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/activity/subscriptions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CreateSubscriptionResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Activity Stream
   * Stream of X Activities


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async stream(options: StreamOptions = {}): Promise<StreamResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/activity/stream';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<StreamResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
