/**
 * Posts client for the X API.
 *
 * This module provides a client for interacting with the Posts endpoints of the X API.
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
  PostsGetCountsAllResponse,
  PostsSearchAllResponse,
  PostsGetQuotedPostsResponse,
  PostsGetInsights28HrResponse,
  PostsGetAnalyticsResponse,
  PostsGetByIdsResponse,
  PostsCreateRequest,
  PostsCreateResponse,
  PostsGetRepostedByResponse,
  PostsHideReplyRequest,
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
export interface PostsGetCountsAllOptions {
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
}

/**
 * Options for searchAll method
 */
export interface PostsSearchAllOptions {
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
}

/**
 * Options for getQuotedPosts method
 */
export interface PostsGetQuotedPostsOptions {
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
}

/**
 * Options for getInsights28Hr method
 */
export interface PostsGetInsights28HrOptions {
  /** A comma separated list of Engagement fields to display. */
  engagementfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getAnalytics method
 */
export interface PostsGetAnalyticsOptions {
  /** A comma separated list of Analytics fields to display. */
  analyticsfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByIds method
 */
export interface PostsGetByIdsOptions {
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
 * Options for getRepostedBy method
 */
export interface PostsGetRepostedByOptions {
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
}

/**
 * Options for hideReply method
 */
export interface PostsHideReplyOptions {
  /** Request body */
  body?: PostsHideReplyRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getCountsRecent method
 */
export interface PostsGetCountsRecentOptions {
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
}

/**
 * Options for getReposts method
 */
export interface PostsGetRepostsOptions {
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
 * Options for getLikingUsers method
 */
export interface PostsGetLikingUsersOptions {
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
}

/**
 * Options for getById method
 */
export interface PostsGetByIdOptions {
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
 * Options for searchRecent method
 */
export interface PostsSearchRecentOptions {
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
}

/**
 * Options for getInsightsHistorical method
 */
export interface PostsGetInsightsHistoricalOptions {
  /** A comma separated list of Engagement fields to display. */
  engagementfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Posts operations
 * 
 * This client provides methods for interacting with the Posts endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Posts related operations.
 * 
 * @category Posts
 */
export class PostsClient {
  private client: Client;

