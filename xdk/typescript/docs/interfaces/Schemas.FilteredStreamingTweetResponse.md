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

[schemas.ts:633](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L633)

___

### errors

• `Optional` **errors**: [`Problem`](Schemas.Problem.md)[]

none

#### Defined in

[schemas.ts:634](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L634)

___

### includes

• `Optional` **includes**: [`Expansions`](Schemas.Expansions.md)

#### Defined in

[schemas.ts:635](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L635)

___

### matchingRules

• `Optional` **matchingRules**: `Record`\<`string`, `any`\>[]

The list of rules which matched the Tweet

#### Defined in

[schemas.ts:636](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L636)
