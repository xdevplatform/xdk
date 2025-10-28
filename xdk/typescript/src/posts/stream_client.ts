/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  PostsGetCountsAllResponse,
  PostsSearchAllResponse,
  PostsGetQuotedPostsResponse,
  PostsGetInsights28HrResponse,
  PostsGetAnalyticsResponse,
  PostsGetByIdsResponse,
  PostsCreateResponse,
  PostsGetRepostedByResponse,
  PostsHideReplyResponse,
  PostsGetCountsRecentResponse,
  PostsGetRepostsResponse,
  PostsGetLikingUsersResponse,
  PostsGetByIdResponse,
  PostsDeleteResponse,
  PostsSearchRecentResponse,
  PostsGetInsightsHistoricalResponse,
} from './models.js';

/**
 * Options for getCountsAll method
 */
export interface PostsGetCountsAllStreamingOptions {
  /** YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). */
  endTime?: string;

  /** Returns results with a Post ID greater than (that is, more recent than) the specified ID. */
  sinceId?: string;

  /** Returns results with a Post ID less than (that is, older than) the specified ID. */
  untilId?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  paginationToken?: string;

  /** The granularity for the search counts results. */
  granularity?: string;

  /** A comma separated list of SearchCount fields to display. */
  searchCountfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for searchAll method
 */
export interface PostsSearchAllStreamingOptions {
  /** YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). */
  endTime?: string;

  /** Returns results with a Post ID greater than (that is, more recent than) the specified ID. */
  sinceId?: string;

  /** Returns results with a Post ID less than (that is, older than) the specified ID. */
  untilId?: string;

  /** The maximum number of search results to be returned by a request. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  paginationToken?: string;

  /** This order in which to return results. */
  sortOrder?: string;

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
 * Options for getQuotedPosts method
 */
export interface PostsGetQuotedPostsStreamingOptions {
  /** The maximum number of results to be returned. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** The set of entities to exclude (e.g. 'replies' or 'retweets'). */
  exclude?: Array<any>;

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
 * Options for getInsights28Hr method
 */
export interface PostsGetInsights28HrStreamingOptions {
  /** A comma separated list of Engagement fields to display. */
  engagementfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getAnalytics method
 */
export interface PostsGetAnalyticsStreamingOptions {
  /** A comma separated list of Analytics fields to display. */
  analyticsfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getByIds method
 */
export interface PostsGetByIdsStreamingOptions {
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
 * Options for getRepostedBy method
 */
export interface PostsGetRepostedByStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for hideReply method
 */
export interface PostsHideReplyStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getCountsRecent method
 */
export interface PostsGetCountsRecentStreamingOptions {
  /** YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). */
  endTime?: string;

  /** Returns results with a Post ID greater than (that is, more recent than) the specified ID. */
  sinceId?: string;

  /** Returns results with a Post ID less than (that is, older than) the specified ID. */
  untilId?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  paginationToken?: string;

  /** The granularity for the search counts results. */
  granularity?: string;

  /** A comma separated list of SearchCount fields to display. */
  searchCountfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getReposts method
 */
export interface PostsGetRepostsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getLikingUsers method
 */
export interface PostsGetLikingUsersStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. */
  paginationToken?: string;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getById method
 */
export interface PostsGetByIdStreamingOptions {
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
 * Options for searchRecent method
 */
export interface PostsSearchRecentStreamingOptions {
  /** YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). */
  endTime?: string;

  /** Returns results with a Post ID greater than (that is, more recent than) the specified ID. */
  sinceId?: string;

  /** Returns results with a Post ID less than (that is, older than) the specified ID. */
  untilId?: string;

  /** The maximum number of search results to be returned by a request. */
  maxResults?: number;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  nextToken?: string;

  /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
  paginationToken?: string;

  /** This order in which to return results. */
  sortOrder?: string;

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
 * Options for getInsightsHistorical method
 */
export interface PostsGetInsightsHistoricalStreamingOptions {
  /** A comma separated list of Engagement fields to display. */
  engagementfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class PostsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get count of all Posts
     * Retrieves the count of Posts matching a search query from the full archive.
     * 
     * @returns Promise with the API response
     */
  async getCountsAll(
    query: string,
    options: PostsGetCountsAllStreamingOptions = {}
  ): Promise<PostsGetCountsAllResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getCountsAll');

    // Destructure options with defaults

