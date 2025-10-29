[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ActivityStreamOptions

# Interface: ActivityStreamOptions

Options for stream method

## Table of contents

### Properties

- [backfillMinutes](ActivityStreamOptions.md#backfillminutes)
- [startTime](ActivityStreamOptions.md#starttime)
- [endTime](ActivityStreamOptions.md#endtime)
- [requestOptions](ActivityStreamOptions.md#requestoptions)

## Properties

### backfillMinutes

• `Optional` **backfillMinutes**: `number`

The number of minutes of backfill requested.

#### Defined in

[activity/client.ts:51](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L51)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.

#### Defined in

[activity/client.ts:54](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L54)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.

#### Defined in

[activity/client.ts:57](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L57)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[activity/client.ts:60](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L60)
