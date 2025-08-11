/**
 * Media client for the X API.
 *
 * This module provides a client for interacting with the Media endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  MediaFinalizeUploadResponse,
  MediaGetByMediaKeyResponse,
  MediaAppendUploadRequest,
  MediaAppendUploadResponse,
  MediaCreateMetadataRequest,
  MediaCreateMetadataResponse,
  MediaGetAnalyticsResponse,
  MediaInitializeUploadRequest,
  MediaInitializeUploadResponse,
  MediaGetUploadStatusResponse,
  MediaUploadRequest,
  MediaUploadResponse,
  MediaCreateSubtitlesRequest,
  MediaCreateSubtitlesResponse,
  MediaDeleteSubtitlesRequest,
  MediaDeleteSubtitlesResponse,
  MediaGetByMediaKeysResponse,
} from './models.js';

/**
 * Client for Media operations
 */
export class MediaClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Finalize Media upload
     * Finalizes a Media upload request.
     * @param id The media id of the targeted media to finalize.* @param options Additional request options
     * @returns Promise with the API response
     */
  async finalizeUpload(
    options?: RequestOptions
  ): Promise<ApiResponse<MediaFinalizeUploadResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/upload/{id}/finalize`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<MediaFinalizeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Media by media key
     * Retrieves details of a specific Media file by its media key.
     * @param mediaKey A single Media Key.
     * @param mediafields A comma separated list of Media fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByMediaKey(
    options?: RequestOptions
  ): Promise<ApiResponse<MediaGetByMediaKeyResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/{media_key}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<MediaGetByMediaKeyResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Append Media upload
     * Appends data to a Media upload request.
     * @param id The media identifier for the media to perform the append operation.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async appendUpload(
    body?: MediaAppendUploadRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<MediaAppendUploadResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/upload/{id}/append`;

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

    return this.client.request<MediaAppendUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create Media metadata
     * Creates metadata for a Media file.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createMetadata(
    body?: MediaCreateMetadataRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<MediaCreateMetadataResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/metadata`;

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

    return this.client.request<MediaCreateMetadataResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Media analytics
     * Retrieves analytics data for media.
     * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
     * @param granularity The granularity for the search counts results.
     * @param mediaAnalyticsfields A comma separated list of MediaAnalytics fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getAnalytics(
    options?: RequestOptions
  ): Promise<ApiResponse<MediaGetAnalyticsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/analytics`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<MediaGetAnalyticsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Initialize media upload
     * Initializes a media upload.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async initializeUpload(
    body?: MediaInitializeUploadRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<MediaInitializeUploadResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/upload/initialize`;

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

    return this.client.request<MediaInitializeUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Media upload status
     * Retrieves the status of a Media upload by its ID.
     * @param mediaId Media id for the requested media upload status.
     * @param command The command for the media upload request.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getUploadStatus(
    options?: RequestOptions
  ): Promise<ApiResponse<MediaGetUploadStatusResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/upload`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<MediaGetUploadStatusResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Upload media
     * Uploads a media file for use in posts or other content.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async upload(
    body?: MediaUploadRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<MediaUploadResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/upload`;

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

    return this.client.request<MediaUploadResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create Media subtitles
     * Creates subtitles for a specific Media file.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createSubtitles(
    body?: MediaCreateSubtitlesRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<MediaCreateSubtitlesResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/subtitles`;

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

    return this.client.request<MediaCreateSubtitlesResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete Media subtitles
     * Deletes subtitles for a specific Media file.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async deleteSubtitles(
    body?: MediaDeleteSubtitlesRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<MediaDeleteSubtitlesResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media/subtitles`;

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

    return this.client.request<MediaDeleteSubtitlesResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Media by media keys
     * Retrieves details of Media files by their media keys.
     * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.
     * @param mediafields A comma separated list of Media fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getByMediaKeys(
    options?: RequestOptions
  ): Promise<ApiResponse<MediaGetByMediaKeysResponse>> {
    const params = new URLSearchParams();

    const path = `/2/media`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<MediaGetByMediaKeysResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
