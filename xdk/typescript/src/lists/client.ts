
/**
 * Lists client for the X API.
 *
 * This module provides a client for interacting with the Lists endpoints of the X API.
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
ListsGetUsersMembershipsResponse,
ListsUnfollowResponse,
ListsGetUsersFollowedResponse,
ListsFollowRequest,
ListsFollowResponse,
ListsGetUsersOwnedResponse,
ListsAddMemberRequest,
ListsAddMemberResponse,
ListsCreateRequest,
ListsCreateResponse,
ListsRemoveMemberByUserIdResponse,
ListsGetUsersPinnedResponse,
ListsPinRequest,
ListsPinResponse,
ListsUnpinResponse,
ListsGetByIdResponse,
ListsUpdateRequest,
ListsUpdateResponse,
ListsDeleteResponse,
} from './models.js';


/**
 * Options for getUsersMemberships method
 */
export interface ListsGetUsersMembershipsOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
    /** A comma separated list of List fields to display. */
    listfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}



/**
 * Options for getUsersFollowed method
 */
export interface ListsGetUsersFollowedOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
    /** A comma separated list of List fields to display. */
    listfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for follow method
 */
export interface ListsFollowOptions {
    
    
    /** Request body */
    body?: ListsFollowRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getUsersOwned method
 */
export interface ListsGetUsersOwnedOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
    /** A comma separated list of List fields to display. */
    listfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for addMember method
 */
export interface ListsAddMemberOptions {
    
    
    /** Request body */
    body?: ListsAddMemberRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for create method
 */
export interface ListsCreateOptions {
    
    
    /** Request body */
    body?: ListsCreateRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}



/**
 * Options for getUsersPinned method
 */
export interface ListsGetUsersPinnedOptions {
    
    
    /** A comma separated list of List fields to display. */
    listfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}




/**
 * Options for getById method
 */
export interface ListsGetByIdOptions {
    
    
    /** A comma separated list of List fields to display. */
    listfields?: Array<any>;
    
    
    
    /** A comma separated list of fields to expand. */
    expansions?: Array<any>;
    
    
    
    /** A comma separated list of User fields to display. */
    userfields?: Array<any>;
    
    
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for update method
 */
export interface ListsUpdateOptions {
    
    
    /** Request body */
    body?: ListsUpdateRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}




/**
 * Client for Lists operations
 */
export class ListsClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }




