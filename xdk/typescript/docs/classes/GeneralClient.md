[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / GeneralClient

# Class: GeneralClient

Client for general operations

This client provides methods for interacting with the general endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all general related operations.

## Table of contents

### Constructors

- [constructor](GeneralClient.md#constructor)

### Methods

- [getOpenApiSpec](GeneralClient.md#getopenapispec)

## Constructors

### constructor

• **new GeneralClient**(`client`): [`GeneralClient`](GeneralClient.md)

Creates a new general client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`GeneralClient`](GeneralClient.md)

#### Defined in

[general/client.ts:33](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/general/client.ts#L33)

## Methods

### getOpenApiSpec

▸ **getOpenApiSpec**(): `Promise`\<`GetOpenApiSpecResponse`\>

Get OpenAPI Spec.
Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)

#### Returns

`Promise`\<`GetOpenApiSpecResponse`\>

Promise with the API response

#### Defined in

[general/client.ts:45](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/general/client.ts#L45)
