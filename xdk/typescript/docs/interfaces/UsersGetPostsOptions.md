[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UsersGetPostsOptions

# Interface: UsersGetPostsOptions

Options for getPosts method

## Table of contents

### Properties

- [sinceId](UsersGetPostsOptions.md#sinceid)
- [untilId](UsersGetPostsOptions.md#untilid)
- [maxResults](UsersGetPostsOptions.md#maxresults)
- [paginationToken](UsersGetPostsOptions.md#paginationtoken)
- [exclude](UsersGetPostsOptions.md#exclude)
- [startTime](UsersGetPostsOptions.md#starttime)
- [endTime](UsersGetPostsOptions.md#endtime)
- [tweetfields](UsersGetPostsOptions.md#tweetfields)
- [expansions](UsersGetPostsOptions.md#expansions)
- [mediafields](UsersGetPostsOptions.md#mediafields)
- [pollfields](UsersGetPostsOptions.md#pollfields)
- [userfields](UsersGetPostsOptions.md#userfields)
- [placefields](UsersGetPostsOptions.md#placefields)
- [requestOptions](UsersGetPostsOptions.md#requestoptions)

## Properties

### sinceId

• `Optional` **sinceId**: `string`

The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.

#### Defined in

[users/client.ts:526](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L526)

___

### untilId

• `Optional` **untilId**: `string`

The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.

#### Defined in

[users/client.ts:529](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L529)

___

### maxResults

• `Optional` **maxResults**: `number`

The maximum number of results.

#### Defined in

[users/client.ts:532](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L532)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get the next 'page' of results.

#### Defined in

[users/client.ts:535](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L535)

___

### exclude

• `Optional` **exclude**: `any`[]

The set of entities to exclude (e.g. 'replies' or 'retweets').

#### Defined in

[users/client.ts:538](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L538)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.

#### Defined in

[users/client.ts:541](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L541)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.

#### Defined in

[users/client.ts:544](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L544)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[users/client.ts:547](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L547)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[users/client.ts:550](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L550)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[users/client.ts:553](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L553)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[users/client.ts:556](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L556)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[users/client.ts:559](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L559)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[users/client.ts:562](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L562)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[users/client.ts:565](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L565)
