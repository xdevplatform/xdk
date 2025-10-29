[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / ComplianceCreateJobsRequest

# Interface: ComplianceCreateJobsRequest

Request body for createJobs
A request to create a new batch compliance job.

## Table of contents

### Properties

- [name](ComplianceCreateJobsRequest.md#name)
- [resumable](ComplianceCreateJobsRequest.md#resumable)
- [type](ComplianceCreateJobsRequest.md#type)

## Properties

### name

• `Optional` **name**: `string`

User-provided name for a compliance job.

#### Defined in

[compliance/models.ts:20](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/compliance/models.ts#L20)

___

### resumable

• `Optional` **resumable**: `boolean`

If true, this endpoint will return a pre-signed URL with resumable uploads enabled.

#### Defined in

[compliance/models.ts:22](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/compliance/models.ts#L22)

___

### type

• `Optional` **type**: `string`

Type of compliance job to list.

#### Defined in

[compliance/models.ts:24](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/compliance/models.ts#L24)
