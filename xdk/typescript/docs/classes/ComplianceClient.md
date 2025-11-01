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

[compliance/client.ts:67](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/compliance/client.ts#L67)

## Methods

### getJobs

▸ **getJobs**(`type`, `options?`): `Promise`\<[`Get2ComplianceJobsResponse`](../interfaces/Schemas.Get2ComplianceJobsResponse.md)\>

Get Compliance Jobs
Retrieves a list of Compliance Jobs filtered by job type and optional status.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `type` | `string` | Type of Compliance Job to list. |
| `options` | `GetJobsOptions` | - |

#### Returns

`Promise`\<[`Get2ComplianceJobsResponse`](../interfaces/Schemas.Get2ComplianceJobsResponse.md)\>

Promise resolving to the API response

#### Defined in

[compliance/client.ts:84](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/compliance/client.ts#L84)

___

### createJobs

▸ **createJobs**(`body`): `Promise`\<[`CreateComplianceJobResponse`](../interfaces/Schemas.CreateComplianceJobResponse.md)\>

Create Compliance Job
Creates a new Compliance Job for the specified job type.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `body` | [`CreateComplianceJobRequest`](../interfaces/Schemas.CreateComplianceJobRequest.md) | Request body |

#### Returns

`Promise`\<[`CreateComplianceJobResponse`](../interfaces/Schemas.CreateComplianceJobResponse.md)\>

Promise resolving to the API response

#### Defined in

[compliance/client.ts:140](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/compliance/client.ts#L140)

___

### getJobsById

▸ **getJobsById**(`id`, `options?`): `Promise`\<[`Get2ComplianceJobsIdResponse`](../interfaces/Schemas.Get2ComplianceJobsIdResponse.md)\>

Get Compliance Job by ID
Retrieves details of a specific Compliance Job by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the Compliance Job to retrieve. |
| `options` | `GetJobsByIdOptions` | - |

#### Returns

`Promise`\<[`Get2ComplianceJobsIdResponse`](../interfaces/Schemas.Get2ComplianceJobsIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[compliance/client.ts:178](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/compliance/client.ts#L178)
