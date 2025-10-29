[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / WebhooksClient

# Class: WebhooksClient

Client for Webhooks operations

This client provides methods for interacting with the Webhooks endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Webhooks related operations.

## Table of contents

### Constructors

- [constructor](WebhooksClient.md#constructor)

### Methods

- [validate](WebhooksClient.md#validate)
- [delete](WebhooksClient.md#delete)
- [get](WebhooksClient.md#get)
- [create](WebhooksClient.md#create)
- [getStreamLinks](WebhooksClient.md#getstreamlinks)
- [createStreamLink](WebhooksClient.md#createstreamlink)
- [deleteStreamLink](WebhooksClient.md#deletestreamlink)

## Constructors

### constructor

• **new WebhooksClient**(`client`): [`WebhooksClient`](WebhooksClient.md)

Creates a new Webhooks client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`WebhooksClient`](WebhooksClient.md)

#### Defined in

[webhooks/client.ts:90](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L90)

## Methods

### validate

▸ **validate**(`webhookId`): `Promise`\<[`WebhooksValidateResponse`](../interfaces/WebhooksValidateResponse.md)\>

Validate webhook
Triggers a CRC check for a given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The ID of the webhook to check. |

#### Returns

`Promise`\<[`WebhooksValidateResponse`](../interfaces/WebhooksValidateResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:106](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L106)

___

### delete

▸ **delete**(`webhookId`): `Promise`\<[`WebhooksDeleteResponse`](../interfaces/WebhooksDeleteResponse.md)\>

Delete webhook
Deletes an existing webhook configuration.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The ID of the webhook to delete. |

#### Returns

`Promise`\<[`WebhooksDeleteResponse`](../interfaces/WebhooksDeleteResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:143](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L143)

___

### get

▸ **get**(`options?`): `Promise`\<[`WebhooksGetResponse`](../interfaces/WebhooksGetResponse.md)\>

Get webhook
Get a list of webhook configs associated with a client app.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`WebhooksGetOptions`](../interfaces/WebhooksGetOptions.md) |

#### Returns

`Promise`\<[`WebhooksGetResponse`](../interfaces/WebhooksGetResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:176](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L176)

___

### create

▸ **create**(`options?`): `Promise`\<[`WebhooksCreateResponse`](../interfaces/WebhooksCreateResponse.md)\>

Create webhook
Creates a new webhook configuration.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`WebhooksCreateOptions`](../interfaces/WebhooksCreateOptions.md) |

#### Returns

`Promise`\<[`WebhooksCreateResponse`](../interfaces/WebhooksCreateResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:215](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L215)

___

### getStreamLinks

▸ **getStreamLinks**(): `Promise`\<[`WebhooksGetStreamLinksResponse`](../interfaces/WebhooksGetStreamLinksResponse.md)\>

Get stream links
Get a list of webhook links associated with a filtered stream ruleset.

#### Returns

`Promise`\<[`WebhooksGetStreamLinksResponse`](../interfaces/WebhooksGetStreamLinksResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:254](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L254)

___

### createStreamLink

▸ **createStreamLink**(`webhookId`, `options?`): `Promise`\<[`WebhooksCreateStreamLinkResponse`](../interfaces/WebhooksCreateStreamLinkResponse.md)\>

Create stream link
Creates a link to deliver FilteredStream events to the given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to link to your FilteredStream ruleset. |
| `options` | [`WebhooksCreateStreamLinkOptions`](../interfaces/WebhooksCreateStreamLinkOptions.md) | - |

#### Returns

`Promise`\<[`WebhooksCreateStreamLinkResponse`](../interfaces/WebhooksCreateStreamLinkResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:289](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L289)

___

### deleteStreamLink

▸ **deleteStreamLink**(`webhookId`): `Promise`\<[`WebhooksDeleteStreamLinkResponse`](../interfaces/WebhooksDeleteStreamLinkResponse.md)\>

Delete stream link
Deletes a link from FilteredStream events to the given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to link to your FilteredStream ruleset. |

#### Returns

`Promise`\<[`WebhooksDeleteStreamLinkResponse`](../interfaces/WebhooksDeleteStreamLinkResponse.md)\>

Promise with the API response

#### Defined in

[webhooks/client.ts:367](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/webhooks/client.ts#L367)
