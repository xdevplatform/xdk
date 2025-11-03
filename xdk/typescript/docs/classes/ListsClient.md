[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ListsClient

# Class: ListsClient

Client for lists operations

This client provides methods for interacting with the lists endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all lists related operations.

## Table of contents

### Constructors

- [constructor](ListsClient.md#constructor)

### Methods

- [getPosts](ListsClient.md#getposts)
- [getById](ListsClient.md#getbyid)
- [update](ListsClient.md#update)
- [delete](ListsClient.md#delete)
- [removeMemberByUserId](ListsClient.md#removememberbyuserid)
- [getMembers](ListsClient.md#getmembers)
- [addMember](ListsClient.md#addmember)
- [getFollowers](ListsClient.md#getfollowers)
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

[lists/client.ts:188](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L188)

## Methods

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

[lists/client.ts:205](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L205)

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

[lists/client.ts:297](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L297)

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

[lists/client.ts:359](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L359)

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

[lists/client.ts:407](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L407)

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

[lists/client.ts:449](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L449)

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

[lists/client.ts:492](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L492)

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

[lists/client.ts:566](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L566)

___

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

[lists/client.ts:614](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L614)

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

[lists/client.ts:684](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/lists/client.ts#L684)
