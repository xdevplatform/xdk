[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UsersClient

# Class: UsersClient

Client for users operations

This client provides methods for interacting with the users endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all users related operations.

## Table of contents

### Constructors

- [constructor](UsersClient.md#constructor)

### Methods

- [blockDms](UsersClient.md#blockdms)
- [getByUsernames](UsersClient.md#getbyusernames)
- [getByIds](UsersClient.md#getbyids)
- [unlikePost](UsersClient.md#unlikepost)
- [getBlocking](UsersClient.md#getblocking)
- [unmuteUser](UsersClient.md#unmuteuser)
- [unpinList](UsersClient.md#unpinlist)
- [getBookmarkFolders](UsersClient.md#getbookmarkfolders)
- [getPosts](UsersClient.md#getposts)
- [unfollowUser](UsersClient.md#unfollowuser)
- [getTimeline](UsersClient.md#gettimeline)
- [getBookmarks](UsersClient.md#getbookmarks)
- [createBookmark](UsersClient.md#createbookmark)
- [getFollowedLists](UsersClient.md#getfollowedlists)
- [followList](UsersClient.md#followlist)
- [getListMemberships](UsersClient.md#getlistmemberships)
- [getOwnedLists](UsersClient.md#getownedlists)
- [getBookmarksByFolderId](UsersClient.md#getbookmarksbyfolderid)
- [repostPost](UsersClient.md#repostpost)
- [unblockDms](UsersClient.md#unblockdms)
- [getMentions](UsersClient.md#getmentions)
- [search](UsersClient.md#search)
- [getFollowers](UsersClient.md#getfollowers)
- [getMe](UsersClient.md#getme)
- [getById](UsersClient.md#getbyid)
- [unfollowList](UsersClient.md#unfollowlist)
- [getMuting](UsersClient.md#getmuting)
- [muteUser](UsersClient.md#muteuser)
- [getByUsername](UsersClient.md#getbyusername)
- [getPinnedLists](UsersClient.md#getpinnedlists)
- [pinList](UsersClient.md#pinlist)
- [deleteBookmark](UsersClient.md#deletebookmark)
- [getLikedPosts](UsersClient.md#getlikedposts)
- [unrepostPost](UsersClient.md#unrepostpost)
- [getRepostsOfMe](UsersClient.md#getrepostsofme)
- [getFollowing](UsersClient.md#getfollowing)
- [followUser](UsersClient.md#followuser)
- [likePost](UsersClient.md#likepost)

## Constructors

### constructor

• **new UsersClient**(`client`): [`UsersClient`](UsersClient.md)

Creates a new users client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `client` | [`Client`](Client.md) | The main X API client instance |

#### Returns

[`UsersClient`](UsersClient.md)

#### Defined in

[users/client.ts:720](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L720)

## Methods

### blockDms

▸ **blockDms**(`id`): `Promise`\<[`UsersDMBlockCreateResponse`](../interfaces/Schemas.UsersDMBlockCreateResponse.md)\>

Block DMs
Blocks direct messages to or from a specific User by their ID for the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the target User that the authenticated user requesting to block dms for. |

#### Returns

`Promise`\<[`UsersDMBlockCreateResponse`](../interfaces/Schemas.UsersDMBlockCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:737](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L737)

___

### getByUsernames

▸ **getByUsernames**(`usernames`, `options?`): `Promise`\<[`Get2UsersByResponse`](../interfaces/Schemas.Get2UsersByResponse.md)\>

Get Users by usernames
Retrieves details of multiple Users by their usernames.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `usernames` | `any`[] | A list of usernames, comma-separated. |
| `options` | `GetByUsernamesOptions` | - |

#### Returns

`Promise`\<[`Get2UsersByResponse`](../interfaces/Schemas.Get2UsersByResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:775](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L775)

___

### getByIds

▸ **getByIds**(`ids`, `options?`): `Promise`\<[`Get2UsersResponse`](../interfaces/Schemas.Get2UsersResponse.md)\>

Get Users by IDs
Retrieves details of multiple Users by their IDs.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ids` | `any`[] | A list of User IDs, comma-separated. You can specify up to 100 IDs. |
| `options` | `GetByIdsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersResponse`](../interfaces/Schemas.Get2UsersResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:839](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L839)

___

### unlikePost

▸ **unlikePost**(`id`, `tweetId`): `Promise`\<[`UsersLikesDeleteResponse`](../interfaces/Schemas.UsersLikesDeleteResponse.md)\>

Unlike Post
Causes the authenticated user to Unlike a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to unlike the Post. |
| `tweetId` | `string` | The ID of the Post that the User is requesting to unlike. |

#### Returns

`Promise`\<[`UsersLikesDeleteResponse`](../interfaces/Schemas.UsersLikesDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:907](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L907)

___

### getBlocking

▸ **getBlocking**(`id`, `options?`): `Promise`\<[`Get2UsersIdBlockingResponse`](../interfaces/Schemas.Get2UsersIdBlockingResponse.md)\>

Get blocking
Retrieves a list of Users blocked by the specified User ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | `GetBlockingOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdBlockingResponse`](../interfaces/Schemas.Get2UsersIdBlockingResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:947](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L947)

___

### unmuteUser

▸ **unmuteUser**(`sourceUserId`, `targetUserId`): `Promise`\<[`MuteUserMutationResponse`](../interfaces/Schemas.MuteUserMutationResponse.md)\>

Unmute User
Causes the authenticated user to unmute a specific user by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `sourceUserId` | `string` | The ID of the authenticated source User that is requesting to unmute the target User. |
| `targetUserId` | `string` | The ID of the User that the source User is requesting to unmute. |

#### Returns

`Promise`\<[`MuteUserMutationResponse`](../interfaces/Schemas.MuteUserMutationResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1025](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1025)

___

### unpinList

▸ **unpinList**(`id`, `listId`): `Promise`\<[`ListUnpinResponse`](../interfaces/Schemas.ListUnpinResponse.md)\>

Unpin List
Causes the authenticated user to unpin a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `listId` | `string` | The ID of the List to unpin. |

#### Returns

`Promise`\<[`ListUnpinResponse`](../interfaces/Schemas.ListUnpinResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1078](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1078)

___

### getBookmarkFolders

▸ **getBookmarkFolders**(`id`, `options?`): `Promise`\<[`BookmarkFoldersResponse`](../interfaces/Schemas.BookmarkFoldersResponse.md)\>

Get Bookmark folders
Retrieves a list of Bookmark folders created by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | `GetBookmarkFoldersOptions` | - |

#### Returns

`Promise`\<[`BookmarkFoldersResponse`](../interfaces/Schemas.BookmarkFoldersResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1118](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1118)

___

### getPosts

▸ **getPosts**(`id`, `options?`): `Promise`\<[`Get2UsersIdTweetsResponse`](../interfaces/Schemas.Get2UsersIdTweetsResponse.md)\>

Get Posts
Retrieves a list of posts authored by a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetPostsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdTweetsResponse`](../interfaces/Schemas.Get2UsersIdTweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1174](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1174)

___

### unfollowUser

▸ **unfollowUser**(`sourceUserId`, `targetUserId`): `Promise`\<[`UsersFollowingDeleteResponse`](../interfaces/Schemas.UsersFollowingDeleteResponse.md)\>

Unfollow User
Causes the authenticated user to unfollow a specific user by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `sourceUserId` | `string` | The ID of the authenticated source User that is requesting to unfollow the target User. |
| `targetUserId` | `string` | The ID of the User that the source User is requesting to unfollow. |

#### Returns

`Promise`\<[`UsersFollowingDeleteResponse`](../interfaces/Schemas.UsersFollowingDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1300](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1300)

___

### getTimeline

▸ **getTimeline**(`id`, `options?`): `Promise`\<[`Get2UsersIdTimelinesReverseChronologicalResponse`](../interfaces/Schemas.Get2UsersIdTimelinesReverseChronologicalResponse.md)\>

Get Timeline
Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User to list Reverse Chronological Timeline Posts of. |
| `options` | `GetTimelineOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdTimelinesReverseChronologicalResponse`](../interfaces/Schemas.Get2UsersIdTimelinesReverseChronologicalResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1349](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1349)

___

### getBookmarks

▸ **getBookmarks**(`id`, `options?`): `Promise`\<[`Get2UsersIdBookmarksResponse`](../interfaces/Schemas.Get2UsersIdBookmarksResponse.md)\>

Get Bookmarks
Retrieves a list of Posts bookmarked by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | `GetBookmarksOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdBookmarksResponse`](../interfaces/Schemas.Get2UsersIdBookmarksResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1471](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1471)

___

### createBookmark

▸ **createBookmark**(`id`, `body`): `Promise`\<[`BookmarkMutationResponse`](../interfaces/Schemas.BookmarkMutationResponse.md)\>

Create Bookmark
Adds a post to the authenticated user’s bookmarks.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to add bookmarks. |
| `body` | [`BookmarkAddRequest`](../interfaces/Schemas.BookmarkAddRequest.md) | Request body |

#### Returns

`Promise`\<[`BookmarkMutationResponse`](../interfaces/Schemas.BookmarkMutationResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1565](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1565)

___

### getFollowedLists

▸ **getFollowedLists**(`id`, `options?`): `Promise`\<[`Get2UsersIdFollowedListsResponse`](../interfaces/Schemas.Get2UsersIdFollowedListsResponse.md)\>

Get followed Lists
Retrieves a list of Lists followed by a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetFollowedListsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdFollowedListsResponse`](../interfaces/Schemas.Get2UsersIdFollowedListsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1608](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1608)

___

### followList

▸ **followList**(`id`, `options?`): `Promise`\<[`ListFollowedResponse`](../interfaces/Schemas.ListFollowedResponse.md)\>

Follow List
Causes the authenticated user to follow a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that will follow the List. |
| `options` | `FollowListOptions` | - |

#### Returns

`Promise`\<[`ListFollowedResponse`](../interfaces/Schemas.ListFollowedResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1682](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1682)

___

### getListMemberships

▸ **getListMemberships**(`id`, `options?`): `Promise`\<[`Get2UsersIdListMembershipsResponse`](../interfaces/Schemas.Get2UsersIdListMembershipsResponse.md)\>

Get List memberships
Retrieves a list of Lists that a specific User is a member of by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetListMembershipsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdListMembershipsResponse`](../interfaces/Schemas.Get2UsersIdListMembershipsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1730](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1730)

___

### getOwnedLists

▸ **getOwnedLists**(`id`, `options?`): `Promise`\<[`Get2UsersIdOwnedListsResponse`](../interfaces/Schemas.Get2UsersIdOwnedListsResponse.md)\>

Get owned Lists
Retrieves a list of Lists owned by a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetOwnedListsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdOwnedListsResponse`](../interfaces/Schemas.Get2UsersIdOwnedListsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1804](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1804)

___

### getBookmarksByFolderId

▸ **getBookmarksByFolderId**(`id`, `folderId`): `Promise`\<[`BookmarkFolderPostsResponse`](../interfaces/Schemas.BookmarkFolderPostsResponse.md)\>

Get Bookmarks by folder ID
Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `folderId` | `string` | The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for. |

#### Returns

`Promise`\<[`BookmarkFolderPostsResponse`](../interfaces/Schemas.BookmarkFolderPostsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1882](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1882)

___

### repostPost

▸ **repostPost**(`id`, `options?`): `Promise`\<[`UsersRetweetsCreateResponse`](../interfaces/Schemas.UsersRetweetsCreateResponse.md)\>

Repost Post
Causes the authenticated user to repost a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to repost the Post. |
| `options` | `RepostPostOptions` | - |

#### Returns

`Promise`\<[`UsersRetweetsCreateResponse`](../interfaces/Schemas.UsersRetweetsCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1925](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1925)

___

### unblockDms

▸ **unblockDms**(`id`): `Promise`\<[`UsersDMUnBlockCreateResponse`](../interfaces/Schemas.UsersDMUnBlockCreateResponse.md)\>

Unblock DMs
Unblocks direct messages to or from a specific User by their ID for the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the target User that the authenticated user requesting to unblock dms for. |

#### Returns

`Promise`\<[`UsersDMUnBlockCreateResponse`](../interfaces/Schemas.UsersDMUnBlockCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:1973](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L1973)

___

### getMentions

▸ **getMentions**(`id`, `options?`): `Promise`\<[`Get2UsersIdMentionsResponse`](../interfaces/Schemas.Get2UsersIdMentionsResponse.md)\>

Get mentions
Retrieves a list of Posts that mention a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetMentionsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdMentionsResponse`](../interfaces/Schemas.Get2UsersIdMentionsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2011](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2011)

___

### search

▸ **search**(`query`, `options?`): `Promise`\<[`Get2UsersSearchResponse`](../interfaces/Schemas.Get2UsersSearchResponse.md)\>

Search Users
Retrieves a list of Users matching a search query.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `any` | TThe the query string by which to query for users. |
| `options` | `SearchOptions` | - |

#### Returns

`Promise`\<[`Get2UsersSearchResponse`](../interfaces/Schemas.Get2UsersSearchResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2127](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2127)

___

### getFollowers

▸ **getFollowers**(`id`, `options?`): `Promise`\<[`Get2UsersIdFollowersResponse`](../interfaces/Schemas.Get2UsersIdFollowersResponse.md)\>

Get followers
Retrieves a list of Users who follow a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetFollowersOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdFollowersResponse`](../interfaces/Schemas.Get2UsersIdFollowersResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2203](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2203)

___

### getMe

▸ **getMe**(`options?`): `Promise`\<[`Get2UsersMeResponse`](../interfaces/Schemas.Get2UsersMeResponse.md)\>

Get my User
Retrieves details of the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetMeOptions` |

#### Returns

`Promise`\<[`Get2UsersMeResponse`](../interfaces/Schemas.Get2UsersMeResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2273](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2273)

___

### getById

▸ **getById**(`id`, `options?`): `Promise`\<[`Get2UsersIdResponse`](../interfaces/Schemas.Get2UsersIdResponse.md)\>

Get User by ID
Retrieves details of a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetByIdOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdResponse`](../interfaces/Schemas.Get2UsersIdResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2330](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2330)

___

### unfollowList

▸ **unfollowList**(`id`, `listId`): `Promise`\<[`ListFollowedResponse`](../interfaces/Schemas.ListFollowedResponse.md)\>

Unfollow List
Causes the authenticated user to unfollow a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that will unfollow the List. |
| `listId` | `string` | The ID of the List to unfollow. |

#### Returns

`Promise`\<[`ListFollowedResponse`](../interfaces/Schemas.ListFollowedResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2396](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2396)

___

### getMuting

▸ **getMuting**(`id`, `options?`): `Promise`\<[`Get2UsersIdMutingResponse`](../interfaces/Schemas.Get2UsersIdMutingResponse.md)\>

Get muting
Retrieves a list of Users muted by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | `GetMutingOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdMutingResponse`](../interfaces/Schemas.Get2UsersIdMutingResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2439](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2439)

___

### muteUser

▸ **muteUser**(`id`, `options?`): `Promise`\<[`MuteUserMutationResponse`](../interfaces/Schemas.MuteUserMutationResponse.md)\>

Mute User
Causes the authenticated user to mute a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to mute the target User. |
| `options` | `MuteUserOptions` | - |

#### Returns

`Promise`\<[`MuteUserMutationResponse`](../interfaces/Schemas.MuteUserMutationResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2513](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2513)

___

### getByUsername

▸ **getByUsername**(`username`, `options?`): `Promise`\<[`Get2UsersByUsernameUsernameResponse`](../interfaces/Schemas.Get2UsersByUsernameUsernameResponse.md)\>

Get User by username
Retrieves details of a specific User by their username.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `username` | `string` | A username. |
| `options` | `GetByUsernameOptions` | - |

#### Returns

`Promise`\<[`Get2UsersByUsernameUsernameResponse`](../interfaces/Schemas.Get2UsersByUsernameUsernameResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2561](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2561)

___

### getPinnedLists

▸ **getPinnedLists**(`id`, `options?`): `Promise`\<[`Get2UsersIdPinnedListsResponse`](../interfaces/Schemas.Get2UsersIdPinnedListsResponse.md)\>

Get pinned Lists
Retrieves a list of Lists pinned by the authenticated user.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User for whom to return results. |
| `options` | `GetPinnedListsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdPinnedListsResponse`](../interfaces/Schemas.Get2UsersIdPinnedListsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2623](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2623)

___

### pinList

▸ **pinList**(`id`, `body`): `Promise`\<[`ListPinnedResponse`](../interfaces/Schemas.ListPinnedResponse.md)\>

Pin List
Causes the authenticated user to pin a specific List by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that will pin the List. |
| `body` | [`ListPinnedRequest`](../interfaces/Schemas.ListPinnedRequest.md) | Request body |

#### Returns

`Promise`\<[`ListPinnedResponse`](../interfaces/Schemas.ListPinnedResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2687](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2687)

___

### deleteBookmark

▸ **deleteBookmark**(`id`, `tweetId`): `Promise`\<[`BookmarkMutationResponse`](../interfaces/Schemas.BookmarkMutationResponse.md)\>

Delete Bookmark
Removes a Post from the authenticated user’s Bookmarks by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User whose bookmark is to be removed. |
| `tweetId` | `string` | The ID of the Post that the source User is removing from bookmarks. |

#### Returns

`Promise`\<[`BookmarkMutationResponse`](../interfaces/Schemas.BookmarkMutationResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2731](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2731)

___

### getLikedPosts

▸ **getLikedPosts**(`id`, `options?`): `Promise`\<[`Get2UsersIdLikedTweetsResponse`](../interfaces/Schemas.Get2UsersIdLikedTweetsResponse.md)\>

Get liked Posts
Retrieves a list of Posts liked by a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetLikedPostsOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdLikedTweetsResponse`](../interfaces/Schemas.Get2UsersIdLikedTweetsResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2774](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2774)

___

### unrepostPost

▸ **unrepostPost**(`id`, `sourceTweetId`): `Promise`\<[`UsersRetweetsDeleteResponse`](../interfaces/Schemas.UsersRetweetsDeleteResponse.md)\>

Unrepost Post
Causes the authenticated user to unrepost a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to repost the Post. |
| `sourceTweetId` | `string` | The ID of the Post that the User is requesting to unretweet. |

#### Returns

`Promise`\<[`UsersRetweetsDeleteResponse`](../interfaces/Schemas.UsersRetweetsDeleteResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2870](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2870)

___

### getRepostsOfMe

▸ **getRepostsOfMe**(`options?`): `Promise`\<[`Get2UsersRepostsOfMeResponse`](../interfaces/Schemas.Get2UsersRepostsOfMeResponse.md)\>

Get Reposts of me
Retrieves a list of Posts that repost content from the authenticated user.

#### Parameters

| Name | Type |
| :------ | :------ |
| `options` | `GetRepostsOfMeOptions` |

#### Returns

`Promise`\<[`Get2UsersRepostsOfMeResponse`](../interfaces/Schemas.Get2UsersRepostsOfMeResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:2912](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L2912)

___

### getFollowing

▸ **getFollowing**(`id`, `options?`): `Promise`\<[`Get2UsersIdFollowingResponse`](../interfaces/Schemas.Get2UsersIdFollowingResponse.md)\>

Get following
Retrieves a list of Users followed by a specific User by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the User to lookup. |
| `options` | `GetFollowingOptions` | - |

#### Returns

`Promise`\<[`Get2UsersIdFollowingResponse`](../interfaces/Schemas.Get2UsersIdFollowingResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:3001](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L3001)

___

### followUser

▸ **followUser**(`id`, `options?`): `Promise`\<[`UsersFollowingCreateResponse`](../interfaces/Schemas.UsersFollowingCreateResponse.md)\>

Follow User
Causes the authenticated user to follow a specific user by their ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to follow the target User. |
| `options` | `FollowUserOptions` | - |

#### Returns

`Promise`\<[`UsersFollowingCreateResponse`](../interfaces/Schemas.UsersFollowingCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:3075](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L3075)

___

### likePost

▸ **likePost**(`id`, `options?`): `Promise`\<[`UsersLikesCreateResponse`](../interfaces/Schemas.UsersLikesCreateResponse.md)\>

Like Post
Causes the authenticated user to Like a specific Post by its ID.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The ID of the authenticated source User that is requesting to like the Post. |
| `options` | `LikePostOptions` | - |

#### Returns

`Promise`\<[`UsersLikesCreateResponse`](../interfaces/Schemas.UsersLikesCreateResponse.md)\>

Promise resolving to the API response

#### Defined in

[users/client.ts:3123](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/client.ts#L3123)
