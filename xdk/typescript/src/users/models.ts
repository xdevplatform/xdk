/**
 * Models for users operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getOwnedLists
 * 
 * @public
 */
export type GetOwnedListsResponse = Schemas.Get2UsersIdOwnedListsResponse;
/**
 * Response for blockDms
 * 
 * @public
 */
export type BlockDmsResponse = Schemas.UsersDMBlockCreateResponse;
/**
 * Response for getLikedPosts
 * 
 * @public
 */
export type GetLikedPostsResponse = Schemas.Get2UsersIdLikedTweetsResponse;
/**
 * Response for unrepostPost
 * 
 * @public
 */
export type UnrepostPostResponse = Schemas.UsersRetweetsDeleteResponse;
/**
 * Response for getMentions
 * 
 * @public
 */
export type GetMentionsResponse = Schemas.Get2UsersIdMentionsResponse;
/**
 * Response for unfollowUser
 * 
 * @public
 */
export type UnfollowUserResponse = Schemas.UsersFollowingDeleteResponse;
/**
 * Response for unblockDms
 * 
 * @public
 */
export type UnblockDmsResponse = Schemas.UsersDMUnBlockCreateResponse;
/**
 * Response for getByIds
 * 
 * @public
 */
export type GetByIdsResponse = Schemas.Get2UsersResponse;
/**
 * Response for unmuteUser
 * 
 * @public
 */
export type UnmuteUserResponse = Schemas.MuteUserMutationResponse;
/**
 * Response for getFollowing
 * 
 * @public
 */
export type GetFollowingResponse = Schemas.Get2UsersIdFollowingResponse;
/**
 * Request for followUser
 * 
 * @public
 */
export type FollowUserRequest = Schemas.UsersFollowingCreateRequest;
/**
 * Response for followUser
 * 
 * @public
 */
export type FollowUserResponse = Schemas.UsersFollowingCreateResponse;
/**
 * Response for getBookmarkFolders
 * 
 * @public
 */
export type GetBookmarkFoldersResponse = Schemas.BookmarkFoldersResponse;
/**
 * Response for getBookmarksByFolderId
 * 
 * @public
 */
export type GetBookmarksByFolderIdResponse = Schemas.BookmarkFolderPostsResponse;
/**
 * Response for getPosts
 * 
 * @public
 */
export type GetPostsResponse = Schemas.Get2UsersIdTweetsResponse;
/**
 * Response for getListMemberships
 * 
 * @public
 */
export type GetListMembershipsResponse = Schemas.Get2UsersIdListMembershipsResponse;
/**
 * Response for unfollowList
 * 
 * @public
 */
export type UnfollowListResponse = Schemas.ListFollowedResponse;
/**
 * Response for getRepostsOfMe
 * 
 * @public
 */
export type GetRepostsOfMeResponse = Schemas.Get2UsersRepostsOfMeResponse;
/**
 * Response for getBlocking
 * 
 * @public
 */
export type GetBlockingResponse = Schemas.Get2UsersIdBlockingResponse;
/**
 * Response for search
 * 
 * @public
 */
export type SearchResponse = Schemas.Get2UsersSearchResponse;
/**
 * Response for getFollowers
 * 
 * @public
 */
export type GetFollowersResponse = Schemas.Get2UsersIdFollowersResponse;
/**
 * Response for getMe
 * 
 * @public
 */
export type GetMeResponse = Schemas.Get2UsersMeResponse;
/**
 * Response for getById
 * 
 * @public
 */
export type GetByIdResponse = Schemas.Get2UsersIdResponse;
/**
 * Response for getByUsernames
 * 
 * @public
 */
export type GetByUsernamesResponse = Schemas.Get2UsersByResponse;
/**
 * Response for getByUsername
 * 
 * @public
 */
export type GetByUsernameResponse = Schemas.Get2UsersByUsernameUsernameResponse;
/**
 * Response for getTimeline
 * 
 * @public
 */
export type GetTimelineResponse = Schemas.Get2UsersIdTimelinesReverseChronologicalResponse;
/**
 * Response for deleteBookmark
 * 
 * @public
 */
export type DeleteBookmarkResponse = Schemas.BookmarkMutationResponse;
/**
 * Response for getPinnedLists
 * 
 * @public
 */
export type GetPinnedListsResponse = Schemas.Get2UsersIdPinnedListsResponse;
/**
 * Request for pinList
 * 
 * @public
 */
export type PinListRequest = Schemas.ListPinnedRequest;
/**
 * Response for pinList
 * 
 * @public
 */
export type PinListResponse = Schemas.ListPinnedResponse;
/**
 * Response for unpinList
 * 
 * @public
 */
export type UnpinListResponse = Schemas.ListUnpinResponse;
/**
 * Response for getFollowedLists
 * 
 * @public
 */
export type GetFollowedListsResponse = Schemas.Get2UsersIdFollowedListsResponse;
/**
 * Request for followList
 * 
 * @public
 */
export type FollowListRequest = Schemas.ListFollowedRequest;
/**
 * Response for followList
 * 
 * @public
 */
export type FollowListResponse = Schemas.ListFollowedResponse;
/**
 * Request for repostPost
 * 
 * @public
 */
export type RepostPostRequest = Schemas.UsersRetweetsCreateRequest;
/**
 * Response for repostPost
 * 
 * @public
 */
export type RepostPostResponse = Schemas.UsersRetweetsCreateResponse;
/**
 * Request for likePost
 * 
 * @public
 */
export type LikePostRequest = Schemas.UsersLikesCreateRequest;
/**
 * Response for likePost
 * 
 * @public
 */
export type LikePostResponse = Schemas.UsersLikesCreateResponse;
/**
 * Response for getMuting
 * 
 * @public
 */
export type GetMutingResponse = Schemas.Get2UsersIdMutingResponse;

/**
 * Request for muteUser
 * 
 * @public
 */
export type { MuteUserRequest as MuteUserRequest } from '../schemas.js';
/**
 * Response for muteUser
 * 
 * @public
 */
export type MuteUserResponse = Schemas.MuteUserMutationResponse;
/**
 * Response for getBookmarks
 * 
 * @public
 */
export type GetBookmarksResponse = Schemas.Get2UsersIdBookmarksResponse;
/**
 * Request for createBookmark
 * 
 * @public
 */
export type CreateBookmarkRequest = Schemas.BookmarkAddRequest;
/**
 * Response for createBookmark
 * 
 * @public
 */
export type CreateBookmarkResponse = Schemas.BookmarkMutationResponse;
/**
 * Response for unlikePost
 * 
 * @public
 */
export type UnlikePostResponse = Schemas.UsersLikesDeleteResponse;