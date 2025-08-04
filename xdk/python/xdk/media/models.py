"""
Media models for the X API.

This module provides models for the Media endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for createMediaMetadata


class CreateMediaMetadataRequest(BaseModel):
    """Request model for createMediaMetadata"""

    id: Optional[str] = None
    metadata: Optional["CreateMediaMetadataRequestMetadata"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponse(BaseModel):
    """Response model for createMediaMetadata"""

    data: Optional["CreateMediaMetadataResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadata(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadata"""

    allow_download_status: Optional[
        "CreateMediaMetadataRequestMetadataAllowDownloadStatus"
    ] = None
    alt_text: Optional["CreateMediaMetadataRequestMetadataAltText"] = None
    audience_policy: Optional["CreateMediaMetadataRequestMetadataAudiencePolicy"] = None
    content_expiration: Optional[
        "CreateMediaMetadataRequestMetadataContentExpiration"
    ] = None
    domain_restrictions: Optional[
        "CreateMediaMetadataRequestMetadataDomainRestrictions"
    ] = None
    found_media_origin: Optional[
        "CreateMediaMetadataRequestMetadataFoundMediaOrigin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional["CreateMediaMetadataRequestMetadataManagementInfo"] = None
    preview_image: Optional["CreateMediaMetadataRequestMetadataPreviewImage"] = None
    sensitive_media_warning: Optional[
        "CreateMediaMetadataRequestMetadataSensitiveMediaWarning"
    ] = None
    shared_info: Optional["CreateMediaMetadataRequestMetadataSharedInfo"] = None
    sticker_info: Optional["CreateMediaMetadataRequestMetadataStickerInfo"] = None
    upload_source: Optional["CreateMediaMetadataRequestMetadataUploadSource"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataAllowDownloadStatus(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataAllowDownloadStatus"""

    allow_download: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataAltText(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataAltText"""

    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataAudiencePolicy(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataAudiencePolicy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataContentExpiration(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataContentExpiration"""

    timestamp_sec: Optional[float] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataDomainRestrictions(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataDomainRestrictions"""

    whitelist: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataFoundMediaOrigin(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataFoundMediaOrigin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataManagementInfo(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataManagementInfo"""

    managed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataPreviewImage(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataPreviewImage"""

    media_key: Optional["CreateMediaMetadataRequestMetadataPreviewImageMediaKey"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataPreviewImageMediaKey(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataPreviewImageMediaKey"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataSensitiveMediaWarning(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataSensitiveMediaWarning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataSharedInfo(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataSharedInfo"""

    shared: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataStickerInfo(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataStickerInfo"""

    stickers: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataRequestMetadataUploadSource(BaseModel):
    """Nested model for CreateMediaMetadataRequestMetadataUploadSource"""

    upload_source: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseData(BaseModel):
    """Nested model for CreateMediaMetadataResponseData"""

    associated_metadata: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadata"
    ] = None
    id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadata(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadata"""

    allow_download_status: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataAllowDownloadStatus"
    ] = None
    alt_text: Optional["CreateMediaMetadataResponseDataAssociatedMetadataAltText"] = (
        None
    )
    audience_policy: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataAudiencePolicy"
    ] = None
    content_expiration: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataContentExpiration"
    ] = None
    domain_restrictions: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataDomainRestrictions"
    ] = None
    found_media_origin: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataFoundMediaOrigin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataManagementInfo"
    ] = None
    preview_image: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataPreviewImage"
    ] = None
    sensitive_media_warning: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataSensitiveMediaWarning"
    ] = None
    shared_info: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataSharedInfo"
    ] = None
    sticker_info: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataStickerInfo"
    ] = None
    upload_source: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataUploadSource"
    ] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataAllowDownloadStatus(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataAllowDownloadStatus"""

    allow_download: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataAltText(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataAltText"""

    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataAudiencePolicy(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataAudiencePolicy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataContentExpiration(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataContentExpiration"""

    timestamp_sec: Optional[float] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataDomainRestrictions(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataDomainRestrictions"""

    whitelist: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataFoundMediaOrigin(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataFoundMediaOrigin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataManagementInfo(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataManagementInfo"""

    managed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataPreviewImage(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataPreviewImage"""

    media_key: Optional[
        "CreateMediaMetadataResponseDataAssociatedMetadataPreviewImageMediaKey"
    ] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataPreviewImageMediaKey(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataPreviewImageMediaKey"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataSensitiveMediaWarning(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataSensitiveMediaWarning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataSharedInfo(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataSharedInfo"""

    shared: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataStickerInfo(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataStickerInfo"""

    stickers: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaMetadataResponseDataAssociatedMetadataUploadSource(BaseModel):
    """Nested model for CreateMediaMetadataResponseDataAssociatedMetadataUploadSource"""

    upload_source: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for createMediaSubtitles


class CreateMediaSubtitlesRequest(BaseModel):
    """Request model for createMediaSubtitles"""

    id: Optional[str] = None
    media_category: Optional[str] = None
    subtitles: Optional["CreateMediaSubtitlesRequestSubtitles"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaSubtitlesResponse(BaseModel):
    """Response model for createMediaSubtitles"""

    data: Optional["CreateMediaSubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaSubtitlesRequestSubtitles(BaseModel):
    """Nested model for CreateMediaSubtitlesRequestSubtitles"""

    display_name: Optional[str] = None
    id: Optional[str] = None
    language_code: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMediaSubtitlesResponseData(BaseModel):
    """Nested model for CreateMediaSubtitlesResponseData"""

    associated_subtitles: Optional[List] = None
    id: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for deleteMediaSubtitles


class DeleteMediaSubtitlesRequest(BaseModel):
    """Request model for deleteMediaSubtitles"""

    id: Optional[str] = None
    language_code: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteMediaSubtitlesResponse(BaseModel):
    """Response model for deleteMediaSubtitles"""

    data: Optional["DeleteMediaSubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteMediaSubtitlesResponseData(BaseModel):
    """Nested model for DeleteMediaSubtitlesResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getMediaUploadStatus


class GetMediaUploadStatusResponse(BaseModel):
    """Response model for getMediaUploadStatus"""

    data: Optional["GetMediaUploadStatusResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMediaUploadStatusResponseData(BaseModel):
    """Nested model for GetMediaUploadStatusResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["GetMediaUploadStatusResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMediaUploadStatusResponseDataProcessingInfo(BaseModel):
    """Nested model for GetMediaUploadStatusResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for mediaUpload


class MediaUploadRequest(BaseModel):
    """Request model for mediaUpload"""

    additional_owners: Optional[List] = None
    media: Any = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class MediaUploadResponse(BaseModel):
    """Response model for mediaUpload"""

    data: Optional["MediaUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class MediaUploadResponseData(BaseModel):
    """Nested model for MediaUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["MediaUploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class MediaUploadResponseDataProcessingInfo(BaseModel):
    """Nested model for MediaUploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for initializeMediaUpload


class InitializeMediaUploadRequest(BaseModel):
    """Request model for initializeMediaUpload"""

    additional_owners: Optional[List] = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None
    total_bytes: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class InitializeMediaUploadResponse(BaseModel):
    """Response model for initializeMediaUpload"""

    data: Optional["InitializeMediaUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class InitializeMediaUploadResponseData(BaseModel):
    """Nested model for InitializeMediaUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["InitializeMediaUploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class InitializeMediaUploadResponseDataProcessingInfo(BaseModel):
    """Nested model for InitializeMediaUploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getMediaAnalytics


class GetMediaAnalyticsResponse(BaseModel):
    """Response model for getMediaAnalytics"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getMediaByMediaKeys


class GetMediaByMediaKeysResponse(BaseModel):
    """Response model for getMediaByMediaKeys"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getMediaByMediaKey


class GetMediaByMediaKeyResponse(BaseModel):
    """Response model for getMediaByMediaKey"""

    data: Optional["GetMediaByMediaKeyResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMediaByMediaKeyResponseData(BaseModel):
    """Nested model for GetMediaByMediaKeyResponseData"""

    height: Optional[int] = None
    media_key: Optional[str] = None
    type: Optional[str] = None
    width: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for finalizeMediaUpload


class FinalizeMediaUploadResponse(BaseModel):
    """Response model for finalizeMediaUpload"""

    data: Optional["FinalizeMediaUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class FinalizeMediaUploadResponseData(BaseModel):
    """Nested model for FinalizeMediaUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["FinalizeMediaUploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class FinalizeMediaUploadResponseDataProcessingInfo(BaseModel):
    """Nested model for FinalizeMediaUploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for appendMediaUpload


class AppendMediaUploadRequest(BaseModel):
    """Request model for appendMediaUpload"""

    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)
    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


class AppendMediaUploadResponse(BaseModel):
    """Response model for appendMediaUpload"""

    data: Optional["AppendMediaUploadResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class AppendMediaUploadResponseData(BaseModel):
    """Nested model for AppendMediaUploadResponseData"""

    expires_at: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
