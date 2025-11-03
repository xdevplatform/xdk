[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / DirectMessagesClient

# Class: DirectMessagesClient

Client for direct messages operations

This client provides methods for interacting with the direct messages endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all direct messages related operations.

## Table of contents

### Constructors

- [constructor](DirectMessagesClient.md#constructor)

### Methods

- [getEvents](DirectMessagesClient.md#getevents)
- [getEventsByParticipantId](DirectMessagesClient.md#geteventsbyparticipantid)
- [createByConversationId](DirectMessagesClient.md#createbyconversationid)
- [createByParticipantId](DirectMessagesClient.md#createbyparticipantid)
- [getEventsByConversationId](DirectMessagesClient.md#geteventsbyconversationid)
- [getEventsById](DirectMessagesClient.md#geteventsbyid)
- [deleteEvents](DirectMessagesClient.md#deleteevents)
- [createConversation](DirectMessagesClient.md#createconversation)

## Constructors

### constructor

• **new DirectMessagesClient**(`client`): [`DirectMessagesClient`](DirectMessagesClient.md)

Creates a new direct messages client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`DirectMessagesClient`](DirectMessagesClient.md)

#### Defined in

[direct_messages/client.ts:211](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L211)

## Methods

### getEvents

▸ **getEvents**(`options?`): `Promise`\<[`Get2DmEventsResponse`](../interfaces/Schemas.Get2DmEventsResponse.md)\>

Get DM events
Retrieves a list of recent direct message events across all conversations.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetEventsOptions` |

#### Returns

`Promise`\<[`Get2DmEventsResponse`](../interfaces/Schemas.Get2DmEventsResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:224](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L224)

___

### getEventsByParticipantId

▸ **getEventsByParticipantId**(`participantId`, `options?`): `Promise`\<[`Get2DmConversationsWithParticipantIdDmEventsResponse`](../interfaces/Schemas.Get2DmConversationsWithParticipantIdDmEventsResponse.md)\>

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `participantId` | `string` | The ID of the participant user for the One to One DM conversation. |
| `options` | `GetEventsByParticipantIdOptions` | - |

#### Returns

`Promise`\<[`Get2DmConversationsWithParticipantIdDmEventsResponse`](../interfaces/Schemas.Get2DmConversationsWithParticipantIdDmEventsResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:311](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L311)

___

### createByConversationId

▸ **createByConversationId**(`dmConversationId`, `options?`): `Promise`\<[`CreateDmEventResponse`](../interfaces/Schemas.CreateDmEventResponse.md)\>

Create DM message by conversation ID
Sends a new direct message to a specific conversation by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dmConversationId` | `string` | The DM Conversation ID. |
| `options` | `CreateByConversationIdOptions` | - |

#### Returns

`Promise`\<[`CreateDmEventResponse`](../interfaces/Schemas.CreateDmEventResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:406](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L406)

___

### createByParticipantId

▸ **createByParticipantId**(`participantId`, `options?`): `Promise`\<[`CreateDmEventResponse`](../interfaces/Schemas.CreateDmEventResponse.md)\>

Create DM message by participant ID
Sends a new direct message to a specific participant by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `participantId` | `string` | The ID of the recipient user that will receive the DM. |
| `options` | `CreateByParticipantIdOptions` | - |

#### Returns

`Promise`\<[`CreateDmEventResponse`](../interfaces/Schemas.CreateDmEventResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:457](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L457)

___

### getEventsByConversationId

▸ **getEventsByConversationId**(`id`, `options?`): `Promise`\<[`Get2DmConversationsIdDmEventsResponse`](../interfaces/Schemas.Get2DmConversationsIdDmEventsResponse.md)\>

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The DM conversation ID. |
| `options` | `GetEventsByConversationIdOptions` | - |

#### Returns

`Promise`\<[`Get2DmConversationsIdDmEventsResponse`](../interfaces/Schemas.Get2DmConversationsIdDmEventsResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:508](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L508)

___

### getEventsById

▸ **getEventsById**(`eventId`, `options?`): `Promise`\<[`Get2DmEventsEventIdResponse`](../interfaces/Schemas.Get2DmEventsEventIdResponse.md)\>

Get DM event by ID
Retrieves details of a specific direct message event by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `eventId` | `string` | dm event id. |
| `options` | `GetEventsByIdOptions` | - |

#### Returns

`Promise`\<[`Get2DmEventsEventIdResponse`](../interfaces/Schemas.Get2DmEventsEventIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:600](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L600)

___

### deleteEvents

▸ **deleteEvents**(`eventId`): `Promise`\<[`DeleteDmResponse`](../interfaces/Schemas.DeleteDmResponse.md)\>

Delete DM event
Deletes a specific direct message event by its ID, if owned by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `eventId` | `string` | The ID of the direct-message event to delete. |

#### Returns

`Promise`\<[`DeleteDmResponse`](../interfaces/Schemas.DeleteDmResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:674](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L674)

___

### createConversation

▸ **createConversation**(`options?`): `Promise`\<[`CreateDmEventResponse`](../interfaces/Schemas.CreateDmEventResponse.md)\>

Create DM conversation
Initiates a new direct message conversation with specified participants.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateConversationOptions` |

#### Returns

`Promise`\<[`CreateDmEventResponse`](../interfaces/Schemas.CreateDmEventResponse.md)\>

Promise resolving to the API response

#### Defined in

[direct_messages/client.ts:708](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/direct_messages/client.ts#L708)
