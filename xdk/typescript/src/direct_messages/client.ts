/**
 * Direct messages client for the X API.
 *
 * This module provides a client for interacting with the Direct messages endpoints of the X API.
 */

import { Client } from "../client.js";
import {
  DirectMessagesCreateDmByParticipantIdRequest,
  DirectMessagesCreateDmByParticipantIdResponse,
  DirectMessagesGetDmEventsByParticipantIdResponse,
  DirectMessagesGetDmEventsByIdResponse,
  DirectMessagesDeleteDmEventsResponse,
  DirectMessagesGetDmConversationsIdDmEventsResponse,
  DirectMessagesCreateDmConversationsRequest,
  DirectMessagesCreateDmConversationsResponse,
  DirectMessagesCreateDmByConversationIdRequest,
  DirectMessagesCreateDmByConversationIdResponse,
  DirectMessagesGetDmEventsResponse
} from "./models.js";

/**
 * Client for Direct messages operations
 */
export class DirectMessagesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Create DM message by participant ID
     * Sends a new direct message to a specific participant by their ID.
     * @param participantId The ID of the recipient user that will receive the DM.* @param body Request body* @returns DirectMessagesCreateDmByParticipantIdResponse Response data
     */
  async createDmByParticipantId(
    participantId: string,
    body?: DirectMessagesCreateDmByParticipantIdRequest
  ): Promise<Record<string, any>> {
    let url =
      this.client.baseUrl +
      "/2/dm_conversations/with/{participant_id}/messages";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{participant_id}", String(participantId));

    const headers = new Headers();

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesCreateDmByParticipantIdResponse;
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
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns DirectMessagesGetDmEventsByParticipantIdResponse Response data
     */
  async getDmEventsByParticipantId(
    participantId: string,
    maxResults?: number,
    paginationToken?: string,
    eventTypes?: Array<any>,
    dmEventfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    userfields?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<DirectMessagesGetDmEventsByParticipantIdResponse> {
    let url =
      this.client.baseUrl +
      "/2/dm_conversations/with/{participant_id}/dm_events";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (eventTypes !== undefined) {
      params.set("event_types", eventTypes.map(String).join(","));
    }

    if (dmEventfields !== undefined) {
      params.set("dm_event.fields", dmEventfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{participant_id}", String(participantId));

    const headers = new Headers();

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesGetDmEventsByParticipantIdResponse;
  }

  /**
     * Get DM event by ID
     * Retrieves details of a specific direct message event by its ID.
     * @param eventId dm event id.
     * @param dmEventfields A comma separated list of DmEvent fields to display.
     * @param expansions A comma separated list of fields to expand.
     * @param mediafields A comma separated list of Media fields to display.
     * @param userfields A comma separated list of User fields to display.
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns DirectMessagesGetDmEventsByIdResponse Response data
     */
  async getDmEventsById(
    eventId: string,
    dmEventfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    userfields?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<DirectMessagesGetDmEventsByIdResponse> {
    let url = this.client.baseUrl + "/2/dm_events/{event_id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (dmEventfields !== undefined) {
      params.set("dm_event.fields", dmEventfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{event_id}", String(eventId));

    const headers = new Headers();

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesGetDmEventsByIdResponse;
  }

  /**
     * Delete DM event
     * Deletes a specific direct message event by its ID, if owned by the authenticated user.
     * @param eventId The ID of the direct-message event to delete.* @returns DirectMessagesDeleteDmEventsResponse Response data
     */
  async deleteDmEvents(
    eventId: string
  ): Promise<DirectMessagesDeleteDmEventsResponse> {
    let url = this.client.baseUrl + "/2/dm_events/{event_id}";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{event_id}", String(eventId));

    const headers = new Headers();

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "DELETE",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesDeleteDmEventsResponse;
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
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns DirectMessagesGetDmConversationsIdDmEventsResponse Response data
     */
  async getDmConversationsIdDmEvents(
    id: string,
    maxResults?: number,
    paginationToken?: string,
    eventTypes?: Array<any>,
    dmEventfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    userfields?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<DirectMessagesGetDmConversationsIdDmEventsResponse> {
    let url = this.client.baseUrl + "/2/dm_conversations/{id}/dm_events";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (eventTypes !== undefined) {
      params.set("event_types", eventTypes.map(String).join(","));
    }

    if (dmEventfields !== undefined) {
      params.set("dm_event.fields", dmEventfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    url = url.replace("{id}", String(id));

    const headers = new Headers();

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesGetDmConversationsIdDmEventsResponse;
  }

  /**
     * Create DM conversation
     * Initiates a new direct message conversation with specified participants.* @param body Request body* @returns DirectMessagesCreateDmConversationsResponse Response data
     */
  async createDmConversations(
    body?: DirectMessagesCreateDmConversationsRequest
  ): Promise<Record<string, any>> {
    let url = this.client.baseUrl + "/2/dm_conversations";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    const headers = new Headers();

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesCreateDmConversationsResponse;
  }

  /**
     * Create DM message by conversation ID
     * Sends a new direct message to a specific conversation by its ID.
     * @param dmConversationId The DM Conversation ID.* @param body Request body* @returns DirectMessagesCreateDmByConversationIdResponse Response data
     */
  async createDmByConversationId(
    dmConversationId: string,
    body?: DirectMessagesCreateDmByConversationIdRequest
  ): Promise<Record<string, any>> {
    let url =
      this.client.baseUrl + "/2/dm_conversations/{dm_conversation_id}/messages";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    url = url.replace("{dm_conversation_id}", String(dmConversationId));

    const headers = new Headers();

    headers.set("Content-Type", "application/json");

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "POST",
        headers,

        body: body ? JSON.stringify(body) : undefined
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesCreateDmByConversationIdResponse;
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
     * @param tweetfields A comma separated list of Tweet fields to display.* @returns DirectMessagesGetDmEventsResponse Response data
     */
  async getDmEvents(
    maxResults?: number,
    paginationToken?: string,
    eventTypes?: Array<any>,
    dmEventfields?: Array<any>,
    expansions?: Array<any>,
    mediafields?: Array<any>,
    userfields?: Array<any>,
    tweetfields?: Array<any>
  ): Promise<DirectMessagesGetDmEventsResponse> {
    let url = this.client.baseUrl + "/2/dm_events";

    // Ensure we have a valid access token
    if (this.client.oauth2Auth && this.client.token) {
      // Check if token needs refresh
      if (this.client.isTokenExpired()) {
        await this.client.refreshToken();
      }
    }
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.set("max_results", String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.set("pagination_token", String(paginationToken));
    }

    if (eventTypes !== undefined) {
      params.set("event_types", eventTypes.map(String).join(","));
    }

    if (dmEventfields !== undefined) {
      params.set("dm_event.fields", dmEventfields.map(String).join(","));
    }

    if (expansions !== undefined) {
      params.set("expansions", expansions.map(String).join(","));
    }

    if (mediafields !== undefined) {
      params.set("media.fields", mediafields.map(String).join(","));
    }

    if (userfields !== undefined) {
      params.set("user.fields", userfields.map(String).join(","));
    }

    if (tweetfields !== undefined) {
      params.set("tweet.fields", tweetfields.map(String).join(","));
    }

    const headers = new Headers();

    // Make the request

    const response = await (this.client.oauth2Session || fetch)(
      url + (params.toString() ? `?${params.toString()}` : ""),
      {
        method: "GET",
        headers
      }
    );

    // Check for errors
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Parse the response data
    const responseData = await response.json();

    return responseData as DirectMessagesGetDmEventsResponse;
  }
}
