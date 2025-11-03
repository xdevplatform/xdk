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
  CreateStreamLinkResponse,
  DeleteStreamLinkResponse,
  GetResponse,
  CreateRequest,
  CreateResponse,
} from './models.js';

/**
 * Options for createStreamLink method
 * 
 * @public
 */
export interface CreateStreamLinkOptions {
  /** A comma separated list of Tweet fields to display. */
  tweetfields?: string;

  /** A comma separated list of fields to expand. */
  expansions?: string;

  /** A comma separated list of Media fields to display. */
  mediafields?: string;

  /** A comma separated list of Poll fields to display. */
  pollfields?: string;

  /** A comma separated list of User fields to display. */
  userfields?: string;

  /** A comma separated list of Place fields to display. */
  placefields?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for get method
 * 
 * @public
 */
export interface GetOptions {
  /** A comma separated list of WebhookConfig fields to display. */
  webhookConfigfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

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


   * @param webhookId The ID of the webhook to check.




   * @returns {Promise<ValidateResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async validate(webhookId: string): Promise<ValidateResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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


   * @param webhookId The ID of the webhook to delete.




   * @returns {Promise<DeleteResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(webhookId: string): Promise<DeleteResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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



   * @returns {Promise<GetStreamLinksResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getStreamLinks(): Promise<GetStreamLinksResponse> {
    // Destructure options (exclude path parameters, they're already function params)

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
   * Create stream link
   * Creates a link to deliver FilteredStream events to the given webhook.


   * @param webhookId The webhook ID to link to your FilteredStream ruleset.




   * @returns {Promise<CreateStreamLinkResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createStreamLink(
    webhookId: string,
    options: CreateStreamLinkOptions = {}
  ): Promise<CreateStreamLinkResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      tweetfields = undefined,

      expansions = undefined,

      mediafields = undefined,

      pollfields = undefined,

      userfields = undefined,

      placefields = undefined,

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

    // Build query parameters
    const params = new URLSearchParams();

    if (tweetfields !== undefined) {
      params.append('tweet.fields', String(tweetfields));
    }

    if (expansions !== undefined) {
      params.append('expansions', String(expansions));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', String(mediafields));
    }

    if (pollfields !== undefined) {
      params.append('poll.fields', String(pollfields));
    }

    if (userfields !== undefined) {
      params.append('user.fields', String(userfields));
    }

    if (placefields !== undefined) {
      params.append('place.fields', String(placefields));
    }

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


   * @param webhookId The webhook ID to link to your FilteredStream ruleset.




   * @returns {Promise<DeleteStreamLinkResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteStreamLink(webhookId: string): Promise<DeleteStreamLinkResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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

  /**
   * Get webhook
   * Get a list of webhook configs associated with a client app.



   * @returns {Promise<GetResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async get(options: GetOptions = {}): Promise<GetResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      webhookConfigfields = [],

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/webhooks';

    // Build query parameters
    const params = new URLSearchParams();

    if (webhookConfigfields !== undefined) {
      params.append('webhook_config.fields', webhookConfigfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
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



   * @returns {Promise<CreateResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(options: CreateOptions = {}): Promise<CreateResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      requestOptions: requestOptions = {},
    } =
      options || {};

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
}
