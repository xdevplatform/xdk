[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / PostsGetCountsAllOptions

# Interface: PostsGetCountsAllOptions

Options for getCountsAll method

## Table of contents

### Properties

- [startTime](PostsGetCountsAllOptions.md#starttime)
- [endTime](PostsGetCountsAllOptions.md#endtime)
- [sinceId](PostsGetCountsAllOptions.md#sinceid)
- [untilId](PostsGetCountsAllOptions.md#untilid)
- [nextToken](PostsGetCountsAllOptions.md#nexttoken)
- [paginationToken](PostsGetCountsAllOptions.md#paginationtoken)
- [granularity](PostsGetCountsAllOptions.md#granularity)
- [searchCountfields](PostsGetCountsAllOptions.md#searchcountfields)
- [requestOptions](PostsGetCountsAllOptions.md#requestoptions)

## Properties

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

#### Defined in

[posts/client.ts:173](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L173)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

#### Defined in

[posts/client.ts:176](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L176)

___

### sinceId

• `Optional` **sinceId**: `string`

Returns results with a Post ID greater than (that is, more recent than) the specified ID.

#### Defined in

[posts/client.ts:179](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L179)

___

### untilId

• `Optional` **untilId**: `string`

Returns results with a Post ID less than (that is, older than) the specified ID.

#### Defined in

[posts/client.ts:182](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L182)

___

### nextToken

• `Optional` **nextToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[posts/client.ts:185](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L185)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[posts/client.ts:188](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L188)

___

### granularity

• `Optional` **granularity**: `string`

The granularity for the search counts results.

#### Defined in

[posts/client.ts:191](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L191)

___

### searchCountfields

• `Optional` **searchCountfields**: `any`[]

A comma separated list of SearchCount fields to display.

#### Defined in

[posts/client.ts:194](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L194)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[posts/client.ts:197](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L197)
