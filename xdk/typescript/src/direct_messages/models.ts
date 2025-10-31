/**
 * Models for direct messages operations
 */

/**
 * Response for getEventsByConversationId
 */
export interface GetEventsByConversationIdResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getEventsByParticipantId
 */
export interface GetEventsByParticipantIdResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getEventsById
 */
export interface GetEventsByIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for deleteEvents
 */
export interface DeleteEventsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getEvents
 */
export interface GetEventsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createByParticipantId
 */
export interface CreateByParticipantIdRequest {}

/**
 * Response for createByParticipantId
 */
export interface CreateByParticipantIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createConversation
 */
export interface CreateConversationRequest {
  /** The conversation type that is being created. */
  conversationType?: string;
  message?: any;
  /** Participants for the DM Conversation. */
  participantIds?: Array<any>;
}

/**
 * Response for createConversation
 */
export interface CreateConversationResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createByConversationId
 */
export interface CreateByConversationIdRequest {}

/**
 * Response for createByConversationId
 */
export interface CreateByConversationIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}
