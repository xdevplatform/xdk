[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / Tweet

# Interface: Tweet

[Schemas](../modules/Schemas.md).Tweet

## Table of contents

### Properties

- [attachments](Schemas.Tweet.md#attachments)
- [authorId](Schemas.Tweet.md#authorid)
- [communityId](Schemas.Tweet.md#communityid)
- [contextAnnotations](Schemas.Tweet.md#contextannotations)
- [conversationId](Schemas.Tweet.md#conversationid)
- [createdAt](Schemas.Tweet.md#createdat)
- [displayTextRange](Schemas.Tweet.md#displaytextrange)
- [editControls](Schemas.Tweet.md#editcontrols)
- [editHistoryTweetIds](Schemas.Tweet.md#edithistorytweetids)
- [entities](Schemas.Tweet.md#entities)
- [geo](Schemas.Tweet.md#geo)
- [id](Schemas.Tweet.md#id)
- [inReplyToUserId](Schemas.Tweet.md#inreplytouserid)
- [lang](Schemas.Tweet.md#lang)
- [nonPublicMetrics](Schemas.Tweet.md#nonpublicmetrics)
- [noteTweet](Schemas.Tweet.md#notetweet)
- [organicMetrics](Schemas.Tweet.md#organicmetrics)
- [possiblySensitive](Schemas.Tweet.md#possiblysensitive)
- [promotedMetrics](Schemas.Tweet.md#promotedmetrics)
- [publicMetrics](Schemas.Tweet.md#publicmetrics)
- [referencedTweets](Schemas.Tweet.md#referencedtweets)
- [replySettings](Schemas.Tweet.md#replysettings)
- [scopes](Schemas.Tweet.md#scopes)
- [source](Schemas.Tweet.md#source)
- [suggestedSourceLinks](Schemas.Tweet.md#suggestedsourcelinks)
- [text](Schemas.Tweet.md#text)
- [username](Schemas.Tweet.md#username)
- [withheld](Schemas.Tweet.md#withheld)

## Properties

### attachments

• `Optional` **attachments**: `Record`\<`string`, `any`\>

Specifies the type of attachments (if any) present in this Tweet.

#### Defined in

[schemas.ts:2531](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2531)

___

### authorId

• `Optional` **authorId**: `string`

#### Defined in

[schemas.ts:2535](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2535)

___

### communityId

• `Optional` **communityId**: `string`

#### Defined in

[schemas.ts:2536](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2536)

___

### contextAnnotations

• `Optional` **contextAnnotations**: [`ContextAnnotation`](Schemas.ContextAnnotation.md)[]

none

#### Defined in

[schemas.ts:2537](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2537)

___

### conversationId

• `Optional` **conversationId**: `string`

#### Defined in

[schemas.ts:2538](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2538)

___

### createdAt

• `Optional` **createdAt**: `string`

Creation time of the Tweet.

#### Defined in

[schemas.ts:2539](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2539)

___

### displayTextRange

• `Optional` **displayTextRange**: [`DisplayTextRange`](../modules/Schemas.md#displaytextrange)

#### Defined in

[schemas.ts:2540](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2540)

___

### editControls

• `Optional` **editControls**: `Record`\<`string`, `any`\>

none

#### Defined in

[schemas.ts:2541](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2541)

___

### editHistoryTweetIds

• `Optional` **editHistoryTweetIds**: `string`[]

A list of Tweet Ids in this Tweet chain.

#### Defined in

[schemas.ts:2542](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2542)

___

### entities

• `Optional` **entities**: [`FullTextEntities`](Schemas.FullTextEntities.md)

#### Defined in

[schemas.ts:2545](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2545)

___

### geo

• `Optional` **geo**: `Record`\<`string`, `any`\>

The location tagged on the Tweet, if the user provided one.

#### Defined in

[schemas.ts:2546](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2546)

___

### id

• `Optional` **id**: `string`

#### Defined in

[schemas.ts:2550](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2550)

___

### inReplyToUserId

• `Optional` **inReplyToUserId**: `string`

#### Defined in

[schemas.ts:2551](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2551)

___

### lang

• `Optional` **lang**: `string`

Language of the Tweet, if detected by X. Returned as a BCP47 language tag.

#### Defined in

[schemas.ts:2552](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2552)

___

### nonPublicMetrics

• `Optional` **nonPublicMetrics**: `Record`\<`string`, `any`\>

Nonpublic engagement metrics for the Tweet at the time of the request.

#### Defined in

[schemas.ts:2553](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2553)

___

### noteTweet

• `Optional` **noteTweet**: `Record`\<`string`, `any`\>

The full-content of the Tweet, including text beyond 280 characters.

#### Defined in

[schemas.ts:2557](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2557)

___

### organicMetrics

• `Optional` **organicMetrics**: `Record`\<`string`, `any`\>

Organic nonpublic engagement metrics for the Tweet at the time of the request.

#### Defined in

[schemas.ts:2561](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2561)

___

### possiblySensitive

• `Optional` **possiblySensitive**: `boolean`

Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences.

#### Defined in

[schemas.ts:2565](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2565)

___

### promotedMetrics

• `Optional` **promotedMetrics**: `Record`\<`string`, `any`\>

Promoted nonpublic engagement metrics for the Tweet at the time of the request.

#### Defined in

[schemas.ts:2566](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2566)

___

### publicMetrics

• `Optional` **publicMetrics**: `Record`\<`string`, `any`\>

Engagement metrics for the Tweet at the time of the request.

#### Defined in

[schemas.ts:2570](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2570)

___

### referencedTweets

• `Optional` **referencedTweets**: `Record`\<`string`, `any`\>[]

A list of Posts this Tweet refers to. For example, if the parent Tweet is a Retweet, a Quoted Tweet or a Reply, it will include the related Tweet referenced to by its parent.

#### Defined in

[schemas.ts:2574](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2574)

___

### replySettings

• `Optional` **replySettings**: [`ReplySettingsWithVerifiedUsers`](../modules/Schemas.md#replysettingswithverifiedusers)

#### Defined in

[schemas.ts:2577](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2577)

___

### scopes

• `Optional` **scopes**: `Record`\<`string`, `any`\>

The scopes for this tweet

#### Defined in

[schemas.ts:2578](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2578)

___

### source

• `Optional` **source**: `string`

This is deprecated.

#### Defined in

[schemas.ts:2579](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2579)

___

### suggestedSourceLinks

• `Optional` **suggestedSourceLinks**: `any`[]

none

#### Defined in

[schemas.ts:2580](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2580)

___

### text

• `Optional` **text**: `string`

#### Defined in

[schemas.ts:2581](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2581)

___

### username

• `Optional` **username**: `string`

#### Defined in

[schemas.ts:2582](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2582)

___

### withheld

• `Optional` **withheld**: [`TweetWithheld`](Schemas.TweetWithheld.md)

#### Defined in

[schemas.ts:2583](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/schemas.ts#L2583)
