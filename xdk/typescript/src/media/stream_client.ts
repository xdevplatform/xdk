/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetByKeyResponse,
  CreateMetadataResponse,
  GetUploadStatusResponse,
  UploadResponse,
  AppendUploadResponse,
  GetByKeysResponse,
  GetAnalyticsResponse,
  InitializeUploadResponse,
  FinalizeUploadResponse,
  CreateSubtitlesResponse,
  DeleteSubtitlesResponse,
} from './models.js';

/**
 * Options for getByKey method
 * 
 * @public
 */
export interface GetByKeyStreamingOptions {
  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createMetadata method
 * 
 * @public
 */
export interface CreateMetadataStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getUploadStatus method
 * 
 * @public
 */
export interface GetUploadStatusStreamingOptions {
  /** The command for the media upload request. */
  command?: string;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for upload method
 * 
 * @public
 */
export interface UploadStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for appendUpload method
 * 
 * @public
 */
export interface AppendUploadStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getByKeys method
 * 
 * @public
 */
export interface GetByKeysStreamingOptions {
  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getAnalytics method
 * 
 * @public
 */
export interface GetAnalyticsStreamingOptions {
  /** A comma separated list of MediaAnalytics fields to display. */
  mediaAnalyticsfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for initializeUpload method
 * 
 * @public
 */
export interface InitializeUploadStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for finalizeUpload method
 * 
 * @public
 */
export interface FinalizeUploadStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createSubtitles method
 * 
 * @public
 */
export interface CreateSubtitlesStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for deleteSubtitles method
 * 
 * @public
 */
export interface DeleteSubtitlesStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class MediaClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Media by media key
     * Retrieves details of a specific Media file by its media key.
     * 
     * @returns Promise with the API response
     */
  async getByKey(
    mediaKey: string,
    options: GetByKeyStreamingOptions = {}
  ): Promise<GetByKeyResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByKey');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      mediafields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetByKeyResponse>(
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
    options: CreateMetadataStreamingOptions = {}
  ): Promise<CreateMetadataResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createMetadata');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/metadata';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateMetadataResponse>(
      'POST',
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
    mediaId: any,
    options: GetUploadStatusStreamingOptions = {}
  ): Promise<GetUploadStatusResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getUploadStatus');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      command = undefined,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/upload';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('media_id', String(mediaId));

    if (command !== undefined) {
      params.append('command', String(command));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetUploadStatusResponse>(
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
  async upload(options: UploadStreamingOptions = {}): Promise<UploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'upload');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/upload';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<UploadResponse>(
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
    options: AppendUploadStreamingOptions = {}
  ): Promise<AppendUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'appendUpload');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/upload/{id}/append';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<AppendUploadResponse>(
      'POST',
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
  async getByKeys(
    mediaKeys: Array<any>,
    options: GetByKeysStreamingOptions = {}
  ): Promise<GetByKeysResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getByKeys');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      mediafields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('media_keys', mediaKeys.join(','));

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetByKeysResponse>(
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
    options: GetAnalyticsStreamingOptions = {}
  ): Promise<GetAnalyticsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getAnalytics');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      mediaAnalyticsfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/analytics';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('media_keys', mediaKeys.join(','));

    params.append('end_time', String(endTime));

    params.append('start_time', String(startTime));

    params.append('granularity', String(granularity));

    if (mediaAnalyticsfields !== undefined) {
      params.append('media_analytics.fields', mediaAnalyticsfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Initialize media upload
     * Initializes a media upload.
     * 
     * @returns Promise with the API response
     */
  async initializeUpload(
    options: InitializeUploadStreamingOptions = {}
  ): Promise<InitializeUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'initializeUpload');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/upload/initialize';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<InitializeUploadResponse>(
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
  async finalizeUpload(
    id: string,
    options: FinalizeUploadStreamingOptions = {}
  ): Promise<FinalizeUploadResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'finalizeUpload');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/media/upload/{id}/finalize';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<FinalizeUploadResponse>(
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
    options: CreateSubtitlesStreamingOptions = {}
  ): Promise<CreateSubtitlesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createSubtitles');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/subtitles';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateSubtitlesResponse>(
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
    options: DeleteSubtitlesStreamingOptions = {}
  ): Promise<DeleteSubtitlesResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteSubtitles');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/media/subtitles';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<DeleteSubtitlesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
