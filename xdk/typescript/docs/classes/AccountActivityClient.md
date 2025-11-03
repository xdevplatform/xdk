[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / AccountActivityClient

# Class: AccountActivityClient

Client for account activity operations

This client provides methods for interacting with the account activity endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all account activity related operations.

## Table of contents

### Constructors

- [constructor](AccountActivityClient.md#constructor)

### Methods

- [getSubscriptions](AccountActivityClient.md#getsubscriptions)
- [createReplayJob](AccountActivityClient.md#createreplayjob)
- [validateSubscription](AccountActivityClient.md#validatesubscription)
- [createSubscription](AccountActivityClient.md#createsubscription)
- [deleteSubscription](AccountActivityClient.md#deletesubscription)
- [getSubscriptionCount](AccountActivityClient.md#getsubscriptioncount)

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

[account_activity/client.ts:54](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L54)

## Methods

### getSubscriptions

▸ **getSubscriptions**(`webhookId`): `Promise`\<[`SubscriptionsListGetResponse`](../interfaces/Schemas.SubscriptionsListGetResponse.md)\>

Get subscriptions
Retrieves a list of all active subscriptions for a given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to pull subscriptions for. |

#### Returns

`Promise`\<[`SubscriptionsListGetResponse`](../interfaces/Schemas.SubscriptionsListGetResponse.md)\>

Promise resolving to the API response

#### Defined in

[account_activity/client.ts:71](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L71)

___

### createReplayJob

▸ **createReplayJob**(`webhookId`, `fromDate`, `toDate`): `Promise`\<[`ReplayJobCreateResponse`](../interfaces/Schemas.ReplayJobCreateResponse.md)\>

Create replay job
Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The unique identifier for the webhook configuration. |
| `fromDate` | `string` | The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format. |
| `toDate` | `string` | The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format. |

#### Returns

`Promise`\<[`ReplayJobCreateResponse`](../interfaces/Schemas.ReplayJobCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[account_activity/client.ts:118](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L118)

___

### validateSubscription

▸ **validateSubscription**(`webhookId`): `Promise`\<[`SubscriptionsGetResponse`](../interfaces/Schemas.SubscriptionsGetResponse.md)\>

Validate subscription
Checks a user’s Account Activity subscription for a given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to check subscription against. |

#### Returns

`Promise`\<[`SubscriptionsGetResponse`](../interfaces/Schemas.SubscriptionsGetResponse.md)\>

Promise resolving to the API response

#### Defined in

[account_activity/client.ts:169](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L169)

___

### createSubscription

▸ **createSubscription**(`webhookId`, `options?`): `Promise`\<[`SubscriptionsCreateResponse`](../interfaces/Schemas.SubscriptionsCreateResponse.md)\>

Create subscription
Creates an Account Activity subscription for the user and the given webhook.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to check subscription against. |
| `options` | `CreateSubscriptionOptions` | - |

#### Returns

`Promise`\<[`SubscriptionsCreateResponse`](../interfaces/Schemas.SubscriptionsCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[account_activity/client.ts:209](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L209)

___

### deleteSubscription

▸ **deleteSubscription**(`webhookId`, `userId`): `Promise`\<[`SubscriptionsDeleteResponse`](../interfaces/Schemas.SubscriptionsDeleteResponse.md)\>

Delete subscription
Deletes an Account Activity subscription for the given webhook and user ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `webhookId` | `string` | The webhook ID to check subscription against. |
| `userId` | `string` | User ID to unsubscribe from. |

#### Returns

`Promise`\<[`SubscriptionsDeleteResponse`](../interfaces/Schemas.SubscriptionsDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[account_activity/client.ts:261](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L261)

___

### getSubscriptionCount

▸ **getSubscriptionCount**(): `Promise`\<[`SubscriptionsCountGetResponse`](../interfaces/Schemas.SubscriptionsCountGetResponse.md)\>

Get subscription count
Retrieves a count of currently active Account Activity subscriptions.

#### Returns

`Promise`\<[`SubscriptionsCountGetResponse`](../interfaces/Schemas.SubscriptionsCountGetResponse.md)\>

Promise resolving to the API response

#### Defined in

[account_activity/client.ts:301](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/account_activity/client.ts#L301)
