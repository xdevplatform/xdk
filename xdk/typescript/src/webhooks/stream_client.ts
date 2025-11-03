/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetStreamLinksResponse,
  CreateStreamLinkResponse,
  DeleteStreamLinkResponse,
  ValidateResponse,
  DeleteResponse,
  GetResponse,
  CreateResponse,
} from './models.js';

/**
 * Options for getStreamLinks method
 * 
 * @public
 */
export interface GetStreamLinksStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createStreamLink method
 * 
 * @public
 */
export interface CreateStreamLinkStreamingOptions {
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
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for deleteStreamLink method
 * 
 * @public
 */
export interface DeleteStreamLinkStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for validate method
 * 
 * @public
 */
export interface ValidateStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for delete method
 * 
 * @public
 */
export interface DeleteStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for get method
 * 
 * @public
 */
export interface GetStreamingOptions {
  /** A comma separated list of WebhookConfig fields to display. */
  webhookConfigfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for create method
 * 
 * @public
 */
export interface CreateStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class WebhooksClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get stream links
     * Get a list of webhook links associated with a filtered stream ruleset.
     * 
     * @returns Promise with the API response
     */
  async getStreamLinks(
    options: GetStreamLinksStreamingOptions = {}
  ): Promise<GetStreamLinksResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getStreamLinks');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks';

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
    return this.client.request<GetStreamLinksResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create stream link
     * Creates a link to deliver FilteredStream events to the given webhook.
     * 
     * @returns Promise with the API response
     */
  async createStreamLink(
    webhookId: string,
    options: CreateStreamLinkStreamingOptions = {}
  ): Promise<CreateStreamLinkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createStreamLink');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      tweetfields = undefined,

      expansions = undefined,

      mediafields = undefined,

      pollfields = undefined,

      userfields = undefined,

      placefields = undefined,

      headers = {},
      signal,
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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateStreamLinkResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete stream link
     * Deletes a link from FilteredStream events to the given webhook.
     * 
     * @returns Promise with the API response
     */
  async deleteStreamLink(
    webhookId: string,
    options: DeleteStreamLinkStreamingOptions = {}
  ): Promise<DeleteStreamLinkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteStreamLink');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/tweets/search/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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
    return this.client.request<DeleteStreamLinkResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Validate webhook
     * Triggers a CRC check for a given webhook.
     * 
     * @returns Promise with the API response
     */
  async validate(
    webhookId: string,
    options: ValidateStreamingOptions = {}
  ): Promise<ValidateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'validate');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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
    return this.client.request<ValidateResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete webhook
     * Deletes an existing webhook configuration.
     * 
     * @returns Promise with the API response
     */
  async delete(
    webhookId: string,
    options: DeleteStreamingOptions = {}
  ): Promise<DeleteResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'delete');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/webhooks/{webhook_id}';

    path = path.replace('{webhook_id}', encodeURIComponent(String(webhookId)));

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
    return this.client.request<DeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get webhook
     * Get a list of webhook configs associated with a client app.
     * 
     * @returns Promise with the API response
     */
  async get(options: GetStreamingOptions = {}): Promise<GetResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'get');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      webhookConfigfields = [],

      headers = {},
      signal,
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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create webhook
     * Creates a new webhook configuration.
     * 
     * @returns Promise with the API response
     */
  async create(options: CreateStreamingOptions = {}): Promise<CreateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'create');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/webhooks';

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
    return this.client.request<CreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
