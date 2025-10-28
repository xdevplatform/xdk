
/**
 * Users client for the X API.
 *
 * This module provides a client for interacting with the Users endpoints of the X API.
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
UsersGetByUsernameResponse,
UsersUnmuteResponse,
UsersGetPostsLikingResponse,
UsersUnfollowResponse,
UsersGetFollowingResponse,
UsersFollowRequest,
UsersFollowResponse,
UsersGetMutingResponse,
UsersMuteRequest,
UsersMuteResponse,
UsersGetRepostsOfMeResponse,
UsersGetFollowersResponse,
UsersBlockDmsResponse,
UsersGetListsMembersResponse,
UsersGetByUsernamesResponse,
UsersGetByIdResponse,
UsersSearchResponse,
UsersUnblockDmsResponse,
UsersGetByIdsResponse,
UsersGetPostsRepostedByResponse,
UsersGetListsFollowersResponse,
UsersGetBlockingResponse,
UsersGetMyResponse,
} from './models.js';


/**
 * Options for getByUsername method
 */
export interface UsersGetByUsernameOptions {
    
    
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
 * Options for getPostsLiking method
 */
export interface UsersGetPostsLikingOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getFollowing method
 */
export interface UsersGetFollowingOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for follow method
 */
export interface UsersFollowOptions {
    
    
    /** Request body */
    body?: UsersFollowRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getMuting method
 */
export interface UsersGetMutingOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for mute method
 */
export interface UsersMuteOptions {
    
    
    /** Request body */
    body?: UsersMuteRequest;
    
    /** Additional request options */
    requestOptions?: RequestOptions;
}


/**
 * Options for getRepostsOfMe method
 */
export interface UsersGetRepostsOfMeOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getFollowers method
 */
export interface UsersGetFollowersOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getListsMembers method
 */
export interface UsersGetListsMembersOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getByUsernames method
 */
export interface UsersGetByUsernamesOptions {
    
    
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
 * Options for getById method
 */
export interface UsersGetByIdOptions {
    
    
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
 * Options for search method
 */
export interface UsersSearchOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. */
    nextToken?: string;
    
    
    
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
 * Options for getByIds method
 */
export interface UsersGetByIdsOptions {
    
    
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
 * Options for getPostsRepostedBy method
 */
export interface UsersGetPostsRepostedByOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get the next 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getListsFollowers method
 */
export interface UsersGetListsFollowersOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getBlocking method
 */
export interface UsersGetBlockingOptions {
    
    
    /** The maximum number of results. */
    maxResults?: number;
    
    
    
    /** This parameter is used to get a specified 'page' of results. */
    paginationToken?: string;
    
    
    
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
 * Options for getMy method
 */
export interface UsersGetMyOptions {
    
    
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
 * Client for Users operations
 */
export class UsersClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }


