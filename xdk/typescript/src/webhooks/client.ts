/**
 * webhooks client for the X API.
 *
 * This module provides a client for interacting with the webhooks endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  ValidateResponse,
  DeleteResponse,
  GetStreamLinksResponse,
  GetResponse,
  CreateRequest,
  CreateResponse,
  CreateStreamLinkResponse,
  DeleteStreamLinkResponse,
} from './models.js';

/**
 * Options for create method
 * 
 * @public
 */
export interface CreateOptions {
  /** Request body */
  body?: CreateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createStreamLink method
 * 
 * @public
 */
export interface CreateStreamLinkOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for webhooks operations
 * 
 * This client provides methods for interacting with the webhooks endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all webhooks related operations.
 * 
 * @category webhooks
 */
export class WebhooksClient {
  private client: Client;

  /**
     * Creates a new webhooks client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Validate webhook
   * Triggers a CRC check for a given webhook.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async validate(): Promise<ValidateResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<ValidateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete webhook
   * Deletes an existing webhook configuration.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(): Promise<DeleteResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get stream links
   * Get a list of webhook links associated with a filtered stream ruleset.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getStreamLinks(): Promise<GetStreamLinksResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetStreamLinksResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get webhook
   * Get a list of webhook configs associated with a client app.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async get(): Promise<GetResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/webhooks';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create webhook
   * Creates a new webhook configuration.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(options: CreateOptions = {}): Promise<CreateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/webhooks';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create stream link
   * Creates a link to deliver FilteredStream events to the given webhook.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createStreamLink(
    options: CreateStreamLinkOptions = {}
  ): Promise<CreateStreamLinkResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks/{webhook_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<CreateStreamLinkResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete stream link
   * Deletes a link from FilteredStream events to the given webhook.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteStreamLink(): Promise<DeleteStreamLinkResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks/{webhook_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DeleteStreamLinkResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
