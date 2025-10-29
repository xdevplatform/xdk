[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UsersClient

# Class: UsersClient

Client for Users operations

This client provides methods for interacting with the Users endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all Users related operations.

## Table of contents

### Constructors

- [constructor](UsersClient.md#constructor)

### Methods

- [createBookmark](UsersClient.md#createbookmark)
- [unblockDms](UsersClient.md#unblockdms)
- [getBookmarksByFolderId](UsersClient.md#getbookmarksbyfolderid)
- [unlikePost](UsersClient.md#unlikepost)
- [getPinnedLists](UsersClient.md#getpinnedlists)
- [pinList](UsersClient.md#pinlist)
- [likePost](UsersClient.md#likepost)
- [getByIds](UsersClient.md#getbyids)
- [unfollow](UsersClient.md#unfollow)
- [getByUsername](UsersClient.md#getbyusername)
- [getById](UsersClient.md#getbyid)
- [deleteBookmark](UsersClient.md#deletebookmark)
- [followList](UsersClient.md#followlist)
- [getByUsernames](UsersClient.md#getbyusernames)
- [mute](UsersClient.md#mute)
- [unpinList](UsersClient.md#unpinlist)
- [repostPost](UsersClient.md#repostpost)
- [unrepostPost](UsersClient.md#unrepostpost)
- [getMe](UsersClient.md#getme)
- [blockDms](UsersClient.md#blockdms)
- [unmute](UsersClient.md#unmute)
- [follow](UsersClient.md#follow)
- [unfollowList](UsersClient.md#unfollowlist)
- [getMentions](UsersClient.md#getmentions)
- [getBookmarks](UsersClient.md#getbookmarks)
- [getTimeline](UsersClient.md#gettimeline)
- [getOwnedLists](UsersClient.md#getownedlists)
- [getBlocking](UsersClient.md#getblocking)
- [search](UsersClient.md#search)
- [getRepostsOfMe](UsersClient.md#getrepostsofme)
- [getFollowers](UsersClient.md#getfollowers)
- [getFollowedLists](UsersClient.md#getfollowedlists)
- [getListMemberships](UsersClient.md#getlistmemberships)
- [getMuting](UsersClient.md#getmuting)
- [getBookmarkFolders](UsersClient.md#getbookmarkfolders)
- [getPosts](UsersClient.md#getposts)
- [getLikedPosts](UsersClient.md#getlikedposts)
- [getFollowing](UsersClient.md#getfollowing)

## Constructors

### constructor

• **new UsersClient**(`client`): [`UsersClient`](UsersClient.md)

Creates a new Users client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`UsersClient`](UsersClient.md)

#### Defined in

[users/client.ts:668](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L668)

## Methods

### createBookmark

▸ **createBookmark**(`id`, `body`): `Promise`\<[`UsersCreateBookmarkResponse`](../interfaces/UsersCreateBookmarkResponse.md)\>

Create Bookmark
Adds a post to the authenticated user’s bookmarks.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to add bookmarks. |
| `body` | [`UsersCreateBookmarkRequest`](../interfaces/UsersCreateBookmarkRequest.md) | Request body |

#### Returns

`Promise`\<[`UsersCreateBookmarkResponse`](../interfaces/UsersCreateBookmarkResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:686](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L686)

___

### unblockDms

▸ **unblockDms**(`id`): `Promise`\<[`UsersUnblockDmsResponse`](../interfaces/UsersUnblockDmsResponse.md)\>

Unblock DMs
Unblocks direct messages to or from a specific User by their ID for the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the target User that the authenticated user requesting to unblock dms for. |

#### Returns

`Promise`\<[`UsersUnblockDmsResponse`](../interfaces/UsersUnblockDmsResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:728](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L728)

___

### getBookmarksByFolderId

▸ **getBookmarksByFolderId**(`id`, `folderId`): `Promise`\<[`UsersGetBookmarksByFolderIdResponse`](../interfaces/UsersGetBookmarksByFolderIdResponse.md)\>

Get Bookmarks by folder ID
Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `folderId` | `string` | The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for. |

#### Returns

`Promise`\<[`UsersGetBookmarksByFolderIdResponse`](../interfaces/UsersGetBookmarksByFolderIdResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:769](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L769)

___

### unlikePost

▸ **unlikePost**(`id`, `tweetId`): `Promise`\<[`UsersUnlikePostResponse`](../interfaces/UsersUnlikePostResponse.md)\>

Unlike Post
Causes the authenticated user to Unlike a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to unlike the Post. |
| `tweetId` | `string` | The ID of the Post that the User is requesting to unlike. |

#### Returns

`Promise`\<[`UsersUnlikePostResponse`](../interfaces/UsersUnlikePostResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:815](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L815)

___

### getPinnedLists

▸ **getPinnedLists**(`id`, `options?`): `Promise`\<[`UsersGetPinnedListsResponse`](../interfaces/UsersGetPinnedListsResponse.md)\>

Get pinned Lists
Retrieves a list of Lists pinned by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | [`UsersGetPinnedListsOptions`](../interfaces/UsersGetPinnedListsOptions.md) | - |

#### Returns

`Promise`\<[`UsersGetPinnedListsResponse`](../interfaces/UsersGetPinnedListsResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:857](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L857)

___

### pinList

▸ **pinList**(`id`, `body`): `Promise`\<[`UsersPinListResponse`](../interfaces/UsersPinListResponse.md)\>

Pin List
Causes the authenticated user to pin a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that will pin the List. |
| `body` | [`UsersPinListRequest`](../interfaces/UsersPinListRequest.md) | Request body |

#### Returns

`Promise`\<[`UsersPinListResponse`](../interfaces/UsersPinListResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:919](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L919)

___

### likePost

▸ **likePost**(`id`, `options?`): `Promise`\<[`UsersLikePostResponse`](../interfaces/UsersLikePostResponse.md)\>

Like Post
Causes the authenticated user to Like a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to like the Post. |
| `options` | [`UsersLikePostOptions`](../interfaces/UsersLikePostOptions.md) | - |

#### Returns

`Promise`\<[`UsersLikePostResponse`](../interfaces/UsersLikePostResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:961](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L961)

___

### getByIds

▸ **getByIds**(`ids`, `options?`): `Promise`\<[`UsersGetByIdsResponse`](../interfaces/UsersGetByIdsResponse.md)\>

Get Users by IDs
Retrieves details of multiple Users by their IDs.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ids` | `any`[] | A list of User IDs, comma-separated. You can specify up to 100 IDs. |
| `options` | [`UsersGetByIdsOptions`](../interfaces/UsersGetByIdsOptions.md) | - |

#### Returns

`Promise`\<[`UsersGetByIdsResponse`](../interfaces/UsersGetByIdsResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1007](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1007)

___

### unfollow

▸ **unfollow**(`sourceUserId`, `targetUserId`): `Promise`\<[`UsersUnfollowResponse`](../interfaces/UsersUnfollowResponse.md)\>

Unfollow User
Causes the authenticated user to unfollow a specific user by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `sourceUserId` | `string` | The ID of the authenticated source User that is requesting to unfollow the target User. |
| `targetUserId` | `string` | The ID of the User that the source User is requesting to unfollow. |

#### Returns

`Promise`\<[`UsersUnfollowResponse`](../interfaces/UsersUnfollowResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1073](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1073)

___

### getByUsername

▸ **getByUsername**(`username`, `options?`): `Promise`\<[`UsersGetByUsernameResponse`](../interfaces/UsersGetByUsernameResponse.md)\>

Get User by username
Retrieves details of a specific User by their username.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `username` | `string` | A username. |
| `options` | [`UsersGetByUsernameOptions`](../interfaces/UsersGetByUsernameOptions.md) | - |

#### Returns

`Promise`\<[`UsersGetByUsernameResponse`](../interfaces/UsersGetByUsernameResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1121](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1121)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`UsersGetByIdResponse`](../interfaces/UsersGetByIdResponse.md)\>

Get User by ID
Retrieves details of a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetByIdOptions`](../interfaces/UsersGetByIdOptions.md) | - |

#### Returns

`Promise`\<[`UsersGetByIdResponse`](../interfaces/UsersGetByIdResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1181](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1181)

___

### deleteBookmark

▸ **deleteBookmark**(`id`, `tweetId`): `Promise`\<[`UsersDeleteBookmarkResponse`](../interfaces/UsersDeleteBookmarkResponse.md)\>

Delete Bookmark
Removes a Post from the authenticated user’s Bookmarks by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User whose bookmark is to be removed. |
| `tweetId` | `string` | The ID of the Post that the source User is removing from bookmarks. |

#### Returns

`Promise`\<[`UsersDeleteBookmarkResponse`](../interfaces/UsersDeleteBookmarkResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1245](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1245)

___

### followList

▸ **followList**(`id`, `options?`): `Promise`\<[`UsersFollowListResponse`](../interfaces/UsersFollowListResponse.md)\>

Follow List
Causes the authenticated user to follow a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that will follow the List. |
| `options` | [`UsersFollowListOptions`](../interfaces/UsersFollowListOptions.md) | - |

#### Returns

`Promise`\<[`UsersFollowListResponse`](../interfaces/UsersFollowListResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1287](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1287)

___

### getByUsernames

▸ **getByUsernames**(`usernames`, `options?`): `Promise`\<[`UsersGetByUsernamesResponse`](../interfaces/UsersGetByUsernamesResponse.md)\>

Get Users by usernames
Retrieves details of multiple Users by their usernames.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `usernames` | `any`[] | A list of usernames, comma-separated. |
| `options` | [`UsersGetByUsernamesOptions`](../interfaces/UsersGetByUsernamesOptions.md) | - |

#### Returns

`Promise`\<[`UsersGetByUsernamesResponse`](../interfaces/UsersGetByUsernamesResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1333](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1333)

___

### mute

▸ **mute**(`id`, `options?`): `Promise`\<[`UsersMuteResponse`](../interfaces/UsersMuteResponse.md)\>

Mute User
Causes the authenticated user to mute a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to mute the target User. |
| `options` | [`UsersMuteOptions`](../interfaces/UsersMuteOptions.md) | - |

#### Returns

`Promise`\<[`UsersMuteResponse`](../interfaces/UsersMuteResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1395](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1395)

___

### unpinList

▸ **unpinList**(`id`, `listId`): `Promise`\<[`UsersUnpinListResponse`](../interfaces/UsersUnpinListResponse.md)\>

Unpin List
Causes the authenticated user to unpin a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `listId` | `string` | The ID of the List to unpin. |

#### Returns

`Promise`\<[`UsersUnpinListResponse`](../interfaces/UsersUnpinListResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1445](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1445)

___

### repostPost

▸ **repostPost**(`id`, `options?`): `Promise`\<[`UsersRepostPostResponse`](../interfaces/UsersRepostPostResponse.md)\>

Repost Post
Causes the authenticated user to repost a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to repost the Post. |
| `options` | [`UsersRepostPostOptions`](../interfaces/UsersRepostPostOptions.md) | - |

#### Returns

`Promise`\<[`UsersRepostPostResponse`](../interfaces/UsersRepostPostResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1484](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1484)

___

### unrepostPost

▸ **unrepostPost**(`id`, `sourceTweetId`): `Promise`\<[`UsersUnrepostPostResponse`](../interfaces/UsersUnrepostPostResponse.md)\>

Unrepost Post
Causes the authenticated user to unrepost a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to repost the Post. |
| `sourceTweetId` | `string` | The ID of the Post that the User is requesting to unretweet. |

#### Returns

`Promise`\<[`UsersUnrepostPostResponse`](../interfaces/UsersUnrepostPostResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1534](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1534)

___

### getMe

▸ **getMe**(`options?`): `Promise`\<[`UsersGetMeResponse`](../interfaces/UsersGetMeResponse.md)\>

Get my User
Retrieves details of the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | [`UsersGetMeOptions`](../interfaces/UsersGetMeOptions.md) |

#### Returns

`Promise`\<[`UsersGetMeResponse`](../interfaces/UsersGetMeResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1575](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1575)

___

### blockDms

▸ **blockDms**(`id`): `Promise`\<[`UsersBlockDmsResponse`](../interfaces/UsersBlockDmsResponse.md)\>

Block DMs
Blocks direct messages to or from a specific User by their ID for the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the target User that the authenticated user requesting to block dms for. |

#### Returns

`Promise`\<[`UsersBlockDmsResponse`](../interfaces/UsersBlockDmsResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1630](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1630)

___

### unmute

▸ **unmute**(`sourceUserId`, `targetUserId`): `Promise`\<[`UsersUnmuteResponse`](../interfaces/UsersUnmuteResponse.md)\>

Unmute User
Causes the authenticated user to unmute a specific user by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `sourceUserId` | `string` | The ID of the authenticated source User that is requesting to unmute the target User. |
| `targetUserId` | `string` | The ID of the User that the source User is requesting to unmute. |

#### Returns

`Promise`\<[`UsersUnmuteResponse`](../interfaces/UsersUnmuteResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1671](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1671)

___

### follow

▸ **follow**(`id`, `options?`): `Promise`\<[`UsersFollowResponse`](../interfaces/UsersFollowResponse.md)\>

Follow User
Causes the authenticated user to follow a specific user by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to follow the target User. |
| `options` | [`UsersFollowOptions`](../interfaces/UsersFollowOptions.md) | - |

#### Returns

`Promise`\<[`UsersFollowResponse`](../interfaces/UsersFollowResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1719](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1719)

___

### unfollowList

▸ **unfollowList**(`id`, `listId`): `Promise`\<[`UsersUnfollowListResponse`](../interfaces/UsersUnfollowListResponse.md)\>

Unfollow List
Causes the authenticated user to unfollow a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that will unfollow the List. |
| `listId` | `string` | The ID of the List to unfollow. |

#### Returns

`Promise`\<[`UsersUnfollowListResponse`](../interfaces/UsersUnfollowListResponse.md)\>

Promise with the API response

#### Defined in

[users/client.ts:1769](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1769)

___

### getMentions

▸ **getMentions**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get mentions
Retrieves a list of Posts that mention a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetMentionsOptions`](../interfaces/UsersGetMentionsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:1811](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1811)

___

### getBookmarks

▸ **getBookmarks**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get Bookmarks
Retrieves a list of Posts bookmarked by the authenticated user.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | [`UsersGetBookmarksOptions`](../interfaces/UsersGetBookmarksOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:1948](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L1948)

___

### getTimeline

▸ **getTimeline**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get Timeline
Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User to list Reverse Chronological Timeline Posts of. |
| `options` | [`UsersGetTimelineOptions`](../interfaces/UsersGetTimelineOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2061](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2061)

___

### getOwnedLists

▸ **getOwnedLists**(`id`, `options?`): `Promise`\<[`UserPaginator`](UserPaginator.md)\>

Get owned Lists
Retrieves a list of Lists owned by a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetOwnedListsOptions`](../interfaces/UsersGetOwnedListsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`UserPaginator`](UserPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2204](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2204)

___

### getBlocking

▸ **getBlocking**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get blocking
Retrieves a list of Users blocked by the specified User ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | [`UsersGetBlockingOptions`](../interfaces/UsersGetBlockingOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2299](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2299)

___

### search

▸ **search**(`query`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Search Users
Retrieves a list of Users matching a search query.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `string` | TThe the query string by which to query for users. |
| `options` | [`UsersSearchOptions`](../interfaces/UsersSearchOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2394](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2394)

___

### getRepostsOfMe

▸ **getRepostsOfMe**(`options?`): `Promise`\<[`PostPaginator`](PostPaginator.md)\>

Get Reposts of me
Retrieves a list of Posts that repost content from the authenticated user.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options` | [`UsersGetRepostsOfMeOptions`](../interfaces/UsersGetRepostsOfMeOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`PostPaginator`](PostPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2487](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2487)

___

### getFollowers

▸ **getFollowers**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get followers
Retrieves a list of Users who follow a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetFollowersOptions`](../interfaces/UsersGetFollowersOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2597](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2597)

___

### getFollowedLists

▸ **getFollowedLists**(`id`, `options?`): `Promise`\<[`UserPaginator`](UserPaginator.md)\>

Get followed Lists
Retrieves a list of Lists followed by a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetFollowedListsOptions`](../interfaces/UsersGetFollowedListsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`UserPaginator`](UserPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2692](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2692)

___

### getListMemberships

▸ **getListMemberships**(`id`, `options?`): `Promise`\<[`UserPaginator`](UserPaginator.md)\>

Get List memberships
Retrieves a list of Lists that a specific User is a member of by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetListMembershipsOptions`](../interfaces/UsersGetListMembershipsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`UserPaginator`](UserPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2787](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2787)

___

### getMuting

▸ **getMuting**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get muting
Retrieves a list of Users muted by the authenticated user.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | [`UsersGetMutingOptions`](../interfaces/UsersGetMutingOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2884](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2884)

___

### getBookmarkFolders

▸ **getBookmarkFolders**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get Bookmark folders
Retrieves a list of Bookmark folders created by the authenticated user.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | [`UsersGetBookmarkFoldersOptions`](../interfaces/UsersGetBookmarkFoldersOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:2979](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L2979)

___

### getPosts

▸ **getPosts**(`id`, `options?`): `Promise`\<[`PostPaginator`](PostPaginator.md)\>

Get Posts
Retrieves a list of posts authored by a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetPostsOptions`](../interfaces/UsersGetPostsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`PostPaginator`](PostPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:3058](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L3058)

___

### getLikedPosts

▸ **getLikedPosts**(`id`, `options?`): `Promise`\<[`PostPaginator`](PostPaginator.md)\>

Get liked Posts
Retrieves a list of Posts liked by a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetLikedPostsOptions`](../interfaces/UsersGetLikedPostsOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`PostPaginator`](PostPaginator.md)\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:3201](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L3201)

___

### getFollowing

▸ **getFollowing**(`id`, `options?`): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get following
Retrieves a list of Users followed by a specific User by their ID.
Returns a paginator for automatic pagination through all results.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | [`UsersGetFollowingOptions`](../interfaces/UsersGetFollowingOptions.md) | Options for the paginated request |

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

A paginator instance for iterating through all results

#### Defined in

[users/client.ts:3314](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/users/client.ts#L3314)
