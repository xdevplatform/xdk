[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / ProcessingInfo

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

[schemas.ts:2153](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2153)

___

### progressPercent

• `Optional` **progressPercent**: `number`

Percent of upload progress

#### Defined in

[schemas.ts:2154](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2154)

___

### state

• `Optional` **state**: ``"in_progress"`` \| ``"failed"`` \| ``"succeeded"`` \| ``"pending"``

State of upload

#### Defined in

[schemas.ts:2155](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L2155)
