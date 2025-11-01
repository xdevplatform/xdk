[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / CommunityNotesClient

# Class: CommunityNotesClient

Client for community notes operations

This client provides methods for interacting with the community notes endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all community notes related operations.

## Table of contents

### Constructors

- [constructor](CommunityNotesClient.md#constructor)

### Methods

- [create](CommunityNotesClient.md#create)
- [evaluate](CommunityNotesClient.md#evaluate)
- [searchWritten](CommunityNotesClient.md#searchwritten)
- [delete](CommunityNotesClient.md#delete)
- [searchEligiblePosts](CommunityNotesClient.md#searcheligibleposts)

## Constructors

### constructor

• **new CommunityNotesClient**(`client`): [`CommunityNotesClient`](CommunityNotesClient.md)

Creates a new community notes client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`CommunityNotesClient`](CommunityNotesClient.md)

#### Defined in

[community_notes/client.ts:120](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/community_notes/client.ts#L120)

## Methods

### create

▸ **create**(`options?`): `Promise`\<[`CreateNoteResponse`](../interfaces/Schemas.CreateNoteResponse.md)\>

Create a Community Note
Creates a community note endpoint for LLM use case.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateOptions` |

#### Returns

`Promise`\<[`CreateNoteResponse`](../interfaces/Schemas.CreateNoteResponse.md)\>

Promise resolving to the API response

#### Defined in

[community_notes/client.ts:133](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/community_notes/client.ts#L133)

___

### evaluate

▸ **evaluate**(`options?`): `Promise`\<[`EvaluateNoteResponse`](../interfaces/Schemas.EvaluateNoteResponse.md)\>

Evaluate a Community Note
Endpoint to evaluate a community note.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `EvaluateOptions` |

#### Returns

`Promise`\<[`EvaluateNoteResponse`](../interfaces/Schemas.EvaluateNoteResponse.md)\>

Promise resolving to the API response

#### Defined in

[community_notes/client.ts:172](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/community_notes/client.ts#L172)

___

### searchWritten

▸ **searchWritten**(`testMode`, `options?`): `Promise`\<[`Get2NotesSearchNotesWrittenResponse`](../interfaces/Schemas.Get2NotesSearchNotesWrittenResponse.md)\>

Search for Community Notes Written
Returns all the community notes written by the user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `testMode` | `boolean` | If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product. |
| `options` | `SearchWrittenOptions` | - |

#### Returns

`Promise`\<[`Get2NotesSearchNotesWrittenResponse`](../interfaces/Schemas.Get2NotesSearchNotesWrittenResponse.md)\>

Promise resolving to the API response

#### Defined in

[community_notes/client.ts:215](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/community_notes/client.ts#L215)

___

### delete

▸ **delete**(`id`): `Promise`\<[`DeleteNoteResponse`](../interfaces/Schemas.DeleteNoteResponse.md)\>

Delete a Community Note
Deletes a community note.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The community note id to delete. |

#### Returns

`Promise`\<[`DeleteNoteResponse`](../interfaces/Schemas.DeleteNoteResponse.md)\>

Promise resolving to the API response

#### Defined in

[community_notes/client.ts:279](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/community_notes/client.ts#L279)

___

### searchEligiblePosts

▸ **searchEligiblePosts**(`testMode`, `options?`): `Promise`\<[`Get2NotesSearchPostsEligibleForNotesResponse`](../interfaces/Schemas.Get2NotesSearchPostsEligibleForNotesResponse.md)\>

Search for Posts Eligible for Community Notes
Returns all the posts that are eligible for community notes.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `testMode` | `boolean` | If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product. |
| `options` | `SearchEligiblePostsOptions` | - |

#### Returns

`Promise`\<[`Get2NotesSearchPostsEligibleForNotesResponse`](../interfaces/Schemas.Get2NotesSearchPostsEligibleForNotesResponse.md)\>

Promise resolving to the API response

#### Defined in

[community_notes/client.ts:317](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/community_notes/client.ts#L317)
