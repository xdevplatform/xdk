/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  ValidateSubscriptionResponse,
  CreateSubscriptionResponse,
  GetSubscriptionsResponse,
  DeleteSubscriptionResponse,
  GetSubscriptionCountResponse,
  CreateReplayJobResponse,
} from './models.js';

/**
 * Options for validateSubscription method
 * 
 * @public
 */
export interface ValidateSubscriptionStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createSubscription method
 * 
 * @public
 */
export interface CreateSubscriptionStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getSubscriptions method
 * 
 * @public
 */
export interface GetSubscriptionsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for deleteSubscription method
 * 
 * @public
 */
export interface DeleteSubscriptionStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getSubscriptionCount method
 * 
 * @public
 */
export interface GetSubscriptionCountStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createReplayJob method
 * 
 * @public
 */
export interface CreateReplayJobStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class AccountActivityClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Validate subscription
     * Checks a user’s Account Activity subscription for a given webhook.
     * 
     * @returns Promise with the API response
     */
  async validateSubscription(
    options: ValidateSubscriptionStreamingOptions = {}
  ): Promise<ValidateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'validateSubscription'
    );

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all`;

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
    return this.client.request<ValidateSubscriptionResponse>(
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
    options: CreateSubscriptionStreamingOptions = {}
  ): Promise<CreateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createSubscription');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<CreateSubscriptionResponse>(
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
    options: GetSubscriptionsStreamingOptions = {}
  ): Promise<GetSubscriptionsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getSubscriptions');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list`;

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
    return this.client.request<GetSubscriptionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete subscription
     * Deletes an Account Activity subscription for the given webhook and user ID.
     * 
     * @returns Promise with the API response
     */
  async deleteSubscription(
    options: DeleteSubscriptionStreamingOptions = {}
  ): Promise<DeleteSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteSubscription');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all`;

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
    return this.client.request<DeleteSubscriptionResponse>(
      'DELETE',
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
  async getSubscriptionCount(
    options: GetSubscriptionCountStreamingOptions = {}
  ): Promise<GetSubscriptionCountResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getSubscriptionCount'
    );

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/subscriptions/count`;

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
    return this.client.request<GetSubscriptionCountResponse>(
      'GET',
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
    options: CreateReplayJobStreamingOptions = {}
  ): Promise<CreateReplayJobResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createReplayJob');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all`;

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
    return this.client.request<CreateReplayJobResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
