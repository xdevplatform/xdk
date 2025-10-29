/**
 * Direct messages client for the X API.
 *
 * This module provides a client for interacting with the Direct messages endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  DirectMessagesGetEventsResponse,
  DirectMessagesCreateByConversationIdRequest,
  DirectMessagesCreateByConversationIdResponse,
  DirectMessagesGetEventsByParticipantIdResponse,
  DirectMessagesGetEventsByConversationIdResponse,
  DirectMessagesGetEventsByIdResponse,
  DirectMessagesDeleteEventsResponse,
  DirectMessagesCreateConversationRequest,
  DirectMessagesCreateConversationResponse,
  DirectMessagesCreateByParticipantIdRequest,
  DirectMessagesCreateByParticipantIdResponse,
} from './models.js';

/**
 * Options for getEvents method
 */
export interface DirectMessagesGetEventsOptions {
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
}

/**
 * Options for createByConversationId method
 */
export interface DirectMessagesCreateByConversationIdOptions {
  /** Request body */
  body?: DirectMessagesCreateByConversationIdRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getEventsByParticipantId method
 */
export interface DirectMessagesGetEventsByParticipantIdOptions {
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
}

/**
 * Options for getEventsByConversationId method
 */
export interface DirectMessagesGetEventsByConversationIdOptions {
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
}

/**
 * Options for getEventsById method
 */
export interface DirectMessagesGetEventsByIdOptions {
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
}

/**
 * Options for createConversation method
 */
export interface DirectMessagesCreateConversationOptions {
  /** Request body */
  body?: DirectMessagesCreateConversationRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for createByParticipantId method
 */
export interface DirectMessagesCreateByParticipantIdOptions {
  /** Request body */
  body?: DirectMessagesCreateByParticipantIdRequest;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Direct messages operations
 * 
 * This client provides methods for interacting with the Direct messages endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Direct messages related operations.
 * 
 * @category Direct messages
 */
export class DirectMessagesClient {
  private client: Client;

  /**
     * Creates a new Direct messages client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Create DM message by conversation ID
   * Sends a new direct message to a specific conversation by its ID.


   * @param dmConversationId The DM Conversation ID.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createByConversationId(
    dmConversationId: string,
    options: DirectMessagesCreateByConversationIdOptions = {}
  ): Promise<DirectMessagesCreateByConversationIdResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

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
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<DirectMessagesCreateByConversationIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get DM event by ID
   * Retrieves details of a specific direct message event by its ID.


   * @param eventId dm event id.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getEventsById(
    eventId: string,
    options: DirectMessagesGetEventsByIdOptions = {}
  ): Promise<DirectMessagesGetEventsByIdResponse> {
    // Destructure options

    const {
      dmEventfields = [],

      expansions = [],

      mediafields = [],

      userfields = [],

      tweetfields = [],

      requestOptions: requestOptions = {},
    } = options;

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
      ...requestOptions,
    };

    return this.client.request<DirectMessagesGetEventsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Delete DM event
   * Deletes a specific direct message event by its ID, if owned by the authenticated user.


   * @param eventId The ID of the direct-message event to delete.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async deleteEvents(
    eventId: string
  ): Promise<DirectMessagesDeleteEventsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/dm_events/{event_id}';

    path = path.replace('{event_id}', encodeURIComponent(String(eventId)));

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<DirectMessagesDeleteEventsResponse>(
      'DELETE',
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
    options: DirectMessagesCreateConversationOptions = {}
  ): Promise<DirectMessagesCreateConversationResponse> {
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

    return this.client.request<DirectMessagesCreateConversationResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create DM message by participant ID
   * Sends a new direct message to a specific participant by their ID.


   * @param participantId The ID of the recipient user that will receive the DM.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createByParticipantId(
    participantId: string,
    options: DirectMessagesCreateByParticipantIdOptions = {}
  ): Promise<DirectMessagesCreateByParticipantIdResponse> {
    // Destructure options

    const {
      body,

      requestOptions: requestOptions = {},
    } = options;

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
      body: body ? JSON.stringify(body) : undefined,

      ...requestOptions,
    };

    return this.client.request<DirectMessagesCreateByParticipantIdResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get DM events
   * Retrieves a list of recent direct message events across all conversations.
   * Returns a paginator for automatic pagination through all results.

   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getEvents(
    options: DirectMessagesGetEventsOptions = {}
  ): Promise<EventPaginator> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/dm_events';

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...requestOptions,
      };

      const response = await this.client.request<
        DirectMessagesGetEventsResponse
      >(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new EventPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get DM events for a DM conversation
   * Retrieves direct message events for a specific conversation.
   * Returns a paginator for automatic pagination through all results.


   * @param participantId The ID of the participant user for the One to One DM conversation.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getEventsByParticipantId(
    participantId: string,
    options: DirectMessagesGetEventsByParticipantIdOptions = {}
  ): Promise<EventPaginator> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/dm_conversations/with/{participant_id}/dm_events';

    path = path.replace(
      '{participant_id}',
      encodeURIComponent(String(participantId))
    );

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...requestOptions,
      };

      const response = await this.client.request<
        DirectMessagesGetEventsByParticipantIdResponse
      >(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new EventPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }

  /**
   * Get DM events for a DM conversation
   * Retrieves direct message events for a specific conversation.
   * Returns a paginator for automatic pagination through all results.


   * @param id The DM conversation ID.


   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  async getEventsByConversationId(
    id: string,
    options: DirectMessagesGetEventsByConversationIdOptions = {}
  ): Promise<EventPaginator> {
    // Destructure options

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

    // Build the path with path parameters
    let path = '/2/dm_conversations/{id}/dm_events';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
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

      // Add pagination token if provided
      if (paginationToken) {
        params.set('pagination_token', paginationToken);
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
        ...requestOptions,
      };

      const response = await this.client.request<
        DirectMessagesGetEventsByConversationIdResponse
      >(
        'GET',
        path + (params.toString() ? `?${params.toString()}` : ''),
        finalRequestOptions
      );

      return {
        data: Array.isArray(response.data) ? response.data : [],
        meta: (response as any).meta,
        includes: (response as any).includes,
        errors: (response as any).errors,
      };
    };

    // Create paginator and fetch first page
    const paginator = new EventPaginator(fetchPage);

    // Fetch the first page immediately
    await paginator.fetchNext();

    return paginator;
  }
}
