[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / Users

# Namespace: Users

## Table of contents

### References

- [MuteUserRequest](Users.md#muteuserrequest)

### Type Aliases

- [BlockDmsResponse](Users.md#blockdmsresponse)
- [GetByUsernamesResponse](Users.md#getbyusernamesresponse)
- [GetByIdsResponse](Users.md#getbyidsresponse)
- [UnlikePostResponse](Users.md#unlikepostresponse)
- [GetBlockingResponse](Users.md#getblockingresponse)
- [UnmuteUserResponse](Users.md#unmuteuserresponse)
- [UnpinListResponse](Users.md#unpinlistresponse)
- [GetBookmarkFoldersResponse](Users.md#getbookmarkfoldersresponse)
- [GetPostsResponse](Users.md#getpostsresponse)
- [UnfollowUserResponse](Users.md#unfollowuserresponse)
- [GetTimelineResponse](Users.md#gettimelineresponse)
- [GetBookmarksResponse](Users.md#getbookmarksresponse)
- [CreateBookmarkRequest](Users.md#createbookmarkrequest)
- [CreateBookmarkResponse](Users.md#createbookmarkresponse)
- [GetFollowedListsResponse](Users.md#getfollowedlistsresponse)
- [FollowListRequest](Users.md#followlistrequest)
- [FollowListResponse](Users.md#followlistresponse)
- [GetListMembershipsResponse](Users.md#getlistmembershipsresponse)
- [GetOwnedListsResponse](Users.md#getownedlistsresponse)
- [GetBookmarksByFolderIdResponse](Users.md#getbookmarksbyfolderidresponse)
- [RepostPostRequest](Users.md#repostpostrequest)
- [RepostPostResponse](Users.md#repostpostresponse)
- [UnblockDmsResponse](Users.md#unblockdmsresponse)
- [GetMentionsResponse](Users.md#getmentionsresponse)
- [SearchResponse](Users.md#searchresponse)
- [GetFollowersResponse](Users.md#getfollowersresponse)
- [GetMeResponse](Users.md#getmeresponse)
- [GetByIdResponse](Users.md#getbyidresponse)
- [UnfollowListResponse](Users.md#unfollowlistresponse)
- [GetMutingResponse](Users.md#getmutingresponse)
- [MuteUserResponse](Users.md#muteuserresponse)
- [GetByUsernameResponse](Users.md#getbyusernameresponse)
- [GetPinnedListsResponse](Users.md#getpinnedlistsresponse)
- [PinListRequest](Users.md#pinlistrequest)
- [PinListResponse](Users.md#pinlistresponse)
- [DeleteBookmarkResponse](Users.md#deletebookmarkresponse)
- [GetLikedPostsResponse](Users.md#getlikedpostsresponse)
- [UnrepostPostResponse](Users.md#unrepostpostresponse)
- [GetRepostsOfMeResponse](Users.md#getrepostsofmeresponse)
- [GetFollowingResponse](Users.md#getfollowingresponse)
- [FollowUserRequest](Users.md#followuserrequest)
- [FollowUserResponse](Users.md#followuserresponse)
- [LikePostRequest](Users.md#likepostrequest)
- [LikePostResponse](Users.md#likepostresponse)

## References

### MuteUserRequest

Re-exports [MuteUserRequest](../interfaces/Schemas.MuteUserRequest.md)

## Type Aliases

### BlockDmsResponse

Ƭ **BlockDmsResponse**: [`UsersDMBlockCreateResponse`](../interfaces/Schemas.UsersDMBlockCreateResponse.md)

Response for blockDms

#### Defined in

[users/models.ts:15](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L15)

___

### GetByUsernamesResponse

Ƭ **GetByUsernamesResponse**: [`Get2UsersByResponse`](../interfaces/Schemas.Get2UsersByResponse.md)

Response for getByUsernames

#### Defined in

[users/models.ts:21](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L21)

___

### GetByIdsResponse

Ƭ **GetByIdsResponse**: [`Get2UsersResponse`](../interfaces/Schemas.Get2UsersResponse.md)

Response for getByIds

#### Defined in

[users/models.ts:27](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L27)

___

### UnlikePostResponse

Ƭ **UnlikePostResponse**: [`UsersLikesDeleteResponse`](../interfaces/Schemas.UsersLikesDeleteResponse.md)

Response for unlikePost

#### Defined in

[users/models.ts:33](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L33)

___

### GetBlockingResponse

Ƭ **GetBlockingResponse**: [`Get2UsersIdBlockingResponse`](../interfaces/Schemas.Get2UsersIdBlockingResponse.md)

Response for getBlocking

#### Defined in

[users/models.ts:39](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L39)

___

### UnmuteUserResponse

Ƭ **UnmuteUserResponse**: [`MuteUserMutationResponse`](../interfaces/Schemas.MuteUserMutationResponse.md)

Response for unmuteUser

#### Defined in

[users/models.ts:45](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L45)

___

### UnpinListResponse

Ƭ **UnpinListResponse**: [`ListUnpinResponse`](../interfaces/Schemas.ListUnpinResponse.md)

Response for unpinList

#### Defined in

[users/models.ts:51](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L51)

___

### GetBookmarkFoldersResponse

Ƭ **GetBookmarkFoldersResponse**: [`BookmarkFoldersResponse`](../interfaces/Schemas.BookmarkFoldersResponse.md)

Response for getBookmarkFolders

#### Defined in

[users/models.ts:57](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L57)

___

### GetPostsResponse

Ƭ **GetPostsResponse**: [`Get2UsersIdTweetsResponse`](../interfaces/Schemas.Get2UsersIdTweetsResponse.md)

Response for getPosts

#### Defined in

[users/models.ts:63](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L63)

___

### UnfollowUserResponse

Ƭ **UnfollowUserResponse**: [`UsersFollowingDeleteResponse`](../interfaces/Schemas.UsersFollowingDeleteResponse.md)

Response for unfollowUser

#### Defined in

[users/models.ts:69](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L69)

___

### GetTimelineResponse

Ƭ **GetTimelineResponse**: [`Get2UsersIdTimelinesReverseChronologicalResponse`](../interfaces/Schemas.Get2UsersIdTimelinesReverseChronologicalResponse.md)

Response for getTimeline

#### Defined in

[users/models.ts:75](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L75)

___

### GetBookmarksResponse

Ƭ **GetBookmarksResponse**: [`Get2UsersIdBookmarksResponse`](../interfaces/Schemas.Get2UsersIdBookmarksResponse.md)

Response for getBookmarks

#### Defined in

[users/models.ts:81](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L81)

___

### CreateBookmarkRequest

Ƭ **CreateBookmarkRequest**: [`BookmarkAddRequest`](../interfaces/Schemas.BookmarkAddRequest.md)

Request for createBookmark

#### Defined in

[users/models.ts:87](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L87)

___

### CreateBookmarkResponse

Ƭ **CreateBookmarkResponse**: [`BookmarkMutationResponse`](../interfaces/Schemas.BookmarkMutationResponse.md)

Response for createBookmark

#### Defined in

[users/models.ts:93](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L93)

___

### GetFollowedListsResponse

Ƭ **GetFollowedListsResponse**: [`Get2UsersIdFollowedListsResponse`](../interfaces/Schemas.Get2UsersIdFollowedListsResponse.md)

Response for getFollowedLists

#### Defined in

[users/models.ts:99](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L99)

___

### FollowListRequest

Ƭ **FollowListRequest**: [`ListFollowedRequest`](../interfaces/Schemas.ListFollowedRequest.md)

Request for followList

#### Defined in

[users/models.ts:105](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L105)

___

### FollowListResponse

Ƭ **FollowListResponse**: [`ListFollowedResponse`](../interfaces/Schemas.ListFollowedResponse.md)

Response for followList

#### Defined in

[users/models.ts:111](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L111)

___

### GetListMembershipsResponse

Ƭ **GetListMembershipsResponse**: [`Get2UsersIdListMembershipsResponse`](../interfaces/Schemas.Get2UsersIdListMembershipsResponse.md)

Response for getListMemberships

#### Defined in

[users/models.ts:117](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L117)

___

### GetOwnedListsResponse

Ƭ **GetOwnedListsResponse**: [`Get2UsersIdOwnedListsResponse`](../interfaces/Schemas.Get2UsersIdOwnedListsResponse.md)

Response for getOwnedLists

#### Defined in

[users/models.ts:123](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L123)

___

### GetBookmarksByFolderIdResponse

Ƭ **GetBookmarksByFolderIdResponse**: [`BookmarkFolderPostsResponse`](../interfaces/Schemas.BookmarkFolderPostsResponse.md)

Response for getBookmarksByFolderId

#### Defined in

[users/models.ts:129](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L129)

___

### RepostPostRequest

Ƭ **RepostPostRequest**: [`UsersRetweetsCreateRequest`](../interfaces/Schemas.UsersRetweetsCreateRequest.md)

Request for repostPost

#### Defined in

[users/models.ts:135](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L135)

___

### RepostPostResponse

Ƭ **RepostPostResponse**: [`UsersRetweetsCreateResponse`](../interfaces/Schemas.UsersRetweetsCreateResponse.md)

Response for repostPost

#### Defined in

[users/models.ts:141](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L141)

___

### UnblockDmsResponse

Ƭ **UnblockDmsResponse**: [`UsersDMUnBlockCreateResponse`](../interfaces/Schemas.UsersDMUnBlockCreateResponse.md)

Response for unblockDms

#### Defined in

[users/models.ts:147](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L147)

___

### GetMentionsResponse

Ƭ **GetMentionsResponse**: [`Get2UsersIdMentionsResponse`](../interfaces/Schemas.Get2UsersIdMentionsResponse.md)

Response for getMentions

#### Defined in

[users/models.ts:153](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L153)

___

### SearchResponse

Ƭ **SearchResponse**: [`Get2UsersSearchResponse`](../interfaces/Schemas.Get2UsersSearchResponse.md)

Response for search

#### Defined in

[users/models.ts:159](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L159)

___

### GetFollowersResponse

Ƭ **GetFollowersResponse**: [`Get2UsersIdFollowersResponse`](../interfaces/Schemas.Get2UsersIdFollowersResponse.md)

Response for getFollowers

#### Defined in

[users/models.ts:165](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L165)

___

### GetMeResponse

Ƭ **GetMeResponse**: [`Get2UsersMeResponse`](../interfaces/Schemas.Get2UsersMeResponse.md)

Response for getMe

#### Defined in

[users/models.ts:171](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L171)

___

### GetByIdResponse

Ƭ **GetByIdResponse**: [`Get2UsersIdResponse`](../interfaces/Schemas.Get2UsersIdResponse.md)

Response for getById

#### Defined in

[users/models.ts:177](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L177)

___

### UnfollowListResponse

Ƭ **UnfollowListResponse**: [`ListFollowedResponse`](../interfaces/Schemas.ListFollowedResponse.md)

Response for unfollowList

#### Defined in

[users/models.ts:183](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L183)

___

### GetMutingResponse

Ƭ **GetMutingResponse**: [`Get2UsersIdMutingResponse`](../interfaces/Schemas.Get2UsersIdMutingResponse.md)

Response for getMuting

#### Defined in

[users/models.ts:189](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L189)

___

### MuteUserResponse

Ƭ **MuteUserResponse**: [`MuteUserMutationResponse`](../interfaces/Schemas.MuteUserMutationResponse.md)

Response for muteUser

#### Defined in

[users/models.ts:202](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L202)

___

### GetByUsernameResponse

Ƭ **GetByUsernameResponse**: [`Get2UsersByUsernameUsernameResponse`](../interfaces/Schemas.Get2UsersByUsernameUsernameResponse.md)

Response for getByUsername

#### Defined in

[users/models.ts:208](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L208)

___

### GetPinnedListsResponse

Ƭ **GetPinnedListsResponse**: [`Get2UsersIdPinnedListsResponse`](../interfaces/Schemas.Get2UsersIdPinnedListsResponse.md)

Response for getPinnedLists

#### Defined in

[users/models.ts:214](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L214)

___

### PinListRequest

Ƭ **PinListRequest**: [`ListPinnedRequest`](../interfaces/Schemas.ListPinnedRequest.md)

Request for pinList

#### Defined in

[users/models.ts:220](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L220)

___

### PinListResponse

Ƭ **PinListResponse**: [`ListPinnedResponse`](../interfaces/Schemas.ListPinnedResponse.md)

Response for pinList

#### Defined in

[users/models.ts:226](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L226)

___

### DeleteBookmarkResponse

Ƭ **DeleteBookmarkResponse**: [`BookmarkMutationResponse`](../interfaces/Schemas.BookmarkMutationResponse.md)

Response for deleteBookmark

#### Defined in

[users/models.ts:232](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L232)

___

### GetLikedPostsResponse

Ƭ **GetLikedPostsResponse**: [`Get2UsersIdLikedTweetsResponse`](../interfaces/Schemas.Get2UsersIdLikedTweetsResponse.md)

Response for getLikedPosts

#### Defined in

[users/models.ts:238](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L238)

___

### UnrepostPostResponse

Ƭ **UnrepostPostResponse**: [`UsersRetweetsDeleteResponse`](../interfaces/Schemas.UsersRetweetsDeleteResponse.md)

Response for unrepostPost

#### Defined in

[users/models.ts:244](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L244)

___

### GetRepostsOfMeResponse

Ƭ **GetRepostsOfMeResponse**: [`Get2UsersRepostsOfMeResponse`](../interfaces/Schemas.Get2UsersRepostsOfMeResponse.md)

Response for getRepostsOfMe

#### Defined in

[users/models.ts:250](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L250)

___

### GetFollowingResponse

Ƭ **GetFollowingResponse**: [`Get2UsersIdFollowingResponse`](../interfaces/Schemas.Get2UsersIdFollowingResponse.md)

Response for getFollowing

#### Defined in

[users/models.ts:256](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L256)

___

### FollowUserRequest

Ƭ **FollowUserRequest**: [`UsersFollowingCreateRequest`](../interfaces/Schemas.UsersFollowingCreateRequest.md)

Request for followUser

#### Defined in

[users/models.ts:262](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L262)

___

### FollowUserResponse

Ƭ **FollowUserResponse**: [`UsersFollowingCreateResponse`](../interfaces/Schemas.UsersFollowingCreateResponse.md)

Response for followUser

#### Defined in

[users/models.ts:268](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L268)

___

### LikePostRequest

Ƭ **LikePostRequest**: [`UsersLikesCreateRequest`](../interfaces/Schemas.UsersLikesCreateRequest.md)

Request for likePost

#### Defined in

[users/models.ts:274](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L274)

___

### LikePostResponse

Ƭ **LikePostResponse**: [`UsersLikesCreateResponse`](../interfaces/Schemas.UsersLikesCreateResponse.md)

Response for likePost

#### Defined in

[users/models.ts:280](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/users/models.ts#L280)
