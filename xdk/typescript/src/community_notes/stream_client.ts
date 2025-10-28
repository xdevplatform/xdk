/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  CommunityNotesSearchNotesWrittenResponse,
  CommunityNotesSearchForEligiblePostsResponse,
  CommunityNotesCreateNotesResponse,
  CommunityNotesDeleteNotesResponse,
} from './models.js';

/**
 * Options for searchNotesWritten method
 */
export interface CommunityNotesSearchNotesWrittenStreamingOptions {
  /** Pagination token to get next set of posts eligible for notes. */
  paginationToken?: string;

  /** Max results to return. */
  maxResults?: number;

  /** A comma separated list of Note fields to display. */
  notefields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for searchForEligiblePosts method
 */
export interface CommunityNotesSearchForEligiblePostsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for createNotes method
 */
export interface CommunityNotesCreateNotesStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class CommunityNotesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Search for Community Notes Written
     * Returns all the community notes written by the user.
     * 
     * @returns Promise with the API response
     */
  async searchNotesWritten(
    testMode: boolean,
    options: CommunityNotesSearchNotesWrittenStreamingOptions = {}
  ): Promise<CommunityNotesSearchNotesWrittenResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'searchNotesWritten');

    // Destructure options with defaults

    const {
      paginationToken = undefined,

      maxResults = undefined,

      notefields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/notes/search/notes_written`;

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
    return this.client.request<CommunityNotesSearchNotesWrittenResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search for Posts Eligible for Community Notes
     * Returns all the posts that are eligible for community notes.
     * 
     * @returns Promise with the API response
     */
  async searchForEligiblePosts(
    testMode: boolean,
    options: CommunityNotesSearchForEligiblePostsStreamingOptions = {}
  ): Promise<CommunityNotesSearchForEligiblePostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'searchForEligiblePosts'
    );

    // Destructure options with defaults

    const {
      paginationToken = undefined,

      maxResults = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

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

    // Build path parameters
    let path = `/2/notes/search/posts_eligible_for_notes`;

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
    return this.client.request<CommunityNotesSearchForEligiblePostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create a Community Note
     * Creates a community note endpoint for LLM use case.
     * 
     * @returns Promise with the API response
     */
  async createNotes(
    options: CommunityNotesCreateNotesStreamingOptions = {}
  ): Promise<CommunityNotesCreateNotesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createNotes');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/notes`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<CommunityNotesCreateNotesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete a Community Note
     * Deletes a community note.
     * 
     * @returns Promise with the API response
     */
  async deleteNotes(id: string): Promise<CommunityNotesDeleteNotesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteNotes');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/notes/{id}`;

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
    return this.client.request<CommunityNotesDeleteNotesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
