[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / PaginatedResponse

# Interface: PaginatedResponse\<T\>

Paginated response interface

Represents the structure of a paginated API response from the X API.

## Type parameters

| Name | Description |
| :------ | :------ |
| `T` | The type of items in the response |

## Table of contents

### Properties

- [data](PaginatedResponse.md#data)
- [meta](PaginatedResponse.md#meta)
- [includes](PaginatedResponse.md#includes)
- [errors](PaginatedResponse.md#errors)

## Properties

### data

• **data**: `T`[]

Array of items in the current page

#### Defined in

[paginator.ts:19](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/paginator.ts#L19)

___

### meta

• `Optional` **meta**: `Object`

Pagination metadata

#### Type declaration

| Name | Type | Description |
| :------ | :------ | :------ |
| `result_count?` | `number` | Number of results in the current page |
| `next_token?` | `string` | Token for fetching the next page |
| `previous_token?` | `string` | Token for fetching the previous page |

#### Defined in

[paginator.ts:21](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/paginator.ts#L21)

___

### includes

• `Optional` **includes**: `Record`\<`string`, `any`\>

Additional included objects (users, tweets, etc.)

#### Defined in

[paginator.ts:30](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/paginator.ts#L30)

___

### errors

• `Optional` **errors**: `any`[]

Any errors in the response

#### Defined in

[paginator.ts:32](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/paginator.ts#L32)
