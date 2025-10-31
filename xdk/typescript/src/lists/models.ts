/**
 * Models for lists operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getPosts
 * 
 * @public
 */
export type GetPostsResponse = Schemas.Get2ListsIdTweetsResponse;
/**
 * Response for getFollowers
 * 
 * @public
 */
export type GetFollowersResponse = Schemas.Get2ListsIdFollowersResponse;
/**
 * Response for getMembers
 * 
 * @public
 */
export type GetMembersResponse = Schemas.Get2ListsIdMembersResponse;
/**
 * Request for addMember
 * 
 * @public
 */
export type AddMemberRequest = Schemas.ListAddUserRequest;
/**
 * Response for addMember
 * 
 * @public
 */
export type AddMemberResponse = Schemas.ListMutateResponse;
/**
 * Response for getById
 * 
 * @public
 */
export type GetByIdResponse = Schemas.Get2ListsIdResponse;
/**
 * Request for update
 * 
 * @public
 */
export type UpdateRequest = Schemas.ListUpdateRequest;
/**
 * Response for update
 * 
 * @public
 */
export type UpdateResponse = Schemas.ListUpdateResponse;
/**
 * Response for delete
 * 
 * @public
 */
export type DeleteResponse = Schemas.ListDeleteResponse;
/**
 * Response for removeMemberByUserId
 * 
 * @public
 */
export type RemoveMemberByUserIdResponse = Schemas.ListMutateResponse;
/**
 * Request for create
 * 
 * @public
 */
export type CreateRequest = Schemas.ListCreateRequest;
/**
 * Response for create
 * 
 * @public
 */
export type CreateResponse = Schemas.ListCreateResponse;