  /**
   * Get User by username
   * Retrieves details of a specific User by their username.
   * @param username A username.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getByUsername(
        
        
        
        username: string,
        
        
        
        
        
        
        options: UsersGetByUsernameOptions = {}
        
    ): Promise<UsersGetByUsernameResponse> {
        // Destructure options
        
        const {
            
            
            userfields = [],
            
            
            
            expansions = [],
            
            
            
            tweetfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/by/username/{username}';
        
        
        path = path.replace('{username}', encodeURIComponent(String(username)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (tweetfields !== undefined) {
            
            tweetfields.forEach(item => params.append('tweet.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersGetByUsernameResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Unmute User
   * Causes the authenticated user to unmute a specific user by their ID.
   * @param sourceUserId The ID of the authenticated source User that is requesting to unmute the target User.
   * @param targetUserId The ID of the User that the source User is requesting to unmute.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unmute(
        
        
        
        sourceUserId: string,
        
        
        
        targetUserId: string,
        
        
        
        
        
        
    ): Promise<UsersUnmuteResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{source_user_id}/muting/{target_user_id}';
        
        
        path = path.replace('{source_user_id}', encodeURIComponent(String(sourceUserId)));
        
        
        
        path = path.replace('{target_user_id}', encodeURIComponent(String(targetUserId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<UsersUnmuteResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Unfollow User
   * Causes the authenticated user to unfollow a specific user by their ID.
   * @param sourceUserId The ID of the authenticated source User that is requesting to unfollow the target User.
   * @param targetUserId The ID of the User that the source User is requesting to unfollow.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unfollow(
        
        
        
        sourceUserId: string,
        
        
        
        targetUserId: string,
        
        
        
        
        
        
    ): Promise<UsersUnfollowResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{source_user_id}/following/{target_user_id}';
        
        
        path = path.replace('{source_user_id}', encodeURIComponent(String(sourceUserId)));
        
        
        
        path = path.replace('{target_user_id}', encodeURIComponent(String(targetUserId)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<UsersUnfollowResponse>(
            'DELETE',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Follow User
   * Causes the authenticated user to follow a specific user by their ID.
   * @param id The ID of the authenticated source User that is requesting to follow the target User.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async follow(
        
        
        
        id: string,
        
        
        
        
        
        
        options: UsersFollowOptions = {}
        
    ): Promise<UsersFollowResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}/following';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersFollowResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Mute User
   * Causes the authenticated user to mute a specific User by their ID.
   * @param id The ID of the authenticated source User that is requesting to mute the target User.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async mute(
        
        
        
        id: string,
        
        
        
        
        
        
        options: UsersMuteOptions = {}
        
    ): Promise<UsersMuteResponse> {
        // Destructure options
        
        const {
            
            
            body,
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}/muting';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            body: body ? JSON.stringify(body) : undefined,
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersMuteResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }








  /**
   * Block DMs
   * Blocks direct messages to or from a specific User by their ID for the authenticated user.
   * @param id The ID of the target User that the authenticated user requesting to block dms for.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async blockDms(
        
        
        
        id: string,
        
        
        
        
        
        
    ): Promise<UsersBlockDmsResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/dm/block';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<UsersBlockDmsResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Get Users by usernames
   * Retrieves details of multiple Users by their usernames.
   * @param usernames A list of usernames, comma-separated.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getByUsernames(
        
        
        
        usernames: Array<any>,
        
        
        
        
        
        
        options: UsersGetByUsernamesOptions = {}
        
    ): Promise<UsersGetByUsernamesResponse> {
        // Destructure options
        
        const {
            
            
            userfields = [],
            
            
            
            expansions = [],
            
            
            
            tweetfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/by';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (usernames !== undefined) {
            
            usernames.forEach(item => params.append('usernames', String(item)));
            
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
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersGetByUsernamesResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Get User by ID
   * Retrieves details of a specific User by their ID.
   * @param id The ID of the User to lookup.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getById(
        
        
        
        id: string,
        
        
        
        
        
        
        options: UsersGetByIdOptions = {}
        
    ): Promise<UsersGetByIdResponse> {
        // Destructure options
        
        const {
            
            
            userfields = [],
            
            
            
            expansions = [],
            
            
            
            tweetfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/{id}';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (tweetfields !== undefined) {
            
            tweetfields.forEach(item => params.append('tweet.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersGetByIdResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }






  /**
   * Unblock DMs
   * Unblocks direct messages to or from a specific User by their ID for the authenticated user.
   * @param id The ID of the target User that the authenticated user requesting to unblock dms for.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async unblockDms(
        
        
        
        id: string,
        
        
        
        
        
        
    ): Promise<UsersUnblockDmsResponse> {
        // Destructure options
        
        const reqOpts = {};
        

        // Build the path with path parameters
        let path = '/2/users/{id}/dm/unblock';
        
        
        path = path.replace('{id}', encodeURIComponent(String(id)));
        
        

        // Build query parameters
        const params = new URLSearchParams();
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            // No optional parameters, using empty request options
            
        };

        return this.client.request<UsersUnblockDmsResponse>(
            'POST',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }




  /**
   * Get Users by IDs
   * Retrieves details of multiple Users by their IDs.
   * @param ids A list of User IDs, comma-separated. You can specify up to 100 IDs.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getByIds(
        
        
        
        ids: Array<any>,
        
        
        
        
        
        
        options: UsersGetByIdsOptions = {}
        
    ): Promise<UsersGetByIdsResponse> {
        // Destructure options
        
        const {
            
            
            userfields = [],
            
            
            
            expansions = [],
            
            
            
            tweetfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (ids !== undefined) {
            
            ids.forEach(item => params.append('ids', String(item)));
            
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
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersGetByIdsResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }










  /**
   * Get my User
   * Retrieves details of the authenticated user.* @returns Promise with the API response
   */
    // Overload 1: Default behavior (unwrapped response)
    async getMy(
        
        
        
        
        
        
        options: UsersGetMyOptions = {}
        
    ): Promise<UsersGetMyResponse> {
        // Destructure options
        
        const {
            
            
            userfields = [],
            
            
            
            expansions = [],
            
            
            
            tweetfields = [],
            
            
            
            requestOptions: reqOpts = {}
        } = options;
        

        // Build the path with path parameters
        let path = '/2/users/me';
        

        // Build query parameters
        const params = new URLSearchParams();
        
        
        
        if (userfields !== undefined) {
            
            userfields.forEach(item => params.append('user.fields', String(item)));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            expansions.forEach(item => params.append('expansions', String(item)));
            
        }
        
        
        
        
        
        if (tweetfields !== undefined) {
            
            tweetfields.forEach(item => params.append('tweet.fields', String(item)));
            
        }
        
        
        

        // Prepare request options
        const finalRequestOptions: RequestOptions = {
            
            
            ...reqOpts
            
        };

        return this.client.request<UsersGetMyResponse>(
            'GET',
            path + (params.toString() ? `?${params.toString()}` : ''),
            finalRequestOptions
        );
    }










