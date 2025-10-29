/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  ActivityUpdateSubscriptionResponse,
  ActivityDeleteSubscriptionResponse,
  ActivityGetSubscriptionsResponse,
  ActivityCreateSubscriptionResponse,
  ActivityStreamResponse,
} from './models.js';

/**
 * Options for updateSubscription method
 */
export interface ActivityUpdateSubscriptionStreamingOptions {
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
 * Options for deleteSubscription method
 */
export interface ActivityDeleteSubscriptionStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getSubscriptions method
 */
export interface ActivityGetSubscriptionsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createSubscription method
 */
export interface ActivityCreateSubscriptionStreamingOptions {
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
 * Options for stream method
 */
export interface ActivityStreamStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided. */
  endTime?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class ActivityClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Activity Stream
     * Stream of X Activities
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async stream(
    options: ActivityStreamStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'stream');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      requestOptions: requestOptions = {},
    } = options;

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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/activity/stream' + (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Update X activity subscription
     * Updates a subscription for an X activity event
     * 
     * @returns Promise with the API response
     */
  async updateSubscription(
    subscriptionId: string,
    options: ActivityUpdateSubscriptionStreamingOptions = {}
  ): Promise<ActivityUpdateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'updateSubscription');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/activity/subscriptions/{subscription_id}`;

    path = path.replace(`{${'subscription_id'}}`, String(subscriptionId));

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
    return this.client.request<ActivityUpdateSubscriptionResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Deletes X activity subscription
     * Deletes a subscription for an X activity event
     * 
     * @returns Promise with the API response
     */
  async deleteSubscription(
    subscriptionId: string,
    options: ActivityDeleteSubscriptionStreamingOptions = {}
  ): Promise<ActivityDeleteSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteSubscription');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/activity/subscriptions/{subscription_id}`;

    path = path.replace(`{${'subscription_id'}}`, String(subscriptionId));

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
    return this.client.request<ActivityDeleteSubscriptionResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get X activity subscriptions
     * Get a list of active subscriptions for XAA
     * 
     * @returns Promise with the API response
     */
  async getSubscriptions(
    options: ActivityGetSubscriptionsStreamingOptions = {}
  ): Promise<ActivityGetSubscriptionsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getSubscriptions');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/activity/subscriptions`;

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
    return this.client.request<ActivityGetSubscriptionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create X activity subscription
     * Creates a subscription for an X activity event
     * 
     * @returns Promise with the API response
     */
  async createSubscription(
    options: ActivityCreateSubscriptionStreamingOptions = {}
  ): Promise<ActivityCreateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createSubscription');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/activity/subscriptions`;

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
    return this.client.request<ActivityCreateSubscriptionResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
