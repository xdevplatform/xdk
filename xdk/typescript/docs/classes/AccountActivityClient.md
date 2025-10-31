[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / AccountActivityClient

# Class: AccountActivityClient

Client for account activity operations

This client provides methods for interacting with the account activity endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all account activity related operations.

## Table of contents

### Constructors

- [constructor](AccountActivityClient.md#constructor)

### Methods

- [validateSubscription](AccountActivityClient.md#validatesubscription)
- [createSubscription](AccountActivityClient.md#createsubscription)
- [getSubscriptions](AccountActivityClient.md#getsubscriptions)
- [deleteSubscription](AccountActivityClient.md#deletesubscription)
- [getSubscriptionCount](AccountActivityClient.md#getsubscriptioncount)
- [createReplayJob](AccountActivityClient.md#createreplayjob)

## Constructors

### constructor

• **new AccountActivityClient**(`client`): [`AccountActivityClient`](AccountActivityClient.md)

Creates a new account activity client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`AccountActivityClient`](AccountActivityClient.md)

#### Defined in

[account_activity/client.ts:54](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L54)

## Methods

### validateSubscription

▸ **validateSubscription**(): `Promise`\<`any`\>

Validate subscription
Checks a user’s Account Activity subscription for a given webhook.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[account_activity/client.ts:68](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L68)

___

### createSubscription

▸ **createSubscription**(`options?`): `Promise`\<`any`\>

Create subscription
Creates an Account Activity subscription for the user and the given webhook.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `CreateSubscriptionOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[account_activity/client.ts:101](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L101)

___

### getSubscriptions

▸ **getSubscriptions**(): `Promise`\<`any`\>

Get subscriptions
Retrieves a list of all active subscriptions for a given webhook.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[account_activity/client.ts:142](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L142)

___

### deleteSubscription

▸ **deleteSubscription**(): `Promise`\<`any`\>

Delete subscription
Deletes an Account Activity subscription for the given webhook and user ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[account_activity/client.ts:178](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L178)

___

### getSubscriptionCount

▸ **getSubscriptionCount**(): `Promise`\<`any`\>

Get subscription count
Retrieves a count of currently active Account Activity subscriptions.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[account_activity/client.ts:210](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L210)

___

### createReplayJob

▸ **createReplayJob**(): `Promise`\<`any`\>

Create replay job
Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[account_activity/client.ts:247](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/account_activity/client.ts#L247)
