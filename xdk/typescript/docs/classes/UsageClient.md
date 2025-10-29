[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UsageClient

# Class: UsageClient

Client for Usage operations

This client provides methods for interacting with the Usage endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Usage related operations.

## Table of contents

### Constructors

- [constructor](UsageClient.md#constructor)

### Methods

- [get](UsageClient.md#get)

## Constructors

### constructor

• **new UsageClient**(`client`): [`UsageClient`](UsageClient.md)

Creates a new Usage client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`UsageClient`](UsageClient.md)

#### Defined in

[usage/client.ts:47](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/usage/client.ts#L47)

## Methods

### get

▸ **get**(`options?`): `Promise`\<[`UsageGetResponse`](../interfaces/UsageGetResponse.md)\>

Get usage
Retrieves usage statistics for Posts over a specified number of days.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`UsageGetOptions`](../interfaces/UsageGetOptions.md) |

#### Returns

`Promise`\<[`UsageGetResponse`](../interfaces/UsageGetResponse.md)\>

Promise with the API response

#### Defined in

[usage/client.ts:59](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/usage/client.ts#L59)
