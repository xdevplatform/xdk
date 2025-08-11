/**
 * Webhooks client for the X API.
 *
 * This module provides a client for interacting with the Webhooks endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  WebhooksValidateResponse,
  WebhooksDeleteResponse,
  WebhooksGetResponse,
  WebhooksCreateRequest,
  WebhooksCreateResponse,
} from './models.js';

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
     * @param webhookId The ID of the webhook to check.* @param options Additional request options
     * @returns Promise with the API response
     */
  async validate(
    options?: RequestOptions
  ): Promise<ApiResponse<WebhooksValidateResponse>> {
    const params = new URLSearchParams();

    const path = `/2/webhooks/{webhook_id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<WebhooksValidateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete webhook
     * Deletes an existing webhook configuration.
     * @param webhookId The ID of the webhook to delete.* @param options Additional request options
     * @returns Promise with the API response
     */
  async delete(
    options?: RequestOptions
  ): Promise<ApiResponse<WebhooksDeleteResponse>> {
    const params = new URLSearchParams();

    const path = `/2/webhooks/{webhook_id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<WebhooksDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get webhook
     * Get a list of webhook configs associated with a client app.
     * @param webhookConfigfields A comma separated list of WebhookConfig fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async get(
    options?: RequestOptions
  ): Promise<ApiResponse<WebhooksGetResponse>> {
    const params = new URLSearchParams();

    const path = `/2/webhooks`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<WebhooksGetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create webhook
     * Creates a new webhook configuration.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async create(
    body?: WebhooksCreateRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<WebhooksCreateResponse>> {
    const params = new URLSearchParams();

    const path = `/2/webhooks`;

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

    return this.client.request<WebhooksCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
