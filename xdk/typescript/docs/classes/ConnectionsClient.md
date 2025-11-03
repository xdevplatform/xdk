[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / ConnectionsClient

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

[connections/client.ts:33](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/connections/client.ts#L33)

## Methods

### deleteAll

▸ **deleteAll**(): `Promise`\<[`KillAllConnectionsResponse`](../interfaces/Schemas.KillAllConnectionsResponse.md)\>

Terminate all connections
Terminates all active streaming connections for the authenticated application.

#### Returns

`Promise`\<[`KillAllConnectionsResponse`](../interfaces/Schemas.KillAllConnectionsResponse.md)\>

Promise resolving to the API response

#### Defined in

[connections/client.ts:46](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/connections/client.ts#L46)
