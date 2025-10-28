
/**
 * Communities client for the X API.
 *
 * This module provides a client for interacting with the Communities endpoints of the X API.
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
CommunitiesSearchResponse,
CommunitiesGetByIdResponse,
} from './models.js';


/**
 * Options for search method
 */
export interface CommunitiesSearchOptions {
    
    
    /** The maximum number of search results to be returned by a request. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
    nextToken?: string;
    
    
    
    /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
    paginationToken?: string;
    
    
    
    /** A comma separated list of Community fields to display. */
    communityfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getById method
 */
export interface CommunitiesGetByIdOptions {
    
    
    /** A comma separated list of Community fields to display. */
    communityfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}



/**
 * Client for Communities operations
 */
export class CommunitiesClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }




  /**
   * Get Community by ID
   * Retrieves details of a specific Community by its ID.
   * @param id The ID of the Community.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getById(
        
        
        
        id: string,
        
        
        
        
        
        
        options: CommunitiesGetByIdOptions = {}
        
    ): Promise<CommunitiesGetByIdResponse> {
        // Destructure options
        
        const {
            
            
            communityfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/communities/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (communityfields !== undefined) {
            
            communityfields.forEach(item => params.append('community.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<CommunitiesGetByIdResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Search Communities
   * Retrieves a list of Communities matching the specified search query.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  search(
    
    
    
    query: string,
    
    
    
    
    options: CommunitiesSearchOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        nextToken = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        communityfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/communities/search';
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (query !== undefined) {
          
          params.append('query', String(query));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (nextToken !== undefined) {
          
          params.append('next_token', String(nextToken));
          
      }
      
      
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (communityfields !== undefined) {
          
          communityfields.forEach(item => params.append('community.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<CommunitiesSearchResponse>(
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





}
