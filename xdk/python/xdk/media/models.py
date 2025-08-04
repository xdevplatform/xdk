"""
Media models for the X API.

This module provides models for the Media endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getMediaByMediaKeys


class GetmediabymediakeysResponse(BaseModel):
    """Response model for getMediaByMediaKeys"""

    data: Optional[List] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for finalizeMediaUpload


class FinalizemediauploadResponse(BaseModel):
    """Response model for finalizeMediaUpload"""

    data: Optional["FinalizemediauploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FinalizemediauploadResponseData(BaseModel):
    """Nested model for FinalizemediauploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["FinalizemediauploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FinalizemediauploadResponseDataProcessingInfo(BaseModel):
    """Nested model for FinalizemediauploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaByMediaKey


class GetmediabymediakeyResponse(BaseModel):
    """Response model for getMediaByMediaKey"""

    data: Optional["GetmediabymediakeyResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetmediabymediakeyResponseData(BaseModel):
    """Nested model for GetmediabymediakeyResponseData"""

    height: Optional[int] = None
    media_key: Optional[str] = None
    type: Optional[str] = None
    width: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaUploadStatus


class GetmediauploadstatusResponse(BaseModel):
    """Response model for getMediaUploadStatus"""

    data: Optional["GetmediauploadstatusResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetmediauploadstatusResponseData(BaseModel):
    """Nested model for GetmediauploadstatusResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["GetmediauploadstatusResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetmediauploadstatusResponseDataProcessingInfo(BaseModel):
    """Nested model for GetmediauploadstatusResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for mediaUpload


class MediauploadRequest(BaseModel):
    """Request model for mediaUpload"""

    additional_owners: Optional[List] = None
    media: Any = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MediauploadResponse(BaseModel):
    """Response model for mediaUpload"""

    data: Optional["MediauploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MediauploadResponseData(BaseModel):
    """Nested model for MediauploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["MediauploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class MediauploadResponseDataProcessingInfo(BaseModel):
    """Nested model for MediauploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createMediaSubtitles


class CreatemediasubtitlesRequest(BaseModel):
    """Request model for createMediaSubtitles"""

    id: Optional[str] = None
    media_category: Optional[str] = None
    subtitles: Optional["CreatemediasubtitlesRequestSubtitles"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediasubtitlesResponse(BaseModel):
    """Response model for createMediaSubtitles"""

    data: Optional["CreatemediasubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediasubtitlesRequestSubtitles(BaseModel):
    """Nested model for CreatemediasubtitlesRequestSubtitles"""

    display_name: Optional[str] = None
    id: Optional[str] = None
    language_code: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediasubtitlesResponseData(BaseModel):
    """Nested model for CreatemediasubtitlesResponseData"""

    associated_subtitles: Optional[List] = None
    id: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteMediaSubtitles


class DeletemediasubtitlesRequest(BaseModel):
    """Request model for deleteMediaSubtitles"""

    id: Optional[str] = None
    language_code: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeletemediasubtitlesResponse(BaseModel):
    """Response model for deleteMediaSubtitles"""

    data: Optional["DeletemediasubtitlesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeletemediasubtitlesResponseData(BaseModel):
    """Nested model for DeletemediasubtitlesResponseData"""

    deleted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createMediaMetadata


class CreatemediametadataRequest(BaseModel):
    """Request model for createMediaMetadata"""

    id: Optional[str] = None
    metadata: Optional["CreatemediametadataRequestMetadata"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponse(BaseModel):
    """Response model for createMediaMetadata"""

    data: Optional["CreatemediametadataResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadata(BaseModel):
    """Nested model for CreatemediametadataRequestMetadata"""

    allow_download_status: Optional[
        "CreatemediametadataRequestMetadataAllowDownloadStatus"
    ] = None
    alt_text: Optional["CreatemediametadataRequestMetadataAltText"] = None
    audience_policy: Optional["CreatemediametadataRequestMetadataAudiencePolicy"] = None
    content_expiration: Optional[
        "CreatemediametadataRequestMetadataContentExpiration"
    ] = None
    domain_restrictions: Optional[
        "CreatemediametadataRequestMetadataDomainRestrictions"
    ] = None
    found_media_origin: Optional[
        "CreatemediametadataRequestMetadataFoundMediaOrigin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional["CreatemediametadataRequestMetadataManagementInfo"] = None
    preview_image: Optional["CreatemediametadataRequestMetadataPreviewImage"] = None
    sensitive_media_warning: Optional[
        "CreatemediametadataRequestMetadataSensitiveMediaWarning"
    ] = None
    shared_info: Optional["CreatemediametadataRequestMetadataSharedInfo"] = None
    sticker_info: Optional["CreatemediametadataRequestMetadataStickerInfo"] = None
    upload_source: Optional["CreatemediametadataRequestMetadataUploadSource"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataAllowDownloadStatus(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataAllowDownloadStatus"""

    allow_download: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataAltText(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataAltText"""

    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataAudiencePolicy(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataAudiencePolicy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataContentExpiration(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataContentExpiration"""

    timestamp_sec: Optional[float] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataDomainRestrictions(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataDomainRestrictions"""

    whitelist: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataFoundMediaOrigin(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataFoundMediaOrigin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataManagementInfo(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataManagementInfo"""

    managed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataPreviewImage(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataPreviewImage"""

    media_key: Optional["CreatemediametadataRequestMetadataPreviewImageMediaKey"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataPreviewImageMediaKey(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataPreviewImageMediaKey"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataSensitiveMediaWarning(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataSensitiveMediaWarning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataSharedInfo(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataSharedInfo"""

    shared: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataStickerInfo(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataStickerInfo"""

    stickers: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataRequestMetadataUploadSource(BaseModel):
    """Nested model for CreatemediametadataRequestMetadataUploadSource"""

    upload_source: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseData(BaseModel):
    """Nested model for CreatemediametadataResponseData"""

    associated_metadata: Optional[
        "CreatemediametadataResponseDataAssociatedMetadata"
    ] = None
    id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadata(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadata"""

    allow_download_status: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataAllowDownloadStatus"
    ] = None
    alt_text: Optional["CreatemediametadataResponseDataAssociatedMetadataAltText"] = (
        None
    )
    audience_policy: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataAudiencePolicy"
    ] = None
    content_expiration: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataContentExpiration"
    ] = None
    domain_restrictions: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataDomainRestrictions"
    ] = None
    found_media_origin: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataFoundMediaOrigin"
    ] = None
    geo_restrictions: Any = None
    management_info: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataManagementInfo"
    ] = None
    preview_image: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataPreviewImage"
    ] = None
    sensitive_media_warning: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataSensitiveMediaWarning"
    ] = None
    shared_info: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataSharedInfo"
    ] = None
    sticker_info: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataStickerInfo"
    ] = None
    upload_source: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataUploadSource"
    ] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataAllowDownloadStatus(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataAllowDownloadStatus"""

    allow_download: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataAltText(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataAltText"""

    text: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataAudiencePolicy(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataAudiencePolicy"""

    creator_subscriptions: Optional[List] = None
    x_subscriptions: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataContentExpiration(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataContentExpiration"""

    timestamp_sec: Optional[float] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataDomainRestrictions(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataDomainRestrictions"""

    whitelist: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataFoundMediaOrigin(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataFoundMediaOrigin"""

    id: Optional[str] = None
    provider: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataManagementInfo(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataManagementInfo"""

    managed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataPreviewImage(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataPreviewImage"""

    media_key: Optional[
        "CreatemediametadataResponseDataAssociatedMetadataPreviewImageMediaKey"
    ] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataPreviewImageMediaKey(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataPreviewImageMediaKey"""

    media: Optional[str] = None
    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataSensitiveMediaWarning(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataSensitiveMediaWarning"""

    adult_content: Optional[bool] = None
    graphic_violence: Optional[bool] = None
    other: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataSharedInfo(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataSharedInfo"""

    shared: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataStickerInfo(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataStickerInfo"""

    stickers: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatemediametadataResponseDataAssociatedMetadataUploadSource(BaseModel):
    """Nested model for CreatemediametadataResponseDataAssociatedMetadataUploadSource"""

    upload_source: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for initializeMediaUpload


class InitializemediauploadRequest(BaseModel):
    """Request model for initializeMediaUpload"""

    additional_owners: Optional[List] = None
    media_category: Optional[str] = None
    media_type: Optional[str] = None
    shared: Optional[bool] = None
    total_bytes: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class InitializemediauploadResponse(BaseModel):
    """Response model for initializeMediaUpload"""

    data: Optional["InitializemediauploadResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class InitializemediauploadResponseData(BaseModel):
    """Nested model for InitializemediauploadResponseData"""

    expires_after_secs: Optional[int] = None
    id: Optional[str] = None
    media_key: Optional[str] = None
    processing_info: Optional["InitializemediauploadResponseDataProcessingInfo"] = None
    size: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class InitializemediauploadResponseDataProcessingInfo(BaseModel):
    """Nested model for InitializemediauploadResponseDataProcessingInfo"""

    check_after_secs: Optional[int] = None
    progress_percent: Optional[int] = None
    state: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for appendMediaUpload


class AppendmediauploadRequest(BaseModel):
    """Request model for appendMediaUpload"""

    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)
    media: Optional[str] = Field(default=None, description="The file to upload.")
    segment_index: Optional[Any] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class AppendmediauploadResponse(BaseModel):
    """Response model for appendMediaUpload"""

    data: Optional["AppendmediauploadResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class AppendmediauploadResponseData(BaseModel):
    """Nested model for AppendmediauploadResponseData"""

    expires_at: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getMediaAnalytics


class GetmediaanalyticsResponse(BaseModel):
    """Response model for getMediaAnalytics"""

    data: Optional[List] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
