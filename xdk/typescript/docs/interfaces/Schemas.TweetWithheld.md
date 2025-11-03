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

[schemas.ts:2791](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2791)

___

### countryCodes

• **countryCodes**: `string`[]

Provides a list of countries where this content is not available.

#### Defined in

[schemas.ts:2792](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2792)

___

### scope

• `Optional` **scope**: ``"tweet"`` \| ``"user"``

Indicates whether the content being withheld is the `tweet` or a `user`.

#### Defined in

[schemas.ts:2795](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2795)
