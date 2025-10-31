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

[activity/client.ts:77](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/activity/client.ts#L77)

## Methods

### updateSubscription

▸ **updateSubscription**(`options?`): `Promise`\<`any`\>

Update X activity subscription
Updates a subscription for an X activity event

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `UpdateSubscriptionOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[activity/client.ts:91](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/activity/client.ts#L91)

___

### deleteSubscription

▸ **deleteSubscription**(): `Promise`\<`any`\>

Deletes X activity subscription
Deletes a subscription for an X activity event

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[activity/client.ts:132](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/activity/client.ts#L132)

___

### stream

▸ **stream**(`options?`): `Promise`\<`any`\>

Activity Stream
Stream of X Activities

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `StreamOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[activity/client.ts:163](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/activity/client.ts#L163)

___

### getSubscriptions

▸ **getSubscriptions**(): `Promise`\<`any`\>

Get X activity subscriptions
Get a list of active subscriptions for XAA

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[activity/client.ts:194](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/activity/client.ts#L194)

___

### createSubscription

▸ **createSubscription**(`options?`): `Promise`\<`any`\>

Create X activity subscription
Creates a subscription for an X activity event

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateSubscriptionOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[activity/client.ts:225](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/activity/client.ts#L225)