  /**
     * Creates a new Posts client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get 28-hour Post insights
   * Retrieves engagement metrics for specified Posts over the last 28 hours.
   * @param tweetIds List of PostIds for 28hr metrics.
   * @param granularity granularity of metrics response.
   * @param requestedMetrics request metrics for historical request.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getInsights28Hr(
    tweetIds: Array<any>,
    granularity: string,
    requestedMetrics: Array<any>,
    options: PostsGetInsights28HrOptions = {}
  ): Promise<PostsGetInsights28HrResponse> {
    // Destructure options

    const {
      engagementfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/insights/28hr';

    // Build query parameters
    const params = new URLSearchParams();

    if (tweetIds !== undefined) {
      params.append('tweet_ids', tweetIds.join(','));
    }

    if (granularity !== undefined) {
      params.append('granularity', String(granularity));
    }

    if (requestedMetrics !== undefined) {
      params.append('requested_metrics', requestedMetrics.join(','));
    }

    if (engagementfields !== undefined) {
      params.append('engagement.fields', engagementfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<PostsGetInsights28HrResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Post analytics
   * Retrieves analytics data for specified Posts within a defined time range.
   * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
   * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
   * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
   * @param granularity The granularity for the search counts results.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getAnalytics(
    ids: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    options: PostsGetAnalyticsOptions = {}
  ): Promise<PostsGetAnalyticsResponse> {
    // Destructure options

    const {
      analyticsfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets/analytics';

    // Build query parameters
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.append('ids', ids.join(','));
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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<PostsGetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Posts by IDs
   * Retrieves details of multiple Posts by their IDs.
   * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByIds(
    ids: Array<any>,
    options: PostsGetByIdsOptions = {}
  ): Promise<PostsGetByIdsResponse> {
    // Destructure options

    const {
      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.append('ids', ids.join(','));
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
      ...reqOpts,
    };

    return this.client.request<PostsGetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create or Edit Post
   * Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.* @param body Request body
* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async create(body: PostsCreateRequest): Promise<PostsCreateResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/tweets';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<PostsCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Hide reply
   * Hides or unhides a reply to a conversation owned by the authenticated user.
   * @param tweetId The ID of the reply that you want to hide or unhide.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async hideReply(
    tweetId: string,
    options: PostsHideReplyOptions = {}
  ): Promise<PostsHideReplyResponse> {
    // Destructure options

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{tweet_id}/hidden';

    path = path.replace('{tweet_id}', encodeURIComponent(String(tweetId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...reqOpts,
    };

    return this.client.request<PostsHideReplyResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Post by ID
   * Retrieves details of a specific Post by its ID.
   * @param id A single Post ID.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getById(
    id: string,
    options: PostsGetByIdOptions = {}
  ): Promise<PostsGetByIdResponse> {
    // Destructure options

    const {
      tweetfields = [],

      expansions = [],

      mediafields = [],

      pollfields = [],

      userfields = [],

      placefields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<PostsGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete Post
   * Deletes a specific Post by its ID, if owned by the authenticated user.
   * @param id The ID of the Post to be deleted.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async delete(id: string): Promise<PostsDeleteResponse> {
    // Destructure options

    const reqOpts = {};

    // Build the path with path parameters
    let path = '/2/tweets/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<PostsDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get historical Post insights
   * Retrieves historical engagement metrics for specified Posts within a defined time range.
   * @param tweetIds List of PostIds for historical metrics.
   * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
   * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
   * @param granularity granularity of metrics response.
   * @param requestedMetrics request metrics for historical request.* @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getInsightsHistorical(
    tweetIds: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    requestedMetrics: Array<any>,
    options: PostsGetInsightsHistoricalOptions = {}
  ): Promise<PostsGetInsightsHistoricalResponse> {
    // Destructure options

    const {
      engagementfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/insights/historical';

    // Build query parameters
    const params = new URLSearchParams();

    if (tweetIds !== undefined) {
      params.append('tweet_ids', tweetIds.join(','));
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
      params.append('requested_metrics', requestedMetrics.join(','));
    }

    if (engagementfields !== undefined) {
      params.append('engagement.fields', engagementfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...reqOpts,
    };

    return this.client.request<PostsGetInsightsHistoricalResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get count of all Posts
   * Retrieves the count of Posts matching a search query from the full archive.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getCountsAll(
    query: string,
    options: PostsGetCountsAllOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/tweets/counts/all';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsGetCountsAllResponse>(
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
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Search all Posts
   * Retrieves Posts from the full archive matching a search query.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async searchAll(
    query: string,
    options: PostsSearchAllOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/tweets/search/all';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsSearchAllResponse>(
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
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Quoted Posts
   * Retrieves a list of Posts that quote a specific Post by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getQuotedPosts(
    id: string,
    options: PostsGetQuotedPostsOptions = {}
  ): Promise<PostPaginator> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/tweets/{id}/quote_tweets';

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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsGetQuotedPostsResponse>(
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
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Reposted by
   * Retrieves a list of Users who reposted a specific Post by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getRepostedBy(
    id: string,
    options: PostsGetRepostedByOptions = {}
  ): Promise<PostPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}/retweeted_by';

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

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsGetRepostedByResponse>(
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
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get count of recent Posts
   * Retrieves the count of Posts from the last 7 days matching a search query.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getCountsRecent(
    query: string,
    options: PostsGetCountsRecentOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/tweets/counts/recent';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsGetCountsRecentResponse>(
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
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Reposts
   * Retrieves a list of Posts that repost a specific Post by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getReposts(
    id: string,
    options: PostsGetRepostsOptions = {}
  ): Promise<PostPaginator> {
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
    let path = '/2/tweets/{id}/retweets';

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

      const response = await this.client.request<PostsGetRepostsResponse>(
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
    const paginator = new PostPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get Liking Users
   * Retrieves a list of Users who liked a specific Post by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getLikingUsers(
    id: string,
    options: PostsGetLikingUsersOptions = {}
  ): Promise<UserPaginator> {
    // Destructure options

    const {
      maxResults = undefined,

      paginationToken = undefined,

      userfields = [],

      expansions = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/tweets/{id}/liking_users';

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

      if (userfields !== undefined) {
        params.append('user.fields', userfields.join(','));
      }

      if (expansions !== undefined) {
        params.append('expansions', expansions.join(','));
      }

      if (tweetfields !== undefined) {
        params.append('tweet.fields', tweetfields.join(','));
      }

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsGetLikingUsersResponse>(
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
   * Search recent Posts
   * Retrieves Posts from the last 7 days matching a search query.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async searchRecent(
    query: string,
    options: PostsSearchRecentOptions = {}
  ): Promise<Paginator<any>> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/tweets/search/recent';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...reqOpts,
      };

      const response = await this.client.request<PostsSearchRecentResponse>(
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
    const paginator = new Paginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }
}
