[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ClientConfig

# Interface: ClientConfig

Configuration options for the X API client

## Table of contents

### Properties

- [baseUrl](ClientConfig.md#baseurl)
- [bearerToken](ClientConfig.md#bearertoken)
- [accessToken](ClientConfig.md#accesstoken)
- [oauth1](ClientConfig.md#oauth1)
- [headers](ClientConfig.md#headers)
- [timeout](ClientConfig.md#timeout)
- [retry](ClientConfig.md#retry)
- [maxRetries](ClientConfig.md#maxretries)
- [userAgent](ClientConfig.md#useragent)

## Properties

### baseUrl

• `Optional` **baseUrl**: `string`

Base URL for API requests

#### Defined in

[client.ts:90](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L90)

___

### bearerToken

• `Optional` **bearerToken**: `string`

Bearer token for authentication

#### Defined in

[client.ts:92](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L92)

___

### accessToken

• `Optional` **accessToken**: `string`

OAuth2 access token

#### Defined in

[client.ts:94](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L94)

___

### oauth1

• `Optional` **oauth1**: `any`

OAuth1 instance for authentication

#### Defined in

[client.ts:96](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L96)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Custom headers to include in requests

#### Defined in

[client.ts:98](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L98)

___

### timeout

• `Optional` **timeout**: `number`

Request timeout in milliseconds

#### Defined in

[client.ts:100](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L100)

___

### retry

• `Optional` **retry**: `boolean`

Whether to automatically retry failed requests

#### Defined in

[client.ts:102](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L102)

___

### maxRetries

• `Optional` **maxRetries**: `number`

Maximum number of retry attempts

#### Defined in

[client.ts:104](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L104)

___

### userAgent

• `Optional` **userAgent**: `string`

User agent string

#### Defined in

[client.ts:106](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/client.ts#L106)
