/**
 * communities client for the X API.
 *
 * This module provides a client for interacting with the communities endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import { GetByIdResponse, SearchResponse } from './models.js';

/**
 * Options for getById method
 * 
 * @public
 */
export interface GetByIdOptions {
  /** A comma separated list of Community fields to display. */
  communityfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for search method
 * 
 * @public
 */
export interface SearchOptions {
  /** The maximum number of search results to be returned by a request. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: any;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  paginationToken?: any;

  /** A comma separated list of Community fields to display. */
  communityfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for communities operations
 * 
 * This client provides methods for interacting with the communities endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all communities related operations.
 * 
 * @category communities
 */
export class CommunitiesClient {
  private client: Client;

  /**
     * Creates a new communities client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get Community by ID
   * Retrieves details of a specific Community by its ID.


   * @param id The ID of the Community.




   * @returns {Promise<GetByIdResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(
    id: string,
    options: GetByIdOptions = {}
  ): Promise<GetByIdResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      communityfields = [],

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/communities/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (communityfields !== undefined) {
      params.append('community.fields', communityfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search Communities
   * Retrieves a list of Communities matching the specified search query.



   * @param query Query to search communities.



   * @returns {Promise<SearchResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async search(
    query: string,
    options: SearchOptions = {}
  ): Promise<SearchResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      communityfields = [],

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/communities/search';

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
