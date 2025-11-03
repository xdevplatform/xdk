[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / MediaClient

# Class: MediaClient

Client for media operations

This client provides methods for interacting with the media endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all media related operations.

## Table of contents

### Constructors

- [constructor](MediaClient.md#constructor)

### Methods

- [getByKey](MediaClient.md#getbykey)
- [createMetadata](MediaClient.md#createmetadata)
- [getUploadStatus](MediaClient.md#getuploadstatus)
- [upload](MediaClient.md#upload)
- [appendUpload](MediaClient.md#appendupload)
- [getByKeys](MediaClient.md#getbykeys)
- [getAnalytics](MediaClient.md#getanalytics)
- [initializeUpload](MediaClient.md#initializeupload)
- [finalizeUpload](MediaClient.md#finalizeupload)
- [createSubtitles](MediaClient.md#createsubtitles)
- [deleteSubtitles](MediaClient.md#deletesubtitles)

## Constructors

### constructor

• **new MediaClient**(`client`): [`MediaClient`](MediaClient.md)

Creates a new media client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`MediaClient`](MediaClient.md)

#### Defined in

[media/client.ts:181](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L181)

## Methods

### getByKey

▸ **getByKey**(`mediaKey`, `options?`): `Promise`\<[`Get2MediaMediaKeyResponse`](../interfaces/Schemas.Get2MediaMediaKeyResponse.md)\>

Get Media by media key
Retrieves details of a specific Media file by its media key.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mediaKey` | `string` | A single Media Key. |
| `options` | `GetByKeyOptions` | - |

#### Returns

`Promise`\<[`Get2MediaMediaKeyResponse`](../interfaces/Schemas.Get2MediaMediaKeyResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:198](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L198)

___

### createMetadata

▸ **createMetadata**(`options?`): `Promise`\<[`MetadataCreateResponse`](../interfaces/Schemas.MetadataCreateResponse.md)\>

Create Media metadata
Creates metadata for a Media file.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateMetadataOptions` |

#### Returns

`Promise`\<[`MetadataCreateResponse`](../interfaces/Schemas.MetadataCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:244](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L244)

___

### getUploadStatus

▸ **getUploadStatus**(`mediaId`, `options?`): `Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Get Media upload status
Retrieves the status of a Media upload by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mediaId` | `any` | Media id for the requested media upload status. |
| `options` | `GetUploadStatusOptions` | - |

#### Returns

`Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:289](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L289)

___

### upload

▸ **upload**(`options?`): `Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Upload media
Uploads a media file for use in posts or other content.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `UploadOptions` |

#### Returns

`Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:337](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L337)

___

### appendUpload

▸ **appendUpload**(`id`, `options?`): `Promise`\<[`MediaUploadAppendResponse`](../interfaces/Schemas.MediaUploadAppendResponse.md)\>

Append Media upload
Appends data to a Media upload request.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The media identifier for the media to perform the append operation. |
| `options` | `AppendUploadOptions` | - |

#### Returns

`Promise`\<[`MediaUploadAppendResponse`](../interfaces/Schemas.MediaUploadAppendResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:380](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L380)

___

### getByKeys

▸ **getByKeys**(`mediaKeys`, `options?`): `Promise`\<[`Get2MediaResponse`](../interfaces/Schemas.Get2MediaResponse.md)\>

Get Media by media keys
Retrieves details of Media files by their media keys.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mediaKeys` | `any`[] | A comma separated list of Media Keys. Up to 100 are allowed in a single request. |
| `options` | `GetByKeysOptions` | - |

#### Returns

`Promise`\<[`Get2MediaResponse`](../interfaces/Schemas.Get2MediaResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:428](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L428)

___

### getAnalytics

▸ **getAnalytics**(`mediaKeys`, `endTime`, `startTime`, `granularity`, `options?`): `Promise`\<[`MediaAnalytics`](../interfaces/Schemas.MediaAnalytics.md)\>

Get Media analytics
Retrieves analytics data for media.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mediaKeys` | `any`[] | A comma separated list of Media Keys. Up to 100 are allowed in a single request. |
| `endTime` | `string` | YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range. |
| `startTime` | `string` | YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range. |
| `granularity` | `string` | The granularity for the search counts results. |
| `options` | `GetAnalyticsOptions` | - |

#### Returns

`Promise`\<[`MediaAnalytics`](../interfaces/Schemas.MediaAnalytics.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:492](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L492)

___

### initializeUpload

▸ **initializeUpload**(`options?`): `Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Initialize media upload
Initializes a media upload.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `InitializeUploadOptions` |

#### Returns

`Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:555](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L555)

___

### finalizeUpload

▸ **finalizeUpload**(`id`): `Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Finalize Media upload
Finalizes a Media upload request.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The media id of the targeted media to finalize. |

#### Returns

`Promise`\<[`MediaUploadResponse`](../interfaces/Schemas.MediaUploadResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:600](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L600)

___

### createSubtitles

▸ **createSubtitles**(`options?`): `Promise`\<[`SubtitlesCreateResponse`](../interfaces/Schemas.SubtitlesCreateResponse.md)\>

Create Media subtitles
Creates subtitles for a specific Media file.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateSubtitlesOptions` |

#### Returns

`Promise`\<[`SubtitlesCreateResponse`](../interfaces/Schemas.SubtitlesCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:634](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L634)

___

### deleteSubtitles

▸ **deleteSubtitles**(`options?`): `Promise`\<[`SubtitlesDeleteResponse`](../interfaces/Schemas.SubtitlesDeleteResponse.md)\>

Delete Media subtitles
Deletes subtitles for a specific Media file.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `DeleteSubtitlesOptions` |

#### Returns

`Promise`\<[`SubtitlesDeleteResponse`](../interfaces/Schemas.SubtitlesDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[media/client.ts:675](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/media/client.ts#L675)
