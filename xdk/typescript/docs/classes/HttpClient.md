[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / HttpClient

# Class: HttpClient

Universal HTTP client that works in both Node.js and browser environments

## Table of contents

### Constructors

- [constructor](HttpClient.md#constructor)

### Methods

- [createHeaders](HttpClient.md#createheaders)
- [request](HttpClient.md#request)
- [get](HttpClient.md#get)
- [post](HttpClient.md#post)
- [put](HttpClient.md#put)
- [delete](HttpClient.md#delete)
- [patch](HttpClient.md#patch)

## Constructors

### constructor

• **new HttpClient**(): [`HttpClient`](HttpClient.md)

#### Returns

[`HttpClient`](HttpClient.md)

#### Defined in

[http-client.ts:41](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L41)

## Methods

### createHeaders

▸ **createHeaders**(`init?`): `Headers`

Create a new Headers instance

#### Parameters

| Name | Type |
| :------ | :------ |
| `init?` | `Record`\<`string`, `string`\> \| `Headers` |

#### Returns

`Headers`

#### Defined in

[http-client.ts:91](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L91)

___

### request

▸ **request**(`url`, `options?`): `Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

Make an HTTP request

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `options` | [`HttpClientRequestOptions`](../interfaces/HttpClientRequestOptions.md) |

#### Returns

`Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

#### Defined in

[http-client.ts:98](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L98)

___

### get

▸ **get**(`url`, `headers?`): `Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

Make a GET request

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `headers?` | `Record`\<`string`, `string`\> |

#### Returns

`Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

#### Defined in

[http-client.ts:135](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L135)

___

### post

▸ **post**(`url`, `body?`, `headers?`): `Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

Make a POST request

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `body?` | `string` |
| `headers?` | `Record`\<`string`, `string`\> |

#### Returns

`Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

#### Defined in

[http-client.ts:148](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L148)

___

### put

▸ **put**(`url`, `body?`, `headers?`): `Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

Make a PUT request

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `body?` | `string` |
| `headers?` | `Record`\<`string`, `string`\> |

#### Returns

`Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

#### Defined in

[http-client.ts:163](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L163)

___

### delete

▸ **delete**(`url`, `headers?`): `Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

Make a DELETE request

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `headers?` | `Record`\<`string`, `string`\> |

#### Returns

`Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

#### Defined in

[http-client.ts:178](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L178)

___

### patch

▸ **patch**(`url`, `body?`, `headers?`): `Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

Make a PATCH request

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `body?` | `string` |
| `headers?` | `Record`\<`string`, `string`\> |

#### Returns

`Promise`\<[`HttpResponse`](../interfaces/HttpResponse.md)\>

#### Defined in

[http-client.ts:191](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/http-client.ts#L191)