    const {
      startTime = undefined,

      endTime = undefined,

      sinceId = undefined,

      untilId = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      granularity = undefined,

      searchCountfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.append('query', String(query));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (sinceId !== undefined) {
      params.append('since_id', String(sinceId));
    }

    if (untilId !== undefined) {
      params.append('until_id', String(untilId));
    }

    if (nextToken !== undefined) {
      params.append('next_token', String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (granularity !== undefined) {
      params.append('granularity', String(granularity));
    }

    if (searchCountfields !== undefined) {
      params.append('search_count.fields', searchCountfields.join(','));
    }

    // Build path parameters
    let path = `/2/tweets/counts/all`;

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
    return this.client.request<PostsGetCountsAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search all Posts
     * Retrieves Posts from the full archive matching a search query.
     * 
     * @returns Promise with the API response
     */
  async searchAll(
    query: string,
    options: PostsSearchAllStreamingOptions = {}
  ): Promise<PostsSearchAllResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'searchAll');

    // Destructure options with defaults

    const {
      startTime = undefined,

      endTime = undefined,

      sinceId = undefined,

      untilId = undefined,

      maxResults = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      sortOrder = undefined,

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

    if (query !== undefined) {
      params.append('query', String(query));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (sinceId !== undefined) {
      params.append('since_id', String(sinceId));
    }

    if (untilId !== undefined) {
      params.append('until_id', String(untilId));
    }

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (nextToken !== undefined) {
      params.append('next_token', String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (sortOrder !== undefined) {
      params.append('sort_order', String(sortOrder));
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
    let path = `/2/tweets/search/all`;

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
    return this.client.request<PostsSearchAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Quoted Posts
     * Retrieves a list of Posts that quote a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getQuotedPosts(
    id: string,
    options: PostsGetQuotedPostsStreamingOptions = {}
  ): Promise<PostsGetQuotedPostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getQuotedPosts');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      exclude = [],

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

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (exclude !== undefined) {
      params.append('exclude', exclude.join(','));
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
    let path = `/2/tweets/{id}/quote_tweets`;

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
    return this.client.request<PostsGetQuotedPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get 28-hour Post insights
     * Retrieves engagement metrics for specified Posts over the last 28 hours.
     * 
     * @returns Promise with the API response
     */
  async getInsights28Hr(
    tweetIds: Array<any>,
    granularity: string,
    requestedMetrics: Array<any>,
    options: PostsGetInsights28HrStreamingOptions = {}
  ): Promise<PostsGetInsights28HrResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getInsights28Hr');

    // Destructure options with defaults

    const {
      engagementfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (tweetIds !== undefined) {
      params.append('tweet_ids', String(tweetIds));
    }

    if (granularity !== undefined) {
      params.append('granularity', String(granularity));
    }

    if (requestedMetrics !== undefined) {
      params.append('requested_metrics', String(requestedMetrics));
    }

    if (engagementfields !== undefined) {
      params.append('engagement.fields', engagementfields.join(','));
    }

    // Build path parameters
    let path = `/2/insights/28hr`;

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
    return this.client.request<PostsGetInsights28HrResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Post analytics
     * Retrieves analytics data for specified Posts within a defined time range.
     * 
     * @returns Promise with the API response
     */
  async getAnalytics(
    ids: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    options: PostsGetAnalyticsStreamingOptions = {}
  ): Promise<PostsGetAnalyticsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getAnalytics');

    // Destructure options with defaults

    const {
      analyticsfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.append('ids', String(ids));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (granularity !== undefined) {
      params.append('granularity', String(granularity));
    }

    if (analyticsfields !== undefined) {
      params.append('analytics.fields', analyticsfields.join(','));
    }

    // Build path parameters
    let path = `/2/tweets/analytics`;

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
    return this.client.request<PostsGetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Posts by IDs
     * Retrieves details of multiple Posts by their IDs.
     * 
     * @returns Promise with the API response
     */
  async getByIds(
    ids: Array<any>,
    options: PostsGetByIdsStreamingOptions = {}
  ): Promise<PostsGetByIdsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByIds');

    // Destructure options with defaults

    const {
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

    if (ids !== undefined) {
      params.append('ids', String(ids));
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
    let path = `/2/tweets`;

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
    return this.client.request<PostsGetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create or Edit Post
     * Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.
     * 
     * @returns Promise with the API response
     */
  async create(body: any): Promise<PostsCreateResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'create');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets`;

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
    return this.client.request<PostsCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Reposted by
     * Retrieves a list of Users who reposted a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getRepostedBy(
    id: string,
    options: PostsGetRepostedByStreamingOptions = {}
  ): Promise<PostsGetRepostedByResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRepostedBy');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Build path parameters
    let path = `/2/tweets/{id}/retweeted_by`;

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
    return this.client.request<PostsGetRepostedByResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Hide reply
     * Hides or unhides a reply to a conversation owned by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async hideReply(
    tweetId: string,
    options: PostsHideReplyStreamingOptions = {}
  ): Promise<PostsHideReplyResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'hideReply');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{tweet_id}/hidden`;

    path = path.replace(`{${'tweet_id'}}`, String(tweetId));

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
    return this.client.request<PostsHideReplyResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get count of recent Posts
     * Retrieves the count of Posts from the last 7 days matching a search query.
     * 
     * @returns Promise with the API response
     */
  async getCountsRecent(
    query: string,
    options: PostsGetCountsRecentStreamingOptions = {}
  ): Promise<PostsGetCountsRecentResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getCountsRecent');

    // Destructure options with defaults

    const {
      startTime = undefined,

      endTime = undefined,

      sinceId = undefined,

      untilId = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      granularity = undefined,

      searchCountfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (query !== undefined) {
      params.append('query', String(query));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (sinceId !== undefined) {
      params.append('since_id', String(sinceId));
    }

    if (untilId !== undefined) {
      params.append('until_id', String(untilId));
    }

    if (nextToken !== undefined) {
      params.append('next_token', String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (granularity !== undefined) {
      params.append('granularity', String(granularity));
    }

    if (searchCountfields !== undefined) {
      params.append('search_count.fields', searchCountfields.join(','));
    }

    // Build path parameters
    let path = `/2/tweets/counts/recent`;

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
    return this.client.request<PostsGetCountsRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Reposts
     * Retrieves a list of Posts that repost a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getReposts(
    id: string,
    options: PostsGetRepostsStreamingOptions = {}
  ): Promise<PostsGetRepostsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getReposts');

    // Destructure options with defaults

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

    // Build path parameters
    let path = `/2/tweets/{id}/retweets`;

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
    return this.client.request<PostsGetRepostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Liking Users
     * Retrieves a list of Users who liked a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getLikingUsers(
    id: string,
    options: PostsGetLikingUsersStreamingOptions = {}
  ): Promise<PostsGetLikingUsersResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getLikingUsers');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Build path parameters
    let path = `/2/tweets/{id}/liking_users`;

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
    return this.client.request<PostsGetLikingUsersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Post by ID
     * Retrieves details of a specific Post by its ID.
     * 
     * @returns Promise with the API response
     */
  async getById(
    id: string,
    options: PostsGetByIdStreamingOptions = {}
  ): Promise<PostsGetByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getById');

    // Destructure options with defaults

    const {
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
    let path = `/2/tweets/{id}`;

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
    return this.client.request<PostsGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete Post
     * Deletes a specific Post by its ID, if owned by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async delete(id: string): Promise<PostsDeleteResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'delete');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/{id}`;

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
    return this.client.request<PostsDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Search recent Posts
     * Retrieves Posts from the last 7 days matching a search query.
     * 
     * @returns Promise with the API response
     */
  async searchRecent(
    query: string,
    options: PostsSearchRecentStreamingOptions = {}
  ): Promise<PostsSearchRecentResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'searchRecent');

    // Destructure options with defaults

    const {
      startTime = undefined,

      endTime = undefined,

      sinceId = undefined,

      untilId = undefined,

      maxResults = undefined,

      nextToken = undefined,

      paginationToken = undefined,

      sortOrder = undefined,

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

    if (query !== undefined) {
      params.append('query', String(query));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (sinceId !== undefined) {
      params.append('since_id', String(sinceId));
    }

    if (untilId !== undefined) {
      params.append('until_id', String(untilId));
    }

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (nextToken !== undefined) {
      params.append('next_token', String(nextToken));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (sortOrder !== undefined) {
      params.append('sort_order', String(sortOrder));
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
    let path = `/2/tweets/search/recent`;

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
    return this.client.request<PostsSearchRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get historical Post insights
     * Retrieves historical engagement metrics for specified Posts within a defined time range.
     * 
     * @returns Promise with the API response
     */
  async getInsightsHistorical(
    tweetIds: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    requestedMetrics: Array<any>,
    options: PostsGetInsightsHistoricalStreamingOptions = {}
  ): Promise<PostsGetInsightsHistoricalResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getInsightsHistorical'
    );

    // Destructure options with defaults

    const {
      engagementfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (tweetIds !== undefined) {
      params.append('tweet_ids', String(tweetIds));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (granularity !== undefined) {
      params.append('granularity', String(granularity));
    }

    if (requestedMetrics !== undefined) {
      params.append('requested_metrics', String(requestedMetrics));
    }

    if (engagementfields !== undefined) {
      params.append('engagement.fields', engagementfields.join(','));
    }

    // Build path parameters
    let path = `/2/insights/historical`;

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
    return this.client.request<PostsGetInsightsHistoricalResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
