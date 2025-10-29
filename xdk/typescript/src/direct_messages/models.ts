/**
 * Models for Direct messages operations
 */

/**
 * Response for getEvents
 */
export interface DirectMessagesGetEventsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createByConversationId
 */
export interface DirectMessagesCreateByConversationIdRequest {}

/**
 * Response for createByConversationId
 */
export interface DirectMessagesCreateByConversationIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getEventsByParticipantId
 */
export interface DirectMessagesGetEventsByParticipantIdResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getEventsByConversationId
 */
export interface DirectMessagesGetEventsByConversationIdResponse {
  data?: Array<any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
  meta?: Record<string, any>;
}

/**
 * Response for getEventsById
 */
export interface DirectMessagesGetEventsByIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
  includes?: Record<string, any>;
}

/**
 * Response for deleteEvents
 */
export interface DirectMessagesDeleteEventsResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createConversation
 */
export interface DirectMessagesCreateConversationRequest {
  /** The conversation type that is being created. */
  conversationType?: string;
  message?: any;
  /** Participants for the DM Conversation. */
  participantIds?: Array<any>;
}

/**
 * Response for createConversation
 */
export interface DirectMessagesCreateConversationResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createByParticipantId
 */
export interface DirectMessagesCreateByParticipantIdRequest {}

/**
 * Response for createByParticipantId
 */
export interface DirectMessagesCreateByParticipantIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}
