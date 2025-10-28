
/**
 * Community notes client for the X API.
 *
 * This module provides a client for interacting with the Community notes endpoints of the X API.
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
CommunityNotesSearchNotesWrittenResponse,
CommunityNotesSearchForEligiblePostsResponse,
CommunityNotesCreateNotesRequest,
CommunityNotesCreateNotesResponse,
CommunityNotesDeleteNotesResponse,
} from './models.js';


/**
 * Options for searchNotesWritten method
 */
export interface CommunityNotesSearchNotesWrittenOptions {
    
    
    /** Pagination token to get next set of posts eligible for notes. */
    paginationToken?: string;
    
    
    
    /** Max results to return. */
    maxResults?: number;
    
    
    
    /** A comma separated list of Note fields to display. */
    notefields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for searchForEligiblePosts method
 */
export interface CommunityNotesSearchForEligiblePostsOptions {
    
    
    /** Pagination token to get next set of posts eligible for notes. */
    paginationToken?: string;
    
    
    
    /** Max results to return. */
    maxResults?: number;
    
    
    
    /** A comma separated list of Tweet fields to display. */
    tweetfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of Media fields to display. */
    mediafields?: Array<any>;
    
    
    
    /** A comma separated list of Poll fields to display. */
    pollfields?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** A comma separated list of Place fields to display. */
    placefields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for createNotes method
 */
export interface CommunityNotesCreateNotesOptions {
    
    
    /** Request body */
    body?: CommunityNotesCreateNotesRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}




/**
 * Client for Community notes operations
 */
export class CommunityNotesClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }






  /**
   * Create a Community Note
   * Creates a community note endpoint for LLM use case.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async createNotes(
        
        
        
        
        
        
        options: CommunityNotesCreateNotesOptions = {}
        
    ): Promise<CommunityNotesCreateNotesResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/notes';
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<CommunityNotesCreateNotesResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Delete a Community Note
   * Deletes a community note.
   * @param id The community note id to delete.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async deleteNotes(
        
        
        
        id: string,
        
        
        
        
        
        
    ): Promise<CommunityNotesDeleteNotesResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/notes/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<CommunityNotesDeleteNotesResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Search for Community Notes Written
   * Returns all the community notes written by the user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   testMode: boolean
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  searchNotesWritten(
    
    
    
    testMode: boolean,
    
    
    
    
    options: CommunityNotesSearchNotesWrittenOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        paginationToken = undefined,
        
        
        
        maxResults = undefined,
        
        
        
        notefields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/notes/search/notes_written';
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (testMode !== undefined) {
          
          params.append('test_mode', String(testMode));
          
      }
      
      
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (notefields !== undefined) {
          
          notefields.forEach(item => params.append('note.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<CommunityNotesSearchNotesWrittenResponse>(
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
   * Search for Posts Eligible for Community Notes
   * Returns all the posts that are eligible for community notes.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   testMode: boolean
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  searchForEligiblePosts(
    
    
    
    testMode: boolean,
    
    
    
    
    options: CommunityNotesSearchForEligiblePostsOptions = {}
    
  ): TweetPaginator {
    // Destructure options
    
    const {
        
        
        paginationToken = undefined,
        
        
        
        maxResults = undefined,
        
        
        
        tweetfields = [],
        
        
        
        expansions = [],
        
        
        
        mediafields = [],
        
        
        
        pollfields = [],
        
        
        
        userfields = [],
        
        
        
        placefields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/notes/search/posts_eligible_for_notes';
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (testMode !== undefined) {
          
          params.append('test_mode', String(testMode));
          
      }
      
      
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (tweetfields !== undefined) {
          
          tweetfields.forEach(item => params.append('tweet.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (mediafields !== undefined) {
          
          mediafields.forEach(item => params.append('media.fields', String(item)));
          
      }
      
      
      
      
      
      if (pollfields !== undefined) {
          
          pollfields.forEach(item => params.append('poll.fields', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (placefields !== undefined) {
          
          placefields.forEach(item => params.append('place.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<CommunityNotesSearchForEligiblePostsResponse>(
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

    return new TweetPaginator(fetchPage);
  }







}
