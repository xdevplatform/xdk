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

- [getQuoted](PostsClient.md#getquoted)
- [getInsights28hr](PostsClient.md#getinsights28hr)
- [hideReply](PostsClient.md#hidereply)
- [getCountsAll](PostsClient.md#getcountsall)
- [getInsightsHistorical](PostsClient.md#getinsightshistorical)
- [getAnalytics](PostsClient.md#getanalytics)
- [getById](PostsClient.md#getbyid)
- [delete](PostsClient.md#delete)
- [getLikingUsers](PostsClient.md#getlikingusers)
- [searchRecent](PostsClient.md#searchrecent)
- [searchAll](PostsClient.md#searchall)
- [getReposts](PostsClient.md#getreposts)
- [getRepostedBy](PostsClient.md#getrepostedby)
- [getByIds](PostsClient.md#getbyids)
- [create](PostsClient.md#create)
- [getCountsRecent](PostsClient.md#getcountsrecent)

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

[posts/client.ts:453](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L453)

## Methods

### getQuoted

▸ **getQuoted**(`id`, `options?`): `Promise`\<[`Get2TweetsIdQuoteTweetsResponse`](../interfaces/Schemas.Get2TweetsIdQuoteTweetsResponse.md)\>

Get Quoted Posts
Retrieves a list of Posts that quote a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | A single Post ID. |
| `options` | `GetQuotedOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsIdQuoteTweetsResponse`](../interfaces/Schemas.Get2TweetsIdQuoteTweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:470](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L470)

___

### getInsights28hr

▸ **getInsights28hr**(`tweetIds`, `granularity`, `requestedMetrics`, `options?`): `Promise`\<[`Get2Insights28hrResponse`](../interfaces/Schemas.Get2Insights28hrResponse.md)\>

Get 28-hour Post insights
Retrieves engagement metrics for specified Posts over the last 28 hours.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `tweetIds` | `any`[] | List of PostIds for 28hr metrics. |
| `granularity` | `string` | granularity of metrics response. |
| `requestedMetrics` | `any`[] | request metrics for historical request. |
| `options` | `GetInsights28hrOptions` | - |

#### Returns

`Promise`\<[`Get2Insights28hrResponse`](../interfaces/Schemas.Get2Insights28hrResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:576](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L576)

___

### hideReply

▸ **hideReply**(`tweetId`, `options?`): `Promise`\<[`TweetHideResponse`](../interfaces/Schemas.TweetHideResponse.md)\>

Hide reply
Hides or unhides a reply to a conversation owned by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `tweetId` | `string` | The ID of the reply that you want to hide or unhide. |
| `options` | `HideReplyOptions` | - |

#### Returns

`Promise`\<[`TweetHideResponse`](../interfaces/Schemas.TweetHideResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:638](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L638)

___

### getCountsAll

▸ **getCountsAll**(`query`, `options?`): `Promise`\<[`Get2TweetsCountsAllResponse`](../interfaces/Schemas.Get2TweetsCountsAllResponse.md)\>

Get count of all Posts
Retrieves the count of Posts matching a search query from the full archive.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length. |
| `options` | `GetCountsAllOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsCountsAllResponse`](../interfaces/Schemas.Get2TweetsCountsAllResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:686](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L686)

___

### getInsightsHistorical

▸ **getInsightsHistorical**(`tweetIds`, `endTime`, `startTime`, `granularity`, `requestedMetrics`, `options?`): `Promise`\<[`Get2InsightsHistoricalResponse`](../interfaces/Schemas.Get2InsightsHistoricalResponse.md)\>

Get historical Post insights
Retrieves historical engagement metrics for specified Posts within a defined time range.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `tweetIds` | `any`[] | List of PostIds for historical metrics. |
| `endTime` | `string` | YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range. |
| `startTime` | `string` | YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range. |
| `granularity` | `string` | granularity of metrics response. |
| `requestedMetrics` | `any`[] | request metrics for historical request. |
| `options` | `GetInsightsHistoricalOptions` | - |

#### Returns

`Promise`\<[`Get2InsightsHistoricalResponse`](../interfaces/Schemas.Get2InsightsHistoricalResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:796](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L796)

___

### getAnalytics

▸ **getAnalytics**(`ids`, `endTime`, `startTime`, `granularity`, `options?`): `Promise`\<[`Analytics`](../interfaces/Schemas.Analytics.md)\>

Get Post analytics
Retrieves analytics data for specified Posts within a defined time range.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ids` | `any`[] | A comma separated list of Post IDs. Up to 100 are allowed in a single request. |
| `endTime` | `string` | YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range. |
| `startTime` | `string` | YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range. |
| `granularity` | `string` | The granularity for the search counts results. |
| `options` | `GetAnalyticsOptions` | - |

#### Returns

`Promise`\<[`Analytics`](../interfaces/Schemas.Analytics.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:880](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L880)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`Get2TweetsIdResponse`](../interfaces/Schemas.Get2TweetsIdResponse.md)\>

Get Post by ID
Retrieves details of a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | A single Post ID. |
| `options` | `GetByIdOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsIdResponse`](../interfaces/Schemas.Get2TweetsIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:947](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L947)

___

### delete

▸ **delete**(`id`): `Promise`\<[`TweetDeleteResponse`](../interfaces/Schemas.TweetDeleteResponse.md)\>

Delete Post
Deletes a specific Post by its ID, if owned by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the Post to be deleted. |

#### Returns

`Promise`\<[`TweetDeleteResponse`](../interfaces/Schemas.TweetDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1027](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1027)

___

### getLikingUsers

▸ **getLikingUsers**(`id`, `options?`): `Promise`\<[`Get2TweetsIdLikingUsersResponse`](../interfaces/Schemas.Get2TweetsIdLikingUsersResponse.md)\>

Get Liking Users
Retrieves a list of Users who liked a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | A single Post ID. |
| `options` | `GetLikingUsersOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsIdLikingUsersResponse`](../interfaces/Schemas.Get2TweetsIdLikingUsersResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1065](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1065)

___

### searchRecent

▸ **searchRecent**(`query`, `options?`): `Promise`\<[`Get2TweetsSearchRecentResponse`](../interfaces/Schemas.Get2TweetsSearchRecentResponse.md)\>

Search recent Posts
Retrieves Posts from the last 7 days matching a search query.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length. |
| `options` | `SearchRecentOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsSearchRecentResponse`](../interfaces/Schemas.Get2TweetsSearchRecentResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1139](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1139)

___

### searchAll

▸ **searchAll**(`query`, `options?`): `Promise`\<[`Get2TweetsSearchAllResponse`](../interfaces/Schemas.Get2TweetsSearchAllResponse.md)\>

Search all Posts
Retrieves Posts from the full archive matching a search query.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length. |
| `options` | `SearchAllOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsSearchAllResponse`](../interfaces/Schemas.Get2TweetsSearchAllResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1269](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1269)

___

### getReposts

▸ **getReposts**(`id`, `options?`): `Promise`\<[`Get2TweetsIdRetweetsResponse`](../interfaces/Schemas.Get2TweetsIdRetweetsResponse.md)\>

Get Reposts
Retrieves a list of Posts that repost a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | A single Post ID. |
| `options` | `GetRepostsOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsIdRetweetsResponse`](../interfaces/Schemas.Get2TweetsIdRetweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1399](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1399)

___

### getRepostedBy

▸ **getRepostedBy**(`id`, `options?`): `Promise`\<[`Get2TweetsIdRetweetedByResponse`](../interfaces/Schemas.Get2TweetsIdRetweetedByResponse.md)\>

Get Reposted by
Retrieves a list of Users who reposted a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | A single Post ID. |
| `options` | `GetRepostedByOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsIdRetweetedByResponse`](../interfaces/Schemas.Get2TweetsIdRetweetedByResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1491](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1491)

___

### getByIds

▸ **getByIds**(`ids`, `options?`): `Promise`\<[`Get2TweetsResponse`](../interfaces/Schemas.Get2TweetsResponse.md)\>

Get Posts by IDs
Retrieves details of multiple Posts by their IDs.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ids` | `any`[] | A comma separated list of Post IDs. Up to 100 are allowed in a single request. |
| `options` | `GetByIdsOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsResponse`](../interfaces/Schemas.Get2TweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1565](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1565)

___

### create

▸ **create**(`body`): `Promise`\<[`TweetCreateResponse`](../interfaces/Schemas.TweetCreateResponse.md)\>

Create or Edit Post
Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `body` | [`TweetCreateRequest`](../interfaces/Schemas.TweetCreateRequest.md) | Request body |

#### Returns

`Promise`\<[`TweetCreateResponse`](../interfaces/Schemas.TweetCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1645](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1645)

___

### getCountsRecent

▸ **getCountsRecent**(`query`, `options?`): `Promise`\<[`Get2TweetsCountsRecentResponse`](../interfaces/Schemas.Get2TweetsCountsRecentResponse.md)\>

Get count of recent Posts
Retrieves the count of Posts from the last 7 days matching a search query.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length. |
| `options` | `GetCountsRecentOptions` | - |

#### Returns

`Promise`\<[`Get2TweetsCountsRecentResponse`](../interfaces/Schemas.Get2TweetsCountsRecentResponse.md)\>

Promise resolving to the API response

#### Defined in

[posts/client.ts:1683](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/posts/client.ts#L1683)
