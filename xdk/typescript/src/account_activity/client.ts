/**
 * Account activity client for the X API.
 *
 * This module provides a client for interacting with the Account activity endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  AccountActivityGetSubscriptionsResponse,
  AccountActivityGetSubscriptionCountResponse,
  AccountActivityCreateReplayJobResponse,
  AccountActivityValidateSubscriptionResponse,
  AccountActivityDeleteSubscriptionResponse,
} from './models.js';

/**
 * Client for Account activity operations
 */
export class AccountActivityClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get subscriptions
     * Retrieves a list of all active subscriptions for a given webhook.
     * @param webhookId The webhook ID to pull subscriptions for.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getSubscriptions(
    options?: RequestOptions
  ): Promise<ApiResponse<AccountActivityGetSubscriptionsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<AccountActivityGetSubscriptionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get subscription count
     * Retrieves a count of currently active Account Activity subscriptions.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getSubscriptionCount(
    options?: RequestOptions
  ): Promise<ApiResponse<AccountActivityGetSubscriptionCountResponse>> {
    const params = new URLSearchParams();

    const path = `/2/account_activity/subscriptions/count`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<AccountActivityGetSubscriptionCountResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create replay job
     * Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.
     * @param webhookId The unique identifier for the webhook configuration.
     * @param fromDate The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format.
     * @param toDate The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format.* @param options Additional request options
     * @returns Promise with the API response
     */
  async createReplayJob(
    options?: RequestOptions
  ): Promise<ApiResponse<AccountActivityCreateReplayJobResponse>> {
    const params = new URLSearchParams();

    const path = `/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<AccountActivityCreateReplayJobResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Validate subscription
     * Checks a user’s Account Activity subscription for a given webhook.
     * @param webhookId The webhook ID to check subscription against.* @param options Additional request options
     * @returns Promise with the API response
     */
  async validateSubscription(
    options?: RequestOptions
  ): Promise<ApiResponse<AccountActivityValidateSubscriptionResponse>> {
    const params = new URLSearchParams();

    const path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<AccountActivityValidateSubscriptionResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete subscription
     * Deletes an Account Activity subscription for the given webhook and user ID.
     * @param webhookId The webhook ID to check subscription against.
     * @param userId User ID to unsubscribe from.* @param options Additional request options
     * @returns Promise with the API response
     */
  async deleteSubscription(
    options?: RequestOptions
  ): Promise<ApiResponse<AccountActivityDeleteSubscriptionResponse>> {
    const params = new URLSearchParams();

    const path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<AccountActivityDeleteSubscriptionResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
