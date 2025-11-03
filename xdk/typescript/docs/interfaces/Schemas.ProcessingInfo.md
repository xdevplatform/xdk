[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / ProcessingInfo

# Interface: ProcessingInfo

[Schemas](../modules/Schemas.md).ProcessingInfo

## Table of contents

### Properties

- [checkAfterSecs](Schemas.ProcessingInfo.md#checkaftersecs)
- [progressPercent](Schemas.ProcessingInfo.md#progresspercent)
- [state](Schemas.ProcessingInfo.md#state)

## Properties

### checkAfterSecs

• `Optional` **checkAfterSecs**: `number`

Number of seconds to check again for status

#### Defined in

[schemas.ts:2155](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2155)

___

### progressPercent

• `Optional` **progressPercent**: `number`

Percent of upload progress

#### Defined in

[schemas.ts:2156](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2156)

___

### state

• `Optional` **state**: ``"in_progress"`` \| ``"failed"`` \| ``"succeeded"`` \| ``"pending"``

State of upload

#### Defined in

[schemas.ts:2157](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/schemas.ts#L2157)
