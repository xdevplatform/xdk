[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / GeneralClient

# Class: GeneralClient

Client for General operations

This client provides methods for interacting with the General endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all General related operations.

## Table of contents

### Constructors

- [constructor](GeneralClient.md#constructor)

### Methods

- [getOpenApiSpec](GeneralClient.md#getopenapispec)

## Constructors

### constructor

• **new GeneralClient**(`client`): [`GeneralClient`](GeneralClient.md)

Creates a new General client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`GeneralClient`](GeneralClient.md)

#### Defined in

[general/client.ts:33](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/general/client.ts#L33)

## Methods

### getOpenApiSpec

▸ **getOpenApiSpec**(): `Promise`\<[`GeneralGetOpenApiSpecResponse`](../interfaces/GeneralGetOpenApiSpecResponse.md)\>

Get OpenAPI Spec.
Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)

#### Returns

`Promise`\<[`GeneralGetOpenApiSpecResponse`](../interfaces/GeneralGetOpenApiSpecResponse.md)\>

Promise with the API response

#### Defined in

[general/client.ts:45](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/general/client.ts#L45)
