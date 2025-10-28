/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  CommunitiesSearchResponse,
  CommunitiesGetByIdResponse,
} from './models.js';

/**
 * Options for search method
 */
export interface CommunitiesSearchStreamingOptions {
  /** The maximum number of search results to be returned by a request. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  paginationToken?: string;

  /** A comma separated list of Community fields to display. */
  communityfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getById method
 */
export interface CommunitiesGetByIdStreamingOptions {
  /** A comma separated list of Community fields to display. */
  communityfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class CommunitiesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Search Communities
     * Retrieves a list of Communities matching the specified search query.
     * 
     * @returns Promise with the API response
     */
  async search(
    query: string,
    options: CommunitiesSearchStreamingOptions = {}
  ): Promise<CommunitiesSearchResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'search');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      communityfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.append('query', String(query));
    }

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (nextToken !== undefined) {
      params.append('next_token', String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (communityfields !== undefined) {
      params.append('community.fields', communityfields.join(','));
    }

    // Build path parameters
    let path = `/2/communities/search`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<CommunitiesSearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Community by ID
     * Retrieves details of a specific Community by its ID.
     * 
     * @returns Promise with the API response
     */
  async getById(
    id: string,
    options: CommunitiesGetByIdStreamingOptions = {}
  ): Promise<CommunitiesGetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options with defaults

    const {
      communityfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (communityfields !== undefined) {
      params.append('community.fields', communityfields.join(','));
    }

    // Build path parameters
    let path = `/2/communities/{id}`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<CommunitiesGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
