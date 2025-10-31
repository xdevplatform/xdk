[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / PostsClient

# Class: PostsClient

Client for posts operations

This client provides methods for interacting with the posts endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all posts related operations.

## Table of contents

### Constructors

- [constructor](PostsClient.md#constructor)

### Methods

- [getInsights28hr](PostsClient.md#getinsights28hr)
- [getRepostedBy](PostsClient.md#getrepostedby)
- [hideReply](PostsClient.md#hidereply)
- [getAnalytics](PostsClient.md#getanalytics)
- [searchAll](PostsClient.md#searchall)
- [searchRecent](PostsClient.md#searchrecent)
- [getByIds](PostsClient.md#getbyids)
- [create](PostsClient.md#create)
- [getCountsAll](PostsClient.md#getcountsall)
- [getLikingUsers](PostsClient.md#getlikingusers)
- [getInsightsHistorical](PostsClient.md#getinsightshistorical)
- [getReposts](PostsClient.md#getreposts)
- [getById](PostsClient.md#getbyid)
- [delete](PostsClient.md#delete)
- [getCountsRecent](PostsClient.md#getcountsrecent)
- [getQuoted](PostsClient.md#getquoted)

## Constructors

### constructor

• **new PostsClient**(`client`): [`PostsClient`](PostsClient.md)

Creates a new posts client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`PostsClient`](PostsClient.md)

#### Defined in

[posts/client.ts:145](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L145)

## Methods

### getInsights28hr

▸ **getInsights28hr**(): `Promise`\<`any`\>

Get 28-hour Post insights
Retrieves engagement metrics for specified Posts over the last 28 hours.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:163](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L163)

___

### getRepostedBy

▸ **getRepostedBy**(`options?`): `Promise`\<`any`\>

Get Reposted by
Retrieves a list of Users who reposted a specific Post by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRepostedByOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:196](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L196)

___

### hideReply

▸ **hideReply**(`options?`): `Promise`\<`any`\>

Hide reply
Hides or unhides a reply to a conversation owned by the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `HideReplyOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:231](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L231)

___

### getAnalytics

▸ **getAnalytics**(): `Promise`\<`any`\>

Get Post analytics
Retrieves analytics data for specified Posts within a defined time range.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:276](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L276)

___

### searchAll

▸ **searchAll**(`options?`): `Promise`\<`any`\>

Search all Posts
Retrieves Posts from the full archive matching a search query.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `SearchAllOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:309](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L309)

___

### searchRecent

▸ **searchRecent**(`options?`): `Promise`\<`any`\>

Search recent Posts
Retrieves Posts from the last 7 days matching a search query.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `SearchRecentOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:342](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L342)

___

### getByIds

▸ **getByIds**(): `Promise`\<`any`\>

Get Posts by IDs
Retrieves details of multiple Posts by their IDs.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:377](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L377)

___

### create

▸ **create**(`body`): `Promise`\<`any`\>

Create or Edit Post
Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `body` | `any` | Request body |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:410](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L410)

___

### getCountsAll

▸ **getCountsAll**(`options?`): `Promise`\<`any`\>

Get count of all Posts
Retrieves the count of Posts matching a search query from the full archive.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetCountsAllOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:445](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L445)

___

### getLikingUsers

▸ **getLikingUsers**(`options?`): `Promise`\<`any`\>

Get Liking Users
Retrieves a list of Users who liked a specific Post by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetLikingUsersOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:480](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L480)

___

### getInsightsHistorical

▸ **getInsightsHistorical**(): `Promise`\<`any`\>

Get historical Post insights
Retrieves historical engagement metrics for specified Posts within a defined time range.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:523](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L523)

___

### getReposts

▸ **getReposts**(`options?`): `Promise`\<`any`\>

Get Reposts
Retrieves a list of Posts that repost a specific Post by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRepostsOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:556](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L556)

___

### getById

▸ **getById**(): `Promise`\<`any`\>

Get Post by ID
Retrieves details of a specific Post by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:591](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L591)

___

### delete

▸ **delete**(): `Promise`\<`any`\>

Delete Post
Deletes a specific Post by its ID, if owned by the authenticated user.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:624](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L624)

___

### getCountsRecent

▸ **getCountsRecent**(`options?`): `Promise`\<`any`\>

Get count of recent Posts
Retrieves the count of Posts from the last 7 days matching a search query.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetCountsRecentOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:657](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L657)

___

### getQuoted

▸ **getQuoted**(`options?`): `Promise`\<`any`\>

Get Quoted Posts
Retrieves a list of Posts that quote a specific Post by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetQuotedOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[posts/client.ts:692](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/posts/client.ts#L692)
