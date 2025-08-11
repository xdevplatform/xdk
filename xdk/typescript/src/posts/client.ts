/**
 * Posts client for the X API.
 *
 * This module provides a client for interacting with the Posts endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  PostsHideReplyRequest,
  PostsHideReplyResponse,
  PostsSearchAllResponse,
  PostsGetUsersTimelineResponse,
  PostsUnrepostResponse,
  PostsGetUsersResponse,
  PostsLikeRequest,
  PostsLikeResponse,
  PostsGetAnalyticsResponse,
  PostsGetCountsRecentResponse,
  PostsGetRepostsResponse,
  PostsGetByIdResponse,
  PostsDeleteResponse,
  PostsGetUsersMentionsResponse,
  PostsSearchRecentResponse,
  PostsGetQuotedPostsResponse,
  PostsGetByIdsResponse,
  PostsCreateRequest,
  PostsCreateResponse,
  PostsGetCountsAllResponse,
  PostsGetInsightsHistoricalResponse,
  PostsGetUsersLikedResponse,
  PostsRepostRequest,
  PostsRepostResponse,
  PostsGetListsResponse,
  PostsGetInsights28HrResponse,
  PostsUnlikeResponse,
} from './models.js';

/**
 * Client for Posts operations
 */
export class PostsClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Hide reply
     * Hides or unhides a reply to a conversation owned by the authenticated user.
     * @param tweetId The ID of the reply that you want to hide or unhide.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async hideReply(
    body?: PostsHideReplyRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<PostsHideReplyResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/{tweet_id}/hidden`;

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

    return this.client.request<PostsHideReplyResponse>(
      'PUT',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Search all Posts
     * Retrieves Posts from the full archive matching a search query.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param maxResults The maximum number of search results to be returned by a request.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param sortOrder This order in which to return results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async searchAll(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsSearchAllResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/search/all`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsSearchAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Timeline
     * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
     * @param id The ID of the authenticated source User to list Reverse Chronological Timeline Posts of.
     * @param sinceId The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
     * @param untilId The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param exclude The set of entities to exclude (e.g. 'replies' or 'retweets').
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersTimeline(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetUsersTimelineResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/timelines/reverse_chronological`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetUsersTimelineResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unrepost Post
     * Causes the authenticated user to unrepost a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to repost the Post.
     * @param sourceTweetId The ID of the Post that the User is requesting to unretweet.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unrepost(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsUnrepostResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/retweets/{source_tweet_id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsUnrepostResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Posts
     * Retrieves a list of posts authored by a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param sinceId The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
     * @param untilId The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param exclude The set of entities to exclude (e.g. 'replies' or 'retweets').
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsers(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetUsersResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetUsersResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Like Post
     * Causes the authenticated user to Like a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to like the Post.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async like(
    body?: PostsLikeRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<PostsLikeResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/likes`;

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

    return this.client.request<PostsLikeResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Post analytics
     * Retrieves analytics data for specified Posts within a defined time range.
     * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
     * @param granularity The granularity for the search counts results.
     * @param analyticsfields A comma separated list of Analytics fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getAnalytics(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetAnalyticsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/analytics`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get count of recent Posts
     * Retrieves the count of Posts from the last 7 days matching a search query.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param granularity The granularity for the search counts results.
     * @param searchCountfields A comma separated list of SearchCount fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getCountsRecent(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetCountsRecentResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/counts/recent`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetCountsRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Reposts
     * Retrieves a list of Posts that repost a specific Post by its ID.
     * @param id A single Post ID.
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
  async getReposts(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetRepostsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/{id}/retweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetRepostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Post by ID
     * Retrieves details of a specific Post by its ID.
     * @param id A single Post ID.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getById(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetByIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/{id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete Post
     * Deletes a specific Post by its ID, if owned by the authenticated user.
     * @param id The ID of the Post to be deleted.* @param options Additional request options
     * @returns Promise with the API response
     */
  async delete(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsDeleteResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/{id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsDeleteResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get mentions
     * Retrieves a list of Posts that mention a specific User by their ID.
     * @param id The ID of the User to lookup.
     * @param sinceId The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
     * @param untilId The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUsersMentions(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetUsersMentionsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/mentions`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetUsersMentionsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Search recent Posts
     * Retrieves Posts from the last 7 days matching a search query.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param maxResults The maximum number of search results to be returned by a request.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param sortOrder This order in which to return results.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async searchRecent(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsSearchRecentResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/search/recent`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsSearchRecentResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Quoted Posts
     * Retrieves a list of Posts that quote a specific Post by its ID.
     * @param id A single Post ID.
     * @param maxResults The maximum number of results to be returned.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param exclude The set of entities to exclude (e.g. 'replies' or 'retweets').
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getQuotedPosts(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetQuotedPostsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/{id}/quote_tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetQuotedPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Posts by IDs
     * Retrieves details of multiple Posts by their IDs.
     * @param ids A comma separated list of Post IDs. Up to 100 are allowed in a single request.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByIds(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetByIdsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetByIdsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create Post
     * Creates a new Post for the authenticated user.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async create(
    body: PostsCreateRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<PostsCreateResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets`;

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

    return this.client.request<PostsCreateResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get count of all Posts
     * Retrieves the count of Posts matching a search query from the full archive.
     * @param query One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
     * @param sinceId Returns results with a Post ID greater than (that is, more recent than) the specified ID.
     * @param untilId Returns results with a Post ID less than (that is, older than) the specified ID.
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * @param granularity The granularity for the search counts results.
     * @param searchCountfields A comma separated list of SearchCount fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getCountsAll(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetCountsAllResponse>> {
    const params = new URLSearchParams();

    const path = `/2/tweets/counts/all`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetCountsAllResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get historical Post insights
     * Retrieves historical engagement metrics for specified Posts within a defined time range.
     * @param tweetIds List of PostIds for historical metrics.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
     * @param granularity granularity of metrics response.
     * @param requestedMetrics request metrics for historical request.
     * @param engagementfields A comma separated list of Engagement fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getInsightsHistorical(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetInsightsHistoricalResponse>> {
    const params = new URLSearchParams();

    const path = `/2/insights/historical`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetInsightsHistoricalResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get liked Posts
     * Retrieves a list of Posts liked by a specific User by their ID.
     * @param id The ID of the User to lookup.
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
  async getUsersLiked(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetUsersLikedResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/liked_tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetUsersLikedResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Repost Post
     * Causes the authenticated user to repost a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to repost the Post.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async repost(
    body?: PostsRepostRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<PostsRepostResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/retweets`;

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

    return this.client.request<PostsRepostResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get List Posts
     * Retrieves a list of Posts associated with a specific List by its ID.
     * @param id The ID of the List.
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
  async getLists(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetListsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/lists/{id}/tweets`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetListsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get 28-hour Post insights
     * Retrieves engagement metrics for specified Posts over the last 28 hours.
     * @param tweetIds List of PostIds for 28hr metrics.
     * @param granularity granularity of metrics response.
     * @param requestedMetrics request metrics for historical request.
     * @param engagementfields A comma separated list of Engagement fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getInsights28Hr(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsGetInsights28HrResponse>> {
    const params = new URLSearchParams();

    const path = `/2/insights/28hr`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsGetInsights28HrResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Unlike Post
     * Causes the authenticated user to Unlike a specific Post by its ID.
     * @param id The ID of the authenticated source User that is requesting to unlike the Post.
     * @param tweetId The ID of the Post that the User is requesting to unlike.* @param options Additional request options
     * @returns Promise with the API response
     */
  async unlike(
    options?: RequestOptions
  ): Promise<ApiResponse<PostsUnlikeResponse>> {
    const params = new URLSearchParams();

    const path = `/2/users/{id}/likes/{tweet_id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<PostsUnlikeResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
