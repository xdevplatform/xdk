[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / Space

# Interface: Space

[Schemas](../modules/Schemas.md).Space

## Table of contents

### Properties

- [createdAt](Schemas.Space.md#createdat)
- [creatorId](Schemas.Space.md#creatorid)
- [endedAt](Schemas.Space.md#endedat)
- [hostIds](Schemas.Space.md#hostids)
- [id](Schemas.Space.md#id)
- [invitedUserIds](Schemas.Space.md#inviteduserids)
- [isTicketed](Schemas.Space.md#isticketed)
- [lang](Schemas.Space.md#lang)
- [participantCount](Schemas.Space.md#participantcount)
- [scheduledStart](Schemas.Space.md#scheduledstart)
- [speakerIds](Schemas.Space.md#speakerids)
- [startedAt](Schemas.Space.md#startedat)
- [state](Schemas.Space.md#state)
- [subscriberCount](Schemas.Space.md#subscribercount)
- [title](Schemas.Space.md#title)
- [topics](Schemas.Space.md#topics)
- [updatedAt](Schemas.Space.md#updatedat)

## Properties

### createdAt

• `Optional` **createdAt**: `string`

Creation time of the Space.

#### Defined in

[schemas.ts:2315](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2315)

___

### creatorId

• `Optional` **creatorId**: `string`

#### Defined in

[schemas.ts:2316](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2316)

___

### endedAt

• `Optional` **endedAt**: `string`

End time of the Space.

#### Defined in

[schemas.ts:2317](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2317)

___

### hostIds

• `Optional` **hostIds**: `string`[]

The user ids for the hosts of the Space.

#### Defined in

[schemas.ts:2318](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2318)

___

### id

• **id**: `string`

#### Defined in

[schemas.ts:2319](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2319)

___

### invitedUserIds

• `Optional` **invitedUserIds**: `string`[]

An array of user ids for people who were invited to a Space.

#### Defined in

[schemas.ts:2320](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2320)

___

### isTicketed

• `Optional` **isTicketed**: `boolean`

Denotes if the Space is a ticketed Space.

#### Defined in

[schemas.ts:2323](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2323)

___

### lang

• `Optional` **lang**: `string`

The language of the Space.

#### Defined in

[schemas.ts:2324](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2324)

___

### participantCount

• `Optional` **participantCount**: `number`

The number of participants in a Space.

#### Defined in

[schemas.ts:2325](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2325)

___

### scheduledStart

• `Optional` **scheduledStart**: `string`

A date time stamp for when a Space is scheduled to begin.

#### Defined in

[schemas.ts:2326](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2326)

___

### speakerIds

• `Optional` **speakerIds**: `string`[]

An array of user ids for people who were speakers in a Space.

#### Defined in

[schemas.ts:2327](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2327)

___

### startedAt

• `Optional` **startedAt**: `string`

When the Space was started as a date string.

#### Defined in

[schemas.ts:2330](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2330)

___

### state

• **state**: ``"live"`` \| ``"scheduled"`` \| ``"ended"``

The current state of the Space.

#### Defined in

[schemas.ts:2331](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2331)

___

### subscriberCount

• `Optional` **subscriberCount**: `number`

The number of people who have either purchased a ticket or set a reminder for this Space.

#### Defined in

[schemas.ts:2332](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2332)

___

### title

• `Optional` **title**: `string`

The title of the Space.

#### Defined in

[schemas.ts:2333](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2333)

___

### topics

• `Optional` **topics**: `Record`\<`string`, `any`\>[]

The topics of a Space, as selected by its creator.

#### Defined in

[schemas.ts:2334](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2334)

___

### updatedAt

• `Optional` **updatedAt**: `string`

When the Space was last updated.

#### Defined in

[schemas.ts:2337](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2337)
