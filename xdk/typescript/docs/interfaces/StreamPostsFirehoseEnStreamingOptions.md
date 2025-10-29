[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamPostsFirehoseEnStreamingOptions

# Interface: StreamPostsFirehoseEnStreamingOptions

Options for postsFirehoseEn method

## Table of contents

### Properties

- [backfillMinutes](StreamPostsFirehoseEnStreamingOptions.md#backfillminutes)
- [startTime](StreamPostsFirehoseEnStreamingOptions.md#starttime)
- [endTime](StreamPostsFirehoseEnStreamingOptions.md#endtime)
- [tweetfields](StreamPostsFirehoseEnStreamingOptions.md#tweetfields)
- [expansions](StreamPostsFirehoseEnStreamingOptions.md#expansions)
- [mediafields](StreamPostsFirehoseEnStreamingOptions.md#mediafields)
- [pollfields](StreamPostsFirehoseEnStreamingOptions.md#pollfields)
- [userfields](StreamPostsFirehoseEnStreamingOptions.md#userfields)
- [placefields](StreamPostsFirehoseEnStreamingOptions.md#placefields)
- [requestOptions](StreamPostsFirehoseEnStreamingOptions.md#requestoptions)
- [headers](StreamPostsFirehoseEnStreamingOptions.md#headers)
- [signal](StreamPostsFirehoseEnStreamingOptions.md#signal)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[stream/stream_client.ts:104](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L104)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:107](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L107)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:110](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L110)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[stream/stream_client.ts:113](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L113)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[stream/stream_client.ts:116](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L116)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[stream/stream_client.ts:119](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L119)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[stream/stream_client.ts:122](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L122)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[stream/stream_client.ts:125](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L125)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[stream/stream_client.ts:128](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L128)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:131](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L131)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:133](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L133)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:135](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L135)
