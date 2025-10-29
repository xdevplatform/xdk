[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / PostsSearchRecentOptions

# Interface: PostsSearchRecentOptions

Options for searchRecent method

## Table of contents

### Properties

- [startTime](PostsSearchRecentOptions.md#starttime)
- [endTime](PostsSearchRecentOptions.md#endtime)
- [sinceId](PostsSearchRecentOptions.md#sinceid)
- [untilId](PostsSearchRecentOptions.md#untilid)
- [maxResults](PostsSearchRecentOptions.md#maxresults)
- [nextToken](PostsSearchRecentOptions.md#nexttoken)
- [paginationToken](PostsSearchRecentOptions.md#paginationtoken)
- [sortOrder](PostsSearchRecentOptions.md#sortorder)
- [tweetfields](PostsSearchRecentOptions.md#tweetfields)
- [expansions](PostsSearchRecentOptions.md#expansions)
- [mediafields](PostsSearchRecentOptions.md#mediafields)
- [pollfields](PostsSearchRecentOptions.md#pollfields)
- [userfields](PostsSearchRecentOptions.md#userfields)
- [placefields](PostsSearchRecentOptions.md#placefields)
- [requestOptions](PostsSearchRecentOptions.md#requestoptions)

## Properties

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

#### Defined in

[posts/client.ts:63](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L63)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

#### Defined in

[posts/client.ts:66](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L66)

___

### sinceId

• `Optional` **sinceId**: `string`

Returns results with a Post ID greater than (that is, more recent than) the specified ID.

#### Defined in

[posts/client.ts:69](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L69)

___

### untilId

• `Optional` **untilId**: `string`

Returns results with a Post ID less than (that is, older than) the specified ID.

#### Defined in

[posts/client.ts:72](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L72)

___

### maxResults

• `Optional` **maxResults**: `number`

The maximum number of search results to be returned by a request.

#### Defined in

[posts/client.ts:75](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L75)

___

### nextToken

• `Optional` **nextToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[posts/client.ts:78](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L78)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[posts/client.ts:81](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L81)

___

### sortOrder

• `Optional` **sortOrder**: `string`

This order in which to return results.

#### Defined in

[posts/client.ts:84](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L84)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[posts/client.ts:87](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L87)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[posts/client.ts:90](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L90)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[posts/client.ts:93](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L93)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[posts/client.ts:96](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L96)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[posts/client.ts:99](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L99)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[posts/client.ts:102](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L102)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[posts/client.ts:105](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/posts/client.ts#L105)
