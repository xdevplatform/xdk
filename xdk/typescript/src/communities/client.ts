/**
 * Communities client for the X API.
 *
 * This module provides a client for interacting with the Communities endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  CommunitiesGetByIdResponse,
  CommunitiesSearchResponse,
} from './models.js';

/**
 * Options for getById method
 */
export interface CommunitiesGetByIdOptions {
  /** A comma separated list of Community fields to display. */
  communityfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for search method
 */
export interface CommunitiesSearchOptions {
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
}

/**
 * Client for Communities operations
 * 
 * This client provides methods for interacting with the Communities endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Communities related operations.
 * 
 * @category Communities
 */
export class CommunitiesClient {
  private client: Client;

  /**
     * Creates a new Communities client instance
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



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(
    id: string,
    options: CommunitiesGetByIdOptions = {}
  ): Promise<CommunitiesGetByIdResponse> {
    // Destructure options

    const {
      communityfields = [],

      requestOptions: requestOptions = {},
    } = options;

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

    return this.client.request<CommunitiesGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search Communities
   * Retrieves a list of Communities matching the specified search query.
   * Returns a paginator for automatic pagination through all results.


   * @param query Query to search communities.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async search(
    query: string,
    options: CommunitiesSearchOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      maxResults = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      communityfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/communities/search';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...requestOptions,
      };

      const response = await this.client.request<CommunitiesSearchResponse>(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }
}
