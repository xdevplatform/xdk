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

[general/client.ts:33](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/general/client.ts#L33)

## Methods

### getOpenApiSpec

▸ **getOpenApiSpec**(): `Promise`\<[`GetOpenApiSpecResponse`](../modules/General.md#getopenapispecresponse)\>

Get OpenAPI Spec.
Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)

#### Returns

`Promise`\<[`GetOpenApiSpecResponse`](../modules/General.md#getopenapispecresponse)\>

Promise resolving to the API response

#### Defined in

[general/client.ts:46](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/general/client.ts#L46)
