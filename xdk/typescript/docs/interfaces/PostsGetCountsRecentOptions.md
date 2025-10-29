[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / PostsGetCountsRecentOptions

# Interface: PostsGetCountsRecentOptions

Options for getCountsRecent method

## Table of contents

### Properties

- [startTime](PostsGetCountsRecentOptions.md#starttime)
- [endTime](PostsGetCountsRecentOptions.md#endtime)
- [sinceId](PostsGetCountsRecentOptions.md#sinceid)
- [untilId](PostsGetCountsRecentOptions.md#untilid)
- [nextToken](PostsGetCountsRecentOptions.md#nexttoken)
- [paginationToken](PostsGetCountsRecentOptions.md#paginationtoken)
- [granularity](PostsGetCountsRecentOptions.md#granularity)
- [searchCountfields](PostsGetCountsRecentOptions.md#searchcountfields)
- [requestOptions](PostsGetCountsRecentOptions.md#requestoptions)

## Properties

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

#### Defined in

[posts/client.ts:294](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L294)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

#### Defined in

[posts/client.ts:297](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L297)

___

### sinceId

• `Optional` **sinceId**: `string`

Returns results with a Post ID greater than (that is, more recent than) the specified ID.

#### Defined in

[posts/client.ts:300](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L300)

___

### untilId

• `Optional` **untilId**: `string`

Returns results with a Post ID less than (that is, older than) the specified ID.

#### Defined in

[posts/client.ts:303](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L303)

___

### nextToken

• `Optional` **nextToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[posts/client.ts:306](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L306)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[posts/client.ts:309](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L309)

___

### granularity

• `Optional` **granularity**: `string`

The granularity for the search counts results.

#### Defined in

[posts/client.ts:312](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L312)

___

### searchCountfields

• `Optional` **searchCountfields**: `any`[]

A comma separated list of SearchCount fields to display.

#### Defined in

[posts/client.ts:315](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L315)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[posts/client.ts:318](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L318)
