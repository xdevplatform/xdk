[X API SDK v2.152 - v0.1.0](../README.md) / [Exports](../modules.md) / UsersClient

# Class: UsersClient

Client for users operations

This client provides methods for interacting with the users endpoints
of the X API. It handles authentication, request formatting, and response
parsing for all users related operations.

## Table of contents

### Constructors

- [constructor](UsersClient.md#constructor)

### Methods

- [getMentions](UsersClient.md#getmentions)
- [getRepostsOfMe](UsersClient.md#getrepostsofme)
- [getBookmarks](UsersClient.md#getbookmarks)
- [createBookmark](UsersClient.md#createbookmark)
- [getBlocking](UsersClient.md#getblocking)
- [getBookmarksByFolderId](UsersClient.md#getbookmarksbyfolderid)
- [getById](UsersClient.md#getbyid)
- [unrepostPost](UsersClient.md#unrepostpost)
- [getFollowers](UsersClient.md#getfollowers)
- [likePost](UsersClient.md#likepost)
- [unlikePost](UsersClient.md#unlikepost)
- [unfollowList](UsersClient.md#unfollowlist)
- [getFollowing](UsersClient.md#getfollowing)
- [followUser](UsersClient.md#followuser)
- [getLikedPosts](UsersClient.md#getlikedposts)
- [unfollowUser](UsersClient.md#unfollowuser)
- [unpinList](UsersClient.md#unpinlist)
- [repostPost](UsersClient.md#repostpost)
- [getPinnedLists](UsersClient.md#getpinnedlists)
- [pinList](UsersClient.md#pinlist)
- [getListMemberships](UsersClient.md#getlistmemberships)
- [unmuteUser](UsersClient.md#unmuteuser)
- [blockDms](UsersClient.md#blockdms)
- [getFollowedLists](UsersClient.md#getfollowedlists)
- [followList](UsersClient.md#followlist)
- [getByIds](UsersClient.md#getbyids)
- [getMe](UsersClient.md#getme)
- [unblockDms](UsersClient.md#unblockdms)
- [getMuting](UsersClient.md#getmuting)
- [muteUser](UsersClient.md#muteuser)
- [getPosts](UsersClient.md#getposts)
- [deleteBookmark](UsersClient.md#deletebookmark)
- [getByUsernames](UsersClient.md#getbyusernames)
- [getByUsername](UsersClient.md#getbyusername)
- [getBookmarkFolders](UsersClient.md#getbookmarkfolders)
- [search](UsersClient.md#search)
- [getTimeline](UsersClient.md#gettimeline)
- [getOwnedLists](UsersClient.md#getownedlists)

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

[users/client.ts:720](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L720)

## Methods

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

[users/client.ts:737](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L737)

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

[users/client.ts:849](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L849)

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

[users/client.ts:938](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L938)

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

[users/client.ts:1032](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1032)

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

[users/client.ts:1075](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1075)

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

[users/client.ts:1153](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1153)

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

[users/client.ts:1196](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1196)

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

[users/client.ts:1262](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1262)

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

[users/client.ts:1308](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1308)

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

[users/client.ts:1382](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1382)

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

[users/client.ts:1434](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1434)

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

[users/client.ts:1478](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1478)

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

[users/client.ts:1521](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1521)

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

[users/client.ts:1595](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1595)

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

[users/client.ts:1643](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1643)

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

[users/client.ts:1739](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1739)

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

[users/client.ts:1792](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1792)

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

[users/client.ts:1832](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1832)

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

[users/client.ts:1880](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1880)

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

[users/client.ts:1944](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1944)

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

[users/client.ts:1984](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L1984)

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

[users/client.ts:2062](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2062)

___

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

[users/client.ts:2111](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2111)

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

[users/client.ts:2149](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2149)

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

[users/client.ts:2223](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2223)

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

[users/client.ts:2271](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2271)

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

[users/client.ts:2331](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2331)

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

[users/client.ts:2388](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2388)

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

[users/client.ts:2426](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2426)

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

[users/client.ts:2500](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2500)

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

[users/client.ts:2548](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2548)

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

[users/client.ts:2674](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2674)

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

[users/client.ts:2717](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2717)

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

[users/client.ts:2781](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2781)

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

[users/client.ts:2843](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2843)

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

[users/client.ts:2899](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2899)

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

[users/client.ts:2975](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L2975)

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

[users/client.ts:3097](https://github.com/xdevplatform/xdk/blob/a332a30384267be8a87066aae5bba329e7c24532/xdk/typescript/src/users/client.ts#L3097)
