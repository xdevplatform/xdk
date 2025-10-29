[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamPostsComplianceStreamingOptions

# Interface: StreamPostsComplianceStreamingOptions

Options for postsCompliance method

## Table of contents

### Properties

- [backfillMinutes](StreamPostsComplianceStreamingOptions.md#backfillminutes)
- [startTime](StreamPostsComplianceStreamingOptions.md#starttime)
- [endTime](StreamPostsComplianceStreamingOptions.md#endtime)
- [requestOptions](StreamPostsComplianceStreamingOptions.md#requestoptions)
- [headers](StreamPostsComplianceStreamingOptions.md#headers)
- [signal](StreamPostsComplianceStreamingOptions.md#signal)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[stream/stream_client.ts:194](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L194)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.

#### Defined in

[stream/stream_client.ts:197](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L197)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.

#### Defined in

[stream/stream_client.ts:200](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L200)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:203](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L203)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:205](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L205)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:207](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L207)
