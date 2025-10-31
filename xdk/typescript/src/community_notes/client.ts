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
  SearchWrittenResponse,
  DeleteResponse,
  SearchEligiblePostsResponse,
  CreateRequest,
  CreateResponse,
  EvaluateRequest,
  EvaluateResponse,
} from './models.js';

/**
 * Options for searchWritten method
 * 
 * @public
 */
export interface SearchWrittenOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for searchEligiblePosts method
 * 
 * @public
 */
export interface SearchEligiblePostsOptions {
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
   * Search for Community Notes Written
   * Returns all the community notes written by the user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async searchWritten(
    options: SearchWrittenOptions = {}
  ): Promise<SearchWrittenResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/notes/search/notes_written';

    // Build query parameters
    const params = new URLSearchParams();

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
   * Delete a Community Note
   * Deletes a community note.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(): Promise<DeleteResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/notes/{id}';

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
   * Search for Posts Eligible for Community Notes
   * Returns all the posts that are eligible for community notes.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async searchEligiblePosts(
    options: SearchEligiblePostsOptions = {}
  ): Promise<SearchEligiblePostsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/notes/search/posts_eligible_for_notes';

    // Build query parameters
    const params = new URLSearchParams();

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
   * Create a Community Note
   * Creates a community note endpoint for LLM use case.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(options: CreateOptions = {}): Promise<CreateResponse> {
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

    return this.client.request<CreateResponse>(
      'POST',
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
  async evaluate(options: EvaluateOptions = {}): Promise<EvaluateResponse> {
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

    return this.client.request<EvaluateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
