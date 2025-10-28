/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  MediaInitializeUploadResponse,
  MediaFinalizeUploadResponse,
  MediaCreateSubtitlesResponse,
  MediaDeleteSubtitlesResponse,
  MediaGetUploadStatusResponse,
  MediaUploadResponse,
  MediaGetByMediaKeyResponse,
  MediaGetByMediaKeysResponse,
  MediaGetAnalyticsResponse,
  MediaCreateMetadataResponse,
  MediaAppendUploadResponse,
} from './models.js';

/**
 * Options for initializeUpload method
 */
export interface MediaInitializeUploadStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for createSubtitles method
 */
export interface MediaCreateSubtitlesStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for deleteSubtitles method
 */
export interface MediaDeleteSubtitlesStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getUploadStatus method
 */
export interface MediaGetUploadStatusStreamingOptions {
  /** The command for the media upload request. */
  command?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for upload method
 */
export interface MediaUploadStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getByMediaKey method
 */
export interface MediaGetByMediaKeyStreamingOptions {
  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getByMediaKeys method
 */
export interface MediaGetByMediaKeysStreamingOptions {
  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getAnalytics method
 */
export interface MediaGetAnalyticsStreamingOptions {
  /** A comma separated list of MediaAnalytics fields to display. */
  mediaAnalyticsfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for createMetadata method
 */
export interface MediaCreateMetadataStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for appendUpload method
 */
export interface MediaAppendUploadStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class MediaClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Initialize media upload
     * Initializes a media upload.
     * 
     * @returns Promise with the API response
     */
  async initializeUpload(
    options: MediaInitializeUploadStreamingOptions = {}
  ): Promise<MediaInitializeUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'initializeUpload');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/upload/initialize`;

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
    return this.client.request<MediaInitializeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Finalize Media upload
     * Finalizes a Media upload request.
     * 
     * @returns Promise with the API response
     */
  async finalizeUpload(id: string): Promise<MediaFinalizeUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'finalizeUpload');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/upload/{id}/finalize`;

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
    return this.client.request<MediaFinalizeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create Media subtitles
     * Creates subtitles for a specific Media file.
     * 
     * @returns Promise with the API response
     */
  async createSubtitles(
    options: MediaCreateSubtitlesStreamingOptions = {}
  ): Promise<MediaCreateSubtitlesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createSubtitles');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/subtitles`;

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
    return this.client.request<MediaCreateSubtitlesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete Media subtitles
     * Deletes subtitles for a specific Media file.
     * 
     * @returns Promise with the API response
     */
  async deleteSubtitles(
    options: MediaDeleteSubtitlesStreamingOptions = {}
  ): Promise<MediaDeleteSubtitlesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteSubtitles');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/subtitles`;

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
    return this.client.request<MediaDeleteSubtitlesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Media upload status
     * Retrieves the status of a Media upload by its ID.
     * 
     * @returns Promise with the API response
     */
  async getUploadStatus(
    mediaId: string,
    options: MediaGetUploadStatusStreamingOptions = {}
  ): Promise<MediaGetUploadStatusResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getUploadStatus');

    // Destructure options with defaults

    const {
      command = undefined,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (mediaId !== undefined) {
      params.append('media_id', String(mediaId));
    }

    if (command !== undefined) {
      params.append('command', String(command));
    }

    // Build path parameters
    let path = `/2/media/upload`;

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
    return this.client.request<MediaGetUploadStatusResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Upload media
     * Uploads a media file for use in posts or other content.
     * 
     * @returns Promise with the API response
     */
  async upload(
    options: MediaUploadStreamingOptions = {}
  ): Promise<MediaUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'upload');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/upload`;

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
    return this.client.request<MediaUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Media by media key
     * Retrieves details of a specific Media file by its media key.
     * 
     * @returns Promise with the API response
     */
  async getByMediaKey(
    mediaKey: string,
    options: MediaGetByMediaKeyStreamingOptions = {}
  ): Promise<MediaGetByMediaKeyResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByMediaKey');

    // Destructure options with defaults

    const {
      mediafields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    // Build path parameters
    let path = `/2/media/{media_key}`;

    path = path.replace(`{${'media_key'}}`, String(mediaKey));

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
    return this.client.request<MediaGetByMediaKeyResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Media by media keys
     * Retrieves details of Media files by their media keys.
     * 
     * @returns Promise with the API response
     */
  async getByMediaKeys(
    mediaKeys: Array<any>,
    options: MediaGetByMediaKeysStreamingOptions = {}
  ): Promise<MediaGetByMediaKeysResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByMediaKeys');

    // Destructure options with defaults

    const {
      mediafields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (mediaKeys !== undefined) {
      params.append('media_keys', String(mediaKeys));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    // Build path parameters
    let path = `/2/media`;

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
    return this.client.request<MediaGetByMediaKeysResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Media analytics
     * Retrieves analytics data for media.
     * 
     * @returns Promise with the API response
     */
  async getAnalytics(
    mediaKeys: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    options: MediaGetAnalyticsStreamingOptions = {}
  ): Promise<MediaGetAnalyticsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getAnalytics');

    // Destructure options with defaults

    const {
      mediaAnalyticsfields = [],

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (mediaKeys !== undefined) {
      params.append('media_keys', String(mediaKeys));
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

    if (mediaAnalyticsfields !== undefined) {
      params.append('media_analytics.fields', mediaAnalyticsfields.join(','));
    }

    // Build path parameters
    let path = `/2/media/analytics`;

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
    return this.client.request<MediaGetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create Media metadata
     * Creates metadata for a Media file.
     * 
     * @returns Promise with the API response
     */
  async createMetadata(
    options: MediaCreateMetadataStreamingOptions = {}
  ): Promise<MediaCreateMetadataResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createMetadata');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/metadata`;

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
    return this.client.request<MediaCreateMetadataResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Append Media upload
     * Appends data to a Media upload request.
     * 
     * @returns Promise with the API response
     */
  async appendUpload(
    id: string,
    options: MediaAppendUploadStreamingOptions = {}
  ): Promise<MediaAppendUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'appendUpload');

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/media/upload/{id}/append`;

    path = path.replace(`{${'id'}}`, String(id));

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
    return this.client.request<MediaAppendUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
