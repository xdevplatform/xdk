[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / CommunitiesClient

# Class: CommunitiesClient

Client for communities operations

This client provides methods for interacting with the communities endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all communities related operations.

## Table of contents

### Constructors

- [constructor](CommunitiesClient.md#constructor)

### Methods

- [search](CommunitiesClient.md#search)
- [getById](CommunitiesClient.md#getbyid)

## Constructors

### constructor

• **new CommunitiesClient**(`client`): [`CommunitiesClient`](CommunitiesClient.md)

Creates a new communities client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`CommunitiesClient`](CommunitiesClient.md)

#### Defined in

[communities/client.ts:68](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/communities/client.ts#L68)

## Methods

### search

▸ **search**(`query`, `options?`): `Promise`\<[`Get2CommunitiesSearchResponse`](../interfaces/Schemas.Get2CommunitiesSearchResponse.md)\>

Search Communities
Retrieves a list of Communities matching the specified search query.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | Query to search communities. |
| `options` | `SearchOptions` | - |

#### Returns

`Promise`\<[`Get2CommunitiesSearchResponse`](../interfaces/Schemas.Get2CommunitiesSearchResponse.md)\>

Promise resolving to the API response

#### Defined in

[communities/client.ts:85](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/communities/client.ts#L85)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`Get2CommunitiesIdResponse`](../interfaces/Schemas.Get2CommunitiesIdResponse.md)\>

Get Community by ID
Retrieves details of a specific Community by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the Community. |
| `options` | `GetByIdOptions` | - |

#### Returns

`Promise`\<[`Get2CommunitiesIdResponse`](../interfaces/Schemas.Get2CommunitiesIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[communities/client.ts:155](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/communities/client.ts#L155)
