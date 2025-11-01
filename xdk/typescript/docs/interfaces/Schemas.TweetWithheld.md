[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / TweetWithheld

# Interface: TweetWithheld

[Schemas](../modules/Schemas.md).TweetWithheld

## Table of contents

### Properties

- [copyright](Schemas.TweetWithheld.md#copyright)
- [countryCodes](Schemas.TweetWithheld.md#countrycodes)
- [scope](Schemas.TweetWithheld.md#scope)

## Properties

### copyright

• **copyright**: `boolean`

Indicates if the content is being withheld for on the basis of copyright infringement.

#### Defined in

[schemas.ts:2789](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2789)

___

### countryCodes

• **countryCodes**: `string`[]

Provides a list of countries where this content is not available.

#### Defined in

[schemas.ts:2790](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2790)

___

### scope

• `Optional` **scope**: ``"tweet"`` \| ``"user"``

Indicates whether the content being withheld is the `tweet` or a `user`.

#### Defined in

[schemas.ts:2793](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2793)
