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
- [getFollowers](ListsClient.md#getfollowers)
- [getMembers](ListsClient.md#getmembers)
- [addMember](ListsClient.md#addmember)
- [getById](ListsClient.md#getbyid)
- [update](ListsClient.md#update)
- [delete](ListsClient.md#delete)
- [removeMemberByUserId](ListsClient.md#removememberbyuserid)
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

[lists/client.ts:115](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L115)

## Methods

### getPosts

▸ **getPosts**(`options?`): `Promise`\<`any`\>

Get List Posts
Retrieves a list of Posts associated with a specific List by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetPostsOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:129](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L129)

___

### getFollowers

▸ **getFollowers**(`options?`): `Promise`\<`any`\>

Get List followers
Retrieves a list of Users who follow a specific List by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetFollowersOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:162](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L162)

___

### getMembers

▸ **getMembers**(`options?`): `Promise`\<`any`\>

Get List members
Retrieves a list of Users who are members of a specific List by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetMembersOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:197](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L197)

___

### addMember

▸ **addMember**(`options?`): `Promise`\<`any`\>

Add List member
Adds a User to a specific List by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `AddMemberOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:232](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L232)

___

### getById

▸ **getById**(): `Promise`\<`any`\>

Get List by ID
Retrieves details of a specific List by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:271](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L271)

___

### update

▸ **update**(`options?`): `Promise`\<`any`\>

Update List
Updates the details of a specific List owned by the authenticated user by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `UpdateOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:304](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L304)

___

### delete

▸ **delete**(): `Promise`\<`any`\>

Delete List
Deletes a specific List owned by the authenticated user by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:343](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L343)

___

### removeMemberByUserId

▸ **removeMemberByUserId**(): `Promise`\<`any`\>

Remove List member
Removes a User from a specific List by its ID and the User’s ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:378](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L378)

___

### create

▸ **create**(`options?`): `Promise`\<`any`\>

Create List
Creates a new List for the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[lists/client.ts:409](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/lists/client.ts#L409)
