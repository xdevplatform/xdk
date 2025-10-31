[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / DirectMessagesClient

# Class: DirectMessagesClient

Client for direct messages operations

This client provides methods for interacting with the direct messages endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all direct messages related operations.

## Table of contents

### Constructors

- [constructor](DirectMessagesClient.md#constructor)

### Methods

- [getEventsByParticipantId](DirectMessagesClient.md#geteventsbyparticipantid)
- [createByParticipantId](DirectMessagesClient.md#createbyparticipantid)
- [getEventsById](DirectMessagesClient.md#geteventsbyid)
- [deleteEvents](DirectMessagesClient.md#deleteevents)
- [createByConversationId](DirectMessagesClient.md#createbyconversationid)
- [createConversation](DirectMessagesClient.md#createconversation)
- [getEventsByConversationId](DirectMessagesClient.md#geteventsbyconversationid)
- [getEvents](DirectMessagesClient.md#getevents)

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

[direct_messages/client.ts:114](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L114)

## Methods

### getEventsByParticipantId

▸ **getEventsByParticipantId**(`options?`): `Promise`\<`any`\>

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetEventsByParticipantIdOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:128](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L128)

___

### createByParticipantId

▸ **createByParticipantId**(`options?`): `Promise`\<`any`\>

Create DM message by participant ID
Sends a new direct message to a specific participant by their ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateByParticipantIdOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:163](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L163)

___

### getEventsById

▸ **getEventsById**(): `Promise`\<`any`\>

Get DM event by ID
Retrieves details of a specific direct message event by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:204](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L204)

___

### deleteEvents

▸ **deleteEvents**(): `Promise`\<`any`\>

Delete DM event
Deletes a specific direct message event by its ID, if owned by the authenticated user.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:237](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L237)

___

### createByConversationId

▸ **createByConversationId**(`options?`): `Promise`\<`any`\>

Create DM message by conversation ID
Sends a new direct message to a specific conversation by its ID.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateByConversationIdOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:270](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L270)

___

### createConversation

▸ **createConversation**(`options?`): `Promise`\<`any`\>

Create DM conversation
Initiates a new direct message conversation with specified participants.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateConversationOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:309](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L309)

___

### getEventsByConversationId

▸ **getEventsByConversationId**(`options?`): `Promise`\<`any`\>

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetEventsByConversationIdOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:350](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L350)

___

### getEvents

▸ **getEvents**(`options?`): `Promise`\<`any`\>

Get DM events
Retrieves a list of recent direct message events across all conversations.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetEventsOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:383](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/direct_messages/client.ts#L383)