  /**
   * Get Liking Users
   * Retrieves a list of Users who liked a specific Post by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getPostsLiking(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetPostsLikingOptions = {}
    
  ): TweetPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/tweets/{id}/liking_users';
    
    
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

      const response = await this.client.request<UsersGetPostsLikingResponse>(
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






  /**
   * Get following
   * Retrieves a list of Users followed by a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getFollowing(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetFollowingOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/following';
    
    
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

      const response = await this.client.request<UsersGetFollowingResponse>(
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
   * Get muting
   * Retrieves a list of Users muted by the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getMuting(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetMutingOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/muting';
    
    
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

      const response = await this.client.request<UsersGetMutingResponse>(
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
   * Get Reposts of me
   * Retrieves a list of Posts that repost content from the authenticated user.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getRepostsOfMe(
    
    
    
    
    options: UsersGetRepostsOfMeOptions = {}
    
  ): TweetPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        tweetfields = [],
        
        
        
        expansions = [],
        
        
        
        mediafields = [],
        
        
        
        pollfields = [],
        
        
        
        userfields = [],
        
        
        
        placefields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/reposts_of_me';
    

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

      const response = await this.client.request<UsersGetRepostsOfMeResponse>(
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




  /**
   * Get followers
   * Retrieves a list of Users who follow a specific User by their ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getFollowers(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetFollowersOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/followers';
    
    
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

      const response = await this.client.request<UsersGetFollowersResponse>(
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
   * Get List members
   * Retrieves a list of Users who are members of a specific List by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getListsMembers(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetListsMembersOptions = {}
    
  ): ListPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/lists/{id}/members';
    
    
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

      const response = await this.client.request<UsersGetListsMembersResponse>(
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

    return new ListPaginator(fetchPage);
  }








  /**
   * Search Users
   * Retrieves a list of Users matching a search query.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   query: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  search(
    
    
    
    query: string,
    
    
    
    
    options: UsersSearchOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        nextToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/search';
    

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
        
        params.set('next_token', paginationToken);
        
      }

      // Prepare request options
      const finalRequestOptions: RequestOptions = {
          
          ...reqOpts
      };

      const response = await this.client.request<UsersSearchResponse>(
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
   * Get Reposted by
   * Retrieves a list of Users who reposted a specific Post by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getPostsRepostedBy(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetPostsRepostedByOptions = {}
    
  ): TweetPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/tweets/{id}/retweeted_by';
    
    
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

      const response = await this.client.request<UsersGetPostsRepostedByResponse>(
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




  /**
   * Get List followers
   * Retrieves a list of Users who follow a specific List by its ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getListsFollowers(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetListsFollowersOptions = {}
    
  ): ListPaginator {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/lists/{id}/followers';
    
    
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

      const response = await this.client.request<UsersGetListsFollowersResponse>(
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

    return new ListPaginator(fetchPage);
  }




  /**
   * Get blocking
   * Retrieves a list of Users blocked by the specified User ID.
   * Returns a paginator for automatic pagination through all results.
   * @param 
   id: string
   
   * @param options Options for the paginated request
   * @returns A paginator instance for iterating through all results
   */
  getBlocking(
    
    
    
    id: string,
    
    
    
    
    options: UsersGetBlockingOptions = {}
    
  ): TwitterPaginator<any> {
    // Destructure options
    
    const {
        
        
        maxResults = undefined,
        
        
        
        paginationToken = undefined,
        
        
        
        userfields = [],
        
        
        
        expansions = [],
        
        
        
        tweetfields = [],
        
        
        requestOptions: reqOpts = {}
    } = options;
    

    // Build the path with path parameters
    let path = '/2/users/{id}/blocking';
    
    
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

      const response = await this.client.request<UsersGetBlockingResponse>(
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
