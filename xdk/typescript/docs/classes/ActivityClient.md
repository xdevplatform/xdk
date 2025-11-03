[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ActivityClient

# Class: ActivityClient

Client for activity operations

This client provides methods for interacting with the activity endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all activity related operations.

## Table of contents

### Constructors

- [constructor](ActivityClient.md#constructor)

### Methods

- [updateSubscription](ActivityClient.md#updatesubscription)
- [deleteSubscription](ActivityClient.md#deletesubscription)
- [stream](ActivityClient.md#stream)
- [getSubscriptions](ActivityClient.md#getsubscriptions)
- [createSubscription](ActivityClient.md#createsubscription)

## Constructors

### constructor

• **new ActivityClient**(`client`): [`ActivityClient`](ActivityClient.md)

Creates a new activity client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`ActivityClient`](ActivityClient.md)

#### Defined in

[activity/client.ts:86](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/activity/client.ts#L86)

## Methods

### updateSubscription

▸ **updateSubscription**(`subscriptionId`, `options?`): `Promise`\<[`ActivitySubscriptionUpdateResponse`](../interfaces/Schemas.ActivitySubscriptionUpdateResponse.md)\>

Update X activity subscription
Updates a subscription for an X activity event

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `subscriptionId` | `string` | The ID of the subscription to update. |
| `options` | `UpdateSubscriptionOptions` | - |

#### Returns

`Promise`\<[`ActivitySubscriptionUpdateResponse`](../interfaces/Schemas.ActivitySubscriptionUpdateResponse.md)\>

Promise resolving to the API response

#### Defined in

[activity/client.ts:103](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/activity/client.ts#L103)

___

### deleteSubscription

▸ **deleteSubscription**(`subscriptionId`): `Promise`\<[`ActivitySubscriptionDeleteResponse`](../interfaces/Schemas.ActivitySubscriptionDeleteResponse.md)\>

Deletes X activity subscription
Deletes a subscription for an X activity event

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `subscriptionId` | `string` | The ID of the subscription to delete. |

#### Returns

`Promise`\<[`ActivitySubscriptionDeleteResponse`](../interfaces/Schemas.ActivitySubscriptionDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[activity/client.ts:154](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/activity/client.ts#L154)

___

### stream

▸ **stream**(`options?`): `Promise`\<[`ActivityStreamingResponse`](../interfaces/Schemas.ActivityStreamingResponse.md)\>

Activity Stream
Stream of X Activities

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `StreamOptions` |

#### Returns

`Promise`\<[`ActivityStreamingResponse`](../interfaces/Schemas.ActivityStreamingResponse.md)\>

Promise resolving to the API response

#### Defined in

[activity/client.ts:193](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/activity/client.ts#L193)

___

### getSubscriptions

▸ **getSubscriptions**(): `Promise`\<[`ActivitySubscriptionGetResponse`](../interfaces/Schemas.ActivitySubscriptionGetResponse.md)\>

Get X activity subscriptions
Get a list of active subscriptions for XAA

#### Returns

`Promise`\<[`ActivitySubscriptionGetResponse`](../interfaces/Schemas.ActivitySubscriptionGetResponse.md)\>

Promise resolving to the API response

#### Defined in

[activity/client.ts:246](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/activity/client.ts#L246)

___

### createSubscription

▸ **createSubscription**(`options?`): `Promise`\<[`ActivitySubscriptionCreateResponse`](../interfaces/Schemas.ActivitySubscriptionCreateResponse.md)\>

Create X activity subscription
Creates a subscription for an X activity event

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateSubscriptionOptions` |

#### Returns

`Promise`\<[`ActivitySubscriptionCreateResponse`](../interfaces/Schemas.ActivitySubscriptionCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[activity/client.ts:278](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/activity/client.ts#L278)
