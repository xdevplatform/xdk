[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / ListsClient

# Class: ListsClient

Client for lists operations

This client provides methods for interacting with the lists endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all lists related operations.

## Table of contents

### Constructors

- [constructor](ListsClient.md#constructor)

### Methods

- [getFollowers](ListsClient.md#getfollowers)
- [getMembers](ListsClient.md#getmembers)
- [addMember](ListsClient.md#addmember)
- [removeMemberByUserId](ListsClient.md#removememberbyuserid)
- [getPosts](ListsClient.md#getposts)
- [getById](ListsClient.md#getbyid)
- [update](ListsClient.md#update)
- [delete](ListsClient.md#delete)
- [create](ListsClient.md#create)

## Constructors

### constructor

• **new ListsClient**(`client`): [`ListsClient`](ListsClient.md)

Creates a new lists client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`ListsClient`](ListsClient.md)

#### Defined in

[lists/client.ts:188](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L188)

## Methods

### getFollowers

▸ **getFollowers**(`id`, `options?`): `Promise`\<[`Get2ListsIdFollowersResponse`](../interfaces/Schemas.Get2ListsIdFollowersResponse.md)\>

Get List followers
Retrieves a list of Users who follow a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | `GetFollowersOptions` | - |

#### Returns

`Promise`\<[`Get2ListsIdFollowersResponse`](../interfaces/Schemas.Get2ListsIdFollowersResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:205](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L205)

___

### getMembers

▸ **getMembers**(`id`, `options?`): `Promise`\<[`Get2ListsIdMembersResponse`](../interfaces/Schemas.Get2ListsIdMembersResponse.md)\>

Get List members
Retrieves a list of Users who are members of a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | `GetMembersOptions` | - |

#### Returns

`Promise`\<[`Get2ListsIdMembersResponse`](../interfaces/Schemas.Get2ListsIdMembersResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:279](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L279)

___

### addMember

▸ **addMember**(`id`, `options?`): `Promise`\<[`ListMutateResponse`](../interfaces/Schemas.ListMutateResponse.md)\>

Add List member
Adds a User to a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List for which to add a member. |
| `options` | `AddMemberOptions` | - |

#### Returns

`Promise`\<[`ListMutateResponse`](../interfaces/Schemas.ListMutateResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:353](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L353)

___

### removeMemberByUserId

▸ **removeMemberByUserId**(`id`, `userId`): `Promise`\<[`ListMutateResponse`](../interfaces/Schemas.ListMutateResponse.md)\>

Remove List member
Removes a User from a specific List by its ID and the User’s ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List to remove a member. |
| `userId` | `string` | The ID of User that will be removed from the List. |

#### Returns

`Promise`\<[`ListMutateResponse`](../interfaces/Schemas.ListMutateResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:405](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L405)

___

### getPosts

▸ **getPosts**(`id`, `options?`): `Promise`\<[`Get2ListsIdTweetsResponse`](../interfaces/Schemas.Get2ListsIdTweetsResponse.md)\>

Get List Posts
Retrieves a list of Posts associated with a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | `GetPostsOptions` | - |

#### Returns

`Promise`\<[`Get2ListsIdTweetsResponse`](../interfaces/Schemas.Get2ListsIdTweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:448](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L448)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`Get2ListsIdResponse`](../interfaces/Schemas.Get2ListsIdResponse.md)\>

Get List by ID
Retrieves details of a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | `GetByIdOptions` | - |

#### Returns

`Promise`\<[`Get2ListsIdResponse`](../interfaces/Schemas.Get2ListsIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:540](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L540)

___

### update

▸ **update**(`id`, `options?`): `Promise`\<[`ListUpdateResponse`](../interfaces/Schemas.ListUpdateResponse.md)\>

Update List
Updates the details of a specific List owned by the authenticated user by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List to modify. |
| `options` | `UpdateOptions` | - |

#### Returns

`Promise`\<[`ListUpdateResponse`](../interfaces/Schemas.ListUpdateResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:602](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L602)

___

### delete

▸ **delete**(`id`): `Promise`\<[`ListDeleteResponse`](../interfaces/Schemas.ListDeleteResponse.md)\>

Delete List
Deletes a specific List owned by the authenticated user by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List to delete. |

#### Returns

`Promise`\<[`ListDeleteResponse`](../interfaces/Schemas.ListDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:650](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L650)

___

### create

▸ **create**(`options?`): `Promise`\<[`ListCreateResponse`](../interfaces/Schemas.ListCreateResponse.md)\>

Create List
Creates a new List for the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateOptions` |

#### Returns

`Promise`\<[`ListCreateResponse`](../interfaces/Schemas.ListCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[lists/client.ts:684](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/lists/client.ts#L684)
