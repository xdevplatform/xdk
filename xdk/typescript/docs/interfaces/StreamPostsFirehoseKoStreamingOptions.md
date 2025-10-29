[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamPostsFirehoseKoStreamingOptions

# Interface: StreamPostsFirehoseKoStreamingOptions

Options for postsFirehoseKo method

## Table of contents

### Properties

- [backfillMinutes](StreamPostsFirehoseKoStreamingOptions.md#backfillminutes)
- [startTime](StreamPostsFirehoseKoStreamingOptions.md#starttime)
- [endTime](StreamPostsFirehoseKoStreamingOptions.md#endtime)
- [tweetfields](StreamPostsFirehoseKoStreamingOptions.md#tweetfields)
- [expansions](StreamPostsFirehoseKoStreamingOptions.md#expansions)
- [mediafields](StreamPostsFirehoseKoStreamingOptions.md#mediafields)
- [pollfields](StreamPostsFirehoseKoStreamingOptions.md#pollfields)
- [userfields](StreamPostsFirehoseKoStreamingOptions.md#userfields)
- [placefields](StreamPostsFirehoseKoStreamingOptions.md#placefields)
- [requestOptions](StreamPostsFirehoseKoStreamingOptions.md#requestoptions)
- [headers](StreamPostsFirehoseKoStreamingOptions.md#headers)
- [signal](StreamPostsFirehoseKoStreamingOptions.md#signal)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[stream/stream_client.ts:489](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L489)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:492](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L492)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:495](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L495)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[stream/stream_client.ts:498](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L498)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[stream/stream_client.ts:501](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L501)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[stream/stream_client.ts:504](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L504)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[stream/stream_client.ts:507](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L507)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[stream/stream_client.ts:510](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L510)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[stream/stream_client.ts:513](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L513)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:516](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L516)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:518](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L518)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:520](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L520)
