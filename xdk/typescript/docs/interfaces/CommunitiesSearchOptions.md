[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / CommunitiesSearchOptions

# Interface: CommunitiesSearchOptions

Options for search method

## Table of contents

### Properties

- [maxResults](CommunitiesSearchOptions.md#maxresults)
- [nextToken](CommunitiesSearchOptions.md#nexttoken)
- [paginationToken](CommunitiesSearchOptions.md#paginationtoken)
- [communityfields](CommunitiesSearchOptions.md#communityfields)
- [requestOptions](CommunitiesSearchOptions.md#requestoptions)

## Properties

### maxResults

• `Optional` **maxResults**: `number`

The maximum number of search results to be returned by a request.

#### Defined in

[communities/client.ts:35](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/communities/client.ts#L35)

___

### nextToken

• `Optional` **nextToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[communities/client.ts:38](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/communities/client.ts#L38)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

#### Defined in

[communities/client.ts:41](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/communities/client.ts#L41)

___

### communityfields

• `Optional` **communityfields**: `any`[]

A comma separated list of Community fields to display.

#### Defined in

[communities/client.ts:44](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/communities/client.ts#L44)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[communities/client.ts:47](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/communities/client.ts#L47)
