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

[usage/client.ts:49](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/usage/client.ts#L49)

## Methods

### get

▸ **get**(`options?`): `Promise`\<[`Get2UsageTweetsResponse`](../interfaces/Schemas.Get2UsageTweetsResponse.md)\>

Get usage
Retrieves usage statistics for Posts over a specified number of days.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetOptions` |

#### Returns

`Promise`\<[`Get2UsageTweetsResponse`](../interfaces/Schemas.Get2UsageTweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[usage/client.ts:62](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/usage/client.ts#L62)
