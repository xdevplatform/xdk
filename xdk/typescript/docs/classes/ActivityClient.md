[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ActivityClient

# Class: ActivityClient

Client for Activity operations

This client provides methods for interacting with the Activity endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Activity related operations.

## Table of contents

### Constructors

- [constructor](ActivityClient.md#constructor)

### Methods

- [updateSubscription](ActivityClient.md#updatesubscription)
- [deleteSubscription](ActivityClient.md#deletesubscription)
- [getSubscriptions](ActivityClient.md#getsubscriptions)
- [createSubscription](ActivityClient.md#createsubscription)
- [stream](ActivityClient.md#stream)

## Constructors

### constructor

• **new ActivityClient**(`client`): [`ActivityClient`](ActivityClient.md)

Creates a new Activity client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`ActivityClient`](ActivityClient.md)

#### Defined in

[activity/client.ts:80](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L80)

## Methods

### updateSubscription

▸ **updateSubscription**(`subscriptionId`, `options?`): `Promise`\<[`ActivityUpdateSubscriptionResponse`](../interfaces/ActivityUpdateSubscriptionResponse.md)\>

Update X activity subscription
Updates a subscription for an X activity event

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `subscriptionId` | `string` | The ID of the subscription to update. |
| `options` | [`ActivityUpdateSubscriptionOptions`](../interfaces/ActivityUpdateSubscriptionOptions.md) | - |

#### Returns

`Promise`\<[`ActivityUpdateSubscriptionResponse`](../interfaces/ActivityUpdateSubscriptionResponse.md)\>

Promise with the API response

#### Defined in

[activity/client.ts:96](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L96)

___

### deleteSubscription

▸ **deleteSubscription**(`subscriptionId`): `Promise`\<[`ActivityDeleteSubscriptionResponse`](../interfaces/ActivityDeleteSubscriptionResponse.md)\>

Deletes X activity subscription
Deletes a subscription for an X activity event

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `subscriptionId` | `string` | The ID of the subscription to delete. |

#### Returns

`Promise`\<[`ActivityDeleteSubscriptionResponse`](../interfaces/ActivityDeleteSubscriptionResponse.md)\>

Promise with the API response

#### Defined in

[activity/client.ts:145](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L145)

___

### getSubscriptions

▸ **getSubscriptions**(): `Promise`\<[`ActivityGetSubscriptionsResponse`](../interfaces/ActivityGetSubscriptionsResponse.md)\>

Get X activity subscriptions
Get a list of active subscriptions for XAA

#### Returns

`Promise`\<[`ActivityGetSubscriptionsResponse`](../interfaces/ActivityGetSubscriptionsResponse.md)\>

Promise with the API response

#### Defined in

[activity/client.ts:183](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L183)

___

### createSubscription

▸ **createSubscription**(`options?`): `Promise`\<[`ActivityCreateSubscriptionResponse`](../interfaces/ActivityCreateSubscriptionResponse.md)\>

Create X activity subscription
Creates a subscription for an X activity event

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`ActivityCreateSubscriptionOptions`](../interfaces/ActivityCreateSubscriptionOptions.md) |

#### Returns

`Promise`\<[`ActivityCreateSubscriptionResponse`](../interfaces/ActivityCreateSubscriptionResponse.md)\>

Promise with the API response

#### Defined in

[activity/client.ts:214](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L214)

___

### stream

▸ **stream**(`options?`): `Promise`\<[`ActivityStreamResponse`](../interfaces/ActivityStreamResponse.md)\>

Activity Stream
Stream of X Activities

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`ActivityStreamOptions`](../interfaces/ActivityStreamOptions.md) |

#### Returns

`Promise`\<[`ActivityStreamResponse`](../interfaces/ActivityStreamResponse.md)\>

Promise with the API response

#### Defined in

[activity/client.ts:253](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/activity/client.ts#L253)
