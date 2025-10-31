[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / TrendsClient

# Class: TrendsClient

Client for trends operations

This client provides methods for interacting with the trends endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all trends related operations.

## Table of contents

### Constructors

- [constructor](TrendsClient.md#constructor)

### Methods

- [getPersonalized](TrendsClient.md#getpersonalized)
- [getByWoeid](TrendsClient.md#getbywoeid)

## Constructors

### constructor

• **new TrendsClient**(`client`): [`TrendsClient`](TrendsClient.md)

Creates a new trends client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`TrendsClient`](TrendsClient.md)

#### Defined in

[trends/client.ts:43](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/trends/client.ts#L43)

## Methods

### getPersonalized

▸ **getPersonalized**(): `Promise`\<`any`\>

Get personalized Trends
Retrieves personalized trending topics for the authenticated user.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[trends/client.ts:55](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/trends/client.ts#L55)

___

### getByWoeid

▸ **getByWoeid**(`options?`): `Promise`\<`any`\>

Get Trends by WOEID
Retrieves trending topics for a specific location identified by its WOEID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetByWoeidOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[trends/client.ts:88](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/trends/client.ts#L88)
