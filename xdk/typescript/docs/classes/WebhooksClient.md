[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / WebhooksClient

# Class: WebhooksClient

Client for webhooks operations

This client provides methods for interacting with the webhooks endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all webhooks related operations.

## Table of contents

### Constructors

- [constructor](WebhooksClient.md#constructor)

### Methods

- [get](WebhooksClient.md#get)
- [create](WebhooksClient.md#create)
- [getStreamLinks](WebhooksClient.md#getstreamlinks)
- [validate](WebhooksClient.md#validate)
- [delete](WebhooksClient.md#delete)
- [createStreamLink](WebhooksClient.md#createstreamlink)
- [deleteStreamLink](WebhooksClient.md#deletestreamlink)

## Constructors

### constructor

• **new WebhooksClient**(`client`): [`WebhooksClient`](WebhooksClient.md)

Creates a new webhooks client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`WebhooksClient`](WebhooksClient.md)

#### Defined in

[webhooks/client.ts:96](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L96)

## Methods

### get

▸ **get**(`options?`): `Promise`\<[`Get2WebhooksResponse`](../interfaces/Schemas.Get2WebhooksResponse.md)\>

Get webhook
Get a list of webhook configs associated with a client app.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetOptions` |

#### Returns

`Promise`\<[`Get2WebhooksResponse`](../interfaces/Schemas.Get2WebhooksResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:109](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L109)

___

### create

▸ **create**(`options?`): `Promise`\<[`WebhookConfigCreateResponse`](../interfaces/Schemas.WebhookConfigCreateResponse.md)\>

Create webhook
Creates a new webhook configuration.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateOptions` |

#### Returns

`Promise`\<[`WebhookConfigCreateResponse`](../interfaces/Schemas.WebhookConfigCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:150](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L150)

___

### getStreamLinks

▸ **getStreamLinks**(): `Promise`\<[`WebhookLinksGetResponse`](../interfaces/Schemas.WebhookLinksGetResponse.md)\>

Get stream links
Get a list of webhook links associated with a filtered stream ruleset.

#### Returns

`Promise`\<[`WebhookLinksGetResponse`](../interfaces/Schemas.WebhookLinksGetResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:189](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L189)

___

### validate

▸ **validate**(`webhookId`): `Promise`\<[`WebhookConfigPutResponse`](../interfaces/Schemas.WebhookConfigPutResponse.md)\>

Validate webhook
Triggers a CRC check for a given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The ID of the webhook to check. |

#### Returns

`Promise`\<[`WebhookConfigPutResponse`](../interfaces/Schemas.WebhookConfigPutResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:225](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L225)

___

### delete

▸ **delete**(`webhookId`): `Promise`\<[`WebhookConfigDeleteResponse`](../interfaces/Schemas.WebhookConfigDeleteResponse.md)\>

Delete webhook
Deletes an existing webhook configuration.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The ID of the webhook to delete. |

#### Returns

`Promise`\<[`WebhookConfigDeleteResponse`](../interfaces/Schemas.WebhookConfigDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:263](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L263)

___

### createStreamLink

▸ **createStreamLink**(`webhookId`, `options?`): `Promise`\<[`WebhookLinksCreateResponse`](../interfaces/Schemas.WebhookLinksCreateResponse.md)\>

Create stream link
Creates a link to deliver FilteredStream events to the given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to link to your FilteredStream ruleset. |
| `options` | `CreateStreamLinkOptions` | - |

#### Returns

`Promise`\<[`WebhookLinksCreateResponse`](../interfaces/Schemas.WebhookLinksCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:301](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L301)

___

### deleteStreamLink

▸ **deleteStreamLink**(`webhookId`): `Promise`\<[`WebhookLinksDeleteResponse`](../interfaces/Schemas.WebhookLinksDeleteResponse.md)\>

Delete stream link
Deletes a link from FilteredStream events to the given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to link to your FilteredStream ruleset. |

#### Returns

`Promise`\<[`WebhookLinksDeleteResponse`](../interfaces/Schemas.WebhookLinksDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[webhooks/client.ts:381](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/webhooks/client.ts#L381)
