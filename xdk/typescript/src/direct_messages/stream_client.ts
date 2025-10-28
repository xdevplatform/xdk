/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  DirectMessagesCreateDmByParticipantIdResponse,
  DirectMessagesGetDmConversationsIdDmEventsResponse,
  DirectMessagesGetDmEventsResponse,
  DirectMessagesCreateDmConversationsResponse,
  DirectMessagesCreateDmByConversationIdResponse,
  DirectMessagesGetDmEventsByParticipantIdResponse,
  DirectMessagesGetDmEventsByIdResponse,
  DirectMessagesDeleteDmEventsResponse,
} from './models.js';

/**
 * Options for createDmByParticipantId method
 */
export interface DirectMessagesCreateDmByParticipantIdStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getDmConversationsIdDmEvents method
 */
export interface DirectMessagesGetDmConversationsIdDmEventsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getDmEvents method
 */
export interface DirectMessagesGetDmEventsStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for createDmConversations method
 */
export interface DirectMessagesCreateDmConversationsStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for createDmByConversationId method
 */
export interface DirectMessagesCreateDmByConversationIdStreamingOptions {
  /** Request body */
  body?: any;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getDmEventsByParticipantId method
 */
export interface DirectMessagesGetDmEventsByParticipantIdStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

/**
 * Options for getDmEventsById method
 */
export interface DirectMessagesGetDmEventsByIdStreamingOptions {
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
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class DirectMessagesClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Create DM message by participant ID
     * Sends a new direct message to a specific participant by their ID.
     * 
     * @returns Promise with the API response
     */
  async createDmByParticipantId(
    participantId: string,
    options: DirectMessagesCreateDmByParticipantIdStreamingOptions = {}
  ): Promise<DirectMessagesCreateDmByParticipantIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'createDmByParticipantId'
    );

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
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
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<DirectMessagesCreateDmByParticipantIdResponse>(
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
  async getDmConversationsIdDmEvents(
    id: string,
    options: DirectMessagesGetDmConversationsIdDmEventsStreamingOptions = {}
  ): Promise<DirectMessagesGetDmConversationsIdDmEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getDmConversationsIdDmEvents'
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

      requestOptions: reqOpts = {},
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
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<
      DirectMessagesGetDmConversationsIdDmEventsResponse
    >(
      'GET',
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
  async getDmEvents(
    options: DirectMessagesGetDmEventsStreamingOptions = {}
  ): Promise<DirectMessagesGetDmEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getDmEvents');

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

      requestOptions: reqOpts = {},
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
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<DirectMessagesGetDmEventsResponse>(
      'GET',
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
  async createDmConversations(
    options: DirectMessagesCreateDmConversationsStreamingOptions = {}
  ): Promise<DirectMessagesCreateDmConversationsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'createDmConversations'
    );

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_conversations`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<DirectMessagesCreateDmConversationsResponse>(
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
  async createDmByConversationId(
    dmConversationId: string,
    options: DirectMessagesCreateDmByConversationIdStreamingOptions = {}
  ): Promise<DirectMessagesCreateDmByConversationIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'createDmByConversationId'
    );

    // Destructure options with defaults

    const {
      body,

      requestOptions: reqOpts = {},
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
        ...reqOpts.headers,
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...reqOpts,
    };

    // Make the request
    return this.client.request<DirectMessagesCreateDmByConversationIdResponse>(
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
  async getDmEventsByParticipantId(
    participantId: string,
    options: DirectMessagesGetDmEventsByParticipantIdStreamingOptions = {}
  ): Promise<DirectMessagesGetDmEventsByParticipantIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(
      requiredAuthTypes,
      'getDmEventsByParticipantId'
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

      requestOptions: reqOpts = {},
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
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<
      DirectMessagesGetDmEventsByParticipantIdResponse
    >(
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
  async getDmEventsById(
    eventId: string,
    options: DirectMessagesGetDmEventsByIdStreamingOptions = {}
  ): Promise<DirectMessagesGetDmEventsByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getDmEventsById');

    // Destructure options with defaults

    const {
      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      requestOptions: reqOpts = {},
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
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<DirectMessagesGetDmEventsByIdResponse>(
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
  async deleteDmEvents(
    eventId: string
  ): Promise<DirectMessagesDeleteDmEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteDmEvents');

    // Destructure options with defaults

    const reqOpts = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/dm_events/{event_id}`;

    path = path.replace(`{${'event_id'}}`, String(eventId));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...reqOpts.headers,
      },
      signal: options.signal,

      ...reqOpts,
    };

    // Make the request
    return this.client.request<DirectMessagesDeleteDmEventsResponse>(
      'DELETE',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
