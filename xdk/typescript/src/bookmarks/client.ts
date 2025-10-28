/**
 * Bookmarks client for the X API.
 *
 * This module provides a client for interacting with the Bookmarks endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import {
  BookmarksGetUsersByFolderIdResponse,
  BookmarksGetUsersResponse,
  BookmarksCreateUsersRequest,
  BookmarksCreateUsersResponse,
  BookmarksDeleteUsersResponse,
  BookmarksGetUsersFoldersResponse,
} from './models.js';

/**
 * Options for getUsers method
 */
export interface BookmarksGetUsersOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

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
 * Options for getUsersFolders method
 */
export interface BookmarksGetUsersFoldersOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Bookmarks operations
 * 
 * This client provides methods for interacting with the Bookmarks endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Bookmarks related operations.
 * 
 * @category Bookmarks
 */
export class BookmarksClient {
  private client: Client;

  /**
     * Creates a new Bookmarks client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get Bookmarks by folder ID
   * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
   * @param id The ID of the authenticated source User for whom to return results.
   * @param folderId The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getUsersByFolderId(
    id: string,
    folderId: string
  ): Promise<BookmarksGetUsersByFolderIdResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/folders/{folder_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{folder_id}', encodeURIComponent(String(folderId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<BookmarksGetUsersByFolderIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create Bookmark
   * Adds a post to the authenticated user’s bookmarks.
   * @param id The ID of the authenticated source User for whom to add bookmarks.* @param body Request body
* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createUsers(
    id: string,
    body: BookmarksCreateUsersRequest
  ): Promise<BookmarksCreateUsersResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<BookmarksCreateUsersResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete Bookmark
   * Removes a Post from the authenticated user’s Bookmarks by its ID.
   * @param id The ID of the authenticated source User whose bookmark is to be removed.
   * @param tweetId The ID of the Post that the source User is removing from bookmarks.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteUsers(
    id: string,
    tweetId: string
  ): Promise<BookmarksDeleteUsersResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/{tweet_id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    path = path.replace('{tweet_id}', encodeURIComponent(String(tweetId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<BookmarksDeleteUsersResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Bookmarks
   * Retrieves a list of Posts bookmarked by the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getUsers(
    id: string,
    options: BookmarksGetUsersOptions = {}
  ): Promise<UserPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
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
        ...reqOpts,
      };

      const response = await this.client.request<BookmarksGetUsersResponse>(
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
    const paginator = new UserPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Bookmark folders
   * Retrieves a list of Bookmark folders created by the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getUsersFolders(
    id: string,
    options: BookmarksGetUsersFoldersOptions = {}
  ): Promise<UserPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/{id}/bookmarks/folders';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();

      if (maxResults !== undefined) {
        params.append('max_results', String(maxResults));
      }

      if (paginationToken !== undefined) {
        params.append('pagination_token', String(paginationToken));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<
        BookmarksGetUsersFoldersResponse
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
    const paginator = new UserPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }
}
