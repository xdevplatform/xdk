/**
 * Media client for the X API.
 *
 * This module provides a client for interacting with the Media endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  MediaFinalizeUploadResponse,
  MediaGetAnalyticsResponse,
  MediaAppendUploadRequest,
  MediaAppendUploadResponse,
  MediaInitializeUploadRequest,
  MediaInitializeUploadResponse,
  MediaGetByMediaKeysResponse,
  MediaCreateSubtitlesRequest,
  MediaCreateSubtitlesResponse,
  MediaDeleteSubtitlesRequest,
  MediaDeleteSubtitlesResponse,
  MediaGetByMediaKeyResponse,
  MediaCreateMetadataRequest,
  MediaCreateMetadataResponse,
  MediaGetUploadStatusResponse,
  MediaUploadRequest,
  MediaUploadResponse,
} from './models.js';

/**
 * Options for getAnalytics method
 */
export interface MediaGetAnalyticsOptions {
  /** A comma separated list of MediaAnalytics fields to display. */
  mediaAnalyticsfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for appendUpload method
 */
export interface MediaAppendUploadOptions {
  /** Request body */
  body?: MediaAppendUploadRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for initializeUpload method
 */
export interface MediaInitializeUploadOptions {
  /** Request body */
  body?: MediaInitializeUploadRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByMediaKeys method
 */
export interface MediaGetByMediaKeysOptions {
  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createSubtitles method
 */
export interface MediaCreateSubtitlesOptions {
  /** Request body */
  body?: MediaCreateSubtitlesRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for deleteSubtitles method
 */
export interface MediaDeleteSubtitlesOptions {
  /** Request body */
  body?: MediaDeleteSubtitlesRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getByMediaKey method
 */
export interface MediaGetByMediaKeyOptions {
  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createMetadata method
 */
export interface MediaCreateMetadataOptions {
  /** Request body */
  body?: MediaCreateMetadataRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getUploadStatus method
 */
export interface MediaGetUploadStatusOptions {
  /** The command for the media upload request. */
  command?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for upload method
 */
export interface MediaUploadOptions {
  /** Request body */
  body?: MediaUploadRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Media operations
 * 
 * This client provides methods for interacting with the Media endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Media related operations.
 * 
 * @category Media
 */
export class MediaClient {
  private client: Client;

  /**
     * Creates a new Media client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Finalize Media upload
   * Finalizes a Media upload request.


   * @param id The media id of the targeted media to finalize.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async finalizeUpload(id: string): Promise<MediaFinalizeUploadResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/media/upload/{id}/finalize';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<MediaFinalizeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media analytics
   * Retrieves analytics data for media.


   * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.



   * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.



   * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.



   * @param granularity The granularity for the search counts results.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getAnalytics(
    mediaKeys: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    options: MediaGetAnalyticsOptions = {}
  ): Promise<MediaGetAnalyticsResponse> {
    // Destructure options

    const {
      mediaAnalyticsfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/analytics';

    // Build query parameters
    const params = new URLSearchParams();

    if (mediaKeys !== undefined) {
      params.append('media_keys', mediaKeys.join(','));
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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<MediaGetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Append Media upload
   * Appends data to a Media upload request.


   * @param id The media identifier for the media to perform the append operation.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async appendUpload(
    id: string,
    options: MediaAppendUploadOptions = {}
  ): Promise<MediaAppendUploadResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/upload/{id}/append';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MediaAppendUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Initialize media upload
   * Initializes a media upload.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async initializeUpload(
    options: MediaInitializeUploadOptions = {}
  ): Promise<MediaInitializeUploadResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/upload/initialize';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MediaInitializeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media by media keys
   * Retrieves details of Media files by their media keys.


   * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByMediaKeys(
    mediaKeys: Array<any>,
    options: MediaGetByMediaKeysOptions = {}
  ): Promise<MediaGetByMediaKeysResponse> {
    // Destructure options

    const {
      mediafields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media';

    // Build query parameters
    const params = new URLSearchParams();

    if (mediaKeys !== undefined) {
      params.append('media_keys', mediaKeys.join(','));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<MediaGetByMediaKeysResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create Media subtitles
   * Creates subtitles for a specific Media file.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createSubtitles(
    options: MediaCreateSubtitlesOptions = {}
  ): Promise<MediaCreateSubtitlesResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/subtitles';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MediaCreateSubtitlesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete Media subtitles
   * Deletes subtitles for a specific Media file.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteSubtitles(
    options: MediaDeleteSubtitlesOptions = {}
  ): Promise<MediaDeleteSubtitlesResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/subtitles';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MediaDeleteSubtitlesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media by media key
   * Retrieves details of a specific Media file by its media key.


   * @param mediaKey A single Media Key.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByMediaKey(
    mediaKey: string,
    options: MediaGetByMediaKeyOptions = {}
  ): Promise<MediaGetByMediaKeyResponse> {
    // Destructure options

    const {
      mediafields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/{media_key}';

    path = path.replace('{media_key}', encodeURIComponent(String(mediaKey)));

    // Build query parameters
    const params = new URLSearchParams();

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<MediaGetByMediaKeyResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create Media metadata
   * Creates metadata for a Media file.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createMetadata(
    options: MediaCreateMetadataOptions = {}
  ): Promise<MediaCreateMetadataResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/metadata';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MediaCreateMetadataResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media upload status
   * Retrieves the status of a Media upload by its ID.


   * @param mediaId Media id for the requested media upload status.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getUploadStatus(
    mediaId: string,
    options: MediaGetUploadStatusOptions = {}
  ): Promise<MediaGetUploadStatusResponse> {
    // Destructure options

    const {
      command = undefined,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/upload';

    // Build query parameters
    const params = new URLSearchParams();

    if (mediaId !== undefined) {
      params.append('media_id', String(mediaId));
    }

    if (command !== undefined) {
      params.append('command', String(command));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<MediaGetUploadStatusResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Upload media
   * Uploads a media file for use in posts or other content.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async upload(options: MediaUploadOptions = {}): Promise<MediaUploadResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/upload';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<MediaUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
