/**
 * Models for direct messages operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getEvents
 * 
 * @public
 */
export type GetEventsResponse = Schemas.Get2DmEventsResponse;
/**
 * Response for getEventsByParticipantId
 * 
 * @public
 */
export type GetEventsByParticipantIdResponse = Schemas.Get2DmConversationsWithParticipantIdDmEventsResponse;
/**
 * Request for createByConversationId
 * 
 * @public
 */
export type CreateByConversationIdRequest = Schemas.CreateMessageRequest;
/**
 * Response for createByConversationId
 * 
 * @public
 */
export type CreateByConversationIdResponse = Schemas.CreateDmEventResponse;
/**
 * Request for createByParticipantId
 * 
 * @public
 */
export type CreateByParticipantIdRequest = Schemas.CreateMessageRequest;
/**
 * Response for createByParticipantId
 * 
 * @public
 */
export type CreateByParticipantIdResponse = Schemas.CreateDmEventResponse;
/**
 * Response for getEventsByConversationId
 * 
 * @public
 */
export type GetEventsByConversationIdResponse = Schemas.Get2DmConversationsIdDmEventsResponse;
/**
 * Response for getEventsById
 * 
 * @public
 */
export type GetEventsByIdResponse = Schemas.Get2DmEventsEventIdResponse;
/**
 * Response for deleteEvents
 * 
 * @public
 */
export type DeleteEventsResponse = Schemas.DeleteDmResponse;
/**
 * Request for createConversation
 * 
 * @public
 */
export type CreateConversationRequest = Schemas.CreateDmConversationRequest;
/**
 * Response for createConversation
 * 
 * @public
 */
export type CreateConversationResponse = Schemas.CreateDmEventResponse;