/**
 * Models for Direct messages operations
 */






/**
 * Request body for createDmByConversationId
 * 
 */
export interface DirectMessagesCreateDmByConversationIdRequest {
    
}







/**
 * Response for createDmByConversationId
 * 
 */
export interface DirectMessagesCreateDmByConversationIdResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for getDmEvents
 * 
 */
export interface DirectMessagesGetDmEventsResponse {
    
    
    
    
    data?: Array<any>;
    
    
    
    errors?: Array<any>;
    
    
    
    includes?: Record<string, any>;
    
    
    
    meta?: Record<string, any>;
    
    
}









/**
 * Response for getDmEventsByParticipantId
 * 
 */
export interface DirectMessagesGetDmEventsByParticipantIdResponse {
    
    
    
    
    data?: Array<any>;
    
    
    
    errors?: Array<any>;
    
    
    
    includes?: Record<string, any>;
    
    
    
    meta?: Record<string, any>;
    
    
}









/**
 * Response for getDmConversationsIdDmEvents
 * 
 */
export interface DirectMessagesGetDmConversationsIdDmEventsResponse {
    
    
    
    
    data?: Array<any>;
    
    
    
    errors?: Array<any>;
    
    
    
    includes?: Record<string, any>;
    
    
    
    meta?: Record<string, any>;
    
    
}








/**
 * Request body for createDmConversations
 * 
 */
export interface DirectMessagesCreateDmConversationsRequest {
    
    
    
    
    /** The conversation type that is being created. */
    
    conversationType?: string;
    
    
    
    message?: any;
    
    
    
    /** Participants for the DM Conversation. */
    
    participantIds?: Array<any>;
    
    
}







/**
 * Response for createDmConversations
 * 
 */
export interface DirectMessagesCreateDmConversationsResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}









/**
 * Response for getDmEventsById
 * 
 */
export interface DirectMessagesGetDmEventsByIdResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
    
    includes?: Record<string, any>;
    
    
}









/**
 * Response for deleteDmEvents
 * 
 */
export interface DirectMessagesDeleteDmEventsResponse {
    
    
    
    
    data?: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}








/**
 * Request body for createDmByParticipantId
 * 
 */
export interface DirectMessagesCreateDmByParticipantIdRequest {
    
}







/**
 * Response for createDmByParticipantId
 * 
 */
export interface DirectMessagesCreateDmByParticipantIdResponse {
    
    
    
    
    data: Record<string, any>;
    
    
    
    errors?: Array<any>;
    
    
}



 