[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / MediaUploadConfigRequest

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

[schemas.ts:1695](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L1695)

___

### mediaCategory

• `Optional` **mediaCategory**: [`MediaCategory`](../modules/Schemas.md#mediacategory)

#### Defined in

[schemas.ts:1696](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L1696)

___

### mediaType

• `Optional` **mediaType**: ``"video/mp4"`` \| ``"video/webm"`` \| ``"video/mp2t"`` \| ``"video/quicktime"`` \| ``"text/srt"`` \| ``"text/vtt"`` \| ``"image/jpeg"`` \| ``"image/gif"`` \| ``"image/bmp"`` \| ``"image/png"`` \| ``"image/webp"`` \| ``"image/pjpeg"`` \| ``"image/tiff"`` \| ``"model/gltf-binary"`` \| ``"model/vnd.usdz+zip"``

The type of media.

#### Defined in

[schemas.ts:1697](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L1697)

___

### shared

• `Optional` **shared**: `boolean`

Whether this media is shared or not.

#### Defined in

[schemas.ts:1713](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L1713)

___

### totalBytes

• `Optional` **totalBytes**: `number`

The total size of the media upload in bytes.

#### Defined in

[schemas.ts:1714](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L1714)
