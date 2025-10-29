[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / TrendsClient

# Class: TrendsClient

Client for Trends operations

This client provides methods for interacting with the Trends endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Trends related operations.

## Table of contents

### Constructors

- [constructor](TrendsClient.md#constructor)

### Methods

- [getByWoeid](TrendsClient.md#getbywoeid)
- [getPersonalizedTrends](TrendsClient.md#getpersonalizedtrends)

## Constructors

### constructor

• **new TrendsClient**(`client`): [`TrendsClient`](TrendsClient.md)

Creates a new Trends client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`TrendsClient`](TrendsClient.md)

#### Defined in

[trends/client.ts:61](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/trends/client.ts#L61)

## Methods

### getByWoeid

▸ **getByWoeid**(`woeid`, `options?`): `Promise`\<[`TrendsGetByWoeidResponse`](../interfaces/TrendsGetByWoeidResponse.md)\>

Get Trends by WOEID
Retrieves trending topics for a specific location identified by its WOEID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `woeid` | `number` | The WOEID of the place to lookup a trend for. |
| `options` | [`TrendsGetByWoeidOptions`](../interfaces/TrendsGetByWoeidOptions.md) | - |

#### Returns

`Promise`\<[`TrendsGetByWoeidResponse`](../interfaces/TrendsGetByWoeidResponse.md)\>

Promise with the API response

#### Defined in

[trends/client.ts:77](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/trends/client.ts#L77)

___

### getPersonalizedTrends

▸ **getPersonalizedTrends**(`options?`): `Promise`\<[`TrendsGetPersonalizedTrendsResponse`](../interfaces/TrendsGetPersonalizedTrendsResponse.md)\>

Get personalized Trends
Retrieves personalized trending topics for the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`TrendsGetPersonalizedTrendsOptions`](../interfaces/TrendsGetPersonalizedTrendsOptions.md) |

#### Returns

`Promise`\<[`TrendsGetPersonalizedTrendsResponse`](../interfaces/TrendsGetPersonalizedTrendsResponse.md)\>

Promise with the API response

#### Defined in

[trends/client.ts:127](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/trends/client.ts#L127)
