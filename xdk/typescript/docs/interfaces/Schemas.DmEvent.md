[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / DmEvent

# Interface: DmEvent

[Schemas](../modules/Schemas.md).DmEvent

## Table of contents

### Properties

- [attachments](Schemas.DmEvent.md#attachments)
- [cashtags](Schemas.DmEvent.md#cashtags)
- [createdAt](Schemas.DmEvent.md#createdat)
- [dmConversationId](Schemas.DmEvent.md#dmconversationid)
- [eventType](Schemas.DmEvent.md#eventtype)
- [hashtags](Schemas.DmEvent.md#hashtags)
- [id](Schemas.DmEvent.md#id)
- [mentions](Schemas.DmEvent.md#mentions)
- [participantIds](Schemas.DmEvent.md#participantids)
- [referencedTweets](Schemas.DmEvent.md#referencedtweets)
- [senderId](Schemas.DmEvent.md#senderid)
- [text](Schemas.DmEvent.md#text)
- [urls](Schemas.DmEvent.md#urls)

## Properties

### attachments

• `Optional` **attachments**: `Record`\<`string`, `any`\>

Specifies the type of attachments (if any) present in this DM.

#### Defined in

[schemas.ts:494](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L494)

___

### cashtags

• `Optional` **cashtags**: `any`[]

none

#### Defined in

[schemas.ts:498](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L498)

___

### createdAt

• `Optional` **createdAt**: `string`

none

#### Defined in

[schemas.ts:499](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L499)

___

### dmConversationId

• `Optional` **dmConversationId**: `string`

#### Defined in

[schemas.ts:500](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L500)

___

### eventType

• **eventType**: `string`

none

#### Defined in

[schemas.ts:501](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L501)

___

### hashtags

• `Optional` **hashtags**: `any`[]

none

#### Defined in

[schemas.ts:502](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L502)

___

### id

• **id**: `string`

#### Defined in

[schemas.ts:503](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L503)

___

### mentions

• `Optional` **mentions**: `any`[]

none

#### Defined in

[schemas.ts:504](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L504)

___

### participantIds

• `Optional` **participantIds**: `string`[]

A list of participants for a ParticipantsJoin or ParticipantsLeave event_type.

#### Defined in

[schemas.ts:505](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L505)

___

### referencedTweets

• `Optional` **referencedTweets**: `Record`\<`string`, `any`\>[]

A list of Posts this DM refers to.

#### Defined in

[schemas.ts:508](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L508)

___

### senderId

• `Optional` **senderId**: `string`

#### Defined in

[schemas.ts:511](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L511)

___

### text

• `Optional` **text**: `string`

none

#### Defined in

[schemas.ts:512](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L512)

___

### urls

• `Optional` **urls**: `any`[]

none

#### Defined in

[schemas.ts:513](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L513)
