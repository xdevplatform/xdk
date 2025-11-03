[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / CreateNoteRequest

# Interface: CreateNoteRequest

[Schemas](../modules/Schemas.md).CreateNoteRequest

## Table of contents

### Properties

- [info](Schemas.CreateNoteRequest.md#info)
- [postId](Schemas.CreateNoteRequest.md#postid)
- [testMode](Schemas.CreateNoteRequest.md#testmode)

## Properties

### info

• **info**: [`NoteInfo`](Schemas.NoteInfo.md)

#### Defined in

[schemas.ts:420](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L420)

___

### postId

• **postId**: `string`

#### Defined in

[schemas.ts:421](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L421)

___

### testMode

• **testMode**: `boolean`

If true, the note being submitted is only for testing the capability of the bot, and won't be publicly visible. If false, the note being submitted will be a new proposed note on the product.

#### Defined in

[schemas.ts:422](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L422)
