[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ApiError

# Class: ApiError

API Error class for handling X API errors

## Hierarchy

- `Error`

  ↳ **`ApiError`**

## Table of contents

### Constructors

- [constructor](ApiError.md#constructor)

### Properties

- [status](ApiError.md#status)
- [statusText](ApiError.md#statustext)
- [headers](ApiError.md#headers)
- [data](ApiError.md#data)

## Constructors

### constructor

• **new ApiError**(`message`, `status`, `statusText`, `headers`, `data?`): [`ApiError`](ApiError.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `message` | `string` |
| `status` | `number` |
| `statusText` | `string` |
| `headers` | `Headers` |
| `data?` | `any` |

#### Returns

[`ApiError`](ApiError.md)

#### Overrides

Error.constructor

#### Defined in

[client.ts:120](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/client.ts#L120)

## Properties

### status

• `Readonly` **status**: `number`

#### Defined in

[client.ts:115](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/client.ts#L115)

___

### statusText

• `Readonly` **statusText**: `string`

#### Defined in

[client.ts:116](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/client.ts#L116)

___

### headers

• `Readonly` **headers**: `Headers`

#### Defined in

[client.ts:117](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/client.ts#L117)

___

### data

• `Optional` `Readonly` **data**: `any`

#### Defined in

[client.ts:118](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/client.ts#L118)
