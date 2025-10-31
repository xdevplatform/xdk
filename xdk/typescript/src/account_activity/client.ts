/**
 * account activity client for the X API.
 *
 * This module provides a client for interacting with the account activity endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetSubscriptionCountResponse,
  GetSubscriptionsResponse,
  CreateReplayJobResponse,
  DeleteSubscriptionResponse,
  ValidateSubscriptionResponse,
  CreateSubscriptionRequest,
  CreateSubscriptionResponse,
} from './models.js';

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
 * Client for account activity operations
 * 
 * This client provides methods for interacting with the account activity endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all account activity related operations.
 * 
 * @category account activity
 */
export class AccountActivityClient {
  private client: Client;

  /**
     * Creates a new account activity client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get subscription count
   * Retrieves a count of currently active Account Activity subscriptions.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptionCount(): Promise<GetSubscriptionCountResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/account_activity/subscriptions/count';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetSubscriptionCountResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get subscriptions
   * Retrieves a list of all active subscriptions for a given webhook.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptions(): Promise<GetSubscriptionsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path =
      '/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list';

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
   * Create replay job
   * Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.








   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createReplayJob(): Promise<CreateReplayJobResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path =
      '/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<CreateReplayJobResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete subscription
   * Deletes an Account Activity subscription for the given webhook and user ID.






   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubscription(): Promise<DeleteSubscriptionResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path =
      '/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all';

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
   * Validate subscription
   * Checks a user’s Account Activity subscription for a given webhook.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async validateSubscription(): Promise<ValidateSubscriptionResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/account_activity/webhooks/{webhook_id}/subscriptions/all';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<ValidateSubscriptionResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create subscription
   * Creates an Account Activity subscription for the user and the given webhook.




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
    let path = '/2/account_activity/webhooks/{webhook_id}/subscriptions/all';

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
}
