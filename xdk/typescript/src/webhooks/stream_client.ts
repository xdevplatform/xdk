/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  WebhooksValidateResponse,
  WebhooksDeleteResponse,
  WebhooksGetResponse,
  WebhooksCreateResponse,
  WebhooksGetStreamLinksResponse,
  WebhooksCreateStreamLinkResponse,
  WebhooksDeleteStreamLinkResponse,
} from './models.js';

/**
 * Options for validate method
 */
export interface WebhooksValidateStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for delete method
 */
export interface WebhooksDeleteStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for get method
 */
export interface WebhooksGetStreamingOptions {
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
 */
export interface WebhooksCreateStreamingOptions {
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
 * Options for getStreamLinks method
 */
export interface WebhooksGetStreamLinksStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createStreamLink method
 */
export interface WebhooksCreateStreamLinkStreamingOptions {
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
 */
export interface WebhooksDeleteStreamLinkStreamingOptions {
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
     * Validate webhook
     * Triggers a CRC check for a given webhook.
     * 
     * @returns Promise with the API response
     */
  async validate(
    webhookId: string,
    options: WebhooksValidateStreamingOptions = {}
  ): Promise<WebhooksValidateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'validate');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/webhooks/{webhook_id}`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

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
    return this.client.request<WebhooksValidateResponse>(
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
    options: WebhooksDeleteStreamingOptions = {}
  ): Promise<WebhooksDeleteResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'delete');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/webhooks/{webhook_id}`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

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
    return this.client.request<WebhooksDeleteResponse>(
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
  async get(
    options: WebhooksGetStreamingOptions = {}
  ): Promise<WebhooksGetResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'get');

    // Destructure options with defaults

    const {
      webhookConfigfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (webhookConfigfields !== undefined) {
      params.append('webhook_config.fields', webhookConfigfields.join(','));
    }

    // Build path parameters
    let path = `/2/webhooks`;

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
    return this.client.request<WebhooksGetResponse>(
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
  async create(
    options: WebhooksCreateStreamingOptions = {}
  ): Promise<WebhooksCreateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'create');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/webhooks`;

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
    return this.client.request<WebhooksCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get stream links
     * Get a list of webhook links associated with a filtered stream ruleset.
     * 
     * @returns Promise with the API response
     */
  async getStreamLinks(
    options: WebhooksGetStreamLinksStreamingOptions = {}
  ): Promise<WebhooksGetStreamLinksResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getStreamLinks');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/webhooks`;

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
    return this.client.request<WebhooksGetStreamLinksResponse>(
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
    options: WebhooksCreateStreamLinkStreamingOptions = {}
  ): Promise<WebhooksCreateStreamLinkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createStreamLink');

    // Destructure options with defaults

    const {
      tweetfields = undefined,

      expansions = undefined,

      mediafields = undefined,

      pollfields = undefined,

      userfields = undefined,

      placefields = undefined,

      requestOptions: requestOptions = {},
    } = options;

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

    // Build path parameters
    let path = `/2/tweets/search/webhooks/{webhook_id}`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

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
    return this.client.request<WebhooksCreateStreamLinkResponse>(
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
    options: WebhooksDeleteStreamLinkStreamingOptions = {}
  ): Promise<WebhooksDeleteStreamLinkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteStreamLink');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/webhooks/{webhook_id}`;

    path = path.replace(`{${'webhook_id'}}`, String(webhookId));

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
    return this.client.request<WebhooksDeleteStreamLinkResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
