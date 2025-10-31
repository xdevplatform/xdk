/**
 * media client for the X API.
 *
 * This module provides a client for interacting with the media endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  CreateSubtitlesRequest,
  CreateSubtitlesResponse,
  DeleteSubtitlesRequest,
  DeleteSubtitlesResponse,
  GetAnalyticsResponse,
  GetUploadStatusResponse,
  UploadRequest,
  UploadResponse,
  CreateMetadataRequest,
  CreateMetadataResponse,
  InitializeUploadRequest,
  InitializeUploadResponse,
  FinalizeUploadResponse,
  AppendUploadRequest,
  AppendUploadResponse,
  GetByKeyResponse,
  GetByKeysResponse,
} from './models.js';

/**
 * Options for createSubtitles method
 * 
 * @public
 */
export interface CreateSubtitlesOptions {
  /** Request body */
  body?: CreateSubtitlesRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for deleteSubtitles method
 * 
 * @public
 */
export interface DeleteSubtitlesOptions {
  /** Request body */
  body?: DeleteSubtitlesRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getUploadStatus method
 * 
 * @public
 */
export interface GetUploadStatusOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for upload method
 * 
 * @public
 */
export interface UploadOptions {
  /** Request body */
  body?: UploadRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createMetadata method
 * 
 * @public
 */
export interface CreateMetadataOptions {
  /** Request body */
  body?: CreateMetadataRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for initializeUpload method
 * 
 * @public
 */
export interface InitializeUploadOptions {
  /** Request body */
  body?: InitializeUploadRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for appendUpload method
 * 
 * @public
 */
export interface AppendUploadOptions {
  /** Request body */
  body?: AppendUploadRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for media operations
 * 
 * This client provides methods for interacting with the media endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all media related operations.
 * 
 * @category media
 */
export class MediaClient {
  private client: Client;

  /**
     * Creates a new media client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Create Media subtitles
   * Creates subtitles for a specific Media file.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createSubtitles(
    options: CreateSubtitlesOptions = {}
  ): Promise<CreateSubtitlesResponse> {
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

    return this.client.request<CreateSubtitlesResponse>(
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
    options: DeleteSubtitlesOptions = {}
  ): Promise<DeleteSubtitlesResponse> {
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

    return this.client.request<DeleteSubtitlesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media analytics
   * Retrieves analytics data for media.










   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getAnalytics(): Promise<GetAnalyticsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/media/analytics';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media upload status
   * Retrieves the status of a Media upload by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getUploadStatus(
    options: GetUploadStatusOptions = {}
  ): Promise<GetUploadStatusResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/media/upload';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetUploadStatusResponse>(
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
  async upload(options: UploadOptions = {}): Promise<UploadResponse> {
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

    return this.client.request<UploadResponse>(
      'POST',
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
    options: CreateMetadataOptions = {}
  ): Promise<CreateMetadataResponse> {
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

    return this.client.request<CreateMetadataResponse>(
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
    options: InitializeUploadOptions = {}
  ): Promise<InitializeUploadResponse> {
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

    return this.client.request<InitializeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Finalize Media upload
   * Finalizes a Media upload request.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async finalizeUpload(): Promise<FinalizeUploadResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/media/upload/{id}/finalize';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<FinalizeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Append Media upload
   * Appends data to a Media upload request.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async appendUpload(
    options: AppendUploadOptions = {}
  ): Promise<AppendUploadResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/media/upload/{id}/append';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<AppendUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media by media key
   * Retrieves details of a specific Media file by its media key.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByKey(): Promise<GetByKeyResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/media/{media_key}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByKeyResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Media by media keys
   * Retrieves details of Media files by their media keys.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getByKeys(): Promise<GetByKeysResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/media';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetByKeysResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
