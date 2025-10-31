[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UsageClient

# Class: UsageClient

Client for usage operations

This client provides methods for interacting with the usage endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all usage related operations.

## Table of contents

### Constructors

- [constructor](UsageClient.md#constructor)

### Methods

- [get](UsageClient.md#get)

## Constructors

### constructor

• **new UsageClient**(`client`): [`UsageClient`](UsageClient.md)

Creates a new usage client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`UsageClient`](UsageClient.md)

#### Defined in

[usage/client.ts:43](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/usage/client.ts#L43)

## Methods

### get

▸ **get**(`options?`): `Promise`\<`any`\>

Get usage
Retrieves usage statistics for Posts over a specified number of days.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[usage/client.ts:55](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/usage/client.ts#L55)
