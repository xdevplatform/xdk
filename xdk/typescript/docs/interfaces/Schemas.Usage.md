[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / Usage

# Interface: Usage

[Schemas](../modules/Schemas.md).Usage

## Table of contents

### Properties

- [capResetDay](Schemas.Usage.md#capresetday)
- [dailyClientAppUsage](Schemas.Usage.md#dailyclientappusage)
- [dailyProjectUsage](Schemas.Usage.md#dailyprojectusage)
- [projectCap](Schemas.Usage.md#projectcap)
- [projectId](Schemas.Usage.md#projectid)
- [projectUsage](Schemas.Usage.md#projectusage)

## Properties

### capResetDay

• `Optional` **capResetDay**: `number`

Number of days left for the Tweet cap to reset

#### Defined in

[schemas.ts:2883](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2883)

___

### dailyClientAppUsage

• `Optional` **dailyClientAppUsage**: [`ClientAppUsage`](Schemas.ClientAppUsage.md)[]

The daily usage breakdown for each Client Application a project

#### Defined in

[schemas.ts:2884](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2884)

___

### dailyProjectUsage

• `Optional` **dailyProjectUsage**: `Record`\<`string`, `any`\>

The daily usage breakdown for a project

#### Defined in

[schemas.ts:2887](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2887)

___

### projectCap

• `Optional` **projectCap**: `number`

Total number of Posts that can be read in this project per month

#### Defined in

[schemas.ts:2891](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2891)

___

### projectId

• `Optional` **projectId**: `string`

The unique identifier for this project

#### Defined in

[schemas.ts:2892](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2892)

___

### projectUsage

• `Optional` **projectUsage**: `number`

The number of Posts read in this project

#### Defined in

[schemas.ts:2893](https://github.com/xdevplatform/xdk/blob/e7c1386f9fab2eee5b465df213d44d7bb91ff7bb/xdk/typescript/src/schemas.ts#L2893)
