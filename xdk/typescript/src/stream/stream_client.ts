/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  StreamGetRuleCountsResponse,
  StreamPostsFirehosePtResponse,
  StreamPostsSample10Response,
  StreamUsersComplianceResponse,
  StreamLikesFirehoseResponse,
  StreamPostsComplianceResponse,
  StreamPostsResponse,
  StreamPostsFirehoseEnResponse,
  StreamPostsFirehoseKoResponse,
  StreamPostsFirehoseResponse,
  StreamLikesSample10Response,
  StreamLikesComplianceResponse,
  StreamPostsFirehoseJaResponse,
  StreamGetRulesResponse,
  StreamUpdateRulesResponse,
  StreamLabelsComplianceResponse,
  StreamPostsSampleResponse,
} from './models.js';

/**
 * Options for getRuleCounts method
 */
export interface StreamGetRuleCountsStreamingOptions {
  /** A comma separated list of RulesCount fields to display. */
  rulesCountfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsFirehosePt method
 */
export interface StreamPostsFirehosePtStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsSample10 method
 */
export interface StreamPostsSample10StreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for usersCompliance method
 */
export interface StreamUsersComplianceStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided. */
  endTime?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for likesFirehose method
 */
export interface StreamLikesFirehoseStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
  endTime?: string;

  /** A comma separated list of LikeWithTweetAuthor fields to display. */
  likeWithTweetAuthorfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsCompliance method
 */
export interface StreamPostsComplianceStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided. */
  endTime?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for posts method
 */
export interface StreamPostsStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsFirehoseEn method
 */
export interface StreamPostsFirehoseEnStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsFirehoseKo method
 */
export interface StreamPostsFirehoseKoStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsFirehose method
 */
export interface StreamPostsFirehoseStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for likesSample10 method
 */
export interface StreamLikesSample10StreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
  endTime?: string;

  /** A comma separated list of LikeWithTweetAuthor fields to display. */
  likeWithTweetAuthorfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for likesCompliance method
 */
export interface StreamLikesComplianceStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided. */
  endTime?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsFirehoseJa method
 */
export interface StreamPostsFirehoseJaStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. */
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getRules method
 */
export interface StreamGetRulesStreamingOptions {
  /** A comma-separated list of Rule IDs. */
  ids?: Array<any>;

  /** The maximum number of results. */
  maxResults?: number;

  /** This value is populated by passing the 'next_token' returned in a request to paginate through results. */
  paginationToken?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for updateRules method
 */
export interface StreamUpdateRulesStreamingOptions {
  /** Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes. */
  dryRun?: boolean;

  /** Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered. */
  deleteAll?: boolean;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for labelsCompliance method
 */
export interface StreamLabelsComplianceStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

  /** YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided. */
  startTime?: string;

