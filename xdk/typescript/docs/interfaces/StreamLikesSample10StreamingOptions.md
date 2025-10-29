[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamLikesSample10StreamingOptions

# Interface: StreamLikesSample10StreamingOptions

Options for likesSample10 method

## Table of contents

### Properties

- [backfillMinutes](StreamLikesSample10StreamingOptions.md#backfillminutes)
- [startTime](StreamLikesSample10StreamingOptions.md#starttime)
- [endTime](StreamLikesSample10StreamingOptions.md#endtime)
- [likeWithTweetAuthorfields](StreamLikesSample10StreamingOptions.md#likewithtweetauthorfields)
- [expansions](StreamLikesSample10StreamingOptions.md#expansions)
- [userfields](StreamLikesSample10StreamingOptions.md#userfields)
- [tweetfields](StreamLikesSample10StreamingOptions.md#tweetfields)
- [requestOptions](StreamLikesSample10StreamingOptions.md#requestoptions)
- [headers](StreamLikesSample10StreamingOptions.md#headers)
- [signal](StreamLikesSample10StreamingOptions.md#signal)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[stream/stream_client.ts:72](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L72)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.

#### Defined in

[stream/stream_client.ts:75](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L75)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.

#### Defined in

[stream/stream_client.ts:78](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L78)

___

### likeWithTweetAuthorfields

• `Optional` **likeWithTweetAuthorfields**: `any`[]

A comma separated list of LikeWithTweetAuthor fields to display.

#### Defined in

[stream/stream_client.ts:81](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L81)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[stream/stream_client.ts:84](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L84)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[stream/stream_client.ts:87](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L87)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[stream/stream_client.ts:90](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L90)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:93](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L93)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:95](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L95)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:97](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L97)
