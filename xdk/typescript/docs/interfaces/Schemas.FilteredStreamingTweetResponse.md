[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / FilteredStreamingTweetResponse

# Interface: FilteredStreamingTweetResponse

[Schemas](../modules/Schemas.md).FilteredStreamingTweetResponse

## Table of contents

### Properties

- [data](Schemas.FilteredStreamingTweetResponse.md#data)
- [errors](Schemas.FilteredStreamingTweetResponse.md#errors)
- [includes](Schemas.FilteredStreamingTweetResponse.md#includes)
- [matchingRules](Schemas.FilteredStreamingTweetResponse.md#matchingrules)

## Properties

### data

• `Optional` **data**: [`Tweet`](Schemas.Tweet.md)

#### Defined in

[schemas.ts:635](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L635)

___

### errors

• `Optional` **errors**: [`Problem`](Schemas.Problem.md)[]

none

#### Defined in

[schemas.ts:636](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L636)

___

### includes

• `Optional` **includes**: [`Expansions`](Schemas.Expansions.md)

#### Defined in

[schemas.ts:637](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L637)

___

### matchingRules

• `Optional` **matchingRules**: `Record`\<`string`, `any`\>[]

The list of rules which matched the Tweet

#### Defined in

[schemas.ts:638](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L638)
