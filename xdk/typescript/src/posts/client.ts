
/**
 * Posts client for the X API.
 *
 * This module provides a client for interacting with the Posts endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { 
    TwitterPaginator, 
    TweetPaginator, 
    UserPaginator, 
    ListPaginator, 
    IdPaginator 
} from '../paginator.js';
import {
PostsUnrepostResponse,
PostsSearchAllResponse,
PostsGetUsersTimelineResponse,
PostsGetUsersResponse,
PostsUnlikeResponse,
PostsGetAnalyticsResponse,
PostsGetUsersMentionsResponse,
PostsGetInsights28HrResponse,
PostsGetByIdResponse,
PostsDeleteResponse,
PostsSearchRecentResponse,
PostsGetRepostsResponse,
PostsGetByIdsResponse,
PostsCreateRequest,
PostsCreateResponse,
PostsGetCountsRecentResponse,
PostsGetInsightsHistoricalResponse,
PostsHideReplyRequest,
PostsHideReplyResponse,
PostsGetUsersLikedResponse,
PostsRepostRequest,
PostsRepostResponse,
PostsLikeRequest,
PostsLikeResponse,
PostsGetListsResponse,
PostsGetQuotedPostsResponse,
PostsGetCountsAllResponse,
} from './models.js';



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
 * Options for getUsersTimeline method
 */
export interface PostsGetUsersTimelineOptions {
    
    
    /** The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified. */
    sinceId?: string;
    
    
    
    /** The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified. */
    untilId?: string;
    
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
    /** The set of entities to exclude (e.g. 'replies' or 'retweets'). */
    exclude?: Array<any>;
    
    
    
    /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified. */
    startTime?: string;
    
    
    
    /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified. */
    endTime?: string;
    
    
    
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
 * Options for getUsers method
 */
export interface PostsGetUsersOptions {
    
    
    /** The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified. */
    sinceId?: string;
    
    
    
    /** The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified. */
    untilId?: string;
    
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
    /** The set of entities to exclude (e.g. 'replies' or 'retweets'). */
    exclude?: Array<any>;
    
    
    
    /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified. */
    startTime?: string;
    
    
    
    /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified. */
    endTime?: string;
    
    
    
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
 * Options for getAnalytics method
 */
export interface PostsGetAnalyticsOptions {
    
    
    /** A comma separated list of Analytics fields to display. */
    analyticsfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getUsersMentions method
 */
export interface PostsGetUsersMentionsOptions {
    
    
    /** The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified. */
    sinceId?: string;
    
    
    
    /** The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified. */
    untilId?: string;
    
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
    /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified. */
    startTime?: string;
    
    
    
    /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified. */
    endTime?: string;
    
    
    
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
 * Options for getInsightsHistorical method
 */
export interface PostsGetInsightsHistoricalOptions {
    
    
    /** A comma separated list of Engagement fields to display. */
    engagementfields?: Array<any>;
    
    
    
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
 * Options for getUsersLiked method
 */
export interface PostsGetUsersLikedOptions {
    
    
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
 * Options for repost method
 */
export interface PostsRepostOptions {
    
    
    /** Request body */
    body?: PostsRepostRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for like method
 */
export interface PostsLikeOptions {
    
    
    /** Request body */
    body?: PostsLikeRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getLists method
 */
export interface PostsGetListsOptions {
    
    
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
 * Client for Posts operations
 */
export class PostsClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }


