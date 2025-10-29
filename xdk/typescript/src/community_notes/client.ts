/**
 * Community notes client for the X API.
 *
 * This module provides a client for interacting with the Community notes endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  CommunityNotesSearchEligiblePostsResponse,
  CommunityNotesDeleteResponse,
  CommunityNotesEvaluateRequest,
  CommunityNotesEvaluateResponse,
  CommunityNotesSearchWrittenResponse,
  CommunityNotesCreateRequest,
  CommunityNotesCreateResponse,
} from './models.js';

/**
 * Options for searchEligiblePosts method
 */
export interface CommunityNotesSearchEligiblePostsOptions {
  /** Pagination token to get next set of posts eligible for notes. */
  paginationToken?: string;

  /** Max results to return. */
  maxResults?: number;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of Poll fields to display. */
  pollfields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Place fields to display. */
  placefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for evaluate method
 */
export interface CommunityNotesEvaluateOptions {
  /** Request body */
  body?: CommunityNotesEvaluateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for searchWritten method
 */
export interface CommunityNotesSearchWrittenOptions {
  /** Pagination token to get next set of posts eligible for notes. */
  paginationToken?: string;

  /** Max results to return. */
  maxResults?: number;

  /** A comma separated list of Note fields to display. */
  notefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for create method
 */
export interface CommunityNotesCreateOptions {
  /** Request body */
  body?: CommunityNotesCreateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Community notes operations
 * 
 * This client provides methods for interacting with the Community notes endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Community notes related operations.
 * 
 * @category Community notes
 */
export class CommunityNotesClient {
  private client: Client;

  /**
     * Creates a new Community notes client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Delete a Community Note
   * Deletes a community note.


   * @param id The community note id to delete.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id: string): Promise<CommunityNotesDeleteResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/notes/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<CommunityNotesDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Evaluate a Community Note
   * Endpoint to evaluate a community note.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async evaluate(
    options: CommunityNotesEvaluateOptions = {}
  ): Promise<CommunityNotesEvaluateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/evaluate_note';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CommunityNotesEvaluateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create a Community Note
   * Creates a community note endpoint for LLM use case.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(
    options: CommunityNotesCreateOptions = {}
  ): Promise<CommunityNotesCreateResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/notes';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CommunityNotesCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search for Posts Eligible for Community Notes
   * Returns all the posts that are eligible for community notes.
   * Returns a paginator for automatic pagination through all results.


   * @param testMode If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async searchEligiblePosts(
    testMode: boolean,
    options: CommunityNotesSearchEligiblePostsOptions = {}
  ): Promise<PostPaginator> {
    // Destructure options

    const {
      paginationToken = undefined,

      maxResults = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/notes/search/posts_eligible_for_notes';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (testMode !== undefined) {
        params.append('test_mode', String(testMode));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (mediafields !== undefined) {
        params.append('media.fields', mediafields.join(','));
      }

      if (pollfields !== undefined) {
        params.append('poll.fields', pollfields.join(','));
      }

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (placefields !== undefined) {
        params.append('place.fields', placefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...requestOptions,
      };

      const response = await this.client.request<
        CommunityNotesSearchEligiblePostsResponse
      >(
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
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Search for Community Notes Written
   * Returns all the community notes written by the user.
   * Returns a paginator for automatic pagination through all results.


   * @param testMode If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async searchWritten(
    testMode: boolean,
    options: CommunityNotesSearchWrittenOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

    const {
      paginationToken = undefined,

      maxResults = undefined,

      notefields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/notes/search/notes_written';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (testMode !== undefined) {
        params.append('test_mode', String(testMode));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (notefields !== undefined) {
        params.append('note.fields', notefields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...requestOptions,
      };

      const response = await this.client.request<
        CommunityNotesSearchWrittenResponse
      >(
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
