/**
 * Media client for the X API.
 *
 * This module provides a client for interacting with the Media endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  MediaAppendUploadRequest,
  MediaAppendUploadResponse,
  MediaGetByMediaKeysResponse,
  MediaCreateSubtitlesRequest,
  MediaCreateSubtitlesResponse,
  MediaDeleteSubtitlesRequest,
  MediaDeleteSubtitlesResponse,
  MediaFinalizeUploadResponse,
  MediaGetByMediaKeyResponse,
  MediaCreateMetadataRequest,
  MediaCreateMetadataResponse,
  MediaGetAnalyticsResponse,
  MediaInitializeUploadRequest,
  MediaInitializeUploadResponse,
  MediaGetUploadStatusResponse,
  MediaUploadRequest,
  MediaUploadResponse
} from "./models.js";

/**
 * Client for Media operations
 */
export class MediaClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Append Media upload
     * Appends data to a Media upload request.
     * @param id The media identifier for the media to perform the append operation.* @param body Request body* @returns MediaAppendUploadResponse Response data
     */
  async appendUpload(
    id: string,
    body?: MediaAppendUploadRequest
  ): Promise<MediaAppendUploadResponse> {
    let url = this.client.baseUrl + "/2/media/upload/{id}/append";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaAppendUploadResponse;
  }

  /**
     * Get Media by media keys
     * Retrieves details of Media files by their media keys.
     * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.
     * @param mediafields A comma separated list of Media fields to display.* @returns MediaGetByMediaKeysResponse Response data
     */
  async getByMediaKeys(
    mediaKeys: Array<any>,
    mediafields?: Array<any>
  ): Promise<MediaGetByMediaKeysResponse> {
    let url = this.client.baseUrl + "/2/media";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (mediaKeys !== undefined) {
      params.set("media_keys", mediaKeys.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaGetByMediaKeysResponse;
  }

  /**
     * Create Media subtitles
     * Creates subtitles for a specific Media file.* @param body Request body* @returns MediaCreateSubtitlesResponse Response data
     */
  async createSubtitles(
    body?: MediaCreateSubtitlesRequest
  ): Promise<MediaCreateSubtitlesResponse> {
    let url = this.client.baseUrl + "/2/media/subtitles";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaCreateSubtitlesResponse;
  }

  /**
     * Delete Media subtitles
     * Deletes subtitles for a specific Media file.* @param body Request body* @returns MediaDeleteSubtitlesResponse Response data
     */
  async deleteSubtitles(
    body?: MediaDeleteSubtitlesRequest
  ): Promise<MediaDeleteSubtitlesResponse> {
    let url = this.client.baseUrl + "/2/media/subtitles";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "DELETE",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaDeleteSubtitlesResponse;
  }

  /**
     * Finalize Media upload
     * Finalizes a Media upload request.
     * @param id The media id of the targeted media to finalize.* @returns MediaFinalizeUploadResponse Response data
     */
  async finalizeUpload(id: string): Promise<MediaFinalizeUploadResponse> {
    let url = this.client.baseUrl + "/2/media/upload/{id}/finalize";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{id}", String(id));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaFinalizeUploadResponse;
  }

  /**
     * Get Media by media key
     * Retrieves details of a specific Media file by its media key.
     * @param mediaKey A single Media Key.
     * @param mediafields A comma separated list of Media fields to display.* @returns MediaGetByMediaKeyResponse Response data
     */
  async getByMediaKey(
    mediaKey: string,
    mediafields?: Array<any>
  ): Promise<MediaGetByMediaKeyResponse> {
    let url = this.client.baseUrl + "/2/media/{media_key}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    url = url.replace("{media_key}", String(mediaKey));

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    if (this.client.bearerToken) {
      headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
    } else if (this.client.accessToken) {
      headers.set("Authorization", `Bearer ${this.client.accessToken}`);
    }

    // Make the request

    const response = await fetch(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaGetByMediaKeyResponse;
  }

  /**
     * Create Media metadata
     * Creates metadata for a Media file.* @param body Request body* @returns MediaCreateMetadataResponse Response data
     */
  async createMetadata(
    body?: MediaCreateMetadataRequest
  ): Promise<MediaCreateMetadataResponse> {
    let url = this.client.baseUrl + "/2/media/metadata";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaCreateMetadataResponse;
  }

  /**
     * Get Media analytics
     * Retrieves analytics data for media.
     * @param mediaKeys A comma separated list of Media Keys. Up to 100 are allowed in a single request.
     * @param endTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
     * @param startTime YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
     * @param granularity The granularity for the search counts results.
     * @param mediaAnalyticsfields A comma separated list of MediaAnalytics fields to display.* @returns MediaGetAnalyticsResponse Response data
     */
  async getAnalytics(
    mediaKeys: Array<any>,
    endTime: string,
    startTime: string,
    granularity: string,
    mediaAnalyticsfields?: Array<any>
  ): Promise<MediaGetAnalyticsResponse> {
    let url = this.client.baseUrl + "/2/media/analytics";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (mediaKeys !== undefined) {
      params.set("media_keys", mediaKeys.map(String).join(","));
    }

    if (endTime !== undefined) {
      params.set("end_time", String(endTime));
    }

    if (startTime !== undefined) {
      params.set("start_time", String(startTime));
    }

    if (granularity !== undefined) {
      params.set("granularity", String(granularity));
    }

    if (mediaAnalyticsfields !== undefined) {
      params.set(
        "media_analytics.fields",
        mediaAnalyticsfields.map(String).join(",")
      );
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaGetAnalyticsResponse;
  }

  /**
     * Initialize media upload
     * Initializes a media upload.* @param body Request body* @returns MediaInitializeUploadResponse Response data
     */
  async initializeUpload(
    body?: MediaInitializeUploadRequest
  ): Promise<MediaInitializeUploadResponse> {
    let url = this.client.baseUrl + "/2/media/upload/initialize";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaInitializeUploadResponse;
  }

  /**
     * Get Media upload status
     * Retrieves the status of a Media upload by its ID.
     * @param mediaId Media id for the requested media upload status.
     * @param command The command for the media upload request.* @returns MediaGetUploadStatusResponse Response data
     */
  async getUploadStatus(
    mediaId: string,
    command?: string
  ): Promise<MediaGetUploadStatusResponse> {
    let url = this.client.baseUrl + "/2/media/upload";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (mediaId !== undefined) {
      params.set("media_id", String(mediaId));
    }

    if (command !== undefined) {
      params.set("command", String(command));
    }

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaGetUploadStatusResponse;
  }

  /**
     * Upload media
     * Uploads a media file for use in posts or other content.* @param body Request body* @returns MediaUploadResponse Response data
     */
  async upload(body?: MediaUploadRequest): Promise<MediaUploadResponse> {
    let url = this.client.baseUrl + "/2/media/upload";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    // Create headers by copying the client's headers
    const headers = new Headers(this.client.headers);

    // Set authentication headers

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as MediaUploadResponse;
  }
}