  /**
   * Unrepost Post
   * Causes the authenticated user to unrepost a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to repost the Post.
   * @param sourceTweetId The ID of the Post that the User is requesting to unretweet.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unrepost(
        
        
        
        id: string,
        
        
        
        sourceTweetId: string,
        
        
        
        
        
        
    ): Promise<PostsUnrepostResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/retweets/{source_tweet_id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        
        
        path = path.replace('{source_tweet_id}', encodeURIComponent(String(sourceTweetId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<PostsUnrepostResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }










  /**
   * Unlike Post
   * Causes the authenticated user to Unlike a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to unlike the Post.
   * @param tweetId The ID of the Post that the User is requesting to unlike.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unlike(
        
        
        
        id: string,
        
        
        
        tweetId: string,
        
        
        
        
        
        
    ): Promise<PostsUnlikeResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/likes/{tweet_id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        
        
        path = path.replace('{tweet_id}', encodeURIComponent(String(tweetId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<PostsUnlikeResponse>(
            'DELETE',
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
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/tweets/analytics';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (ids !== undefined) {
            
            ids.forEach(item => params.append('ids', String(item)));
            
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
            
            analyticsfields.forEach(item => params.append('analytics.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsGetAnalyticsResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
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
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/insights/28hr';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (tweetIds !== undefined) {
            
            tweetIds.forEach(item => params.append('tweet_ids', String(item)));
            
        }
        
        
        
        
        
        if (granularity !== undefined) {
            
            params.append('granularity', String(granularity));
            
        }
        
        
        
        
        
        if (requestedMetrics !== undefined) {
            
            requestedMetrics.forEach(item => params.append('requested_metrics', String(item)));
            
        }
        
        
        
        
        
        if (engagementfields !== undefined) {
            
            engagementfields.forEach(item => params.append('engagement.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsGetInsights28HrResponse>(
            'GET',
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
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/tweets/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (tweetfields !== undefined) {
            
            tweetfields.forEach(item => params.append('tweet.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (mediafields !== undefined) {
            
            mediafields.forEach(item => params.append('media.fields', String(item)));
            
        }
        
        
        
        
        
        if (pollfields !== undefined) {
            
            pollfields.forEach(item => params.append('poll.fields', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (placefields !== undefined) {
            
            placefields.forEach(item => params.append('place.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
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
    async delete(
        
        
        
        id: string,
        
        
        
        
        
        
    ): Promise<PostsDeleteResponse> {
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
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/tweets';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (ids !== undefined) {
            
            ids.forEach(item => params.append('ids', String(item)));
            
        }
        
        
        
        
        
        if (tweetfields !== undefined) {
            
            tweetfields.forEach(item => params.append('tweet.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (mediafields !== undefined) {
            
            mediafields.forEach(item => params.append('media.fields', String(item)));
            
        }
        
        
        
        
        
        if (pollfields !== undefined) {
            
            pollfields.forEach(item => params.append('poll.fields', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (placefields !== undefined) {
            
            placefields.forEach(item => params.append('place.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsGetByIdsResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Create Post
   * Creates a new Post for the authenticated user.* @param body Request body
* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async create(
        
        
        
        
        body: PostsCreateRequest,
        
        
        
    ): Promise<PostsCreateResponse> {
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
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/insights/historical';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (tweetIds !== undefined) {
            
            tweetIds.forEach(item => params.append('tweet_ids', String(item)));
            
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
            
            requestedMetrics.forEach(item => params.append('requested_metrics', String(item)));
            
        }
        
        
        
        
        
        if (engagementfields !== undefined) {
            
            engagementfields.forEach(item => params.append('engagement.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsGetInsightsHistoricalResponse>(
            'GET',
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
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/tweets/{tweet_id}/hidden';
        
        
        path = path.replace('{tweet_id}', encodeURIComponent(String(tweetId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsHideReplyResponse>(
            'PUT',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Repost Post
   * Causes the authenticated user to repost a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to repost the Post.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async repost(
        
        
        
        id: string,
        
        
        
        
        
        
        options: PostsRepostOptions = {}
        
    ): Promise<PostsRepostResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}/retweets';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsRepostResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Like Post
   * Causes the authenticated user to Like a specific Post by its ID.
   * @param id The ID of the authenticated source User that is requesting to like the Post.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async like(
        
        
        
        id: string,
        
        
        
        
        
        
        options: PostsLikeOptions = {}
        
    ): Promise<PostsLikeResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}/likes';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<PostsLikeResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
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
  searchAll(
    
    
    
    query: string,
    
    
    
    
    options: PostsSearchAllOptions = {}
    
  ): TwitterPaginator<any> {
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
        
        
        requestOptions: reqOpts = {}
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
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsSearchAllResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TwitterPaginator(fetchPage);
  }




  /**
   * Get Timeline
   * Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsersTimeline(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetUsersTimelineOptions = {}
    
  ): UserPaginator {
    // Destructure options
    
    const {
        
        
        sinceId = undefined,
        
        
        
        untilId = undefined,
        
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        exclude = [],
        
        
        
        startTime = undefined,
        
        
        
        endTime = undefined,
        
        
        
        tweetfields = [],
        
        
        
        expansions = [],
        
        
        
        mediafields = [],
        
        
        
        pollfields = [],
        
        
        
        userfields = [],
        
        
        
        placefields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/timelines/reverse_chronological';
    
    
    path = path.replace('{id}', encodeURIComponent(String(id)));
    
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (sinceId !== undefined) {
          
          params.append('since_id', String(sinceId));
          
      }
      
      
      
      
      
      if (untilId !== undefined) {
          
          params.append('until_id', String(untilId));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (exclude !== undefined) {
          
          exclude.forEach(item => params.append('exclude', String(item)));
          
      }
      
      
      
      
      
      if (startTime !== undefined) {
          
          params.append('start_time', String(startTime));
          
      }
      
      
      
      
      
      if (endTime !== undefined) {
          
          params.append('end_time', String(endTime));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetUsersTimelineResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new UserPaginator(fetchPage);
  }




  /**
   * Get Posts
   * Retrieves a list of posts authored by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsers(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetUsersOptions = {}
    
  ): UserPaginator {
    // Destructure options
    
    const {
        
        
        sinceId = undefined,
        
        
        
        untilId = undefined,
        
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        exclude = [],
        
        
        
        startTime = undefined,
        
        
        
        endTime = undefined,
        
        
        
        tweetfields = [],
        
        
        
        expansions = [],
        
        
        
        mediafields = [],
        
        
        
        pollfields = [],
        
        
        
        userfields = [],
        
        
        
        placefields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/tweets';
    
    
    path = path.replace('{id}', encodeURIComponent(String(id)));
    
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (sinceId !== undefined) {
          
          params.append('since_id', String(sinceId));
          
      }
      
      
      
      
      
      if (untilId !== undefined) {
          
          params.append('until_id', String(untilId));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (exclude !== undefined) {
          
          exclude.forEach(item => params.append('exclude', String(item)));
          
      }
      
      
      
      
      
      if (startTime !== undefined) {
          
          params.append('start_time', String(startTime));
          
      }
      
      
      
      
      
      if (endTime !== undefined) {
          
          params.append('end_time', String(endTime));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetUsersResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new UserPaginator(fetchPage);
  }








  /**
   * Get mentions
   * Retrieves a list of Posts that mention a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsersMentions(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetUsersMentionsOptions = {}
    
  ): UserPaginator {
    // Destructure options
    
    const {
        
        
        sinceId = undefined,
        
        
        
        untilId = undefined,
        
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        startTime = undefined,
        
        
        
        endTime = undefined,
        
        
        
        tweetfields = [],
        
        
        
        expansions = [],
        
        
        
        mediafields = [],
        
        
        
        pollfields = [],
        
        
        
        userfields = [],
        
        
        
        placefields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/mentions';
    
    
    path = path.replace('{id}', encodeURIComponent(String(id)));
    
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (sinceId !== undefined) {
          
          params.append('since_id', String(sinceId));
          
      }
      
      
      
      
      
      if (untilId !== undefined) {
          
          params.append('until_id', String(untilId));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (startTime !== undefined) {
          
          params.append('start_time', String(startTime));
          
      }
      
      
      
      
      
      if (endTime !== undefined) {
          
          params.append('end_time', String(endTime));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetUsersMentionsResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new UserPaginator(fetchPage);
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
  searchRecent(
    
    
    
    query: string,
    
    
    
    
    options: PostsSearchRecentOptions = {}
    
  ): TwitterPaginator<any> {
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
        
        
        requestOptions: reqOpts = {}
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
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsSearchRecentResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TwitterPaginator(fetchPage);
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
  getReposts(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetRepostsOptions = {}
    
  ): TweetPaginator {
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
        
        
        requestOptions: reqOpts = {}
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
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetRepostsResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TweetPaginator(fetchPage);
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
  getCountsRecent(
    
    
    
    query: string,
    
    
    
    
    options: PostsGetCountsRecentOptions = {}
    
  ): TwitterPaginator<any> {
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
        
        
        requestOptions: reqOpts = {}
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
          
          searchCountfields.forEach(item => params.append('search_count.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetCountsRecentResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TwitterPaginator(fetchPage);
  }








  /**
   * Get liked Posts
   * Retrieves a list of Posts liked by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsersLiked(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetUsersLikedOptions = {}
    
  ): UserPaginator {
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
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/liked_tweets';
    
    
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
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetUsersLikedResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new UserPaginator(fetchPage);
  }








  /**
   * Get List Posts
   * Retrieves a list of Posts associated with a specific List by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getLists(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetListsOptions = {}
    
  ): ListPaginator {
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
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/lists/{id}/tweets';
    
    
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
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetListsResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new ListPaginator(fetchPage);
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
  getQuotedPosts(
    
    
    
    id: string,
    
    
    
    
    options: PostsGetQuotedPostsOptions = {}
    
  ): TweetPaginator {
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
        
        
        requestOptions: reqOpts = {}
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
          
          exclude.forEach(item => params.append('exclude', String(item)));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetQuotedPostsResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TweetPaginator(fetchPage);
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
  getCountsAll(
    
    
    
    query: string,
    
    
    
    
    options: PostsGetCountsAllOptions = {}
    
  ): TwitterPaginator<any> {
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
        
        
        requestOptions: reqOpts = {}
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
          
          searchCountfields.forEach(item => params.append('search_count.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<PostsGetCountsAllResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TwitterPaginator(fetchPage);
  }



}
