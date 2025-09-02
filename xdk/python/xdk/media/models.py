"""
media models for the X API.

This module provides models for the media endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for create_metadata


class CreateMetadataRequest(BaseModel):
    """Request model for create_metadata"""

    id: Optional[str] = None
    metadata: Optional["CreateMetadataRequestMetadata"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponse(BaseModel):
    """Response model for create_metadata"""

    data: Optional["CreateMetadataResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadata(BaseModel):
    """Nested model for CreateMetadataRequestMetadata"""

    allow_download_status: Optional[
        "CreateMetadataRequestMetadataAllowDownloadStatus"
    ] = None
    alt_text: Optional["CreateMetadataRequestMetadataAltText"] = None
    audience_policy: Optional["CreateMetadataRequestMetadataAudiencePolicy"] = None
    content_expiration: Optional["CreateMetadataRequestMetadataContentExpiration"] = (
        None
    )
    domain_restrictions: Optional["CreateMetadataRequestMetadataDomainRestrictions"] = (
        None
    )
    found_media_origin: Optional["CreateMetadataRequestMetadataFoundMediaOrigin"] = None
    geo_restrictions: Any = None
    management_info: Optional["CreateMetadataRequestMetadataManagementInfo"] = None
    preview_image: Optional["CreateMetadataRequestMetadataPreviewImage"] = None
    sensitive_media_warning: Optional[
        "CreateMetadataRequestMetadataSensitiveMediaWarning"
    ] = None
    shared_info: Optional["CreateMetadataRequestMetadataSharedInfo"] = None
    sticker_info: Optional["CreateMetadataRequestMetadataStickerInfo"] = None
    upload_source: Optional["CreateMetadataRequestMetadataUploadSource"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataAllowDownloadStatus(BaseModel):
    """Nested model for CreateMetadataRequestMetadataAllowDownloadStatus"""

    allow_download: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataAltText(BaseModel):
    """Nested model for CreateMetadataRequestMetadataAltText"""

    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataAudiencePolicy(BaseModel):
    """Nested model for CreateMetadataRequestMetadataAudiencePolicy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataContentExpiration(BaseModel):
    """Nested model for CreateMetadataRequestMetadataContentExpiration"""

    timestamp_sec: Optional[float] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataDomainRestrictions(BaseModel):
    """Nested model for CreateMetadataRequestMetadataDomainRestrictions"""

    whitelist: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataFoundMediaOrigin(BaseModel):
    """Nested model for CreateMetadataRequestMetadataFoundMediaOrigin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataManagementInfo(BaseModel):
    """Nested model for CreateMetadataRequestMetadataManagementInfo"""

    managed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataPreviewImage(BaseModel):
    """Nested model for CreateMetadataRequestMetadataPreviewImage"""

    media_key: Optional["CreateMetadataRequestMetadataPreviewImageMediaKey"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataPreviewImageMediaKey(BaseModel):
    """Nested model for CreateMetadataRequestMetadataPreviewImageMediaKey"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataSensitiveMediaWarning(BaseModel):
    """Nested model for CreateMetadataRequestMetadataSensitiveMediaWarning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataSharedInfo(BaseModel):
    """Nested model for CreateMetadataRequestMetadataSharedInfo"""

    shared: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataStickerInfo(BaseModel):
    """Nested model for CreateMetadataRequestMetadataStickerInfo"""

    stickers: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataRequestMetadataUploadSource(BaseModel):
    """Nested model for CreateMetadataRequestMetadataUploadSource"""

    upload_source: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseData(BaseModel):
    """Nested model for CreateMetadataResponseData"""

    associated_metadata: Optional["CreateMetadataResponseDataAssociatedMetadata"] = None
    id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadata(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadata"""

    allow_download_status: Optional[
        "CreateMetadataResponseDataAssociatedMetadataAllowDownloadStatus"
    ] = None
    alt_text: Optional["CreateMetadataResponseDataAssociatedMetadataAltText"] = None
    audience_policy: Optional[
        "CreateMetadataResponseDataAssociatedMetadataAudiencePolicy"
    ] = None
    content_expiration: Optional[
        "CreateMetadataResponseDataAssociatedMetadataContentExpiration"
    ] = None
    domain_restrictions: Optional[
        "CreateMetadataResponseDataAssociatedMetadataDomainRestrictions"
    ] = None
    found_media_origin: Optional[
        "CreateMetadataResponseDataAssociatedMetadataFoundMediaOrigin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional[
        "CreateMetadataResponseDataAssociatedMetadataManagementInfo"
    ] = None
    preview_image: Optional[
        "CreateMetadataResponseDataAssociatedMetadataPreviewImage"
    ] = None
    sensitive_media_warning: Optional[
        "CreateMetadataResponseDataAssociatedMetadataSensitiveMediaWarning"
    ] = None
    shared_info: Optional["CreateMetadataResponseDataAssociatedMetadataSharedInfo"] = (
        None
    )
    sticker_info: Optional[
        "CreateMetadataResponseDataAssociatedMetadataStickerInfo"
    ] = None
    upload_source: Optional[
        "CreateMetadataResponseDataAssociatedMetadataUploadSource"
    ] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataAllowDownloadStatus(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataAllowDownloadStatus"""

    allow_download: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataAltText(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataAltText"""

    text: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataAudiencePolicy(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataAudiencePolicy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataContentExpiration(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataContentExpiration"""

    timestamp_sec: Optional[float] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataDomainRestrictions(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataDomainRestrictions"""

    whitelist: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataFoundMediaOrigin(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataFoundMediaOrigin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataManagementInfo(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataManagementInfo"""

    managed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataPreviewImage(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataPreviewImage"""

    media_key: Optional[
        "CreateMetadataResponseDataAssociatedMetadataPreviewImageMediaKey"
    ] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataPreviewImageMediaKey(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataPreviewImageMediaKey"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataSensitiveMediaWarning(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataSensitiveMediaWarning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataSharedInfo(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataSharedInfo"""

    shared: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataStickerInfo(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataStickerInfo"""

    stickers: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateMetadataResponseDataAssociatedMetadataUploadSource(BaseModel):
    """Nested model for CreateMetadataResponseDataAssociatedMetadataUploadSource"""

    upload_source: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_analytics


class GetAnalyticsResponse(BaseModel):
    """Response model for get_analytics"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_keys


class GetByKeysResponse(BaseModel):
    """Response model for get_by_keys"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for finalize_upload


class FinalizeUploadResponse(BaseModel):
    """Response model for finalize_upload"""

    data: Optional["FinalizeUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class FinalizeUploadResponseData(BaseModel):
    """Nested model for FinalizeUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["FinalizeUploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class FinalizeUploadResponseDataProcessingInfo(BaseModel):
    """Nested model for FinalizeUploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for append_upload


class AppendUploadRequest(BaseModel):
    """Request model for append_upload"""

    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)
    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


class AppendUploadResponse(BaseModel):
    """Response model for append_upload"""

    data: Optional["AppendUploadResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class AppendUploadResponseData(BaseModel):
    """Nested model for AppendUploadResponseData"""

    expires_at: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_upload_status


class GetUploadStatusResponse(BaseModel):
    """Response model for get_upload_status"""

    data: Optional["GetUploadStatusResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUploadStatusResponseData(BaseModel):
    """Nested model for GetUploadStatusResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["GetUploadStatusResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUploadStatusResponseDataProcessingInfo(BaseModel):
    """Nested model for GetUploadStatusResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for upload


class UploadRequest(BaseModel):
    """Request model for upload"""

    additional_owners: Optional[List] = None
    media: Any = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class UploadResponse(BaseModel):
    """Response model for upload"""

    data: Optional["UploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UploadResponseData(BaseModel):
    """Nested model for UploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["UploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class UploadResponseDataProcessingInfo(BaseModel):
    """Nested model for UploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_subtitles


class CreateSubtitlesRequest(BaseModel):
    """Request model for create_subtitles"""

    id: Optional[str] = None
    media_category: Optional[str] = None
    subtitles: Optional["CreateSubtitlesRequestSubtitles"] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateSubtitlesResponse(BaseModel):
    """Response model for create_subtitles"""

    data: Optional["CreateSubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateSubtitlesRequestSubtitles(BaseModel):
    """Nested model for CreateSubtitlesRequestSubtitles"""

    display_name: Optional[str] = None
    id: Optional[str] = None
    language_code: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateSubtitlesResponseData(BaseModel):
    """Nested model for CreateSubtitlesResponseData"""

    associated_subtitles: Optional[List] = None
    id: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete_subtitles


class DeleteSubtitlesRequest(BaseModel):
    """Request model for delete_subtitles"""

    id: Optional[str] = None
    language_code: Optional[str] = None
    media_category: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteSubtitlesResponse(BaseModel):
    """Response model for delete_subtitles"""

    data: Optional["DeleteSubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteSubtitlesResponseData(BaseModel):
    """Nested model for DeleteSubtitlesResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for initialize_upload


class InitializeUploadRequest(BaseModel):
    """Request model for initialize_upload"""

    additional_owners: Optional[List] = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None
    total_bytes: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class InitializeUploadResponse(BaseModel):
    """Response model for initialize_upload"""

    data: Optional["InitializeUploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class InitializeUploadResponseData(BaseModel):
    """Nested model for InitializeUploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["InitializeUploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class InitializeUploadResponseDataProcessingInfo(BaseModel):
    """Nested model for InitializeUploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_key


class GetByKeyResponse(BaseModel):
    """Response model for get_by_key"""

    data: Optional["GetByKeyResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByKeyResponseData(BaseModel):
    """Nested model for GetByKeyResponseData"""

    height: Optional[int] = None
    media_key: Optional[str] = None
    type: Optional[str] = None
    width: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
