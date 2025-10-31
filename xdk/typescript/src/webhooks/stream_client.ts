/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  CreateStreamLinkResponse,
  DeleteStreamLinkResponse,
  GetStreamLinksResponse,
  GetResponse,
  CreateResponse,
  ValidateResponse,
  DeleteResponse,
} from './models.js';

/**
 * Options for createStreamLink method
 */
export interface CreateStreamLinkStreamingOptions {
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
export interface DeleteStreamLinkStreamingOptions {
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
export interface GetStreamLinksStreamingOptions {
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
export interface GetStreamingOptions {
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
/**
 * Options for validate method
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
 */
export interface DeleteStreamingOptions {
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
     * Create stream link
     * Creates a link to deliver FilteredStream events to the given webhook.
     * 
     * @returns Promise with the API response
     */
  async createStreamLink(
    options: CreateStreamLinkStreamingOptions = {}
  ): Promise<CreateStreamLinkResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createStreamLink');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/webhooks/{webhook_id}`;

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
    options: DeleteStreamLinkStreamingOptions = {}
  ): Promise<DeleteStreamLinkResponse> {
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
    return this.client.request<DeleteStreamLinkResponse>(
      'DELETE',
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
    options: GetStreamLinksStreamingOptions = {}
  ): Promise<GetStreamLinksResponse> {
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
    return this.client.request<GetStreamLinksResponse>(
      'GET',
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

    // Destructure options with defaults

    const requestOptions = {};

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

      ...options,
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
    return this.client.request<CreateResponse>(
      'POST',
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
    options: ValidateStreamingOptions = {}
  ): Promise<ValidateResponse> {
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
  async delete(options: DeleteStreamingOptions = {}): Promise<DeleteResponse> {
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
    return this.client.request<DeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
