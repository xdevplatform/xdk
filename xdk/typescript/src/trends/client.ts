/**
 * Trends client for the X API.
 *
 * This module provides a client for interacting with the Trends endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  TwitterPaginator,
  TweetPaginator,
  UserPaginator,
  ListPaginator,
  IdPaginator,
} from '../paginator.js';
import {
  TrendsGetUsersPersonalizedResponse,
  TrendsGetByWoeidResponse,
} from './models.js';

/**
 * Options for getUsersPersonalized method
 */
export interface TrendsGetUsersPersonalizedOptions {
  /** A comma separated list of PersonalizedTrend fields to display. */
  personalizedTrendfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByWoeid method
 */
export interface TrendsGetByWoeidOptions {
  /** The maximum number of results. */
  maxTrends?: number;

  /** A comma separated list of Trend fields to display. */
  trendfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Trends operations
 */
export class TrendsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get personalized Trends
   * Retrieves personalized trending topics for the authenticated user.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getUsersPersonalized(
    options: TrendsGetUsersPersonalizedOptions = {}
  ): Promise<TrendsGetUsersPersonalizedResponse> {
    // Destructure options

    const {
      personalizedTrendfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/users/personalized_trends';

    // Build query parameters
    const params = new URLSearchParams();

    if (personalizedTrendfields !== undefined) {
      personalizedTrendfields.forEach(item =>
        params.append('personalized_trend.fields', String(item))
      );
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<TrendsGetUsersPersonalizedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Trends by WOEID
   * Retrieves trending topics for a specific location identified by its WOEID.
   * @param woeid The WOEID of the place to lookup a trend for.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByWoeid(
    woeid: number,
    options: TrendsGetByWoeidOptions = {}
  ): Promise<TrendsGetByWoeidResponse> {
    // Destructure options

    const {
      maxTrends = undefined,

      trendfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/trends/by/woeid/{woeid}';

    path = path.replace('{woeid}', encodeURIComponent(String(woeid)));

    // Build query parameters
    const params = new URLSearchParams();

    if (maxTrends !== undefined) {
      params.append('max_trends', String(maxTrends));
    }

    if (trendfields !== undefined) {
      trendfields.forEach(item => params.append('trend.fields', String(item)));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<TrendsGetByWoeidResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
