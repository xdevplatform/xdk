/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  TrendsGetByWoeidResponse,
  TrendsGetPersonalizedTrendsResponse,
} from './models.js';

/**
 * Options for getByWoeid method
 */
export interface TrendsGetByWoeidStreamingOptions {
  /** The maximum number of results. */
  maxTrends?: number;

  /** A comma separated list of Trend fields to display. */
  trendfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getPersonalizedTrends method
 */
export interface TrendsGetPersonalizedTrendsStreamingOptions {
  /** A comma separated list of PersonalizedTrend fields to display. */
  personalizedTrendfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class TrendsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Trends by WOEID
     * Retrieves trending topics for a specific location identified by its WOEID.
     * 
     * @returns Promise with the API response
     */
  async getByWoeid(
    woeid: number,
    options: TrendsGetByWoeidStreamingOptions = {}
  ): Promise<TrendsGetByWoeidResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByWoeid');

    // Destructure options with defaults

    const {
      maxTrends = undefined,

      trendfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (maxTrends !== undefined) {
      params.append('max_trends', String(maxTrends));
    }

    if (trendfields !== undefined) {
      params.append('trend.fields', trendfields.join(','));
    }

    // Build path parameters
    let path = `/2/trends/by/woeid/{woeid}`;

    path = path.replace(`{${'woeid'}}`, String(woeid));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<TrendsGetByWoeidResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get personalized Trends
     * Retrieves personalized trending topics for the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async getPersonalizedTrends(
    options: TrendsGetPersonalizedTrendsStreamingOptions = {}
  ): Promise<TrendsGetPersonalizedTrendsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getPersonalizedTrends'
    );

    // Destructure options with defaults

    const {
      personalizedTrendfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (personalizedTrendfields !== undefined) {
      params.append(
        'personalized_trend.fields',
        personalizedTrendfields.join(',')
      );
    }

    // Build path parameters
    let path = `/2/users/personalized_trends`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<TrendsGetPersonalizedTrendsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
