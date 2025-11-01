[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / MediaUploadConfigRequest

# Interface: MediaUploadConfigRequest

[Schemas](../modules/Schemas.md).MediaUploadConfigRequest

## Table of contents

### Properties

- [additionalOwners](Schemas.MediaUploadConfigRequest.md#additionalowners)
- [mediaCategory](Schemas.MediaUploadConfigRequest.md#mediacategory)
- [mediaType](Schemas.MediaUploadConfigRequest.md#mediatype)
- [shared](Schemas.MediaUploadConfigRequest.md#shared)
- [totalBytes](Schemas.MediaUploadConfigRequest.md#totalbytes)

## Properties

### additionalOwners

• `Optional` **additionalOwners**: `string`[]

none

#### Defined in

[schemas.ts:1693](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1693)

___

### mediaCategory

• `Optional` **mediaCategory**: [`MediaCategory`](../modules/Schemas.md#mediacategory)

#### Defined in

[schemas.ts:1694](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1694)

___

### mediaType

• `Optional` **mediaType**: ``"video/mp4"`` \| ``"video/webm"`` \| ``"video/mp2t"`` \| ``"video/quicktime"`` \| ``"text/srt"`` \| ``"text/vtt"`` \| ``"image/jpeg"`` \| ``"image/gif"`` \| ``"image/bmp"`` \| ``"image/png"`` \| ``"image/webp"`` \| ``"image/pjpeg"`` \| ``"image/tiff"`` \| ``"model/gltf-binary"`` \| ``"model/vnd.usdz+zip"``

The type of media.

#### Defined in

[schemas.ts:1695](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1695)

___

### shared

• `Optional` **shared**: `boolean`

Whether this media is shared or not.

#### Defined in

[schemas.ts:1711](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1711)

___

### totalBytes

• `Optional` **totalBytes**: `number`

The total size of the media upload in bytes.

#### Defined in

[schemas.ts:1712](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1712)
