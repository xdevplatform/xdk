/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import { AaasubscriptionsCreateAccountActivitySubscriptionResponse } from './models.js';

/**
 * Options for createAccountActivitySubscription method
 */
export interface AaasubscriptionsCreateAccountActivitySubscriptionStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class AaasubscriptionsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Create subscription
     * Creates an Account Activity subscription for the user and the given webhook.
     * 
     * @returns Promise with the API response
     */
  async createAccountActivitySubscription(
    webhookId: string,
    options: AaasubscriptionsCreateAccountActivitySubscriptionStreamingOptions = {}
  ): Promise<AaasubscriptionsCreateAccountActivitySubscriptionResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'createAccountActivitySubscription'
    );

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
    return this.client.request<
      AaasubscriptionsCreateAccountActivitySubscriptionResponse
    >(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
