/**
 * Aaasubscriptions client for the X API.
 *
 * This module provides a client for interacting with the Aaasubscriptions endpoints of the X API.
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
  AaasubscriptionsCreateAccountActivitySubscriptionRequest,
  AaasubscriptionsCreateAccountActivitySubscriptionResponse,
} from './models.js';

/**
 * Options for createAccountActivitySubscription method
 */
export interface AaasubscriptionsCreateAccountActivitySubscriptionOptions {
  /** Request body */
  body?: AaasubscriptionsCreateAccountActivitySubscriptionRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Aaasubscriptions operations
 * 
 * This client provides methods for interacting with the Aaasubscriptions endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Aaasubscriptions related operations.
 * 
 * @category Aaasubscriptions
 */
export class AaasubscriptionsClient {
  private client: Client;

  /**
     * Creates a new Aaasubscriptions client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Create subscription
   * Creates an Account Activity subscription for the user and the given webhook.
   * @param webhookId The webhook ID to check subscription against.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createAccountActivitySubscription(
    webhookId: string,
    options: AaasubscriptionsCreateAccountActivitySubscriptionOptions = {}
  ): Promise<AaasubscriptionsCreateAccountActivitySubscriptionResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/account_activity/webhooks/{webhook_id}/subscriptions/all';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<
      AaasubscriptionsCreateAccountActivitySubscriptionResponse
    >(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
