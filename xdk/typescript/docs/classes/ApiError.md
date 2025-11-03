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

[client.ts:118](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L118)

## Properties

### status

• `Readonly` **status**: `number`

#### Defined in

[client.ts:113](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L113)

___

### statusText

• `Readonly` **statusText**: `string`

#### Defined in

[client.ts:114](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L114)

___

### headers

• `Readonly` **headers**: `Headers`

#### Defined in

[client.ts:115](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L115)

___

### data

• `Optional` `Readonly` **data**: `any`

#### Defined in

[client.ts:116](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L116)
