/**
 * Direct messages client for the X API.
 *
 * This module provides a client for interacting with the Direct messages endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  DirectMessagesGetDmEventsByIdResponse,
  DirectMessagesDeleteDmEventsResponse,
  DirectMessagesGetDmEventsByParticipantIdResponse,
  DirectMessagesGetDmConversationsIdDmEventsResponse,
  DirectMessagesCreateDmByConversationIdRequest,
  DirectMessagesCreateDmByConversationIdResponse,
  DirectMessagesGetDmEventsResponse,
  DirectMessagesCreateDmConversationsRequest,
  DirectMessagesCreateDmConversationsResponse,
  DirectMessagesCreateDmByParticipantIdRequest,
  DirectMessagesCreateDmByParticipantIdResponse,
} from './models.js';

/**
 * Client for Direct messages operations
 */
export class DirectMessagesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get DM event by ID
     * Retrieves details of a specific direct message event by its ID.
     * @param eventId dm event id.
     * @param dmEventfields A comma separated list of DmEvent fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getDmEventsById(
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesGetDmEventsByIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_events/{event_id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<DirectMessagesGetDmEventsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Delete DM event
     * Deletes a specific direct message event by its ID, if owned by the authenticated user.
     * @param eventId The ID of the direct-message event to delete.* @param options Additional request options
     * @returns Promise with the API response
     */
  async deleteDmEvents(
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesDeleteDmEventsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_events/{event_id}`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<DirectMessagesDeleteDmEventsResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get DM events for a DM conversation
     * Retrieves direct message events for a specific conversation.
     * @param participantId The ID of the participant user for the One to One DM conversation.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param eventTypes The set of event_types to include in the results.
     * @param dmEventfields A comma separated list of DmEvent fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getDmEventsByParticipantId(
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesGetDmEventsByParticipantIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_conversations/with/{participant_id}/dm_events`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<
      DirectMessagesGetDmEventsByParticipantIdResponse
    >(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get DM events for a DM conversation
     * Retrieves direct message events for a specific conversation.
     * @param id The DM conversation ID.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param eventTypes The set of event_types to include in the results.
     * @param dmEventfields A comma separated list of DmEvent fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getDmConversationsIdDmEvents(
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesGetDmConversationsIdDmEventsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_conversations/{id}/dm_events`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<
      DirectMessagesGetDmConversationsIdDmEventsResponse
    >(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create DM message by conversation ID
     * Sends a new direct message to a specific conversation by its ID.
     * @param dmConversationId The DM Conversation ID.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createDmByConversationId(
    body?: DirectMessagesCreateDmByConversationIdRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesCreateDmByConversationIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_conversations/{dm_conversation_id}/messages`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<DirectMessagesCreateDmByConversationIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get DM events
     * Retrieves a list of recent direct message events across all conversations.
     * @param maxResults The maximum number of results.
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * @param eventTypes The set of event_types to include in the results.
     * @param dmEventfields A comma separated list of DmEvent fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getDmEvents(
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesGetDmEventsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_events`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<DirectMessagesGetDmEventsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create DM conversation
     * Initiates a new direct message conversation with specified participants.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createDmConversations(
    body?: DirectMessagesCreateDmConversationsRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesCreateDmConversationsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_conversations`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<DirectMessagesCreateDmConversationsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create DM message by participant ID
     * Sends a new direct message to a specific participant by their ID.
     * @param participantId The ID of the recipient user that will receive the DM.* @param body Request body* @param options Additional request options
     * @returns Promise with the API response
     */
  async createDmByParticipantId(
    body?: DirectMessagesCreateDmByParticipantIdRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<DirectMessagesCreateDmByParticipantIdResponse>> {
    const params = new URLSearchParams();

    const path = `/2/dm_conversations/with/{participant_id}/messages`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<DirectMessagesCreateDmByParticipantIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
