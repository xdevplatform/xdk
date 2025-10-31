[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamClient

# Class: StreamClient

## Table of contents

### Constructors

- [constructor](StreamClient.md#constructor)

### Methods

- [postsSample](StreamClient.md#postssample)
- [postsFirehoseEn](StreamClient.md#postsfirehoseen)
- [postsSample10](StreamClient.md#postssample10)
- [likesFirehose](StreamClient.md#likesfirehose)
- [likesSample10](StreamClient.md#likessample10)
- [postsFirehose](StreamClient.md#postsfirehose)
- [postsFirehoseKo](StreamClient.md#postsfirehoseko)
- [labelsCompliance](StreamClient.md#labelscompliance)
- [postsCompliance](StreamClient.md#postscompliance)
- [usersCompliance](StreamClient.md#userscompliance)
- [posts](StreamClient.md#posts)
- [likesCompliance](StreamClient.md#likescompliance)
- [postsFirehosePt](StreamClient.md#postsfirehosept)
- [postsFirehoseJa](StreamClient.md#postsfirehoseja)
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

[stream/stream_client.ts:254](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L254)

## Methods

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

#### Defined in

[stream/stream_client.ts:266](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L266)

___

### postsFirehoseEn

▸ **postsFirehoseEn**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream English Posts
Streams all public English-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsFirehoseEnStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:329](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L329)

___

### postsSample10

▸ **postsSample10**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream 10% sampled Posts
Streams a 10% sample of public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsSample10StreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:392](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L392)

___

### likesFirehose

▸ **likesFirehose**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream all Likes
Streams all public Likes in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `LikesFirehoseStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:455](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L455)

___

### likesSample10

▸ **likesSample10**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream sampled Likes
Streams a 10% sample of public Likes in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `LikesSample10StreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:518](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L518)

___

### postsFirehose

▸ **postsFirehose**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream all Posts
Streams all public Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsFirehoseStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:581](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L581)

___

### postsFirehoseKo

▸ **postsFirehoseKo**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Korean Posts
Streams all public Korean-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsFirehoseKoStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:644](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L644)

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

#### Defined in

[stream/stream_client.ts:707](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L707)

___

### postsCompliance

▸ **postsCompliance**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Posts compliance data
Streams all compliance data related to Posts.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsComplianceStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:770](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L770)

___

### usersCompliance

▸ **usersCompliance**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Users compliance data
Streams all compliance data related to Users.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `UsersComplianceStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:833](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L833)

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

#### Defined in

[stream/stream_client.ts:896](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L896)

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

#### Defined in

[stream/stream_client.ts:957](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L957)

___

### postsFirehosePt

▸ **postsFirehosePt**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Portuguese Posts
Streams all public Portuguese-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsFirehosePtStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:1020](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L1020)

___

### postsFirehoseJa

▸ **postsFirehoseJa**(`options?`): `Promise`\<`EventDrivenStream`\>

Stream Japanese Posts
Streams all public Japanese-language Posts in real-time.

Returns an event-driven stream that's easy to use.
Use .on() to listen for events like 'data', 'error', 'close'.
Also supports async iteration with for await...of.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `PostsFirehoseJaStreamingOptions` |

#### Returns

`Promise`\<`EventDrivenStream`\>

#### Defined in

[stream/stream_client.ts:1083](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L1083)

___

### getRuleCounts

▸ **getRuleCounts**(`options?`): `Promise`\<`any`\>

Get stream rule counts
Retrieves the count of rules in the active rule set for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRuleCountsStreamingOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:1144](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L1144)

___

### getRules

▸ **getRules**(`options?`): `Promise`\<`any`\>

Get stream rules
Retrieves the active rule set or a subset of rules for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRulesStreamingOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:1190](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L1190)

___

### updateRules

▸ **updateRules**(`body`, `options?`): `Promise`\<`any`\>

Update stream rules
Adds or deletes rules from the active rule set for the filtered stream.

#### Parameters

| Name | Type |
| :------ | :------ |
| `body` | `any` |
| `options` | `UpdateRulesStreamingOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[stream/stream_client.ts:1236](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/stream/stream_client.ts#L1236)
