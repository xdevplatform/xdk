/**
 * Webhooks client for the X API.
 *
 * This module provides a client for interacting with the Webhooks endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  TwitterPaginator,
  TweetPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import {
  WebhooksValidateResponse,
  WebhooksDeleteResponse,
  WebhooksGetResponse,
  WebhooksCreateRequest,
  WebhooksCreateResponse,
} from './models.js';

/**
 * Options for get method
 */
export interface WebhooksGetOptions {
  /** A comma separated list of WebhookConfig fields to display. */
  webhookConfigfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for create method
 */
export interface WebhooksCreateOptions {
  /** Request body */
  body?: WebhooksCreateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Webhooks operations
 */
export class WebhooksClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Validate webhook
   * Triggers a CRC check for a given webhook.
   * @param webhookId The ID of the webhook to check.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async validate(webhookId: string): Promise<WebhooksValidateResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<WebhooksValidateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete webhook
   * Deletes an existing webhook configuration.
   * @param webhookId The ID of the webhook to delete.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(webhookId: string): Promise<WebhooksDeleteResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<WebhooksDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get webhook
   * Get a list of webhook configs associated with a client app.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async get(options: WebhooksGetOptions = {}): Promise<WebhooksGetResponse> {
    // Destructure options

    const {
      webhookConfigfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/webhooks';

    // Build query parameters
    const params = new URLSearchParams();

    if (webhookConfigfields !== undefined) {
      webhookConfigfields.forEach(item =>
        params.append('webhook_config.fields', String(item))
      );
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<WebhooksGetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create webhook
   * Creates a new webhook configuration.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(
    options: WebhooksCreateOptions = {}
  ): Promise<WebhooksCreateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/webhooks';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<WebhooksCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
