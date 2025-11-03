[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / TweetCreateRequest

# Interface: TweetCreateRequest

[Schemas](../modules/Schemas.md).TweetCreateRequest

## Table of contents

### Properties

- [cardUri](Schemas.TweetCreateRequest.md#carduri)
- [communityId](Schemas.TweetCreateRequest.md#communityid)
- [directMessageDeepLink](Schemas.TweetCreateRequest.md#directmessagedeeplink)
- [editOptions](Schemas.TweetCreateRequest.md#editoptions)
- [forSuperFollowersOnly](Schemas.TweetCreateRequest.md#forsuperfollowersonly)
- [geo](Schemas.TweetCreateRequest.md#geo)
- [media](Schemas.TweetCreateRequest.md#media)
- [nullcast](Schemas.TweetCreateRequest.md#nullcast)
- [poll](Schemas.TweetCreateRequest.md#poll)
- [quoteTweetId](Schemas.TweetCreateRequest.md#quotetweetid)
- [reply](Schemas.TweetCreateRequest.md#reply)
- [replySettings](Schemas.TweetCreateRequest.md#replysettings)
- [shareWithFollowers](Schemas.TweetCreateRequest.md#sharewithfollowers)
- [text](Schemas.TweetCreateRequest.md#text)

## Properties

### cardUri

• `Optional` **cardUri**: `string`

Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.

#### Defined in

[schemas.ts:2616](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2616)

___

### communityId

• `Optional` **communityId**: `string`

#### Defined in

[schemas.ts:2617](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2617)

___

### directMessageDeepLink

• `Optional` **directMessageDeepLink**: `string`

Link to take the conversation from the public timeline to a private Direct Message.

#### Defined in

[schemas.ts:2618](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2618)

___

### editOptions

• `Optional` **editOptions**: `Record`\<`string`, `any`\>

Options for editing an existing Post. When provided, this request will edit the specified Post instead of creating a new one.

#### Defined in

[schemas.ts:2619](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2619)

___

### forSuperFollowersOnly

• `Optional` **forSuperFollowersOnly**: `boolean`

Exclusive Tweet for super followers.

#### Defined in

[schemas.ts:2623](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2623)

___

### geo

• `Optional` **geo**: `Record`\<`string`, `any`\>

Place ID being attached to the Tweet for geo location.

#### Defined in

[schemas.ts:2624](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2624)

___

### media

• `Optional` **media**: `Record`\<`string`, `any`\>

Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.

#### Defined in

[schemas.ts:2628](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2628)

___

### nullcast

• `Optional` **nullcast**: `boolean`

Nullcasted (promoted-only) Posts do not appear in the public timeline and are not served to followers.

#### Defined in

[schemas.ts:2632](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2632)

___

### poll

• `Optional` **poll**: `Record`\<`string`, `any`\>

Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.

#### Defined in

[schemas.ts:2633](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2633)

___

### quoteTweetId

• `Optional` **quoteTweetId**: `string`

#### Defined in

[schemas.ts:2637](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2637)

___

### reply

• `Optional` **reply**: `Record`\<`string`, `any`\>

Tweet information of the Tweet being replied to.

#### Defined in

[schemas.ts:2638](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2638)

___

### replySettings

• `Optional` **replySettings**: ``"mentionedUsers"`` \| ``"following"`` \| ``"subscribers"`` \| ``"verified"``

Settings to indicate who can reply to the Tweet.

#### Defined in

[schemas.ts:2642](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2642)

___

### shareWithFollowers

• `Optional` **shareWithFollowers**: `boolean`

Share community post with followers too.

#### Defined in

[schemas.ts:2647](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2647)

___

### text

• `Optional` **text**: `string`

#### Defined in

[schemas.ts:2648](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2648)
