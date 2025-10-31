/**
 * Models for community notes operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for searchWritten
 * 
 * @public
 */
export type SearchWrittenResponse = Schemas.Get2NotesSearchNotesWrittenResponse;
/**
 * Response for delete
 * 
 * @public
 */
export type DeleteResponse = Schemas.DeleteNoteResponse;
/**
 * Response for searchEligiblePosts
 * 
 * @public
 */
export type SearchEligiblePostsResponse = Schemas.Get2NotesSearchPostsEligibleForNotesResponse;
/**
 * Request for create
 * 
 * @public
 */
export type CreateRequest = Schemas.CreateNoteRequest;
/**
 * Response for create
 * 
 * @public
 */
export type CreateResponse = Schemas.CreateNoteResponse;
/**
 * Request for evaluate
 * 
 * @public
 */
export type EvaluateRequest = Schemas.EvaluateNoteRequest;
/**
 * Response for evaluate
 * 
 * @public
 */
export type EvaluateResponse = Schemas.EvaluateNoteResponse;