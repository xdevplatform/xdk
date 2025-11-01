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

[trends/client.ts:62](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/trends/client.ts#L62)

## Methods

### getPersonalized

▸ **getPersonalized**(`options?`): `Promise`\<[`Get2UsersPersonalizedTrendsResponse`](../interfaces/Schemas.Get2UsersPersonalizedTrendsResponse.md)\>

Get personalized Trends
Retrieves personalized trending topics for the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetPersonalizedOptions` |

#### Returns

`Promise`\<[`Get2UsersPersonalizedTrendsResponse`](../interfaces/Schemas.Get2UsersPersonalizedTrendsResponse.md)\>

Promise resolving to the API response

#### Defined in

[trends/client.ts:75](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/trends/client.ts#L75)

___

### getByWoeid

▸ **getByWoeid**(`woeid`, `options?`): `Promise`\<[`Get2TrendsByWoeidWoeidResponse`](../interfaces/Schemas.Get2TrendsByWoeidWoeidResponse.md)\>

Get Trends by WOEID
Retrieves trending topics for a specific location identified by its WOEID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `woeid` | `number` | The WOEID of the place to lookup a trend for. |
| `options` | `GetByWoeidOptions` | - |

#### Returns

`Promise`\<[`Get2TrendsByWoeidWoeidResponse`](../interfaces/Schemas.Get2TrendsByWoeidWoeidResponse.md)\>

Promise resolving to the API response

#### Defined in

[trends/client.ts:125](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/trends/client.ts#L125)
