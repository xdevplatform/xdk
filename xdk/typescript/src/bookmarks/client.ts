/**
 * Bookmarks client for the X API.
 *
 * This module provides a client for interacting with the Bookmarks endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  BookmarksGetUsersFoldersResponse,
  BookmarksDeleteUsersResponse,
  BookmarksGetUsersByFolderIdResponse,
  BookmarksGetUsersResponse,
  BookmarksCreateUsersRequest,
  BookmarksCreateUsersResponse,
} from './models.js';

/**
 * Client for Bookmarks operations
 */
export class BookmarksClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Bookmark folders
     * Retrieves a list of Bookmark folders created by the authenticated user.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersFolders(
    id: string,
    paginationToken?: string,
    maxResults?: number,
    options?: RequestOptions
  ): Promise<ApiResponse<BookmarksGetUsersFoldersResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    const path = `/2/users/{id}/bookmarks/folders`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<BookmarksGetUsersFoldersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete Bookmark
     * Removes a Post from the authenticated user’s Bookmarks by its ID.
     * @param id The ID of the authenticated source User whose bookmark is to be removed.
     * @param tweetId The ID of the Post that the source User is removing from bookmarks.* @param options Additional request options
     * @returns Promise with the API response
     */
  async deleteUsers(
    tweetId: string,
    id: string,
    options?: RequestOptions
  ): Promise<ApiResponse<BookmarksDeleteUsersResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/bookmarks/{tweet_id}`
      .replace('{id}', String(id))
      .replace('{tweet_id}', String(tweetId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<BookmarksDeleteUsersResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Bookmarks by folder ID
     * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param folderId The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersByFolderId(
    folderId: string,
    id: string,
    options?: RequestOptions
  ): Promise<ApiResponse<BookmarksGetUsersByFolderIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/bookmarks/folders/{folder_id}`
      .replace('{id}', String(id))
      .replace('{folder_id}', String(folderId));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<BookmarksGetUsersByFolderIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Bookmarks
     * Retrieves a list of Posts bookmarked by the authenticated user.
     * @param id The ID of the authenticated source User for whom to return results.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsers(
    id: string,
    placefields?: Array<any>,
    userfields?: Array<any>,
    pollfields?: Array<any>,
    mediafields?: Array<any>,
    tweetfields?: Array<any>,
    paginationToken?: string,
    maxResults?: number,
    expansions?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<BookmarksGetUsersResponse>> {
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (mediafields !== undefined) {
      params.set('media.fields', String(mediafields));
    }

    if (pollfields !== undefined) {
      params.set('poll.fields', String(pollfields));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (placefields !== undefined) {
      params.set('place.fields', String(placefields));
    }

    const path = `/2/users/{id}/bookmarks`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<BookmarksGetUsersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create Bookmark
     * Adds a post to the authenticated user’s bookmarks.
     * @param id The ID of the authenticated source User for whom to add bookmarks.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createUsers(
    id: string,
    body: BookmarksCreateUsersRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<BookmarksCreateUsersResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/bookmarks`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<BookmarksCreateUsersResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
