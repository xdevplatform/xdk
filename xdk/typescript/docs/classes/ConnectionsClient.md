[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ConnectionsClient

# Class: ConnectionsClient

Client for connections operations

This client provides methods for interacting with the connections endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all connections related operations.

## Table of contents

### Constructors

- [constructor](ConnectionsClient.md#constructor)

### Methods

- [deleteAll](ConnectionsClient.md#deleteall)

## Constructors

### constructor

• **new ConnectionsClient**(`client`): [`ConnectionsClient`](ConnectionsClient.md)

Creates a new connections client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`ConnectionsClient`](ConnectionsClient.md)

#### Defined in

[connections/client.ts:33](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/connections/client.ts#L33)

## Methods

### deleteAll

▸ **deleteAll**(): `Promise`\<`any`\>

Terminate all connections
Terminates all active streaming connections for the authenticated application.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[connections/client.ts:45](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/connections/client.ts#L45)
