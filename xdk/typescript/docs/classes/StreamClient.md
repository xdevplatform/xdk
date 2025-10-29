[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamClient

# Class: StreamClient

## Table of contents

### Constructors

- [constructor](StreamClient.md#constructor)

### Methods

- [postsFirehosePt](StreamClient.md#postsfirehosept)
- [likesSample10](StreamClient.md#likessample10)
- [postsFirehoseEn](StreamClient.md#postsfirehoseen)
- [usersCompliance](StreamClient.md#userscompliance)
- [likesFirehose](StreamClient.md#likesfirehose)
- [postsCompliance](StreamClient.md#postscompliance)
- [postsFirehoseJa](StreamClient.md#postsfirehoseja)
- [posts](StreamClient.md#posts)
- [labelsCompliance](StreamClient.md#labelscompliance)
- [postsSample](StreamClient.md#postssample)
- [postsFirehose](StreamClient.md#postsfirehose)
- [postsSample10](StreamClient.md#postssample10)
- [likesCompliance](StreamClient.md#likescompliance)
- [postsFirehoseKo](StreamClient.md#postsfirehoseko)
- [getRuleCounts](StreamClient.md#getrulecounts)
- [getRules](StreamClient.md#getrules)
- [updateRules](StreamClient.md#updaterules)

## Constructors

### constructor

• **new StreamClient**(`client`): [`StreamClient`](StreamClient.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `client` | [`Client`](Client.md) |

#### Returns

[`StreamClient`](StreamClient.md)

#### Defined in

[stream/stream_client.ts:526](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L526)

## Methods

### postsFirehosePt

▸ **postsFirehosePt**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Portuguese Posts
Streams all public Portuguese-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsFirehosePtStreamingOptions`](../interfaces/StreamPostsFirehosePtStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:538](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L538)

___

### likesSample10

▸ **likesSample10**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream sampled Likes
Streams a 10% sample of public Likes in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamLikesSample10StreamingOptions`](../interfaces/StreamLikesSample10StreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:662](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L662)

___

### postsFirehoseEn

▸ **postsFirehoseEn**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream English Posts
Streams all public English-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsFirehoseEnStreamingOptions`](../interfaces/StreamPostsFirehoseEnStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:777](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L777)

___

### usersCompliance

▸ **usersCompliance**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Users compliance data
Streams all compliance data related to Users.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamUsersComplianceStreamingOptions`](../interfaces/StreamUsersComplianceStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:901](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L901)

___

### likesFirehose

▸ **likesFirehose**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream all Likes
Streams all public Likes in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamLikesFirehoseStreamingOptions`](../interfaces/StreamLikesFirehoseStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:989](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L989)

___

### postsCompliance

▸ **postsCompliance**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Posts compliance data
Streams all compliance data related to Posts.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsComplianceStreamingOptions`](../interfaces/StreamPostsComplianceStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1104](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1104)

___

### postsFirehoseJa

▸ **postsFirehoseJa**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Japanese Posts
Streams all public Japanese-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsFirehoseJaStreamingOptions`](../interfaces/StreamPostsFirehoseJaStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1192](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1192)

___

### posts

▸ **posts**(`options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream filtered Posts
Streams Posts in real-time matching the active rule set.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`StreamPostsStreamingOptions`](../interfaces/StreamPostsStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1316](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1316)

___

### labelsCompliance

▸ **labelsCompliance**(`options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Post labels
Streams all labeling events applied to Posts.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`StreamLabelsComplianceStreamingOptions`](../interfaces/StreamLabelsComplianceStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1435](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1435)

___

### postsSample

▸ **postsSample**(`options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream sampled Posts
Streams a 1% sample of public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`StreamPostsSampleStreamingOptions`](../interfaces/StreamPostsSampleStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1518](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1518)

___

### postsFirehose

▸ **postsFirehose**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream all Posts
Streams all public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsFirehoseStreamingOptions`](../interfaces/StreamPostsFirehoseStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1625](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1625)

___

### postsSample10

▸ **postsSample10**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream 10% sampled Posts
Streams a 10% sample of public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsSample10StreamingOptions`](../interfaces/StreamPostsSample10StreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1749](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1749)

___

### likesCompliance

▸ **likesCompliance**(`options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Likes compliance data
Streams all compliance data related to Likes for Users.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`StreamLikesComplianceStreamingOptions`](../interfaces/StreamLikesComplianceStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1873](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1873)

___

### postsFirehoseKo

▸ **postsFirehoseKo**(`partition`, `options?`): `Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

Stream Korean Posts
Streams all public Korean-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `partition` | `number` |
| `options` | [`StreamPostsFirehoseKoStreamingOptions`](../interfaces/StreamPostsFirehoseKoStreamingOptions.md) |

#### Returns

`Promise`\<[`EventDrivenStream`](EventDrivenStream.md)\>

#### Defined in

[stream/stream_client.ts:1956](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L1956)

___

### getRuleCounts

▸ **getRuleCounts**(`options?`): `Promise`\<[`StreamGetRuleCountsResponse`](../interfaces/StreamGetRuleCountsResponse.md)\>

Get stream rule counts
Retrieves the count of rules in the active rule set for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`StreamGetRuleCountsStreamingOptions`](../interfaces/StreamGetRuleCountsStreamingOptions.md) |

#### Returns

`Promise`\<[`StreamGetRuleCountsResponse`](../interfaces/StreamGetRuleCountsResponse.md)\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:2078](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L2078)

___

### getRules

▸ **getRules**(`options?`): `Promise`\<[`StreamGetRulesResponse`](../interfaces/StreamGetRulesResponse.md)\>

Get stream rules
Retrieves the active rule set or a subset of rules for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`StreamGetRulesStreamingOptions`](../interfaces/StreamGetRulesStreamingOptions.md) |

#### Returns

`Promise`\<[`StreamGetRulesResponse`](../interfaces/StreamGetRulesResponse.md)\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:2132](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L2132)

___

### updateRules

▸ **updateRules**(`body`, `options?`): `Promise`\<[`StreamUpdateRulesResponse`](../interfaces/StreamUpdateRulesResponse.md)\>

Update stream rules
Adds or deletes rules from the active rule set for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `body` | `any` |
| `options` | [`StreamUpdateRulesStreamingOptions`](../interfaces/StreamUpdateRulesStreamingOptions.md) |

#### Returns

`Promise`\<[`StreamUpdateRulesResponse`](../interfaces/StreamUpdateRulesResponse.md)\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:2198](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L2198)
