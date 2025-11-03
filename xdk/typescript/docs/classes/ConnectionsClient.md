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

[connections/client.ts:33](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/connections/client.ts#L33)

## Methods

### deleteAll

▸ **deleteAll**(): `Promise`\<[`KillAllConnectionsResponse`](../interfaces/Schemas.KillAllConnectionsResponse.md)\>

Terminate all connections
Terminates all active streaming connections for the authenticated application.

#### Returns

`Promise`\<[`KillAllConnectionsResponse`](../interfaces/Schemas.KillAllConnectionsResponse.md)\>

Promise resolving to the API response

#### Defined in

[connections/client.ts:46](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/connections/client.ts#L46)
