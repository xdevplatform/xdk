[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ListsClient

# Class: ListsClient

Client for Lists operations

This client provides methods for interacting with the Lists endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Lists related operations.

## Table of contents

### Constructors

- [constructor](ListsClient.md#constructor)

### Methods

- [addMember](ListsClient.md#addmember)
- [getById](ListsClient.md#getbyid)
- [update](ListsClient.md#update)
- [delete](ListsClient.md#delete)
- [removeMemberByUserId](ListsClient.md#removememberbyuserid)
- [create](ListsClient.md#create)
- [getFollowers](ListsClient.md#getfollowers)
- [getMembers](ListsClient.md#getmembers)
- [getPosts](ListsClient.md#getposts)

## Constructors

### constructor

• **new ListsClient**(`client`): [`ListsClient`](ListsClient.md)

Creates a new Lists client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`ListsClient`](ListsClient.md)

#### Defined in

[lists/client.ts:174](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L174)

## Methods

### addMember

▸ **addMember**(`id`, `options?`): `Promise`\<[`ListsAddMemberResponse`](../interfaces/ListsAddMemberResponse.md)\>

Add List member
Adds a User to a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List for which to add a member. |
| `options` | [`ListsAddMemberOptions`](../interfaces/ListsAddMemberOptions.md) | - |

#### Returns

`Promise`\<[`ListsAddMemberResponse`](../interfaces/ListsAddMemberResponse.md)\>

Promise with the API response

#### Defined in

[lists/client.ts:190](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L190)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`ListsGetByIdResponse`](../interfaces/ListsGetByIdResponse.md)\>

Get List by ID
Retrieves details of a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | [`ListsGetByIdOptions`](../interfaces/ListsGetByIdOptions.md) | - |

#### Returns

`Promise`\<[`ListsGetByIdResponse`](../interfaces/ListsGetByIdResponse.md)\>

Promise with the API response

#### Defined in

[lists/client.ts:236](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L236)

___

### update

▸ **update**(`id`, `options?`): `Promise`\<[`ListsUpdateResponse`](../interfaces/ListsUpdateResponse.md)\>

Update List
Updates the details of a specific List owned by the authenticated user by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List to modify. |
| `options` | [`ListsUpdateOptions`](../interfaces/ListsUpdateOptions.md) | - |

#### Returns

`Promise`\<[`ListsUpdateResponse`](../interfaces/ListsUpdateResponse.md)\>

Promise with the API response

#### Defined in

[lists/client.ts:296](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L296)

___

### delete

▸ **delete**(`id`): `Promise`\<[`ListsDeleteResponse`](../interfaces/ListsDeleteResponse.md)\>

Delete List
Deletes a specific List owned by the authenticated user by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List to delete. |

#### Returns

`Promise`\<[`ListsDeleteResponse`](../interfaces/ListsDeleteResponse.md)\>

Promise with the API response

#### Defined in

[lists/client.ts:342](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L342)

___

### removeMemberByUserId

▸ **removeMemberByUserId**(`id`, `userId`): `Promise`\<[`ListsRemoveMemberByUserIdResponse`](../interfaces/ListsRemoveMemberByUserIdResponse.md)\>

Remove List member
Removes a User from a specific List by its ID and the User’s ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List to remove a member. |
| `userId` | `string` | The ID of User that will be removed from the List. |

#### Returns

`Promise`\<[`ListsRemoveMemberByUserIdResponse`](../interfaces/ListsRemoveMemberByUserIdResponse.md)\>

Promise with the API response

#### Defined in

[lists/client.ts:383](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L383)

___

### create

▸ **create**(`options?`): `Promise`\<[`ListsCreateResponse`](../interfaces/ListsCreateResponse.md)\>

Create List
Creates a new List for the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`ListsCreateOptions`](../interfaces/ListsCreateOptions.md) |

#### Returns

`Promise`\<[`ListsCreateResponse`](../interfaces/ListsCreateResponse.md)\>

Promise with the API response

#### Defined in

[lists/client.ts:421](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L421)

___

### getFollowers

▸ **getFollowers**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get List followers
Retrieves a list of Users who follow a specific List by its ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | [`ListsGetFollowersOptions`](../interfaces/ListsGetFollowersOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[lists/client.ts:462](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L462)

___

### getMembers

▸ **getMembers**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get List members
Retrieves a list of Users who are members of a specific List by its ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | [`ListsGetMembersOptions`](../interfaces/ListsGetMembersOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[lists/client.ts:557](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L557)

___

### getPosts

▸ **getPosts**(`id`, `options?`): `Promise`\<[`PostPaginator`](PostPaginator.md)\>

Get List Posts
Retrieves a list of Posts associated with a specific List by its ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the List. |
| `options` | [`ListsGetPostsOptions`](../interfaces/ListsGetPostsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`PostPaginator`](PostPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[lists/client.ts:652](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/lists/client.ts#L652)
