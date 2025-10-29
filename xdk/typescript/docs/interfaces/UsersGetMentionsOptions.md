[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UsersGetMentionsOptions

# Interface: UsersGetMentionsOptions

Options for getMentions method

## Table of contents

### Properties

- [sinceId](UsersGetMentionsOptions.md#sinceid)
- [untilId](UsersGetMentionsOptions.md#untilid)
- [maxResults](UsersGetMentionsOptions.md#maxresults)
- [paginationToken](UsersGetMentionsOptions.md#paginationtoken)
- [startTime](UsersGetMentionsOptions.md#starttime)
- [endTime](UsersGetMentionsOptions.md#endtime)
- [tweetfields](UsersGetMentionsOptions.md#tweetfields)
- [expansions](UsersGetMentionsOptions.md#expansions)
- [mediafields](UsersGetMentionsOptions.md#mediafields)
- [pollfields](UsersGetMentionsOptions.md#pollfields)
- [userfields](UsersGetMentionsOptions.md#userfields)
- [placefields](UsersGetMentionsOptions.md#placefields)
- [requestOptions](UsersGetMentionsOptions.md#requestoptions)

## Properties

### sinceId

• `Optional` **sinceId**: `string`

The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.

#### Defined in

[users/client.ts:67](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L67)

___

### untilId

• `Optional` **untilId**: `string`

The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.

#### Defined in

[users/client.ts:70](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L70)

___

### maxResults

• `Optional` **maxResults**: `number`

The maximum number of results.

#### Defined in

[users/client.ts:73](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L73)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get the next 'page' of results.

#### Defined in

[users/client.ts:76](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L76)

___

### startTime

• `Optional` **startTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.

#### Defined in

[users/client.ts:79](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L79)

___

### endTime

• `Optional` **endTime**: `string`

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.

#### Defined in

[users/client.ts:82](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L82)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[users/client.ts:85](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L85)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[users/client.ts:88](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L88)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[users/client.ts:91](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L91)

___

### pollfields

• `Optional` **pollfields**: `any`[]

A comma separated list of Poll fields to display.

#### Defined in

[users/client.ts:94](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L94)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[users/client.ts:97](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L97)

___

### placefields

• `Optional` **placefields**: `any`[]

A comma separated list of Place fields to display.

#### Defined in

[users/client.ts:100](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L100)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[users/client.ts:103](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L103)