  /** YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided. */
  endTime?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for postsSample method
 */
export interface StreamPostsSampleStreamingOptions {
  /** The number of minutes of backfill requested. */
  backfillMinutes?: number;

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

export class StreamClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Stream Portuguese Posts
     * Streams all public Portuguese-language Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsFirehosePt(
    partition: number,
    options: StreamPostsFirehosePtStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehosePt');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/firehose/stream/lang/pt' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream 10% sampled Posts
     * Streams a 10% sample of public Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsSample10(
    partition: number,
    options: StreamPostsSample10StreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsSample10');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/sample10/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream Users compliance data
     * Streams all compliance data related to Users.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async usersCompliance(
    partition: number,
    options: StreamUsersComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'usersCompliance');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/users/compliance/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream all Likes
     * Streams all public Likes in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async likesFirehose(
    partition: number,
    options: StreamLikesFirehoseStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likesFirehose');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      likeWithTweetAuthorfields = [],

      expansions = [],

      userfields = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (likeWithTweetAuthorfields !== undefined) {
      params.append(
        'like_with_tweet_author.fields',
        likeWithTweetAuthorfields.join(',')
      );
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/likes/firehose/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream Posts compliance data
     * Streams all compliance data related to Posts.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsCompliance(
    partition: number,
    options: StreamPostsComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsCompliance');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/compliance/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream filtered Posts
     * Streams Posts in real-time matching the active rule set.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async posts(
    options: StreamPostsStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'posts');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/search/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream English Posts
     * Streams all public English-language Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsFirehoseEn(
    partition: number,
    options: StreamPostsFirehoseEnStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehoseEn');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/firehose/stream/lang/en' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream Korean Posts
     * Streams all public Korean-language Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsFirehoseKo(
    partition: number,
    options: StreamPostsFirehoseKoStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehoseKo');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/firehose/stream/lang/ko' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream all Posts
     * Streams all public Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsFirehose(
    partition: number,
    options: StreamPostsFirehoseStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehose');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/firehose/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream sampled Likes
     * Streams a 10% sample of public Likes in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async likesSample10(
    partition: number,
    options: StreamLikesSample10StreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likesSample10');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      likeWithTweetAuthorfields = [],

      expansions = [],

      userfields = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    if (likeWithTweetAuthorfields !== undefined) {
      params.append(
        'like_with_tweet_author.fields',
        likeWithTweetAuthorfields.join(',')
      );
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/likes/sample10/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream Likes compliance data
     * Streams all compliance data related to Likes for Users.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async likesCompliance(
    options: StreamLikesComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likesCompliance');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/likes/compliance/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream Japanese Posts
     * Streams all public Japanese-language Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsFirehoseJa(
    partition: number,
    options: StreamPostsFirehoseJaStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehoseJa');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (partition !== undefined) {
      params.append('partition', String(partition));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/firehose/stream/lang/ja' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream Post labels
     * Streams all labeling events applied to Posts.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async labelsCompliance(
    options: StreamLabelsComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'labelsCompliance');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

      startTime = undefined,

      endTime = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
    }

    if (startTime !== undefined) {
      params.append('start_time', String(startTime));
    }

    if (endTime !== undefined) {
      params.append('end_time', String(endTime));
    }

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/label/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Stream sampled Posts
     * Streams a 1% sample of public Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsSample(
    options: StreamPostsSampleStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsSample');

    // Destructure options with defaults

    const {
      backfillMinutes = undefined,

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

    if (backfillMinutes !== undefined) {
      params.append('backfill_minutes', String(backfillMinutes));
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

    // Make the authenticated request using the main client's request method
    // We need raw: true to get the raw Response object for streaming
    const url =
      '/2/tweets/sample/stream' +
      (params.toString() ? `?${params.toString()}` : '');

    // For streaming requests, we don't want to timeout the initial connection
    // Instead, we'll handle timeouts at the stream level
    const response = (await this.client.request('GET', url, {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...reqOpts,
    })) as Response;

    // Handle errors
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Return the readable stream
    // The response.body is the actual ReadableStream for streaming
    if (!response.body) {
      throw new Error('Response body is not available for streaming');
    }

    // Wrap the ReadableStream in an event-driven interface
    const eventStream = new EventDrivenStream();
    await eventStream.connect(response.body);
    return eventStream;
  }

  /**
     * Get stream rule counts
     * Retrieves the count of rules in the active rule set for the filtered stream.
     * 
     * @returns Promise with the API response
     */
  async getRuleCounts(
    options: StreamGetRuleCountsStreamingOptions = {}
  ): Promise<StreamGetRuleCountsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRuleCounts');

    // Destructure options with defaults

    const {
      rulesCountfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (rulesCountfields !== undefined) {
      params.append('rules_count.fields', rulesCountfields.join(','));
    }

    // Build path parameters
    let path = `/2/tweets/search/stream/rules/counts`;

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
    return this.client.request<StreamGetRuleCountsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get stream rules
     * Retrieves the active rule set or a subset of rules for the filtered stream.
     * 
     * @returns Promise with the API response
     */
  async getRules(
    options: StreamGetRulesStreamingOptions = {}
  ): Promise<StreamGetRulesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRules');

    // Destructure options with defaults

    const {
      ids = [],

      maxResults = undefined,

      paginationToken = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (ids !== undefined) {
      params.append('ids', ids.join(','));
    }

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    // Build path parameters
    let path = `/2/tweets/search/stream/rules`;

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
    return this.client.request<StreamGetRulesResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Update stream rules
     * Adds or deletes rules from the active rule set for the filtered stream.
     * 
     * @returns Promise with the API response
     */
  async updateRules(
    body: any,
    options: StreamUpdateRulesStreamingOptions = {}
  ): Promise<StreamUpdateRulesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'updateRules');

    // Destructure options with defaults

    const {
      dryRun = undefined,

      deleteAll = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (dryRun !== undefined) {
      params.append('dry_run', String(dryRun));
    }

    if (deleteAll !== undefined) {
      params.append('delete_all', String(deleteAll));
    }

    // Build path parameters
    let path = `/2/tweets/search/stream/rules`;

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
    return this.client.request<StreamUpdateRulesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
