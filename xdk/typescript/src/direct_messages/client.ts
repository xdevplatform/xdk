/**
 * direct messages client for the X API.
 *
 * This module provides a client for interacting with the direct messages endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetEventsByParticipantIdResponse,
  CreateByParticipantIdRequest,
  CreateByParticipantIdResponse,
  GetEventsByIdResponse,
  DeleteEventsResponse,
  CreateByConversationIdRequest,
  CreateByConversationIdResponse,
  CreateConversationRequest,
  CreateConversationResponse,
  GetEventsByConversationIdResponse,
  GetEventsResponse,
} from './models.js';

/**
 * Options for getEventsByParticipantId method
 * 
 * @public
 */
export interface GetEventsByParticipantIdOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createByParticipantId method
 * 
 * @public
 */
export interface CreateByParticipantIdOptions {
  /** Request body */
  body?: CreateByParticipantIdRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createByConversationId method
 * 
 * @public
 */
export interface CreateByConversationIdOptions {
  /** Request body */
  body?: CreateByConversationIdRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createConversation method
 * 
 * @public
 */
export interface CreateConversationOptions {
  /** Request body */
  body?: CreateConversationRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getEventsByConversationId method
 * 
 * @public
 */
export interface GetEventsByConversationIdOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getEvents method
 * 
 * @public
 */
export interface GetEventsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for direct messages operations
 * 
 * This client provides methods for interacting with the direct messages endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all direct messages related operations.
 * 
 * @category direct messages
 */
export class DirectMessagesClient {
  private client: Client;

  /**
     * Creates a new direct messages client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get DM events for a DM conversation
   * Retrieves direct message events for a specific conversation.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsByParticipantId(
    options: GetEventsByParticipantIdOptions = {}
  ): Promise<GetEventsByParticipantIdResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/dm_conversations/with/{participant_id}/dm_events';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetEventsByParticipantIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create DM message by participant ID
   * Sends a new direct message to a specific participant by their ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createByParticipantId(
    options: CreateByParticipantIdOptions = {}
  ): Promise<CreateByParticipantIdResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/dm_conversations/with/{participant_id}/messages';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CreateByParticipantIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get DM event by ID
   * Retrieves details of a specific direct message event by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsById(): Promise<GetEventsByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/dm_events/{event_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetEventsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete DM event
   * Deletes a specific direct message event by its ID, if owned by the authenticated user.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteEvents(): Promise<DeleteEventsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/dm_events/{event_id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DeleteEventsResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create DM message by conversation ID
   * Sends a new direct message to a specific conversation by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createByConversationId(
    options: CreateByConversationIdOptions = {}
  ): Promise<CreateByConversationIdResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/dm_conversations/{dm_conversation_id}/messages';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CreateByConversationIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create DM conversation
   * Initiates a new direct message conversation with specified participants.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createConversation(
    options: CreateConversationOptions = {}
  ): Promise<CreateConversationResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/dm_conversations';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<CreateConversationResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get DM events for a DM conversation
   * Retrieves direct message events for a specific conversation.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsByConversationId(
    options: GetEventsByConversationIdOptions = {}
  ): Promise<GetEventsByConversationIdResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/dm_conversations/{id}/dm_events';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetEventsByConversationIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get DM events
   * Retrieves a list of recent direct message events across all conversations.


   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getEvents(options: GetEventsOptions = {}): Promise<GetEventsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/dm_events';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetEventsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
