/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the Stream endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  StreamLikesFirehoseResponse,
  StreamPostsFirehoseEnResponse,
  StreamLikesSample10Response,
  StreamPostsComplianceResponse,
  StreamPostsSampleResponse,
  StreamPostsFirehoseJaResponse,
  StreamPostsFirehoseKoResponse,
  StreamLabelsComplianceResponse,
  StreamPostsSample10Response,
  StreamPostsFirehoseResponse,
  StreamUsersComplianceResponse,
  StreamPostsResponse,
  StreamPostsFirehosePtResponse,
  StreamGetRulesResponse,
  StreamUpdateRulesRequest,
  StreamUpdateRulesResponse,
  StreamGetRuleCountsResponse,
  StreamLikesComplianceResponse,
} from './models.js';

/**
 * Client for Stream operations
 */
export class StreamClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Stream all Likes
     * Streams all public Likes in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param likeWithTweetAuthorfields A comma separated list of LikeWithTweetAuthor fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async likesFirehose(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    likeWithTweetAuthorfields?: any,
    expansions?: any,
    userfields?: any,
    tweetfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamLikesFirehoseResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
    }

    if (likeWithTweetAuthorfields !== undefined) {
      params.set(
        'like_with_tweet_author.fields',
        String(likeWithTweetAuthorfields)
      );
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/likes/firehose/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamLikesFirehoseResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream English Posts
     * Streams all public English-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsFirehoseEn(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsFirehoseEnResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/firehose/stream/lang/en`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsFirehoseEnResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream sampled Likes
     * Streams a 10% sample of public Likes in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param likeWithTweetAuthorfields A comma separated list of LikeWithTweetAuthor fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async likesSample10(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    likeWithTweetAuthorfields?: any,
    expansions?: any,
    userfields?: any,
    tweetfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamLikesSample10Response>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
    }

    if (likeWithTweetAuthorfields !== undefined) {
      params.set(
        'like_with_tweet_author.fields',
        String(likeWithTweetAuthorfields)
      );
    }

    if (expansions !== undefined) {
      params.set('expansions', String(expansions));
    }

    if (userfields !== undefined) {
      params.set('user.fields', String(userfields));
    }

    if (tweetfields !== undefined) {
      params.set('tweet.fields', String(tweetfields));
    }

    const path = `/2/likes/sample10/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamLikesSample10Response>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Posts compliance data
     * Streams all compliance data related to Posts.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsCompliance(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsComplianceResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
    }

    const path = `/2/tweets/compliance/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsComplianceResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream sampled Posts
     * Streams a 1% sample of public Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsSample(
    backfillMinutes?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsSampleResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
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

    const path = `/2/tweets/sample/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsSampleResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Japanese Posts
     * Streams all public Japanese-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsFirehoseJa(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsFirehoseJaResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/firehose/stream/lang/ja`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsFirehoseJaResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Korean Posts
     * Streams all public Korean-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsFirehoseKo(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsFirehoseKoResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/firehose/stream/lang/ko`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsFirehoseKoResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Post labels
     * Streams all labeling events applied to Posts.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.* @param options Additional request options
     * @returns Promise with the API response
     */
  async labelsCompliance(
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamLabelsComplianceResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
    }

    const path = `/2/tweets/label/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamLabelsComplianceResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream 10% sampled Posts
     * Streams a 10% sample of public Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsSample10(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsSample10Response>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/sample10/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsSample10Response>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream all Posts
     * Streams all public Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsFirehose(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsFirehoseResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/firehose/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsFirehoseResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Users compliance data
     * Streams all compliance data related to Users.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.* @param options Additional request options
     * @returns Promise with the API response
     */
  async usersCompliance(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamUsersComplianceResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
    }

    const path = `/2/users/compliance/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamUsersComplianceResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream filtered Posts
     * Streams Posts in real-time matching the active rule set.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async posts(
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/search/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Portuguese Posts
     * Streams all public Portuguese-language Posts in real-time.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param partition The partition number.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
     * @param tweetfields A comma separated list of Tweet fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param pollfields A comma separated list of Poll fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param placefields A comma separated list of Place fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async postsFirehosePt(
    partition: any,
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    tweetfields?: any,
    expansions?: any,
    mediafields?: any,
    pollfields?: any,
    userfields?: any,
    placefields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamPostsFirehosePtResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.set('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
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

    const path = `/2/tweets/firehose/stream/lang/pt`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamPostsFirehosePtResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get stream rules
     * Retrieves the active rule set or a subset of rules for the filtered stream.
     * @param ids A comma-separated list of Rule IDs.
     * @param maxResults The maximum number of results.
     * @param paginationToken This value is populated by passing the 'next_token' returned in a request to paginate through results.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getRules(
    ids?: any,
    maxResults?: any,
    paginationToken?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamGetRulesResponse>> {
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.set('ids', String(ids));
    }

    if (maxResults !== undefined) {
      params.set('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set('pagination_token', String(paginationToken));
    }

    const path = `/2/tweets/search/stream/rules`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamGetRulesResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Update stream rules
     * Adds or deletes rules from the active rule set for the filtered stream.
     * @param dryRun Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
     * @param deleteAll Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async updateRules(
    dryRun?: any,
    deleteAll?: any,
    body?: StreamUpdateRulesRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamUpdateRulesResponse>> {
    const params = new URLSearchParams();

    if (dryRun !== undefined) {
      params.set('dry_run', String(dryRun));
    }

    if (deleteAll !== undefined) {
      params.set('delete_all', String(deleteAll));
    }

    const path = `/2/tweets/search/stream/rules`;

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

    return this.client.request<StreamUpdateRulesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get stream rule counts
     * Retrieves the count of rules in the active rule set for the filtered stream.
     * @param rulesCountfields A comma separated list of RulesCount fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getRuleCounts(
    rulesCountfields?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamGetRuleCountsResponse>> {
    const params = new URLSearchParams();

    if (rulesCountfields !== undefined) {
      params.set('rules_count.fields', String(rulesCountfields));
    }

    const path = `/2/tweets/search/stream/rules/counts`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamGetRuleCountsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Stream Likes compliance data
     * Streams all compliance data related to Likes for Users.
     * @param backfillMinutes The number of minutes of backfill requested.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided.* @param options Additional request options
     * @returns Promise with the API response
     */
  async likesCompliance(
    backfillMinutes?: any,
    startTime?: any,
    endTime?: any,
    options?: RequestOptions
  ): Promise<ApiResponse<StreamLikesComplianceResponse>> {
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.set('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.set('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.set('end_time', String(endTime));
    }

    const path = `/2/likes/compliance/stream`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<StreamLikesComplianceResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
