/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetEventsByConversationIdResponse,
  GetEventsByParticipantIdResponse,
  GetEventsByIdResponse,
  DeleteEventsResponse,
  GetEventsResponse,
  CreateByParticipantIdResponse,
  CreateConversationResponse,
  CreateByConversationIdResponse,
} from './models.js';

/**
 * Options for getEventsByConversationId method
 */
export interface GetEventsByConversationIdStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getEventsByParticipantId method
 */
export interface GetEventsByParticipantIdStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getEventsById method
 */
export interface GetEventsByIdStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for deleteEvents method
 */
export interface DeleteEventsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getEvents method
 */
export interface GetEventsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createByParticipantId method
 */
export interface CreateByParticipantIdStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createConversation method
 */
export interface CreateConversationStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createByConversationId method
 */
export interface CreateByConversationIdStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class DirectMessagesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get DM events for a DM conversation
     * Retrieves direct message events for a specific conversation.
     * 
     * @returns Promise with the API response
     */
  async getEventsByConversationId(
    options: GetEventsByConversationIdStreamingOptions = {}
  ): Promise<GetEventsByConversationIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getEventsByConversationId'
    );

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_conversations/{id}/dm_events`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetEventsByConversationIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get DM events for a DM conversation
     * Retrieves direct message events for a specific conversation.
     * 
     * @returns Promise with the API response
     */
  async getEventsByParticipantId(
    options: GetEventsByParticipantIdStreamingOptions = {}
  ): Promise<GetEventsByParticipantIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getEventsByParticipantId'
    );

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_conversations/with/{participant_id}/dm_events`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetEventsByParticipantIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get DM event by ID
     * Retrieves details of a specific direct message event by its ID.
     * 
     * @returns Promise with the API response
     */
  async getEventsById(
    options: GetEventsByIdStreamingOptions = {}
  ): Promise<GetEventsByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getEventsById');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_events/{event_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetEventsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Delete DM event
     * Deletes a specific direct message event by its ID, if owned by the authenticated user.
     * 
     * @returns Promise with the API response
     */
  async deleteEvents(
    options: DeleteEventsStreamingOptions = {}
  ): Promise<DeleteEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteEvents');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_events/{event_id}`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<DeleteEventsResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get DM events
     * Retrieves a list of recent direct message events across all conversations.
     * 
     * @returns Promise with the API response
     */
  async getEvents(
    options: GetEventsStreamingOptions = {}
  ): Promise<GetEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getEvents');

    // Destructure options with defaults

    const { requestOptions: requestOptions = {} } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_events`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<GetEventsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create DM message by participant ID
     * Sends a new direct message to a specific participant by their ID.
     * 
     * @returns Promise with the API response
     */
  async createByParticipantId(
    options: CreateByParticipantIdStreamingOptions = {}
  ): Promise<CreateByParticipantIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'createByParticipantId'
    );

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_conversations/with/{participant_id}/messages`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<CreateByParticipantIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create DM conversation
     * Initiates a new direct message conversation with specified participants.
     * 
     * @returns Promise with the API response
     */
  async createConversation(
    options: CreateConversationStreamingOptions = {}
  ): Promise<CreateConversationResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createConversation');

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_conversations`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<CreateConversationResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create DM message by conversation ID
     * Sends a new direct message to a specific conversation by its ID.
     * 
     * @returns Promise with the API response
     */
  async createByConversationId(
    options: CreateByConversationIdStreamingOptions = {}
  ): Promise<CreateByConversationIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'createByConversationId'
    );

    // Destructure options with defaults

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_conversations/{dm_conversation_id}/messages`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<CreateByConversationIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
