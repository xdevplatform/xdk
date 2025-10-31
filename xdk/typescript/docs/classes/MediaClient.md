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

- [createSubtitles](MediaClient.md#createsubtitles)
- [deleteSubtitles](MediaClient.md#deletesubtitles)
- [getAnalytics](MediaClient.md#getanalytics)
- [getUploadStatus](MediaClient.md#getuploadstatus)
- [upload](MediaClient.md#upload)
- [createMetadata](MediaClient.md#createmetadata)
- [initializeUpload](MediaClient.md#initializeupload)
- [finalizeUpload](MediaClient.md#finalizeupload)
- [appendUpload](MediaClient.md#appendupload)
- [getByKey](MediaClient.md#getbykey)
- [getByKeys](MediaClient.md#getbykeys)

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

[media/client.ts:139](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L139)

## Methods

### createSubtitles

▸ **createSubtitles**(`options?`): `Promise`\<`any`\>

Create Media subtitles
Creates subtitles for a specific Media file.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateSubtitlesOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:151](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L151)

___

### deleteSubtitles

▸ **deleteSubtitles**(`options?`): `Promise`\<`any`\>

Delete Media subtitles
Deletes subtitles for a specific Media file.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `DeleteSubtitlesOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:190](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L190)

___

### getAnalytics

▸ **getAnalytics**(): `Promise`\<`any`\>

Get Media analytics
Retrieves analytics data for media.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:237](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L237)

___

### getUploadStatus

▸ **getUploadStatus**(`options?`): `Promise`\<`any`\>

Get Media upload status
Retrieves the status of a Media upload by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetUploadStatusOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:270](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L270)

___

### upload

▸ **upload**(`options?`): `Promise`\<`any`\>

Upload media
Uploads a media file for use in posts or other content.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `UploadOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:303](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L303)

___

### createMetadata

▸ **createMetadata**(`options?`): `Promise`\<`any`\>

Create Media metadata
Creates metadata for a Media file.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateMetadataOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:340](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L340)

___

### initializeUpload

▸ **initializeUpload**(`options?`): `Promise`\<`any`\>

Initialize media upload
Initializes a media upload.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `InitializeUploadOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:379](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L379)

___

### finalizeUpload

▸ **finalizeUpload**(): `Promise`\<`any`\>

Finalize Media upload
Finalizes a Media upload request.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:420](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L420)

___

### appendUpload

▸ **appendUpload**(`options?`): `Promise`\<`any`\>

Append Media upload
Appends data to a Media upload request.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `AppendUploadOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:453](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L453)

___

### getByKey

▸ **getByKey**(): `Promise`\<`any`\>

Get Media by media key
Retrieves details of a specific Media file by its media key.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:494](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L494)

___

### getByKeys

▸ **getByKeys**(): `Promise`\<`any`\>

Get Media by media keys
Retrieves details of Media files by their media keys.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[media/client.ts:527](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/media/client.ts#L527)