  /**
   * Unfollow List
   * Causes the authenticated user to unfollow a specific List by its ID.
   * @param id The ID of the authenticated source User that will unfollow the List.
   * @param listId The ID of the List to unfollow.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unfollow(
        
        
        
        id: string,
        
        
        
        listId: string,
        
        
        
        
        
        
    ): Promise<ListsUnfollowResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/followed_lists/{list_id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        
        
        path = path.replace('{list_id}', encodeURIComponent(String(listId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<ListsUnfollowResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Follow List
   * Causes the authenticated user to follow a specific List by its ID.
   * @param id The ID of the authenticated source User that will follow the List.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async follow(
        
        
        
        id: string,
        
        
        
        
        
        
        options: ListsFollowOptions = {}
        
    ): Promise<ListsFollowResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}/followed_lists';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<ListsFollowResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Add List member
   * Adds a User to a specific List by its ID.
   * @param id The ID of the List for which to add a member.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async addMember(
        
        
        
        id: string,
        
        
        
        
        
        
        options: ListsAddMemberOptions = {}
        
    ): Promise<ListsAddMemberResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/lists/{id}/members';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<ListsAddMemberResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Create List
   * Creates a new List for the authenticated user.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async create(
        
        
        
        
        
        
        options: ListsCreateOptions = {}
        
    ): Promise<ListsCreateResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/lists';
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<ListsCreateResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Remove List member
   * Removes a User from a specific List by its ID and the User’s ID.
   * @param id The ID of the List to remove a member.
   * @param userId The ID of User that will be removed from the List.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async removeMemberByUserId(
        
        
        
        id: string,
        
        
        
        userId: string,
        
        
        
        
        
        
    ): Promise<ListsRemoveMemberByUserIdResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/lists/{id}/members/{user_id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        
        
        path = path.replace('{user_id}', encodeURIComponent(String(userId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<ListsRemoveMemberByUserIdResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Get pinned Lists
   * Retrieves a list of Lists pinned by the authenticated user.
   * @param id The ID of the authenticated source User for whom to return results.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getUsersPinned(
        
        
        
        id: string,
        
        
        
        
        
        
        options: ListsGetUsersPinnedOptions = {}
        
    ): Promise<ListsGetUsersPinnedResponse> {
        // Destructure options
        
        const {
            
            
            listfields = [],
            
            
            
            expansions = [],
            
            
            
            userfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}/pinned_lists';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (listfields !== undefined) {
            
            listfields.forEach(item => params.append('list.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<ListsGetUsersPinnedResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Pin List
   * Causes the authenticated user to pin a specific List by its ID.
   * @param id The ID of the authenticated source User that will pin the List.* @param body Request body
* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async pin(
        
        
        
        id: string,
        
        
        
        
        body: ListsPinRequest,
        
        
        
    ): Promise<ListsPinResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/pinned_lists';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: JSON.stringify(body || {}),
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<ListsPinResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Unpin List
   * Causes the authenticated user to unpin a specific List by its ID.
   * @param id The ID of the authenticated source User for whom to return results.
   * @param listId The ID of the List to unpin.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unpin(
        
        
        
        id: string,
        
        
        
        listId: string,
        
        
        
        
        
        
    ): Promise<ListsUnpinResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/pinned_lists/{list_id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        
        
        path = path.replace('{list_id}', encodeURIComponent(String(listId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<ListsUnpinResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Get List by ID
   * Retrieves details of a specific List by its ID.
   * @param id The ID of the List.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getById(
        
        
        
        id: string,
        
        
        
        
        
        
        options: ListsGetByIdOptions = {}
        
    ): Promise<ListsGetByIdResponse> {
        // Destructure options
        
        const {
            
            
            listfields = [],
            
            
            
            expansions = [],
            
            
            
            userfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/lists/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (listfields !== undefined) {
            
            listfields.forEach(item => params.append('list.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<ListsGetByIdResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Update List
   * Updates the details of a specific List owned by the authenticated user by its ID.
   * @param id The ID of the List to modify.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async update(
        
        
        
        id: string,
        
        
        
        
        
        
        options: ListsUpdateOptions = {}
        
    ): Promise<ListsUpdateResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/lists/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<ListsUpdateResponse>(
            'PUT',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Delete List
   * Deletes a specific List owned by the authenticated user by its ID.
   * @param id The ID of the List to delete.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async delete(
        
        
        
        id: string,
        
        
        
        
        
        
    ): Promise<ListsDeleteResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/lists/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<ListsDeleteResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Get List memberships
   * Retrieves a list of Lists that a specific User is a member of by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsersMemberships(
    
    
    
    id: string,
    
    
    
    
    options: ListsGetUsersMembershipsOptions = {}
    
  ): UserPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        listfields = [],
        
        
        
        expansions = [],
        
        
        
        userfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/list_memberships';
    
    
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
      
      
      
      
      
      if (listfields !== undefined) {
          
          listfields.forEach(item => params.append('list.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<ListsGetUsersMembershipsResponse>(
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

    return new UserPaginator(fetchPage);
  }






  /**
   * Get followed Lists
   * Retrieves a list of Lists followed by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsersFollowed(
    
    
    
    id: string,
    
    
    
    
    options: ListsGetUsersFollowedOptions = {}
    
  ): UserPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        listfields = [],
        
        
        
        expansions = [],
        
        
        
        userfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/followed_lists';
    
    
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
      
      
      
      
      
      if (listfields !== undefined) {
          
          listfields.forEach(item => params.append('list.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<ListsGetUsersFollowedResponse>(
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

    return new UserPaginator(fetchPage);
  }






  /**
   * Get owned Lists
   * Retrieves a list of Lists owned by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getUsersOwned(
    
    
    
    id: string,
    
    
    
    
    options: ListsGetUsersOwnedOptions = {}
    
  ): UserPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        listfields = [],
        
        
        
        expansions = [],
        
        
        
        userfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/owned_lists';
    
    
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
      
      
      
      
      
      if (listfields !== undefined) {
          
          listfields.forEach(item => params.append('list.fields', String(item)));
          
      }
      
      
      
      
      
      if (expansions !== undefined) {
          
          expansions.forEach(item => params.append('expansions', String(item)));
          
      }
      
      
      
      
      
      if (userfields !== undefined) {
          
          userfields.forEach(item => params.append('user.fields', String(item)));
          
      }
      
      
      

      // Add pagination token if provided
      if (paginationToken) {
        
        params.set('pagination_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<ListsGetUsersOwnedResponse>(
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

    return new UserPaginator(fetchPage);
  }





















}
