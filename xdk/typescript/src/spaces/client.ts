/**
 * spaces client for the X API.
 *
 * This module provides a client for interacting with the spaces endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetByCreatorIdsResponse,
  SearchResponse,
  GetPostsResponse,
  GetByIdResponse,
  GetByIdsResponse,
  GetBuyersResponse,
} from './models.js';

/**
 * Options for search method
 * 
 * @public
 */
export interface SearchOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getPosts method
 * 
 * @public
 */
export interface GetPostsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getBuyers method
 * 
 * @public
 */
export interface GetBuyersOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for spaces operations
 * 
 * This client provides methods for interacting with the spaces endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all spaces related operations.
 * 
 * @category spaces
 */
export class SpacesClient {
  private client: Client;

  /**
     * Creates a new spaces client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get Spaces by creator IDs
   * Retrieves details of Spaces created by specified User IDs.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByCreatorIds(): Promise<GetByCreatorIdsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/spaces/by/creator_ids';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByCreatorIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search Spaces
   * Retrieves a list of Spaces matching the specified search query.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async search(options: SearchOptions = {}): Promise<SearchResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/spaces/search';

    // Build query parameters
    const params = new URLSearchParams();

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

  /**
   * Get Space Posts
   * Retrieves a list of Posts shared in a specific Space by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getPosts(options: GetPostsOptions = {}): Promise<GetPostsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/spaces/{id}/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get space by ID
   * Retrieves details of a specific space by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(): Promise<GetByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/spaces/{id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Spaces by IDs
   * Retrieves details of multiple Spaces by their IDs.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(): Promise<GetByIdsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/spaces';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Space ticket buyers
   * Retrieves a list of Users who purchased tickets to a specific Space by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getBuyers(options: GetBuyersOptions = {}): Promise<GetBuyersResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/spaces/{id}/buyers';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetBuyersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
