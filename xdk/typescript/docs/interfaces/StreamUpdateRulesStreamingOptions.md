[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / StreamUpdateRulesStreamingOptions

# Interface: StreamUpdateRulesStreamingOptions

Options for updateRules method

## Table of contents

### Properties

- [dryRun](StreamUpdateRulesStreamingOptions.md#dryrun)
- [deleteAll](StreamUpdateRulesStreamingOptions.md#deleteall)
- [requestOptions](StreamUpdateRulesStreamingOptions.md#requestoptions)
- [headers](StreamUpdateRulesStreamingOptions.md#headers)
- [signal](StreamUpdateRulesStreamingOptions.md#signal)

## Properties

### dryRun

• `Optional` **dryRun**: `boolean`

Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.

#### Defined in

[stream/stream_client.ts:324](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L324)

___

### deleteAll

• `Optional` **deleteAll**: `boolean`

Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.

#### Defined in

[stream/stream_client.ts:327](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L327)

___

### requestOptions

• `Optional` **requestOptions**: [`RequestOptions`](RequestOptions.md)

Additional request options

#### Defined in

[stream/stream_client.ts:330](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L330)

___

### headers

• `Optional` **headers**: `Record`\<`string`, `string`\>

Additional headers

#### Defined in

[stream/stream_client.ts:332](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L332)

___

### signal

• `Optional` **signal**: `AbortSignal`

AbortSignal for cancelling the request

#### Defined in

[stream/stream_client.ts:334](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/stream/stream_client.ts#L334)
