[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / CreateComplianceJobRequest

# Interface: CreateComplianceJobRequest

[Schemas](../modules/Schemas.md).CreateComplianceJobRequest

## Table of contents

### Properties

- [name](Schemas.CreateComplianceJobRequest.md#name)
- [resumable](Schemas.CreateComplianceJobRequest.md#resumable)
- [type](Schemas.CreateComplianceJobRequest.md#type)

## Properties

### name

• `Optional` **name**: `string`

#### Defined in

[schemas.ts:375](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L375)

___

### resumable

• `Optional` **resumable**: `boolean`

If true, this endpoint will return a pre-signed URL with resumable uploads enabled.

#### Defined in

[schemas.ts:376](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L376)

___

### type

• **type**: ``"tweets"`` \| ``"users"``

Type of compliance job to list.

#### Defined in

[schemas.ts:377](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L377)
