[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ComplianceClient

# Class: ComplianceClient

Client for compliance operations

This client provides methods for interacting with the compliance endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all compliance related operations.

## Table of contents

### Constructors

- [constructor](ComplianceClient.md#constructor)

### Methods

- [getJobs](ComplianceClient.md#getjobs)
- [createJobs](ComplianceClient.md#createjobs)
- [getJobsById](ComplianceClient.md#getjobsbyid)

## Constructors

### constructor

• **new ComplianceClient**(`client`): [`ComplianceClient`](ComplianceClient.md)

Creates a new compliance client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`ComplianceClient`](ComplianceClient.md)

#### Defined in

[compliance/client.ts:48](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/compliance/client.ts#L48)

## Methods

### getJobs

▸ **getJobs**(`options?`): `Promise`\<`any`\>

Get Compliance Jobs
Retrieves a list of Compliance Jobs filtered by job type and optional status.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetJobsOptions` |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[compliance/client.ts:62](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/compliance/client.ts#L62)

___

### createJobs

▸ **createJobs**(`body`): `Promise`\<`any`\>

Create Compliance Job
Creates a new Compliance Job for the specified job type.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `body` | `any` | Request body |

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[compliance/client.ts:95](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/compliance/client.ts#L95)

___

### getJobsById

▸ **getJobsById**(): `Promise`\<`any`\>

Get Compliance Job by ID
Retrieves details of a specific Compliance Job by its ID.

#### Returns

`Promise`\<`any`\>

Promise with the API response

#### Defined in

[compliance/client.ts:130](https://github.com/xdevplatform/xdk/blob/a701cd88782eaa1dd81e314e3b527b2c3f9e2f7b/xdk/typescript/src/compliance/client.ts#L130)
