
/**
 * Direct messages client for the X API.
 *
 * This module provides a client for interacting with the Direct messages endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { 
    TwitterPaginator, 
    TweetPaginator, 
    UserPaginator, 
    ListPaginator, 
    IdPaginator 
} from '../paginator.js';
import {
DirectMessagesCreateDmByParticipantIdRequest,
DirectMessagesCreateDmByParticipantIdResponse,
DirectMessagesGetDmConversationsIdDmEventsResponse,
DirectMessagesGetDmEventsResponse,
DirectMessagesCreateDmConversationsRequest,
DirectMessagesCreateDmConversationsResponse,
DirectMessagesCreateDmByConversationIdRequest,
DirectMessagesCreateDmByConversationIdResponse,
DirectMessagesGetDmEventsByParticipantIdResponse,
DirectMessagesGetDmEventsByIdResponse,
DirectMessagesDeleteDmEventsResponse,
} from './models.js';


/**
 * Options for createDmByParticipantId method
 */
export interface DirectMessagesCreateDmByParticipantIdOptions {
    
    
    /** Request body */
    body?: DirectMessagesCreateDmByParticipantIdRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getDmConversationsIdDmEvents method
 */
export interface DirectMessagesGetDmConversationsIdDmEventsOptions {
    
    
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
 * Options for getDmEvents method
 */
export interface DirectMessagesGetDmEventsOptions {
    
    
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
 * Options for createDmConversations method
 */
export interface DirectMessagesCreateDmConversationsOptions {
    
    
    /** Request body */
    body?: DirectMessagesCreateDmConversationsRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for createDmByConversationId method
 */
export interface DirectMessagesCreateDmByConversationIdOptions {
    
    
    /** Request body */
    body?: DirectMessagesCreateDmByConversationIdRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getDmEventsByParticipantId method
 */
export interface DirectMessagesGetDmEventsByParticipantIdOptions {
    
    
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
 * Options for getDmEventsById method
 */
export interface DirectMessagesGetDmEventsByIdOptions {
    
    
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
   * @param participantId The ID of the recipient user that will receive the DM.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async createDmByParticipantId(
        
        
        
        participantId: string,
        
        
        
        
        
        
        options: DirectMessagesCreateDmByParticipantIdOptions = {}
        
    ): Promise<DirectMessagesCreateDmByParticipantIdResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/dm_conversations/with/{participant_id}/messages';
        
        
        path = path.replace('{participant_id}', encodeURIComponent(String(participantId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<DirectMessagesCreateDmByParticipantIdResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }








  /**
   * Create DM conversation
   * Initiates a new direct message conversation with specified participants.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async createDmConversations(
        
        
        
        
        
        
        options: DirectMessagesCreateDmConversationsOptions = {}
        
    ): Promise<DirectMessagesCreateDmConversationsResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/dm_conversations';
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<DirectMessagesCreateDmConversationsResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Create DM message by conversation ID
   * Sends a new direct message to a specific conversation by its ID.
   * @param dmConversationId The DM Conversation ID.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async createDmByConversationId(
        
        
        
        dmConversationId: string,
        
        
        
        
        
        
        options: DirectMessagesCreateDmByConversationIdOptions = {}
        
    ): Promise<DirectMessagesCreateDmByConversationIdResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/dm_conversations/{dm_conversation_id}/messages';
        
        
        path = path.replace('{dm_conversation_id}', encodeURIComponent(String(dmConversationId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<DirectMessagesCreateDmByConversationIdResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Get DM event by ID
   * Retrieves details of a specific direct message event by its ID.
   * @param eventId dm event id.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getDmEventsById(
        
        
        
        eventId: string,
        
        
        
        
        
        
        options: DirectMessagesGetDmEventsByIdOptions = {}
        
    ): Promise<DirectMessagesGetDmEventsByIdResponse> {
        // Destructure options
        
        const {
            
            
            dmEventfields = [],
            
            
            
            expansions = [],
            
            
            
            mediafields = [],
            
            
            
            userfields = [],
            
            
            
            tweetfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/dm_events/{event_id}';
        
        
        path = path.replace('{event_id}', encodeURIComponent(String(eventId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (dmEventfields !== undefined) {
            
            dmEventfields.forEach(item => params.append('dm_event.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (mediafields !== undefined) {
            
            mediafields.forEach(item => params.append('media.fields', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (tweetfields !== undefined) {
            
            tweetfields.forEach(item => params.append('tweet.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<DirectMessagesGetDmEventsByIdResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Delete DM event
   * Deletes a specific direct message event by its ID, if owned by the authenticated user.
   * @param eventId The ID of the direct-message event to delete.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async deleteDmEvents(
        
        
        
        eventId: string,
        
        
        
        
        
        
    ): Promise<DirectMessagesDeleteDmEventsResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/dm_events/{event_id}';
        
        
        path = path.replace('{event_id}', encodeURIComponent(String(eventId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<DirectMessagesDeleteDmEventsResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }








  /**
   * Get DM events for a DM conversation
   * Retrieves direct message events for a specific conversation.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getDmConversationsIdDmEvents(
    
    
    
    id: string,
    
    
    
    
    options: DirectMessagesGetDmConversationsIdDmEventsOptions = {}
    
  ): IdPaginator {
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
        
        
        requestOptions: reqOpts = {}
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
          
          eventTypes.forEach(item => params.append('event_types', String(item)));
          
      }
      
      
      
      
      
      if (dmEventfields !== undefined) {
          
          dmEventfields.forEach(item => params.append('dm_event.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<DirectMessagesGetDmConversationsIdDmEventsResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new IdPaginator(fetchPage);
  }




  /**
   * Get DM events
   * Retrieves a list of recent direct message events across all conversations.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getDmEvents(
    
    
    
    
    options: DirectMessagesGetDmEventsOptions = {}
    
  ): TwitterPaginator<any> {
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
        
        
        requestOptions: reqOpts = {}
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
          
          eventTypes.forEach(item => params.append('event_types', String(item)));
          
      }
      
      
      
      
      
      if (dmEventfields !== undefined) {
          
          dmEventfields.forEach(item => params.append('dm_event.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<DirectMessagesGetDmEventsResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new TwitterPaginator(fetchPage);
  }








  /**
   * Get DM events for a DM conversation
   * Retrieves direct message events for a specific conversation.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   participantId: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getDmEventsByParticipantId(
    
    
    
    participantId: string,
    
    
    
    
    options: DirectMessagesGetDmEventsByParticipantIdOptions = {}
    
  ): IdPaginator {
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
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/dm_conversations/with/{participant_id}/dm_events';
    
    
    path = path.replace('{participant_id}', encodeURIComponent(String(participantId)));
    
    

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
          
          eventTypes.forEach(item => params.append('event_types', String(item)));
          
      }
      
      
      
      
      
      if (dmEventfields !== undefined) {
          
          dmEventfields.forEach(item => params.append('dm_event.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<DirectMessagesGetDmEventsByParticipantIdResponse>(
          'GET',
          path + (params.toString() ? `?${params.toString()}` : ''),
          finalRequestOptions
      );

      return {
        data: (response.data as any)?.data || [],
        meta: (response.data as any)?.meta,
        includes: (response.data as any)?.includes,
        errors: (response.data as any)?.errors
      };
    };

    return new IdPaginator(fetchPage);
  }







}
