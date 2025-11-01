/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetEventsResponse,
  CreateByConversationIdResponse,
  CreateByParticipantIdResponse,
  GetEventsByIdResponse,
  DeleteEventsResponse,
  CreateConversationResponse,
  GetEventsByParticipantIdResponse,
  GetEventsByConversationIdResponse,
} from './models.js';

/**
 * Options for getEvents method
 * 
 * @public
 */
export interface GetEventsStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: any;

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
 * 
 * @public
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
/**
 * Options for createByParticipantId method
 * 
 * @public
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
 * Options for getEventsById method
 * 
 * @public
 */
export interface GetEventsByIdStreamingOptions {
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
 * 
 * @public
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
 * Options for createConversation method
 * 
 * @public
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
 * Options for getEventsByParticipantId method
 * 
 * @public
 */
export interface GetEventsByParticipantIdStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: any;

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
 * 
 * @public
 */
export interface GetEventsByConversationIdStreamingOptions {
  /** The maximum number of results. */
  maxResults?: number;

  /** This parameter is used to get a specified 'page' of results. */
  paginationToken?: any;

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
    options: GetEventsStreamingOptions = {}
  ): Promise<GetEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getEvents');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      eventTypes = [],

      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_events';

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetEventsResponse>(
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

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_conversations/{dm_conversation_id}/messages';

    path = path.replace(
      '{dm_conversation_id}',
      encodeURIComponent(String(dmConversationId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateByConversationIdResponse>(
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

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_conversations/with/{participant_id}/messages';

    path = path.replace(
      '{participant_id}',
      encodeURIComponent(String(participantId))
    );

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateByParticipantIdResponse>(
      'POST',
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
    options: GetEventsByIdStreamingOptions = {}
  ): Promise<GetEventsByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getEventsById');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_events/{event_id}';

    path = path.replace('{event_id}', encodeURIComponent(String(eventId)));

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
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
    eventId: string,
    options: DeleteEventsStreamingOptions = {}
  ): Promise<DeleteEventsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'deleteEvents');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/dm_events/{event_id}';

    path = path.replace('{event_id}', encodeURIComponent(String(eventId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<DeleteEventsResponse>(
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
    options: CreateConversationStreamingOptions = {}
  ): Promise<CreateConversationResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('OAuth2UserToken');

    requiredAuthTypes.push('UserToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createConversation');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      body,

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_conversations';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateConversationResponse>(
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

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      eventTypes = [],

      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_conversations/with/{participant_id}/dm_events';

    path = path.replace(
      '{participant_id}',
      encodeURIComponent(String(participantId))
    );

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetEventsByParticipantIdResponse>(
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

    // Destructure options (exclude path parameters, they're already function params)

    const {
      maxResults = undefined,

      paginationToken = undefined,

      eventTypes = [],

      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/dm_conversations/{id}/dm_events';

    path = path.replace('{id}', encodeURIComponent(String(id)));

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

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetEventsByConversationIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
