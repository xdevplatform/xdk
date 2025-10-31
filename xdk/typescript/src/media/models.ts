/**
 * Models for media operations
 */

/**
 * Response for getUploadStatus
 * A response from getting a media upload request status.
 */
export interface GetUploadStatusResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for upload
 */
export interface UploadRequest {
  additionalOwners?: Array<any>;
  media?: any;
  /** A string enum value which identifies a media use-case. This identifier is used to enforce use-case specific constraints (e.g. file size) and enable advanced features. */
  mediaCategory?: string;
  /** The type of image or subtitle. */
  mediaType?: string;
  /** Whether this media is shared or not. */
  shared?: boolean;
}

/**
 * Response for upload
 * A response from getting a media upload request status.
 */
export interface UploadResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createSubtitles
 */
export interface CreateSubtitlesRequest {
  /** The unique identifier of this Media. */
  id?: string;
  /** The media category of uploaded media to which subtitles should be added/deleted */
  mediaCategory?: string;
  subtitles?: Record<string, any>;
}

/**
 * Response for createSubtitles
 */
export interface CreateSubtitlesResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for deleteSubtitles
 */
export interface DeleteSubtitlesRequest {
  /** The unique identifier of this Media. */
  id?: string;
  /** The language code should be a BCP47 code (e.g. 'EN", "SP") */
  languageCode?: string;
  /** The media category of uploaded media to which subtitles should be added/deleted */
  mediaCategory?: string;
}

/**
 * Response for deleteSubtitles
 */
export interface DeleteSubtitlesResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getByKey
 */
export interface GetByKeyResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getByKeys
 */
export interface GetByKeysResponse {
  data?: Array<any>;
  errors?: Array<any>;
}

/**
 * Request body for appendUpload
 */
export interface AppendUploadRequest {}

/**
 * Response for appendUpload
 * A response from getting a media upload request status.
 */
export interface AppendUploadResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for finalizeUpload
 * A response from getting a media upload request status.
 */
export interface FinalizeUploadResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createMetadata
 */
export interface CreateMetadataRequest {
  /** The unique identifier of this Media. */
  id?: string;
  metadata?: Record<string, any>;
}

/**
 * Response for createMetadata
 */
export interface CreateMetadataResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for initializeUpload
 */
export interface InitializeUploadRequest {
  additionalOwners?: Array<any>;
  /** A string enum value which identifies a media use-case. This identifier is used to enforce use-case specific constraints (e.g. file size, video duration) and enable advanced features. */
  mediaCategory?: string;
  /** The type of media. */
  mediaType?: string;
  /** Whether this media is shared or not. */
  shared?: boolean;
  /** The total size of the media upload in bytes. */
  totalBytes?: number;
}

/**
 * Response for initializeUpload
 * A response from getting a media upload request status.
 */
export interface InitializeUploadResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getAnalytics
 */
export interface GetAnalyticsResponse {
  data?: Array<any>;
  errors?: Array<any>;
}
