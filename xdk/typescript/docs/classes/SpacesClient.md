[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / SpacesClient

# Class: SpacesClient

Client for spaces operations

This client provides methods for interacting with the spaces endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all spaces related operations.

## Table of contents

### Constructors

- [constructor](SpacesClient.md#constructor)

### Methods

- [getByIds](SpacesClient.md#getbyids)
- [search](SpacesClient.md#search)
- [getBuyers](SpacesClient.md#getbuyers)
- [getPosts](SpacesClient.md#getposts)
- [getById](SpacesClient.md#getbyid)
- [getByCreatorIds](SpacesClient.md#getbycreatorids)

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

[spaces/client.ts:190](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L190)

## Methods

### getByIds

▸ **getByIds**(`ids`, `options?`): `Promise`\<[`Get2SpacesResponse`](../interfaces/Schemas.Get2SpacesResponse.md)\>

Get Spaces by IDs
Retrieves details of multiple Spaces by their IDs.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ids` | `any`[] | The list of Space IDs to return. |
| `options` | `GetByIdsOptions` | - |

#### Returns

`Promise`\<[`Get2SpacesResponse`](../interfaces/Schemas.Get2SpacesResponse.md)\>

Promise resolving to the API response

#### Defined in

[spaces/client.ts:207](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L207)

___

### search

▸ **search**(`query`, `options?`): `Promise`\<[`Get2SpacesSearchResponse`](../interfaces/Schemas.Get2SpacesSearchResponse.md)\>

Search Spaces
Retrieves a list of Spaces matching the specified search query.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | The search query. |
| `options` | `SearchOptions` | - |

#### Returns

`Promise`\<[`Get2SpacesSearchResponse`](../interfaces/Schemas.Get2SpacesSearchResponse.md)\>

Promise resolving to the API response

#### Defined in

[spaces/client.ts:277](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L277)

___

### getBuyers

▸ **getBuyers**(`id`, `options?`): `Promise`\<[`Get2SpacesIdBuyersResponse`](../interfaces/Schemas.Get2SpacesIdBuyersResponse.md)\>

Get Space ticket buyers
Retrieves a list of Users who purchased tickets to a specific Space by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the Space to be retrieved. |
| `options` | `GetBuyersOptions` | - |

#### Returns

`Promise`\<[`Get2SpacesIdBuyersResponse`](../interfaces/Schemas.Get2SpacesIdBuyersResponse.md)\>

Promise resolving to the API response

#### Defined in

[spaces/client.ts:359](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L359)

___

### getPosts

▸ **getPosts**(`id`, `options?`): `Promise`\<[`Get2SpacesIdTweetsResponse`](../interfaces/Schemas.Get2SpacesIdTweetsResponse.md)\>

Get Space Posts
Retrieves a list of Posts shared in a specific Space by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the Space to be retrieved. |
| `options` | `GetPostsOptions` | - |

#### Returns

`Promise`\<[`Get2SpacesIdTweetsResponse`](../interfaces/Schemas.Get2SpacesIdTweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[spaces/client.ts:433](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L433)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`Get2SpacesIdResponse`](../interfaces/Schemas.Get2SpacesIdResponse.md)\>

Get space by ID
Retrieves details of a specific space by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the Space to be retrieved. |
| `options` | `GetByIdOptions` | - |

#### Returns

`Promise`\<[`Get2SpacesIdResponse`](../interfaces/Schemas.Get2SpacesIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[spaces/client.ts:519](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L519)

___

### getByCreatorIds

▸ **getByCreatorIds**(`userIds`, `options?`): `Promise`\<[`Get2SpacesByCreatorIdsResponse`](../interfaces/Schemas.Get2SpacesByCreatorIdsResponse.md)\>

Get Spaces by creator IDs
Retrieves details of Spaces created by specified User IDs.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `userIds` | `any`[] | The IDs of Users to search through. |
| `options` | `GetByCreatorIdsOptions` | - |

#### Returns

`Promise`\<[`Get2SpacesByCreatorIdsResponse`](../interfaces/Schemas.Get2SpacesByCreatorIdsResponse.md)\>

Promise resolving to the API response

#### Defined in

[spaces/client.ts:587](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/spaces/client.ts#L587)
