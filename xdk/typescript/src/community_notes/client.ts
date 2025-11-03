/**
 * community notes client for the X API.
 *
 * This module provides a client for interacting with the community notes endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  CreateRequest,
  CreateResponse,
  SearchWrittenResponse,
  SearchEligiblePostsResponse,
  EvaluateRequest,
  EvaluateResponse,
  DeleteResponse,
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
 * Options for searchWritten method
 * 
 * @public
 */
export interface SearchWrittenOptions {
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
 * Options for searchEligiblePosts method
 * 
 * @public
 */
export interface SearchEligiblePostsOptions {
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
 * 
 * @public
 */
export interface EvaluateOptions {
  /** Request body */
  body?: EvaluateRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for community notes operations
 * 
 * This client provides methods for interacting with the community notes endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all community notes related operations.
 * 
 * @category community notes
 */
export class CommunityNotesClient {
  private client: Client;

  /**
     * Creates a new community notes client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Create a Community Note
   * Creates a community note endpoint for LLM use case.



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
    let path = '/2/notes';

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
   * Search for Community Notes Written
   * Returns all the community notes written by the user.



   * @param testMode If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.



   * @returns {Promise<SearchWrittenResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async searchWritten(
    testMode: boolean,
    options: SearchWrittenOptions = {}
  ): Promise<SearchWrittenResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      paginationToken = undefined,

      maxResults = undefined,

      notefields = [],

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/notes/search/notes_written';

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchWrittenResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Search for Posts Eligible for Community Notes
   * Returns all the posts that are eligible for community notes.



   * @param testMode If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.



   * @returns {Promise<SearchEligiblePostsResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async searchEligiblePosts(
    testMode: boolean,
    options: SearchEligiblePostsOptions = {}
  ): Promise<SearchEligiblePostsResponse> {
    // Destructure options (exclude path parameters, they're already function params)

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
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/notes/search/posts_eligible_for_notes';

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<SearchEligiblePostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Evaluate a Community Note
   * Endpoint to evaluate a community note.



   * @returns {Promise<EvaluateResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async evaluate(options: EvaluateOptions = {}): Promise<EvaluateResponse> {
    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/evaluate_note';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<EvaluateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete a Community Note
   * Deletes a community note.


   * @param id The community note id to delete.




   * @returns {Promise<DeleteResponse>} Promise resolving to the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id: string): Promise<DeleteResponse> {
    // Destructure options (exclude path parameters, they're already function params)

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

    return this.client.request<DeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
