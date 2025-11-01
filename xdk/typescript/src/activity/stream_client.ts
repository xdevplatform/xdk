/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  StreamResponse,
  UpdateSubscriptionResponse,
  DeleteSubscriptionResponse,
  GetSubscriptionsResponse,
  CreateSubscriptionResponse,
} from './models.js';

/**
 * Options for stream method
 * 
 * @public
 */
export interface StreamStreamingOptions {
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
/**
 * Options for updateSubscription method
 * 
 * @public
 */
export interface UpdateSubscriptionStreamingOptions {
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



     * @returns {Promise<EventDrivenStream>} Event-driven stream for handling streaming data
     */
  async stream(
    options: StreamStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'stream');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url = path + (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },

      signal: signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...requestOptions,
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
    options: UpdateSubscriptionStreamingOptions = {}
  ): Promise<UpdateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'updateSubscription');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<UpdateSubscriptionResponse>(
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
    options: DeleteSubscriptionStreamingOptions = {}
  ): Promise<DeleteSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteSubscription');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<DeleteSubscriptionResponse>(
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
    options: GetSubscriptionsStreamingOptions = {}
  ): Promise<GetSubscriptionsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getSubscriptions');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/activity/subscriptions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetSubscriptionsResponse>(
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
    options: CreateSubscriptionStreamingOptions = {}
  ): Promise<CreateSubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createSubscription');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/activity/subscriptions';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateSubscriptionResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
