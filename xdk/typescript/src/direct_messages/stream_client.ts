/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  DirectMessagesGetEventsResponse,
  DirectMessagesCreateByConversationIdResponse,
  DirectMessagesGetEventsByParticipantIdResponse,
  DirectMessagesGetEventsByConversationIdResponse,
  DirectMessagesGetEventsByIdResponse,
  DirectMessagesDeleteEventsResponse,
  DirectMessagesCreateConversationResponse,
  DirectMessagesCreateByParticipantIdResponse,
} from './models.js';

/**
 * Options for getEvents method
 */
export interface DirectMessagesGetEventsStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** The set of event_types to include in the results. */
  eventTypes?: Array<any>;

  /** A comma separated list of DmEvent fields to display. */
  dmEventfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

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
export interface DirectMessagesCreateByConversationIdStreamingOptions {
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
 * Options for getEventsByParticipantId method
 */
export interface DirectMessagesGetEventsByParticipantIdStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** The set of event_types to include in the results. */
  eventTypes?: Array<any>;

  /** A comma separated list of DmEvent fields to display. */
  dmEventfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getEventsByConversationId method
 */
export interface DirectMessagesGetEventsByConversationIdStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: string;

  /** The set of event_types to include in the results. */
  eventTypes?: Array<any>;

  /** A comma separated list of DmEvent fields to display. */
  dmEventfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

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
export interface DirectMessagesGetEventsByIdStreamingOptions {
  /** A comma separated list of DmEvent fields to display. */
  dmEventfields?: Array<any>;

  /** A comma separated list of fields to expand. */
  expansions?: Array<any>;

  /** A comma separated list of Media fields to display. */
  mediafields?: Array<any>;

  /** A comma separated list of User fields to display. */
  userfields?: Array<any>;

  /** A comma separated list of Tweet fields to display. */
  tweetfields?: Array<any>;

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
export interface DirectMessagesDeleteEventsStreamingOptions {
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
export interface DirectMessagesCreateConversationStreamingOptions {
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
 * Options for createByParticipantId method
 */
export interface DirectMessagesCreateByParticipantIdStreamingOptions {
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
     * Get DM events
     * Retrieves a list of recent direct message events across all conversations.
     * 
     * @returns Promise with the API response
     */
  async getEvents(
    options: DirectMessagesGetEventsStreamingOptions = {}
  ): Promise<DirectMessagesGetEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getEvents');

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      eventTypes = [],

      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (eventTypes !== undefined) {
      params.append('event_types', eventTypes.join(','));
    }

    if (dmEventfields !== undefined) {
      params.append('dm_event.fields', dmEventfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

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
    return this.client.request<DirectMessagesGetEventsResponse>(
      'GET',
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
    dmConversationId: string,
    options: DirectMessagesCreateByConversationIdStreamingOptions = {}
  ): Promise<DirectMessagesCreateByConversationIdResponse> {
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

    path = path.replace(`{${'dm_conversation_id'}}`, String(dmConversationId));

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
    return this.client.request<DirectMessagesCreateByConversationIdResponse>(
      'POST',
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
    participantId: string,
    options: DirectMessagesGetEventsByParticipantIdStreamingOptions = {}
  ): Promise<DirectMessagesGetEventsByParticipantIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getEventsByParticipantId'
    );

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      eventTypes = [],

      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (eventTypes !== undefined) {
      params.append('event_types', eventTypes.join(','));
    }

    if (dmEventfields !== undefined) {
      params.append('dm_event.fields', dmEventfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Build path parameters
    let path = `/2/dm_conversations/with/{participant_id}/dm_events`;

    path = path.replace(`{${'participant_id'}}`, String(participantId));

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
    return this.client.request<DirectMessagesGetEventsByParticipantIdResponse>(
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
  async getEventsByConversationId(
    id: string,
    options: DirectMessagesGetEventsByConversationIdStreamingOptions = {}
  ): Promise<DirectMessagesGetEventsByConversationIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getEventsByConversationId'
    );

    // Destructure options with defaults

    const {
      maxResults = undefined,

      paginationToken = undefined,

      eventTypes = [],

      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (maxResults !== undefined) {
      params.append('max_results', String(maxResults));
    }

    if (paginationToken !== undefined) {
      params.append('pagination_token', String(paginationToken));
    }

    if (eventTypes !== undefined) {
      params.append('event_types', eventTypes.join(','));
    }

    if (dmEventfields !== undefined) {
      params.append('dm_event.fields', dmEventfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Build path parameters
    let path = `/2/dm_conversations/{id}/dm_events`;

    path = path.replace(`{${'id'}}`, String(id));

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
    return this.client.request<DirectMessagesGetEventsByConversationIdResponse>(
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
    eventId: string,
    options: DirectMessagesGetEventsByIdStreamingOptions = {}
  ): Promise<DirectMessagesGetEventsByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getEventsById');

    // Destructure options with defaults

    const {
      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (dmEventfields !== undefined) {
      params.append('dm_event.fields', dmEventfields.join(','));
    }

    if (expansions !== undefined) {
      params.append('expansions', expansions.join(','));
    }

    if (mediafields !== undefined) {
      params.append('media.fields', mediafields.join(','));
    }

    if (userfields !== undefined) {
      params.append('user.fields', userfields.join(','));
    }

    if (tweetfields !== undefined) {
      params.append('tweet.fields', tweetfields.join(','));
    }

    // Build path parameters
    let path = `/2/dm_events/{event_id}`;

    path = path.replace(`{${'event_id'}}`, String(eventId));

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
    return this.client.request<DirectMessagesGetEventsByIdResponse>(
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
    eventId: string,
    options: DirectMessagesDeleteEventsStreamingOptions = {}
  ): Promise<DirectMessagesDeleteEventsResponse> {
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

    path = path.replace(`{${'event_id'}}`, String(eventId));

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
    return this.client.request<DirectMessagesDeleteEventsResponse>(
      'DELETE',
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
    options: DirectMessagesCreateConversationStreamingOptions = {}
  ): Promise<DirectMessagesCreateConversationResponse> {
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
    return this.client.request<DirectMessagesCreateConversationResponse>(
      'POST',
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
    participantId: string,
    options: DirectMessagesCreateByParticipantIdStreamingOptions = {}
  ): Promise<DirectMessagesCreateByParticipantIdResponse> {
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

    path = path.replace(`{${'participant_id'}}`, String(participantId));

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
    return this.client.request<DirectMessagesCreateByParticipantIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
