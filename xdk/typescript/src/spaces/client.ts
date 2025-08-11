/**
 * Spaces client for the X API.
 *
 * This module provides a client for interacting with the Spaces endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  SpacesGetPostsResponse,
  SpacesGetByIdResponse,
  SpacesGetByCreatorIdsResponse,
  SpacesSearchResponse,
  SpacesGetByIdsResponse,
  SpacesGetBuyersResponse,
} from './models.js';

/**
 * Client for Spaces operations
 */
export class SpacesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Space Posts
     * Retrieves a list of Posts shared in a specific Space by its ID.
     * @param id The ID of the Space to be retrieved.
     * @param maxResults The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getPosts(
    options?: RequestOptions
  ): Promise<ApiResponse<SpacesGetPostsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/spaces/{id}/tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<SpacesGetPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get space by ID
     * Retrieves details of a specific space by its ID.
     * @param id The ID of the Space to be retrieved.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getById(
    options?: RequestOptions
  ): Promise<ApiResponse<SpacesGetByIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/spaces/{id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<SpacesGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Spaces by creator IDs
     * Retrieves details of Spaces created by specified User IDs.
     * @param userIds The IDs of Users to search through.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByCreatorIds(
    options?: RequestOptions
  ): Promise<ApiResponse<SpacesGetByCreatorIdsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/spaces/by/creator_ids`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<SpacesGetByCreatorIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Search Spaces
     * Retrieves a list of Spaces matching the specified search query.
     * @param query The search query.
     * @param state The state of Spaces to search for.
     * @param maxResults The number of results to return.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async search(
    options?: RequestOptions
  ): Promise<ApiResponse<SpacesSearchResponse>> {
    const params = new URLSearchParams();

    const path = `/2/spaces/search`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<SpacesSearchResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Spaces by IDs
     * Retrieves details of multiple Spaces by their IDs.
     * @param ids The list of Space IDs to return.
     * @param spacefields A comma separated list of Space fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param topicfields A comma separated list of Topic fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByIds(
    options?: RequestOptions
  ): Promise<ApiResponse<SpacesGetByIdsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/spaces`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<SpacesGetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Space ticket buyers
     * Retrieves a list of Users who purchased tickets to a specific Space by its ID.
     * @param id The ID of the Space to be retrieved.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param maxResults The maximum number of results.
     * @param userfields A comma separated list of User fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getBuyers(
    options?: RequestOptions
  ): Promise<ApiResponse<SpacesGetBuyersResponse>> {
    const params = new URLSearchParams();

    const path = `/2/spaces/{id}/buyers`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<SpacesGetBuyersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
