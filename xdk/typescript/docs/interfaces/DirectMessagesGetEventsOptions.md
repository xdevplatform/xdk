[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / DirectMessagesGetEventsOptions

# Interface: DirectMessagesGetEventsOptions

Options for getEvents method

## Table of contents

### Properties

- [maxResults](DirectMessagesGetEventsOptions.md#maxresults)
- [paginationToken](DirectMessagesGetEventsOptions.md#paginationtoken)
- [eventTypes](DirectMessagesGetEventsOptions.md#eventtypes)
- [dmEventfields](DirectMessagesGetEventsOptions.md#dmeventfields)
- [expansions](DirectMessagesGetEventsOptions.md#expansions)
- [mediafields](DirectMessagesGetEventsOptions.md#mediafields)
- [userfields](DirectMessagesGetEventsOptions.md#userfields)
- [tweetfields](DirectMessagesGetEventsOptions.md#tweetfields)
- [requestOptions](DirectMessagesGetEventsOptions.md#requestoptions)

## Properties

### maxResults

• `Optional` **maxResults**: `number`

The maximum number of results.

#### Defined in

[direct_messages/client.ts:33](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L33)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get a specified 'page' of results.

#### Defined in

[direct_messages/client.ts:36](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L36)

___

### eventTypes

• `Optional` **eventTypes**: `any`[]

The set of event_types to include in the results.

#### Defined in

[direct_messages/client.ts:39](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L39)

___

### dmEventfields

• `Optional` **dmEventfields**: `any`[]

A comma separated list of DmEvent fields to display.

#### Defined in

[direct_messages/client.ts:42](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L42)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[direct_messages/client.ts:45](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L45)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[direct_messages/client.ts:48](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L48)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[direct_messages/client.ts:51](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L51)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[direct_messages/client.ts:54](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L54)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[direct_messages/client.ts:57](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L57)
