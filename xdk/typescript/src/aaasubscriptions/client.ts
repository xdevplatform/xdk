/**
 * Aaasubscriptions client for the X API.
 *
 * This module provides a client for interacting with the Aaasubscriptions endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  AaasubscriptionsCreateAccountActivitySubscriptionRequest,
  AaasubscriptionsCreateAccountActivitySubscriptionResponse,
} from './models.js';

/**
 * Client for Aaasubscriptions operations
 */
export class AaasubscriptionsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Create subscription
     * Creates an Account Activity subscription for the user and the given webhook.
     * @param webhookId The webhook ID to check subscription against.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createAccountActivitySubscription(
    webhookId: string,
    body?: AaasubscriptionsCreateAccountActivitySubscriptionRequest,
    options?: RequestOptions
  ): Promise<
    ApiResponse<AaasubscriptionsCreateAccountActivitySubscriptionResponse>
  > {
    const params = new URLSearchParams();

    const path = `/2/account_activity/webhooks/{webhook_id}/subscriptions/all`.replace(
      '{webhook_id}',
      String(webhookId)
    );

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<
      AaasubscriptionsCreateAccountActivitySubscriptionResponse
    >(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
