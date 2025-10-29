[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamPostsResponse

# Interface: StreamPostsResponse

Response for posts
A Tweet or error that can be returned by the streaming Tweet API. The values returned with a successful streamed Tweet includes the user provided rules that the Tweet matched.

## Table of contents

### Properties

- [data](StreamPostsResponse.md#data)
- [errors](StreamPostsResponse.md#errors)
- [includes](StreamPostsResponse.md#includes)
- [matchingRules](StreamPostsResponse.md#matchingrules)

## Properties

### data

• `Optional` **data**: `Record`\<`string`, `any`\>

#### Defined in

[stream/models.ts:78](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/models.ts#L78)

___

### errors

• `Optional` **errors**: `any`[]

#### Defined in

[stream/models.ts:79](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/models.ts#L79)

___

### includes

• `Optional` **includes**: `Record`\<`string`, `any`\>

#### Defined in

[stream/models.ts:80](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/models.ts#L80)

___

### matchingRules

• `Optional` **matchingRules**: `any`[]

The list of rules which matched the Tweet

#### Defined in

[stream/models.ts:82](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/models.ts#L82)
