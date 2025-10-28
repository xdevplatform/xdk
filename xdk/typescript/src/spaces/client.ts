
/**
 * Spaces client for the X API.
 *
 * This module provides a client for interacting with the Spaces endpoints of the X API.
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
SpacesGetByIdsResponse,
SpacesGetByIdResponse,
SpacesGetBuyersResponse,
SpacesGetByCreatorIdsResponse,
SpacesSearchResponse,
SpacesGetPostsResponse,
} from './models.js';


/**
 * Options for getByIds method
 */
export interface SpacesGetByIdsOptions {
    
    
    /** A comma separated list of Space fields to display. */
    spacefields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** A comma separated list of Topic fields to display. */
    topicfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getById method
 */
export interface SpacesGetByIdOptions {
    
    
    /** A comma separated list of Space fields to display. */
    spacefields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** A comma separated list of Topic fields to display. */
    topicfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getBuyers method
 */
export interface SpacesGetBuyersOptions {
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of Tweet fields to display. */
    tweetfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getByCreatorIds method
 */
export interface SpacesGetByCreatorIdsOptions {
    
    
    /** A comma separated list of Space fields to display. */
    spacefields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** A comma separated list of Topic fields to display. */
    topicfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for search method
 */
export interface SpacesSearchOptions {
    
    
    /** The state of Spaces to search for. */
    state?: string;
    
    
    
    /** The number of results to return. */
    maxResults?: number;
    
    
    
    /** A comma separated list of Space fields to display. */
    spacefields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** A comma separated list of Topic fields to display. */
    topicfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getPosts method
 */
export interface SpacesGetPostsOptions {
    
    
    /** The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100. */
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
 * Client for Spaces operations
 */
export class SpacesClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }


  /**
   * Get Spaces by IDs
   * Retrieves details of multiple Spaces by their IDs.
   * @param ids The list of Space IDs to return.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getByIds(
        
        
        
        ids: Array<any>,
        
        
        
        
        
        
        options: SpacesGetByIdsOptions = {}
        
    ): Promise<SpacesGetByIdsResponse> {
        // Destructure options
        
        const {
            
            
            spacefields = [],
            
            
            
            expansions = [],
            
            
            
            userfields = [],
            
            
            
            topicfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/spaces';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (ids !== undefined) {
            
            ids.forEach(item => params.append('ids', String(item)));
            
        }
        
        
        
        
        
        if (spacefields !== undefined) {
            
            spacefields.forEach(item => params.append('space.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (topicfields !== undefined) {
            
            topicfields.forEach(item => params.append('topic.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<SpacesGetByIdsResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Get space by ID
   * Retrieves details of a specific space by its ID.
   * @param id The ID of the Space to be retrieved.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getById(
        
        
        
        id: string,
        
        
        
        
        
        
        options: SpacesGetByIdOptions = {}
        
    ): Promise<SpacesGetByIdResponse> {
        // Destructure options
        
        const {
            
            
            spacefields = [],
            
            
            
            expansions = [],
            
            
            
            userfields = [],
            
            
            
            topicfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/spaces/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (spacefields !== undefined) {
            
            spacefields.forEach(item => params.append('space.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (topicfields !== undefined) {
            
            topicfields.forEach(item => params.append('topic.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<SpacesGetByIdResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Get Spaces by creator IDs
   * Retrieves details of Spaces created by specified User IDs.
   * @param userIds The IDs of Users to search through.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getByCreatorIds(
        
        
        
        userIds: Array<any>,
        
        
        
        
        
        
        options: SpacesGetByCreatorIdsOptions = {}
        
    ): Promise<SpacesGetByCreatorIdsResponse> {
        // Destructure options
        
        const {
            
            
            spacefields = [],
            
            
            
            expansions = [],
            
            
            
            userfields = [],
            
            
            
            topicfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/spaces/by/creator_ids';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (userIds !== undefined) {
            
            userIds.forEach(item => params.append('user_ids', String(item)));
            
        }
        
        
        
        
        
        if (spacefields !== undefined) {
            
            spacefields.forEach(item => params.append('space.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (topicfields !== undefined) {
            
            topicfields.forEach(item => params.append('topic.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<SpacesGetByCreatorIdsResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Search Spaces
   * Retrieves a list of Spaces matching the specified search query.
   * @param query The search query.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async search(
        
        
        
        query: string,
        
        
        
        
        
        
        options: SpacesSearchOptions = {}
        
    ): Promise<SpacesSearchResponse> {
        // Destructure options
        
        const {
            
            
            state = undefined,
            
            
            
            maxResults = undefined,
            
            
            
            spacefields = [],
            
            
            
            expansions = [],
            
            
            
            userfields = [],
            
            
            
            topicfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/spaces/search';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (query !== undefined) {
            
            params.append('query', String(query));
            
        }
        
        
        
        
        
        if (state !== undefined) {
            
            params.append('state', String(state));
            
        }
        
        
        
        
        
        if (maxResults !== undefined) {
            
            params.append('max_results', String(maxResults));
            
        }
        
        
        
        
        
        if (spacefields !== undefined) {
            
            spacefields.forEach(item => params.append('space.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (topicfields !== undefined) {
            
            topicfields.forEach(item => params.append('topic.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<SpacesSearchResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Get Space Posts
   * Retrieves a list of Posts shared in a specific Space by its ID.
   * @param id The ID of the Space to be retrieved.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getPosts(
        
        
        
        id: string,
        
        
        
        
        
        
        options: SpacesGetPostsOptions = {}
        
    ): Promise<SpacesGetPostsResponse> {
        // Destructure options
        
        const {
            
            
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
        let path = '/2/spaces/{id}/tweets';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
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
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<SpacesGetPostsResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }










  /**
   * Get Space ticket buyers
   * Retrieves a list of Users who purchased tickets to a specific Space by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getBuyers(
    
    
    
    id: string,
    
    
    
    
    options: SpacesGetBuyersOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        paginationToken = undefined,
        
        
        
        maxResults = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/spaces/{id}/buyers';
    
    
    path = path.replace('{id}', encodeURIComponent(String(id)));
    
    

    // Create the fetch function for the paginator
    const fetchPage = async (paginationToken?: string) => {
      // Build query parameters
      const params = new URLSearchParams();
      
      
      
      if (paginationToken !== undefined) {
          
          params.append('pagination_token', String(paginationToken));
          
      }
      
      
      
      
      
      if (maxResults !== undefined) {
          
          params.append('max_results', String(maxResults));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
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

      const response = await this.client.request<SpacesGetBuyersResponse>(
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
