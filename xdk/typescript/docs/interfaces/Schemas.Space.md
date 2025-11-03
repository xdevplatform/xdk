[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / Space

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

[schemas.ts:2317](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2317)

___

### creatorId

• `Optional` **creatorId**: `string`

#### Defined in

[schemas.ts:2318](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2318)

___

### endedAt

• `Optional` **endedAt**: `string`

End time of the Space.

#### Defined in

[schemas.ts:2319](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2319)

___

### hostIds

• `Optional` **hostIds**: `string`[]

The user ids for the hosts of the Space.

#### Defined in

[schemas.ts:2320](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2320)

___

### id

• **id**: `string`

#### Defined in

[schemas.ts:2321](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2321)

___

### invitedUserIds

• `Optional` **invitedUserIds**: `string`[]

An array of user ids for people who were invited to a Space.

#### Defined in

[schemas.ts:2322](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2322)

___

### isTicketed

• `Optional` **isTicketed**: `boolean`

Denotes if the Space is a ticketed Space.

#### Defined in

[schemas.ts:2325](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2325)

___

### lang

• `Optional` **lang**: `string`

The language of the Space.

#### Defined in

[schemas.ts:2326](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2326)

___

### participantCount

• `Optional` **participantCount**: `number`

The number of participants in a Space.

#### Defined in

[schemas.ts:2327](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2327)

___

### scheduledStart

• `Optional` **scheduledStart**: `string`

A date time stamp for when a Space is scheduled to begin.

#### Defined in

[schemas.ts:2328](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2328)

___

### speakerIds

• `Optional` **speakerIds**: `string`[]

An array of user ids for people who were speakers in a Space.

#### Defined in

[schemas.ts:2329](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2329)

___

### startedAt

• `Optional` **startedAt**: `string`

When the Space was started as a date string.

#### Defined in

[schemas.ts:2332](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2332)

___

### state

• **state**: ``"live"`` \| ``"scheduled"`` \| ``"ended"``

The current state of the Space.

#### Defined in

[schemas.ts:2333](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2333)

___

### subscriberCount

• `Optional` **subscriberCount**: `number`

The number of people who have either purchased a ticket or set a reminder for this Space.

#### Defined in

[schemas.ts:2334](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2334)

___

### title

• `Optional` **title**: `string`

The title of the Space.

#### Defined in

[schemas.ts:2335](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2335)

___

### topics

• `Optional` **topics**: `Record`\<`string`, `any`\>[]

The topics of a Space, as selected by its creator.

#### Defined in

[schemas.ts:2336](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2336)

___

### updatedAt

• `Optional` **updatedAt**: `string`

When the Space was last updated.

#### Defined in

[schemas.ts:2339](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2339)
