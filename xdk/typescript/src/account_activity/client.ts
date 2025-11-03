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
  GetSubscriptionsResponse,
  CreateReplayJobResponse,
  ValidateSubscriptionResponse,
  CreateSubscriptionRequest,
  CreateSubscriptionResponse,
  DeleteSubscriptionResponse,
  GetSubscriptionCountResponse,
} from './models.js';

/**
 * Options for createSubscription method
 * 
 * @public
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
   * Get subscriptions
   * Retrieves a list of all active subscriptions for a given webhook.


   * @param webhookId The webhook ID to pull subscriptions for.




   * @returns {Promise<GetSubscriptionsResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptions(webhookId: string): Promise<GetSubscriptionsResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path =
      '/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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


   * @param webhookId The unique identifier for the webhook configuration.




   * @param fromDate The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format.



   * @param toDate The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format.



   * @returns {Promise<CreateReplayJobResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createReplayJob(
    webhookId: string,
    fromDate: string,
    toDate: string
  ): Promise<CreateReplayJobResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path =
      '/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

    // Build query parameters
    const params = new URLSearchParams();

    if (fromDate !== undefined) {
      params.append('from_date', String(fromDate));
    }

    if (toDate !== undefined) {
      params.append('to_date', String(toDate));
    }

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
   * Validate subscription
   * Checks a user’s Account Activity subscription for a given webhook.


   * @param webhookId The webhook ID to check subscription against.




   * @returns {Promise<ValidateSubscriptionResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async validateSubscription(
    webhookId: string
  ): Promise<ValidateSubscriptionResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/account_activity/webhooks/{webhook_id}/subscriptions/all';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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


   * @param webhookId The webhook ID to check subscription against.




   * @returns {Promise<CreateSubscriptionResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createSubscription(
    webhookId: string,
    options: CreateSubscriptionOptions = {}
  ): Promise<CreateSubscriptionResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/account_activity/webhooks/{webhook_id}/subscriptions/all';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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
   * Delete subscription
   * Deletes an Account Activity subscription for the given webhook and user ID.


   * @param webhookId The webhook ID to check subscription against.



   * @param userId User ID to unsubscribe from.




   * @returns {Promise<DeleteSubscriptionResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubscription(
    webhookId: string,
    userId: string
  ): Promise<DeleteSubscriptionResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path =
      '/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

    path = path.replace('{user_id}', encodeURIComponent(String(userId)));

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
   * Get subscription count
   * Retrieves a count of currently active Account Activity subscriptions.



   * @returns {Promise<GetSubscriptionCountResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getSubscriptionCount(): Promise<GetSubscriptionCountResponse> {
    // Destructure options (exclude path parameters, they're already function params)

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
}
