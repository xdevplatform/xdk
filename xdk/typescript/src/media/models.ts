/**
 * Models for media operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Request for createSubtitles
 * 
 * @public
 */
export type CreateSubtitlesRequest = Schemas.SubtitlesCreateRequest;
/**
 * Response for createSubtitles
 * 
 * @public
 */
export type CreateSubtitlesResponse = Schemas.SubtitlesCreateResponse;
/**
 * Request for deleteSubtitles
 * 
 * @public
 */
export type DeleteSubtitlesRequest = Schemas.SubtitlesDeleteRequest;
/**
 * Response for deleteSubtitles
 * 
 * @public
 */
export type DeleteSubtitlesResponse = Schemas.SubtitlesDeleteResponse;
/**
 * Response for getAnalytics
 * 
 * @public
 */
export type GetAnalyticsResponse = Schemas.MediaAnalytics;
/**
 * Response for getUploadStatus
 * 
 * @public
 */
export type GetUploadStatusResponse = Schemas.MediaUploadResponse;
/**
 * Request for upload
 * 
 * @public
 */
export type UploadRequest = Schemas.MediaUploadRequestOneShot;
/**
 * Response for upload
 * 
 * @public
 */
export type UploadResponse = Schemas.MediaUploadResponse;
/**
 * Request for createMetadata
 * 
 * @public
 */
export type CreateMetadataRequest = Schemas.MetadataCreateRequest;
/**
 * Response for createMetadata
 * 
 * @public
 */
export type CreateMetadataResponse = Schemas.MetadataCreateResponse;
/**
 * Request for initializeUpload
 * 
 * @public
 */
export type InitializeUploadRequest = Schemas.MediaUploadConfigRequest;
/**
 * Response for initializeUpload
 * 
 * @public
 */
export type InitializeUploadResponse = Schemas.MediaUploadResponse;
/**
 * Response for finalizeUpload
 * 
 * @public
 */
export type FinalizeUploadResponse = Schemas.MediaUploadResponse;
/**
 * Request for appendUpload
 * 
 * @public
 */
export type AppendUploadRequest = Schemas.MediaUploadAppendRequest;
/**
 * Response for appendUpload
 * 
 * @public
 */
export type AppendUploadResponse = Schemas.MediaUploadAppendResponse;
/**
 * Response for getByKey
 * 
 * @public
 */
export type GetByKeyResponse = Schemas.Get2MediaMediaKeyResponse;
/**
 * Response for getByKeys
 * 
 * @public
 */
export type GetByKeysResponse = Schemas.Get2MediaResponse;