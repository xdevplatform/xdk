[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / DirectMessagesClient

# Class: DirectMessagesClient

Client for Direct messages operations

This client provides methods for interacting with the Direct messages endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Direct messages related operations.

## Table of contents

### Constructors

- [constructor](DirectMessagesClient.md#constructor)

### Methods

- [createByConversationId](DirectMessagesClient.md#createbyconversationid)
- [getEventsById](DirectMessagesClient.md#geteventsbyid)
- [deleteEvents](DirectMessagesClient.md#deleteevents)
- [createConversation](DirectMessagesClient.md#createconversation)
- [createByParticipantId](DirectMessagesClient.md#createbyparticipantid)
- [getEvents](DirectMessagesClient.md#getevents)
- [getEventsByParticipantId](DirectMessagesClient.md#geteventsbyparticipantid)
- [getEventsByConversationId](DirectMessagesClient.md#geteventsbyconversationid)

## Constructors

### constructor

• **new DirectMessagesClient**(`client`): [`DirectMessagesClient`](DirectMessagesClient.md)

Creates a new Direct messages client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`DirectMessagesClient`](DirectMessagesClient.md)

#### Defined in

[direct_messages/client.ts:197](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L197)

## Methods

### createByConversationId

▸ **createByConversationId**(`dmConversationId`, `options?`): `Promise`\<[`DirectMessagesCreateByConversationIdResponse`](../interfaces/DirectMessagesCreateByConversationIdResponse.md)\>

Create DM message by conversation ID
Sends a new direct message to a specific conversation by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dmConversationId` | `string` | The DM Conversation ID. |
| `options` | [`DirectMessagesCreateByConversationIdOptions`](../interfaces/DirectMessagesCreateByConversationIdOptions.md) | - |

#### Returns

`Promise`\<[`DirectMessagesCreateByConversationIdResponse`](../interfaces/DirectMessagesCreateByConversationIdResponse.md)\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:213](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L213)

___

### getEventsById

▸ **getEventsById**(`eventId`, `options?`): `Promise`\<[`DirectMessagesGetEventsByIdResponse`](../interfaces/DirectMessagesGetEventsByIdResponse.md)\>

Get DM event by ID
Retrieves details of a specific direct message event by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `eventId` | `string` | dm event id. |
| `options` | [`DirectMessagesGetEventsByIdOptions`](../interfaces/DirectMessagesGetEventsByIdOptions.md) | - |

#### Returns

`Promise`\<[`DirectMessagesGetEventsByIdResponse`](../interfaces/DirectMessagesGetEventsByIdResponse.md)\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:262](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L262)

___

### deleteEvents

▸ **deleteEvents**(`eventId`): `Promise`\<[`DirectMessagesDeleteEventsResponse`](../interfaces/DirectMessagesDeleteEventsResponse.md)\>

Delete DM event
Deletes a specific direct message event by its ID, if owned by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `eventId` | `string` | The ID of the direct-message event to delete. |

#### Returns

`Promise`\<[`DirectMessagesDeleteEventsResponse`](../interfaces/DirectMessagesDeleteEventsResponse.md)\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:334](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L334)

___

### createConversation

▸ **createConversation**(`options?`): `Promise`\<[`DirectMessagesCreateConversationResponse`](../interfaces/DirectMessagesCreateConversationResponse.md)\>

Create DM conversation
Initiates a new direct message conversation with specified participants.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`DirectMessagesCreateConversationOptions`](../interfaces/DirectMessagesCreateConversationOptions.md) |

#### Returns

`Promise`\<[`DirectMessagesCreateConversationResponse`](../interfaces/DirectMessagesCreateConversationResponse.md)\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:369](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L369)

___

### createByParticipantId

▸ **createByParticipantId**(`participantId`, `options?`): `Promise`\<[`DirectMessagesCreateByParticipantIdResponse`](../interfaces/DirectMessagesCreateByParticipantIdResponse.md)\>

Create DM message by participant ID
Sends a new direct message to a specific participant by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `participantId` | `string` | The ID of the recipient user that will receive the DM. |
| `options` | [`DirectMessagesCreateByParticipantIdOptions`](../interfaces/DirectMessagesCreateByParticipantIdOptions.md) | - |

#### Returns

`Promise`\<[`DirectMessagesCreateByParticipantIdResponse`](../interfaces/DirectMessagesCreateByParticipantIdResponse.md)\>

Promise with the API response

#### Defined in

[direct_messages/client.ts:412](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L412)

___

### getEvents

▸ **getEvents**(`options?`): `Promise`\<[`EventPaginator`](EventPaginator.md)\>

Get DM events
Retrieves a list of recent direct message events across all conversations.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options` | [`DirectMessagesGetEventsOptions`](../interfaces/DirectMessagesGetEventsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`EventPaginator`](EventPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[direct_messages/client.ts:457](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L457)

___

### getEventsByParticipantId

▸ **getEventsByParticipantId**(`participantId`, `options?`): `Promise`\<[`EventPaginator`](EventPaginator.md)\>

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `participantId` | `string` | The ID of the participant user for the One to One DM conversation. |
| `options` | [`DirectMessagesGetEventsByParticipantIdOptions`](../interfaces/DirectMessagesGetEventsByParticipantIdOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`EventPaginator`](EventPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[direct_messages/client.ts:569](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L569)

___

### getEventsByConversationId

▸ **getEventsByConversationId**(`id`, `options?`): `Promise`\<[`EventPaginator`](EventPaginator.md)\>

Get DM events for a DM conversation
Retrieves direct message events for a specific conversation.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The DM conversation ID. |
| `options` | [`DirectMessagesGetEventsByConversationIdOptions`](../interfaces/DirectMessagesGetEventsByConversationIdOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`EventPaginator`](EventPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[direct_messages/client.ts:687](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/direct_messages/client.ts#L687)
