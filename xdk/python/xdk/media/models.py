"""
Media models for the X API.

This module provides models for the Media endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for finalizeMediaUpload


class FinalizeMediaUploadResponse(BaseModel):
    """Response model for finalizeMediaUpload"""

    data: Optional["FinalizeMediaUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FinalizeMediaUploadResponseData(BaseModel):
    """Nested model for FinalizeMediaUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["FinalizeMediaUploadResponseDataProcessing_info"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FinalizeMediaUploadResponseDataProcessing_info(BaseModel):
    """Nested model for FinalizeMediaUploadResponseDataProcessing_info"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for appendMediaUpload


class AppendMediaUploadRequest(BaseModel):
    """Request model for appendMediaUpload"""

    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)
    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class AppendMediaUploadResponse(BaseModel):
    """Response model for appendMediaUpload"""

    data: Optional["AppendMediaUploadResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class AppendMediaUploadResponseData(BaseModel):
    """Nested model for AppendMediaUploadResponseData"""

    expires_at: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaByMediaKeys


class GetMediaByMediaKeysResponse(BaseModel):
    """Response model for getMediaByMediaKeys"""

    data: Optional[List] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaByMediaKey


class GetMediaByMediaKeyResponse(BaseModel):
    """Response model for getMediaByMediaKey"""

    data: Optional["GetMediaByMediaKeyResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMediaByMediaKeyResponseData(BaseModel):
    """Nested model for GetMediaByMediaKeyResponseData"""

    height: Optional[int] = None
    media_key: Optional[str] = None
    type: Optional[str] = None
    width: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaAnalytics


class GetMediaAnalyticsResponse(BaseModel):
    """Response model for getMediaAnalytics"""

    data: Optional[List] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaUploadStatus


class GetMediaUploadStatusResponse(BaseModel):
    """Response model for getMediaUploadStatus"""

    data: Optional["GetMediaUploadStatusResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMediaUploadStatusResponseData(BaseModel):
    """Nested model for GetMediaUploadStatusResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["GetMediaUploadStatusResponseDataProcessing_info"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetMediaUploadStatusResponseDataProcessing_info(BaseModel):
    """Nested model for GetMediaUploadStatusResponseDataProcessing_info"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for mediaUpload


class MediaUploadRequest(BaseModel):
    """Request model for mediaUpload"""

    additional_owners: Optional[List] = None
    media: Any = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MediaUploadResponse(BaseModel):
    """Response model for mediaUpload"""

    data: Optional["MediaUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MediaUploadResponseData(BaseModel):
    """Nested model for MediaUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["MediaUploadResponseDataProcessing_info"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MediaUploadResponseDataProcessing_info(BaseModel):
    """Nested model for MediaUploadResponseDataProcessing_info"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createMediaMetadata


class CreateMediaMetadataRequest(BaseModel):
    """Request model for createMediaMetadata"""

    id: Optional[str] = None
    metadata: Optional["CreateMediaMetadataRequestMetadata"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponse(BaseModel):
    """Response model for createMediaMetadata"""

    data: Optional["CreateMediaMetadataResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadata(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadata"""

    allow_download_status: Optional[
        "CreateMediaMetadataRequestMetadataAllow_download_status"
    ] = None
    alt_text: Optional["CreateMediaMetadataRequestMetadataAlt_text"] = None
    audience_policy: Optional["CreateMediaMetadataRequestMetadataAudience_policy"] = (
        None
    )
    content_expiration: Optional[
        "CreateMediaMetadataRequestMetadataContent_expiration"
    ] = None
    domain_restrictions: Optional[
        "CreateMediaMetadataRequestMetadataDomain_restrictions"
    ] = None
    found_media_origin: Optional[
        "CreateMediaMetadataRequestMetadataFound_media_origin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional["CreateMediaMetadataRequestMetadataManagement_info"] = (
        None
    )
    preview_image: Optional["CreateMediaMetadataRequestMetadataPreview_image"] = None
    sensitive_media_warning: Optional[
        "CreateMediaMetadataRequestMetadataSensitive_media_warning"
    ] = None
    shared_info: Optional["CreateMediaMetadataRequestMetadataShared_info"] = None
    sticker_info: Optional["CreateMediaMetadataRequestMetadataSticker_info"] = None
    upload_source: Optional["CreateMediaMetadataRequestMetadataUpload_source"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataAllow_download_status(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataAllow_download_status"""

    allow_download: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataAlt_text(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataAlt_text"""

    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataAudience_policy(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataAudience_policy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataContent_expiration(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataContent_expiration"""

    timestamp_sec: Optional[float] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataDomain_restrictions(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataDomain_restrictions"""

    whitelist: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataFound_media_origin(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataFound_media_origin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataManagement_info(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataManagement_info"""

    managed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataPreview_image(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataPreview_image"""

    media_key: Optional["CreateMediaMetadataRequestMetadataPreview_imageMedia_key"] = (
        None
    )

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataPreview_imageMedia_key(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataPreview_imageMedia_key"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataSensitive_media_warning(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataSensitive_media_warning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataShared_info(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataShared_info"""

    shared: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataSticker_info(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataSticker_info"""

    stickers: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataRequestMetadataUpload_source(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataUpload_source"""

    upload_source: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseData(BaseModel):
    """Nested model for CreateMediaMetadataResponseData"""

    associated_metadata: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadata"
    ] = None
    id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadata(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadata"""

    allow_download_status: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataAllow_download_status"
    ] = None
    alt_text: Optional["CreateMediaMetadataResponseDataAssociated_metadataAlt_text"] = (
        None
    )
    audience_policy: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataAudience_policy"
    ] = None
    content_expiration: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataContent_expiration"
    ] = None
    domain_restrictions: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataDomain_restrictions"
    ] = None
    found_media_origin: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataFound_media_origin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataManagement_info"
    ] = None
    preview_image: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataPreview_image"
    ] = None
    sensitive_media_warning: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataSensitive_media_warning"
    ] = None
    shared_info: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataShared_info"
    ] = None
    sticker_info: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataSticker_info"
    ] = None
    upload_source: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataUpload_source"
    ] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataAllow_download_status(
    BaseModel
):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataAllow_download_status"""

    allow_download: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataAlt_text(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataAlt_text"""

    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataAudience_policy(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataAudience_policy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataContent_expiration(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataContent_expiration"""

    timestamp_sec: Optional[float] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataDomain_restrictions(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataDomain_restrictions"""

    whitelist: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataFound_media_origin(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataFound_media_origin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataManagement_info(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataManagement_info"""

    managed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataPreview_image(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataPreview_image"""

    media_key: Optional[
        "CreateMediaMetadataResponseDataAssociated_metadataPreview_imageMedia_key"
    ] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataPreview_imageMedia_key(
    BaseModel
):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataPreview_imageMedia_key"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataSensitive_media_warning(
    BaseModel
):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataSensitive_media_warning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataShared_info(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataShared_info"""

    shared: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataSticker_info(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataSticker_info"""

    stickers: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaMetadataResponseDataAssociated_metadataUpload_source(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociated_metadataUpload_source"""

    upload_source: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for initializeMediaUpload


class InitializeMediaUploadRequest(BaseModel):
    """Request model for initializeMediaUpload"""

    additional_owners: Optional[List] = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None
    total_bytes: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class InitializeMediaUploadResponse(BaseModel):
    """Response model for initializeMediaUpload"""

    data: Optional["InitializeMediaUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class InitializeMediaUploadResponseData(BaseModel):
    """Nested model for InitializeMediaUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["InitializeMediaUploadResponseDataProcessing_info"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class InitializeMediaUploadResponseDataProcessing_info(BaseModel):
    """Nested model for InitializeMediaUploadResponseDataProcessing_info"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createMediaSubtitles


class CreateMediaSubtitlesRequest(BaseModel):
    """Request model for createMediaSubtitles"""

    id: Optional[str] = None
    media_category: Optional[str] = None
    subtitles: Optional["CreateMediaSubtitlesRequestSubtitles"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaSubtitlesResponse(BaseModel):
    """Response model for createMediaSubtitles"""

    data: Optional["CreateMediaSubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaSubtitlesRequestSubtitles(BaseModel):
    """Nested model for CreateMediaSubtitlesRequestSubtitles"""

    display_name: Optional[str] = None
    id: Optional[str] = None
    language_code: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateMediaSubtitlesResponseData(BaseModel):
    """Nested model for CreateMediaSubtitlesResponseData"""

    associated_subtitles: Optional[List] = None
    id: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteMediaSubtitles


class DeleteMediaSubtitlesRequest(BaseModel):
    """Request model for deleteMediaSubtitles"""

    id: Optional[str] = None
    language_code: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeleteMediaSubtitlesResponse(BaseModel):
    """Response model for deleteMediaSubtitles"""

    data: Optional["DeleteMediaSubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeleteMediaSubtitlesResponseData(BaseModel):
    """Nested model for DeleteMediaSubtitlesResponseData"""

    deleted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
