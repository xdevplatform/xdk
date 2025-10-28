/**
 * Activity client for the X API.
 *
 * This module provides a client for interacting with the Activity endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import {
  ActivityStreamResponse,
  ActivityUpdateSubscriptionRequest,
  ActivityUpdateSubscriptionResponse,
  ActivityDeleteSubscriptionResponse,
  ActivityGetSubscriptionsResponse,
  ActivityCreateSubscriptionRequest,
  ActivityCreateSubscriptionResponse,
} from './models.js';

/**
 * Options for stream method
 */
export interface ActivityStreamOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided. */
  endTime?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for updateSubscription method
 */
export interface ActivityUpdateSubscriptionOptions {
  /** Request body */
  body?: ActivityUpdateSubscriptionRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createSubscription method
 */
export interface ActivityCreateSubscriptionOptions {
  /** Request body */
  body?: ActivityCreateSubscriptionRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Activity operations
 * 
 * This client provides methods for interacting with the Activity endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Activity related operations.
 * 
 * @category Activity
 */
export class ActivityClient {
  private client: Client;

  /**
     * Creates a new Activity client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Activity Stream
   * Stream of X Activities* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async stream(
    options: ActivityStreamOptions = {}
  ): Promise<ActivityStreamResponse> {
    // Destructure options

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/activity/stream';

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<ActivityStreamResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Update X activity subscription
   * Updates a subscription for an X activity event
   * @param subscriptionId The ID of the subscription to update.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async updateSubscription(
    subscriptionId: string,
    options: ActivityUpdateSubscriptionOptions = {}
  ): Promise<ActivityUpdateSubscriptionResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/activity/subscriptions/{subscription_id}';

    path = path.replace(
      '{subscription_id}',
      encodeURIComponent(String(subscriptionId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<ActivityUpdateSubscriptionResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Deletes X activity subscription
   * Deletes a subscription for an X activity event
   * @param subscriptionId The ID of the subscription to delete.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubscription(
    subscriptionId: string
  ): Promise<ActivityDeleteSubscriptionResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/activity/subscriptions/{subscription_id}';

    path = path.replace(
      '{subscription_id}',
      encodeURIComponent(String(subscriptionId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<ActivityDeleteSubscriptionResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get X activity subscriptions
   * Get a list of active subscriptions for XAA* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptions(): Promise<ActivityGetSubscriptionsResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/activity/subscriptions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<ActivityGetSubscriptionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create X activity subscription
   * Creates a subscription for an X activity event* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createSubscription(
    options: ActivityCreateSubscriptionOptions = {}
  ): Promise<ActivityCreateSubscriptionResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/activity/subscriptions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<ActivityCreateSubscriptionResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
