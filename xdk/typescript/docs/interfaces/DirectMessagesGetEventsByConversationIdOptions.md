[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / DirectMessagesGetEventsByConversationIdOptions

# Interface: DirectMessagesGetEventsByConversationIdOptions

Options for getEventsByConversationId method

## Table of contents

### Properties

- [maxResults](DirectMessagesGetEventsByConversationIdOptions.md#maxresults)
- [paginationToken](DirectMessagesGetEventsByConversationIdOptions.md#paginationtoken)
- [eventTypes](DirectMessagesGetEventsByConversationIdOptions.md#eventtypes)
- [dmEventfields](DirectMessagesGetEventsByConversationIdOptions.md#dmeventfields)
- [expansions](DirectMessagesGetEventsByConversationIdOptions.md#expansions)
- [mediafields](DirectMessagesGetEventsByConversationIdOptions.md#mediafields)
- [userfields](DirectMessagesGetEventsByConversationIdOptions.md#userfields)
- [tweetfields](DirectMessagesGetEventsByConversationIdOptions.md#tweetfields)
- [requestOptions](DirectMessagesGetEventsByConversationIdOptions.md#requestoptions)

## Properties

### maxResults

• `Optional` **maxResults**: `number`

The maximum number of results.

#### Defined in

[direct_messages/client.ts:108](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L108)

___

### paginationToken

• `Optional` **paginationToken**: `string`

This parameter is used to get a specified 'page' of results.

#### Defined in

[direct_messages/client.ts:111](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L111)

___

### eventTypes

• `Optional` **eventTypes**: `any`[]

The set of event_types to include in the results.

#### Defined in

[direct_messages/client.ts:114](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L114)

___

### dmEventfields

• `Optional` **dmEventfields**: `any`[]

A comma separated list of DmEvent fields to display.

#### Defined in

[direct_messages/client.ts:117](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L117)

___

### expansions

• `Optional` **expansions**: `any`[]

A comma separated list of fields to expand.

#### Defined in

[direct_messages/client.ts:120](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L120)

___

### mediafields

• `Optional` **mediafields**: `any`[]

A comma separated list of Media fields to display.

#### Defined in

[direct_messages/client.ts:123](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L123)

___

### userfields

• `Optional` **userfields**: `any`[]

A comma separated list of User fields to display.

#### Defined in

[direct_messages/client.ts:126](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L126)

___

### tweetfields

• `Optional` **tweetfields**: `any`[]

A comma separated list of Tweet fields to display.

#### Defined in

[direct_messages/client.ts:129](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L129)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[direct_messages/client.ts:132](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L132)
