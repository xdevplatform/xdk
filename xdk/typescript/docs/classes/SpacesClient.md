[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / SpacesClient

# Class: SpacesClient

Client for spaces operations

This client provides methods for interacting with the spaces endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all spaces related operations.

## Table of contents

### Constructors

- [constructor](SpacesClient.md#constructor)

### Methods

- [getByCreatorIds](SpacesClient.md#getbycreatorids)
- [search](SpacesClient.md#search)
- [getPosts](SpacesClient.md#getposts)
- [getById](SpacesClient.md#getbyid)
- [getByIds](SpacesClient.md#getbyids)
- [getBuyers](SpacesClient.md#getbuyers)

## Constructors

### constructor

• **new SpacesClient**(`client`): [`SpacesClient`](SpacesClient.md)

Creates a new spaces client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`SpacesClient`](SpacesClient.md)

#### Defined in

[spaces/client.ts:70](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L70)

## Methods

### getByCreatorIds

▸ **getByCreatorIds**(): `Promise`\<`any`\>

Get Spaces by creator IDs
Retrieves details of Spaces created by specified User IDs.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[spaces/client.ts:84](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L84)

___

### search

▸ **search**(`options?`): `Promise`\<`any`\>

Search Spaces
Retrieves a list of Spaces matching the specified search query.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `SearchOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[spaces/client.ts:117](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L117)

___

### getPosts

▸ **getPosts**(`options?`): `Promise`\<`any`\>

Get Space Posts
Retrieves a list of Posts shared in a specific Space by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetPostsOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[spaces/client.ts:150](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L150)

___

### getById

▸ **getById**(): `Promise`\<`any`\>

Get space by ID
Retrieves details of a specific space by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[spaces/client.ts:183](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L183)

___

### getByIds

▸ **getByIds**(): `Promise`\<`any`\>

Get Spaces by IDs
Retrieves details of multiple Spaces by their IDs.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[spaces/client.ts:216](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L216)

___

### getBuyers

▸ **getBuyers**(`options?`): `Promise`\<`any`\>

Get Space ticket buyers
Retrieves a list of Users who purchased tickets to a specific Space by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetBuyersOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[spaces/client.ts:249](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/spaces/client.ts#L249)
