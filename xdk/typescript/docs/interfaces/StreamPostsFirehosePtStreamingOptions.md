[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamPostsFirehosePtStreamingOptions

# Interface: StreamPostsFirehosePtStreamingOptions

Options for postsFirehosePt method

## Table of contents

### Properties

- [backfillMinutes](StreamPostsFirehosePtStreamingOptions.md#backfillminutes)
- [startTime](StreamPostsFirehosePtStreamingOptions.md#starttime)
- [endTime](StreamPostsFirehosePtStreamingOptions.md#endtime)
- [tweetfields](StreamPostsFirehosePtStreamingOptions.md#tweetfields)
- [expansions](StreamPostsFirehosePtStreamingOptions.md#expansions)
- [mediafields](StreamPostsFirehosePtStreamingOptions.md#mediafields)
- [pollfields](StreamPostsFirehosePtStreamingOptions.md#pollfields)
- [userfields](StreamPostsFirehosePtStreamingOptions.md#userfields)
- [placefields](StreamPostsFirehosePtStreamingOptions.md#placefields)
- [requestOptions](StreamPostsFirehosePtStreamingOptions.md#requestoptions)
- [headers](StreamPostsFirehosePtStreamingOptions.md#headers)
- [signal](StreamPostsFirehosePtStreamingOptions.md#signal)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[stream/stream_client.ts:34](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L34)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:37](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L37)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:40](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L40)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[stream/stream_client.ts:43](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L43)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[stream/stream_client.ts:46](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L46)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[stream/stream_client.ts:49](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L49)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[stream/stream_client.ts:52](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L52)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[stream/stream_client.ts:55](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L55)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[stream/stream_client.ts:58](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L58)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:61](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L61)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:63](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L63)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:65](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L65)
