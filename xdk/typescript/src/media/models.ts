/**
 * Models for Media operations
 */






/**
 * Request body for initializeUpload
 * 
 */
export interface MediaInitializeUploadRequest {
    
    
    
    
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
 * 
 * A response from getting a media upload request status.
 * 
 */
export interface MediaInitializeUploadResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for getAnalytics
 * 
 */
export interface MediaGetAnalyticsResponse {
    
    
    
    
    data?: Array<any>;
    
    
    
    errors?: Array<any>;
    
    
}








/**
 * Request body for createMetadata
 * 
 */
export interface MediaCreateMetadataRequest {
    
    
    
    
    /** The unique identifier of this Media. */
    
    id?: string;
    
    
    
    metadata?: Record<string, any>;
    
    
}







/**
 * Response for createMetadata
 * 
 */
export interface MediaCreateMetadataResponse {
    
    
    
    
    data?: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for getUploadStatus
 * 
 * A response from getting a media upload request status.
 * 
 */
export interface MediaGetUploadStatusResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}








/**
 * Request body for upload
 * 
 */
export interface MediaUploadRequest {
    
    
    
    
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
 * 
 * A response from getting a media upload request status.
 * 
 */
export interface MediaUploadResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for getByMediaKeys
 * 
 */
export interface MediaGetByMediaKeysResponse {
    
    
    
    
    data?: Array<any>;
    
    
    
    errors?: Array<any>;
    
    
}








/**
 * Request body for appendUpload
 * 
 */
export interface MediaAppendUploadRequest {
    
}







/**
 * Response for appendUpload
 * 
 * A response from getting a media upload request status.
 * 
 */
export interface MediaAppendUploadResponse {
    
    
    
    
    data?: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}








/**
 * Request body for createSubtitles
 * 
 */
export interface MediaCreateSubtitlesRequest {
    
    
    
    
    /** The unique identifier of this Media. */
    
    id?: string;
    
    
    
    /** The media category of uploaded media to which subtitles should be added/deleted */
    
    mediaCategory?: string;
    
    
    
    subtitles?: Record<string, any>;
    
    
}







/**
 * Response for createSubtitles
 * 
 */
export interface MediaCreateSubtitlesResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}








/**
 * Request body for deleteSubtitles
 * 
 */
export interface MediaDeleteSubtitlesRequest {
    
    
    
    
    /** The unique identifier of this Media. */
    
    id?: string;
    
    
    
    /** The language code should be a BCP47 code (e.g. 'EN", "SP") */
    
    languageCode?: string;
    
    
    
    /** The media category of uploaded media to which subtitles should be added/deleted */
    
    mediaCategory?: string;
    
    
}







/**
 * Response for deleteSubtitles
 * 
 */
export interface MediaDeleteSubtitlesResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for getByMediaKey
 * 
 */
export interface MediaGetByMediaKeyResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for finalizeUpload
 * 
 * A response from getting a media upload request status.
 * 
 */
export interface MediaFinalizeUploadResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}



 