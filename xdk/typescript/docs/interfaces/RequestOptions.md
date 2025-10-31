[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / RequestOptions

# Interface: RequestOptions

Request options for API calls

## Table of contents

### Properties

- [timeout](RequestOptions.md#timeout)
- [headers](RequestOptions.md#headers)
- [signal](RequestOptions.md#signal)
- [body](RequestOptions.md#body)
- [raw](RequestOptions.md#raw)

## Properties

### timeout

• `Optional` **timeout**: `number`

Request timeout in milliseconds

#### Defined in

[client.ts:133](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L133)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[client.ts:135](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L135)

___

### signal

• `Optional` **signal**: `AbortSignal`

Request signal for cancellation

#### Defined in

[client.ts:137](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L137)

___

### body

• `Optional` **body**: `string`

Request body

#### Defined in

[client.ts:139](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L139)

___

### raw

• `Optional` **raw**: `boolean`

Return raw HTTP wrapper instead of parsed body

#### Defined in

[client.ts:141](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L141)
