/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  PostsSampleResponse,
  PostsFirehoseEnResponse,
  PostsSample10Response,
  LikesFirehoseResponse,
  GetRuleCountsResponse,
  LikesSample10Response,
  PostsFirehoseResponse,
  PostsFirehoseKoResponse,
  GetRulesResponse,
  UpdateRulesResponse,
  LabelsComplianceResponse,
  PostsComplianceResponse,
  UsersComplianceResponse,
  PostsResponse,
  LikesComplianceResponse,
  PostsFirehosePtResponse,
  PostsFirehoseJaResponse,
} from './models.js';

/**
 * Options for postsSample method
 * 
 * @public
 */
export interface PostsSampleStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsFirehoseEn method
 * 
 * @public
 */
export interface PostsFirehoseEnStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsSample10 method
 * 
 * @public
 */
export interface PostsSample10StreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for likesFirehose method
 * 
 * @public
 */
export interface LikesFirehoseStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getRuleCounts method
 * 
 * @public
 */
export interface GetRuleCountsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for likesSample10 method
 * 
 * @public
 */
export interface LikesSample10StreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsFirehose method
 * 
 * @public
 */
export interface PostsFirehoseStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsFirehoseKo method
 * 
 * @public
 */
export interface PostsFirehoseKoStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getRules method
 * 
 * @public
 */
export interface GetRulesStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for updateRules method
 * 
 * @public
 */
export interface UpdateRulesStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for labelsCompliance method
 * 
 * @public
 */
export interface LabelsComplianceStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsCompliance method
 * 
 * @public
 */
export interface PostsComplianceStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for usersCompliance method
 * 
 * @public
 */
export interface UsersComplianceStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for posts method
 * 
 * @public
 */
export interface PostsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for likesCompliance method
 * 
 * @public
 */
export interface LikesComplianceStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsFirehosePt method
 * 
 * @public
 */
export interface PostsFirehosePtStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for postsFirehoseJa method
 * 
 * @public
 */
export interface PostsFirehoseJaStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class StreamClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
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
    options: PostsSampleStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsSample');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: PostsFirehoseEnStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehoseEn');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: PostsSample10StreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsSample10');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: LikesFirehoseStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likesFirehose');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: LikesSample10StreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likesSample10');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: PostsFirehoseStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehose');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: PostsFirehoseKoStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehoseKo');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: LabelsComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'labelsCompliance');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: PostsComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsCompliance');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: UsersComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'usersCompliance');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
  async posts(options: PostsStreamingOptions = {}): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'posts');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: LikesComplianceStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'likesCompliance');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
     * Stream Portuguese Posts
     * Streams all public Portuguese-language Posts in real-time.
     * 
     * Returns an event-driven stream that's easy to use.
     * Use .on() to listen for events like 'data', 'error', 'close'.
     * Also supports async iteration with for await...of.
     */
  async postsFirehosePt(
    options: PostsFirehosePtStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehosePt');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: PostsFirehoseJaStreamingOptions = {}
  ): Promise<EventDrivenStream> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'postsFirehoseJa');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

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
        ...(options.headers || {}),
      },

      signal: options.signal,
      raw: true, // Get raw Response object for streaming
      timeout: 0, // Disable timeout for streaming requests
      ...options,
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
    options: GetRuleCountsStreamingOptions = {}
  ): Promise<GetRuleCountsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRuleCounts');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/stream/rules/counts`;

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
    return this.client.request<GetRuleCountsResponse>(
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
    options: GetRulesStreamingOptions = {}
  ): Promise<GetRulesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getRules');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/stream/rules`;

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
    return this.client.request<GetRulesResponse>(
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
    options: UpdateRulesStreamingOptions = {}
  ): Promise<UpdateRulesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'updateRules');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/tweets/search/stream/rules`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<UpdateRulesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
