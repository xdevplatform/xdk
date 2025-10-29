[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamPostsSample10StreamingOptions

# Interface: StreamPostsSample10StreamingOptions

Options for postsSample10 method

## Table of contents

### Properties

- [backfillMinutes](StreamPostsSample10StreamingOptions.md#backfillminutes)
- [startTime](StreamPostsSample10StreamingOptions.md#starttime)
- [endTime](StreamPostsSample10StreamingOptions.md#endtime)
- [tweetfields](StreamPostsSample10StreamingOptions.md#tweetfields)
- [expansions](StreamPostsSample10StreamingOptions.md#expansions)
- [mediafields](StreamPostsSample10StreamingOptions.md#mediafields)
- [pollfields](StreamPostsSample10StreamingOptions.md#pollfields)
- [userfields](StreamPostsSample10StreamingOptions.md#userfields)
- [placefields](StreamPostsSample10StreamingOptions.md#placefields)
- [requestOptions](StreamPostsSample10StreamingOptions.md#requestoptions)
- [headers](StreamPostsSample10StreamingOptions.md#headers)
- [signal](StreamPostsSample10StreamingOptions.md#signal)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[stream/stream_client.ts:431](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L431)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:434](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L434)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:437](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L437)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[stream/stream_client.ts:440](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L440)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[stream/stream_client.ts:443](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L443)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[stream/stream_client.ts:446](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L446)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[stream/stream_client.ts:449](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L449)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[stream/stream_client.ts:452](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L452)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[stream/stream_client.ts:455](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L455)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:458](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L458)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:460](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L460)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:462](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L462)
