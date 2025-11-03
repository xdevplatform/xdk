[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / StreamClient

# Class: StreamClient

## Table of contents

### Constructors

- [constructor](StreamClient.md#constructor)

### Methods

- [postsFirehoseJa](StreamClient.md#postsfirehoseja)
- [posts](StreamClient.md#posts)
- [postsSample10](StreamClient.md#postssample10)
- [likesFirehose](StreamClient.md#likesfirehose)
- [likesCompliance](StreamClient.md#likescompliance)
- [postsFirehoseEn](StreamClient.md#postsfirehoseen)
- [postsCompliance](StreamClient.md#postscompliance)
- [postsFirehose](StreamClient.md#postsfirehose)
- [likesSample10](StreamClient.md#likessample10)
- [postsFirehosePt](StreamClient.md#postsfirehosept)
- [postsFirehoseKo](StreamClient.md#postsfirehoseko)
- [labelsCompliance](StreamClient.md#labelscompliance)
- [usersCompliance](StreamClient.md#userscompliance)
- [postsSample](StreamClient.md#postssample)
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

[stream/stream_client.ts:560](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L560)

## Methods

### postsFirehoseJa

▸ **postsFirehoseJa**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream Japanese Posts
Streams all public Japanese-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsFirehoseJaStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:580](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L580)

___

### posts

▸ **posts**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream filtered Posts
Streams Posts in real-time matching the active rule set.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:710](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L710)

___

### postsSample10

▸ **postsSample10**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream 10% sampled Posts
Streams a 10% sample of public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsSample10StreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:839](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L839)

___

### likesFirehose

▸ **likesFirehose**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream all Likes
Streams all public Likes in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `LikesFirehoseStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:973](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L973)

___

### likesCompliance

▸ **likesCompliance**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Likes compliance data
Streams all compliance data related to Likes for Users.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `LikesComplianceStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1094](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1094)

___

### postsFirehoseEn

▸ **postsFirehoseEn**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream English Posts
Streams all public English-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsFirehoseEnStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1189](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1189)

___

### postsCompliance

▸ **postsCompliance**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream Posts compliance data
Streams all compliance data related to Posts.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsComplianceStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1323](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1323)

___

### postsFirehose

▸ **postsFirehose**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream all Posts
Streams all public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsFirehoseStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1421](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1421)

___

### likesSample10

▸ **likesSample10**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream sampled Likes
Streams a 10% sample of public Likes in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `LikesSample10StreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1555](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1555)

___

### postsFirehosePt

▸ **postsFirehosePt**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream Portuguese Posts
Streams all public Portuguese-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsFirehosePtStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1680](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1680)

___

### postsFirehoseKo

▸ **postsFirehoseKo**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream Korean Posts
Streams all public Korean-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `PostsFirehoseKoStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1814](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1814)

___

### labelsCompliance

▸ **labelsCompliance**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Post labels
Streams all labeling events applied to Posts.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `LabelsComplianceStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:1944](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L1944)

___

### usersCompliance

▸ **usersCompliance**(`partition`, `options?`): `Promise`\<`EventDrivenStream`\>

Stream Users compliance data
Streams all compliance data related to Users.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `partition` | `number` | The partition number. |
| `options` | `UsersComplianceStreamingOptions` | - |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:2039](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L2039)

___

### postsSample

▸ **postsSample**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream sampled Posts
Streams a 1% sample of public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsSampleStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

Event-driven stream for handling streaming data

#### Defined in

[stream/stream_client.ts:2133](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L2133)

___

### getRuleCounts

▸ **getRuleCounts**(`options?`): `Promise`\<[`Get2TweetsSearchStreamRulesCountsResponse`](../interfaces/Schemas.Get2TweetsSearchStreamRulesCountsResponse.md)\>

Get stream rule counts
Retrieves the count of rules in the active rule set for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRuleCountsStreamingOptions` |

#### Returns

`Promise`\<[`Get2TweetsSearchStreamRulesCountsResponse`](../interfaces/Schemas.Get2TweetsSearchStreamRulesCountsResponse.md)\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:2242](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L2242)

___

### getRules

▸ **getRules**(`options?`): `Promise`\<[`RulesLookupResponse`](../interfaces/Schemas.RulesLookupResponse.md)\>

Get stream rules
Retrieves the active rule set or a subset of rules for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRulesStreamingOptions` |

#### Returns

`Promise`\<[`RulesLookupResponse`](../interfaces/Schemas.RulesLookupResponse.md)\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:2299](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L2299)

___

### updateRules

▸ **updateRules**(`body`, `options?`): `Promise`\<[`AddOrDeleteRulesResponse`](../interfaces/Schemas.AddOrDeleteRulesResponse.md)\>

Update stream rules
Adds or deletes rules from the active rule set for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `body` | `any` |
| `options` | `UpdateRulesStreamingOptions` |

#### Returns

`Promise`\<[`AddOrDeleteRulesResponse`](../interfaces/Schemas.AddOrDeleteRulesResponse.md)\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:2368](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/stream/stream_client.ts#L2368)
