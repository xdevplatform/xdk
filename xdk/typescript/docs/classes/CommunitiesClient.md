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

- [getById](CommunitiesClient.md#getbyid)
- [search](CommunitiesClient.md#search)

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

[communities/client.ts:43](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/communities/client.ts#L43)

## Methods

### getById

▸ **getById**(): `Promise`\<`any`\>

Get Community by ID
Retrieves details of a specific Community by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[communities/client.ts:57](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/communities/client.ts#L57)

___

### search

▸ **search**(`options?`): `Promise`\<`any`\>

Search Communities
Retrieves a list of Communities matching the specified search query.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `SearchOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[communities/client.ts:90](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/communities/client.ts#L90)
