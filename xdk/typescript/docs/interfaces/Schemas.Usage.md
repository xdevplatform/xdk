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

[schemas.ts:2881](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2881)

___

### dailyClientAppUsage

• `Optional` **dailyClientAppUsage**: [`ClientAppUsage`](Schemas.ClientAppUsage.md)[]

The daily usage breakdown for each Client Application a project

#### Defined in

[schemas.ts:2882](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2882)

___

### dailyProjectUsage

• `Optional` **dailyProjectUsage**: `Record`\<`string`, `any`\>

The daily usage breakdown for a project

#### Defined in

[schemas.ts:2885](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2885)

___

### projectCap

• `Optional` **projectCap**: `number`

Total number of Posts that can be read in this project per month

#### Defined in

[schemas.ts:2889](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2889)

___

### projectId

• `Optional` **projectId**: `string`

The unique identifier for this project

#### Defined in

[schemas.ts:2890](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2890)

___

### projectUsage

• `Optional` **projectUsage**: `number`

The number of Posts read in this project

#### Defined in

[schemas.ts:2891](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2891)
