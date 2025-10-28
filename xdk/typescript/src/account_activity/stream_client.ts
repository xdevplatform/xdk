/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  AccountActivityDeleteSubscriptionResponse,
  AccountActivityCreateReplayJobResponse,
  AccountActivityGetSubscriptionsResponse,
  AccountActivityValidateSubscriptionResponse,
  AccountActivityCreateSubscriptionResponse,
  AccountActivityGetSubscriptionCountResponse,
} from './models.js';

/**
 * Options for createSubscription method
 */
export interface AccountActivityCreateSubscriptionStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class AccountActivityClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Delete subscription
     * Deletes an Account Activity subscription for the given webhook and user ID.
     * 
     * @returns Promise with the API response
     */
  async deleteSubscription(
    webhookId: string,
    userId: string
  ): Promise<AccountActivityDeleteSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteSubscription');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

    path = path.replace(`{${'user_id'}}`, String(userId));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<AccountActivityDeleteSubscriptionResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create replay job
     * Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.
     * 
     * @returns Promise with the API response
     */
  async createReplayJob(
    webhookId: string,
    fromDate: string,
    toDate: string
  ): Promise<AccountActivityCreateReplayJobResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createReplayJob');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    if (fromDate !== undefined) {
      params.append('from_date', String(fromDate));
    }

    if (toDate !== undefined) {
      params.append('to_date', String(toDate));
    }

    // Build path parameters
    let path = `/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<AccountActivityCreateReplayJobResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get subscriptions
     * Retrieves a list of all active subscriptions for a given webhook.
     * 
     * @returns Promise with the API response
     */
  async getSubscriptions(
    webhookId: string
  ): Promise<AccountActivityGetSubscriptionsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getSubscriptions');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<AccountActivityGetSubscriptionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Validate subscription
     * Checks a user’s Account Activity subscription for a given webhook.
     * 
     * @returns Promise with the API response
     */
  async validateSubscription(
    webhookId: string
  ): Promise<AccountActivityValidateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'validateSubscription'
    );

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<AccountActivityValidateSubscriptionResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create subscription
     * Creates an Account Activity subscription for the user and the given webhook.
     * 
     * @returns Promise with the API response
     */
  async createSubscription(
    webhookId: string,
    options: AccountActivityCreateSubscriptionStreamingOptions = {}
  ): Promise<AccountActivityCreateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createSubscription');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<AccountActivityCreateSubscriptionResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get subscription count
     * Retrieves a count of currently active Account Activity subscriptions.
     * 
     * @returns Promise with the API response
     */
  async getSubscriptionCount(): Promise<
    AccountActivityGetSubscriptionCountResponse
  > {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getSubscriptionCount'
    );

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/subscriptions/count`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<AccountActivityGetSubscriptionCountResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
