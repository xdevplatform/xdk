/**
 * Trends client for the X API.
 *
 * This module provides a client for interacting with the Trends endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  TrendsGetByWoeidResponse,
  TrendsGetUsersPersonalizedResponse,
} from './models.js';

/**
 * Client for Trends operations
 */
export class TrendsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Trends by WOEID
     * Retrieves trending topics for a specific location identified by its WOEID.
     * @param woeid The WOEID of the place to lookup a trend for.
     * @param maxTrends The maximum number of results.
     * @param trendfields A comma separated list of Trend fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByWoeid(
    woeid: number,
    trendfields?: Array<any>,
    maxTrends?: number,
    options?: RequestOptions
  ): Promise<ApiResponse<TrendsGetByWoeidResponse>> {
    const params = new URLSearchParams();

    if (maxTrends !== undefined) {
      params.set('max_trends', String(maxTrends));
    }

    if (trendfields !== undefined) {
      params.set('trend.fields', String(trendfields));
    }

    const path = `/2/trends/by/woeid/{woeid}`.replace('{woeid}', String(woeid));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<TrendsGetByWoeidResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get personalized Trends
     * Retrieves personalized trending topics for the authenticated user.
     * @param personalizedTrendfields A comma separated list of PersonalizedTrend fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersPersonalized(
    personalizedTrendfields?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<TrendsGetUsersPersonalizedResponse>> {
    const params = new URLSearchParams();

    if (personalizedTrendfields !== undefined) {
      params.set('personalized_trend.fields', String(personalizedTrendfields));
    }

    const path = `/2/users/personalized_trends`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<TrendsGetUsersPersonalizedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
