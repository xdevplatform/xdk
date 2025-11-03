[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / User

# Interface: User

[Schemas](../modules/Schemas.md).User

## Table of contents

### Properties

- [affiliation](Schemas.User.md#affiliation)
- [connectionStatus](Schemas.User.md#connectionstatus)
- [createdAt](Schemas.User.md#createdat)
- [description](Schemas.User.md#description)
- [entities](Schemas.User.md#entities)
- [id](Schemas.User.md#id)
- [location](Schemas.User.md#location)
- [mostRecentTweetId](Schemas.User.md#mostrecenttweetid)
- [name](Schemas.User.md#name)
- [pinnedTweetId](Schemas.User.md#pinnedtweetid)
- [profileBannerUrl](Schemas.User.md#profilebannerurl)
- [profileImageUrl](Schemas.User.md#profileimageurl)
- [protected](Schemas.User.md#protected)
- [publicMetrics](Schemas.User.md#publicmetrics)
- [receivesYourDm](Schemas.User.md#receivesyourdm)
- [subscriptionType](Schemas.User.md#subscriptiontype)
- [url](Schemas.User.md#url)
- [username](Schemas.User.md#username)
- [verified](Schemas.User.md#verified)
- [verifiedType](Schemas.User.md#verifiedtype)
- [withheld](Schemas.User.md#withheld)

## Properties

### affiliation

• `Optional` **affiliation**: `Record`\<`string`, `any`\>

Metadata about a user's affiliation.

#### Defined in

[schemas.ts:2914](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2914)

___

### connectionStatus

• `Optional` **connectionStatus**: (``"following"`` \| ``"follow_request_received"`` \| ``"follow_request_sent"`` \| ``"blocking"`` \| ``"followed_by"`` \| ``"muting"``)[]

Returns detailed information about the relationship between two users.

#### Defined in

[schemas.ts:2915](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2915)

___

### createdAt

• `Optional` **createdAt**: `string`

Creation time of this User.

#### Defined in

[schemas.ts:2923](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2923)

___

### description

• `Optional` **description**: `string`

The text of this User's profile description (also known as bio), if the User provided one.

#### Defined in

[schemas.ts:2924](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2924)

___

### entities

• `Optional` **entities**: `Record`\<`string`, `any`\>

A list of metadata found in the User's profile description.

#### Defined in

[schemas.ts:2925](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2925)

___

### id

• **id**: `string`

#### Defined in

[schemas.ts:2929](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2929)

___

### location

• `Optional` **location**: `string`

The location specified in the User's profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.

#### Defined in

[schemas.ts:2930](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2930)

___

### mostRecentTweetId

• `Optional` **mostRecentTweetId**: `string`

#### Defined in

[schemas.ts:2931](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2931)

___

### name

• **name**: `string`

The friendly name of this User, as shown on their profile.

#### Defined in

[schemas.ts:2932](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2932)

___

### pinnedTweetId

• `Optional` **pinnedTweetId**: `string`

#### Defined in

[schemas.ts:2933](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2933)

___

### profileBannerUrl

• `Optional` **profileBannerUrl**: `string`

The URL to the profile banner for this User.

#### Defined in

[schemas.ts:2934](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2934)

___

### profileImageUrl

• `Optional` **profileImageUrl**: `string`

The URL to the profile image for this User.

#### Defined in

[schemas.ts:2935](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2935)

___

### protected

• `Optional` **protected**: `boolean`

Indicates if this User has chosen to protect their Posts (in other words, if this User's Posts are private).

#### Defined in

[schemas.ts:2936](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2936)

___

### publicMetrics

• `Optional` **publicMetrics**: `Record`\<`string`, `any`\>

A list of metrics for this User.

#### Defined in

[schemas.ts:2937](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2937)

___

### receivesYourDm

• `Optional` **receivesYourDm**: `boolean`

Indicates if you can send a DM to this User

#### Defined in

[schemas.ts:2938](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2938)

___

### subscriptionType

• `Optional` **subscriptionType**: ``"Basic"`` \| ``"Premium"`` \| ``"PremiumPlus"`` \| ``"None"``

The X Blue subscription type of the user, eg: Basic, Premium, PremiumPlus or None.

#### Defined in

[schemas.ts:2939](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2939)

___

### url

• `Optional` **url**: `string`

The URL specified in the User's profile.

#### Defined in

[schemas.ts:2944](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2944)

___

### username

• **username**: `string`

#### Defined in

[schemas.ts:2945](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2945)

___

### verified

• `Optional` **verified**: `boolean`

Indicate if this User is a verified X User.

#### Defined in

[schemas.ts:2946](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2946)

___

### verifiedType

• `Optional` **verifiedType**: ``"blue"`` \| ``"government"`` \| ``"business"`` \| ``"none"``

The X Blue verified type of the user, eg: blue, government, business or none.

#### Defined in

[schemas.ts:2947](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2947)

___

### withheld

• `Optional` **withheld**: [`UserWithheld`](Schemas.UserWithheld.md)

#### Defined in

[schemas.ts:2952](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2952)
