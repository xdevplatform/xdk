/**
 * Lists client for the X API.
 *
 * This module provides a client for interacting with the Lists endpoints of the X API.
 */

import { Client } from '../client.js';
import {
    
    
    ListsRemoveMemberByUserIdResponse,
    
    
    
    ListsGetUsersFollowedResponse,
    
    
    
    ListsFollowRequest,
    
    ListsFollowResponse,
    
    
    
    
    ListsGetByIdResponse,
    
    
    
    ListsUpdateRequest,
    
    ListsUpdateResponse,
    
    
    
    
    ListsDeleteResponse,
    
    
    
    ListsGetUsersMembershipsResponse,
    
    
    
    ListsGetUsersOwnedResponse,
    
    
    
    ListsUnfollowResponse,
    
    
    
    ListsCreateRequest,
    
    ListsCreateResponse,
    
    
    
    
    ListsUnpinResponse,
    
    
    
    ListsGetUsersPinnedResponse,
    
    
    
    ListsPinRequest,
    
    ListsPinResponse,
    
    
    
    
    ListsAddMemberRequest,
    
    ListsAddMemberResponse,
    
    
    
} from './models.js';

/**
 * Client for Lists operations
 */
export class ListsClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }

    
    /**
     * Remove List member
     * 
     * 
     * Removes a User from a specific List by its ID and the User’s ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the List to remove a member.
     * 
     * 
     * 
     * @param userId The ID of User that will be removed from the List.
     * 
     * 
     * 
     * @returns ListsRemoveMemberByUserIdResponse Response data
     */
    async removeMemberByUserId(
        
        
        
        id: string,
        
        
        
        userId: string,
        
        
        
        
        
        
        
        
    ): Promise<ListsRemoveMemberByUserIdResponse> {
        let url = this.client.baseUrl + "/2/lists/{id}/members/{user_id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        url = url.replace("{user_id}", String(userId));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "DELETE",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsRemoveMemberByUserIdResponse;
        
    }
    
    /**
     * Get followed Lists
     * 
     * 
     * Retrieves a list of Lists followed by a specific User by their ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the User to lookup.
     * 
     * 
     * 
     * @param maxResults The maximum number of results.
     * 
     * 
     * 
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * 
     * 
     * 
     * @param listfields A comma separated list of List fields to display.
     * 
     * 
     * 
     * @param expansions A comma separated list of fields to expand.
     * 
     * 
     * 
     * @param userfields A comma separated list of User fields to display.
     * 
     * 
     * 
     * @returns ListsGetUsersFollowedResponse Response data
     */
    async getUsersFollowed(
        
        
        
        id: string,
        
        
        
        
        
        
        
        maxResults?: number,
        
        
        
        paginationToken?: string,
        
        
        
        listfields?: Array<any>,
        
        
        
        expansions?: Array<any>,
        
        
        
        userfields?: Array<any>,
        
        
        
        
    ): Promise<ListsGetUsersFollowedResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/followed_lists";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        if (maxResults !== undefined) {
            
            params.set("max_results", String(maxResults));
            
        }
        
        
        
        
        
        if (paginationToken !== undefined) {
            
            params.set("pagination_token", String(paginationToken));
            
        }
        
        
        
        
        
        if (listfields !== undefined) {
            
            params.set("list.fields", listfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            params.set("expansions", expansions.map(String).join(","));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            params.set("user.fields", userfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "GET",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsGetUsersFollowedResponse;
        
    }
    
    /**
     * Follow List
     * 
     * 
     * Causes the authenticated user to follow a specific List by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User that will follow the List.
     * 
     * 
     * 
     * 
     * 
     * 
     * 
     * @param body Request body
     * 
     * 
     * 
     * @returns ListsFollowResponse Response data
     */
    async follow(
        
        
        
        id: string,
        
        
        
        
        
        
        
        
        body?: ListsFollowRequest,
        
    ): Promise<ListsFollowResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/followed_lists";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        headers.set("Content-Type", "application/json");
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "POST",
            headers,
            
            body: body ? JSON.stringify(body) : undefined,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsFollowResponse;
        
    }
    
    /**
     * Get List by ID
     * 
     * 
     * Retrieves details of a specific List by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the List.
     * 
     * 
     * 
     * @param listfields A comma separated list of List fields to display.
     * 
     * 
     * 
     * @param expansions A comma separated list of fields to expand.
     * 
     * 
     * 
     * @param userfields A comma separated list of User fields to display.
     * 
     * 
     * 
     * @returns ListsGetByIdResponse Response data
     */
    async getById(
        
        
        
        id: string,
        
        
        
        
        
        
        
        listfields?: Array<any>,
        
        
        
        expansions?: Array<any>,
        
        
        
        userfields?: Array<any>,
        
        
        
        
    ): Promise<ListsGetByIdResponse> {
        let url = this.client.baseUrl + "/2/lists/{id}";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        if (listfields !== undefined) {
            
            params.set("list.fields", listfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            params.set("expansions", expansions.map(String).join(","));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            params.set("user.fields", userfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "GET",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsGetByIdResponse;
        
    }
    
    /**
     * Update List
     * 
     * 
     * Updates the details of a specific List owned by the authenticated user by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the List to modify.
     * 
     * 
     * 
     * 
     * 
     * 
     * 
     * @param body Request body
     * 
     * 
     * 
     * @returns ListsUpdateResponse Response data
     */
    async update(
        
        
        
        id: string,
        
        
        
        
        
        
        
        
        body?: ListsUpdateRequest,
        
    ): Promise<ListsUpdateResponse> {
        let url = this.client.baseUrl + "/2/lists/{id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        headers.set("Content-Type", "application/json");
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "PUT",
            headers,
            
            body: body ? JSON.stringify(body) : undefined,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsUpdateResponse;
        
    }
    
    /**
     * Delete List
     * 
     * 
     * Deletes a specific List owned by the authenticated user by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the List to delete.
     * 
     * 
     * 
     * @returns ListsDeleteResponse Response data
     */
    async delete(
        
        
        
        id: string,
        
        
        
        
        
        
        
        
    ): Promise<ListsDeleteResponse> {
        let url = this.client.baseUrl + "/2/lists/{id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "DELETE",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsDeleteResponse;
        
    }
    
    /**
     * Get List memberships
     * 
     * 
     * Retrieves a list of Lists that a specific User is a member of by their ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the User to lookup.
     * 
     * 
     * 
     * @param maxResults The maximum number of results.
     * 
     * 
     * 
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * 
     * 
     * 
     * @param listfields A comma separated list of List fields to display.
     * 
     * 
     * 
     * @param expansions A comma separated list of fields to expand.
     * 
     * 
     * 
     * @param userfields A comma separated list of User fields to display.
     * 
     * 
     * 
     * @returns ListsGetUsersMembershipsResponse Response data
     */
    async getUsersMemberships(
        
        
        
        id: string,
        
        
        
        
        
        
        
        maxResults?: number,
        
        
        
        paginationToken?: string,
        
        
        
        listfields?: Array<any>,
        
        
        
        expansions?: Array<any>,
        
        
        
        userfields?: Array<any>,
        
        
        
        
    ): Promise<ListsGetUsersMembershipsResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/list_memberships";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        if (maxResults !== undefined) {
            
            params.set("max_results", String(maxResults));
            
        }
        
        
        
        
        
        if (paginationToken !== undefined) {
            
            params.set("pagination_token", String(paginationToken));
            
        }
        
        
        
        
        
        if (listfields !== undefined) {
            
            params.set("list.fields", listfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            params.set("expansions", expansions.map(String).join(","));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            params.set("user.fields", userfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "GET",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsGetUsersMembershipsResponse;
        
    }
    
    /**
     * Get owned Lists
     * 
     * 
     * Retrieves a list of Lists owned by a specific User by their ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the User to lookup.
     * 
     * 
     * 
     * @param maxResults The maximum number of results.
     * 
     * 
     * 
     * @param paginationToken This parameter is used to get a specified 'page' of results.
     * 
     * 
     * 
     * @param listfields A comma separated list of List fields to display.
     * 
     * 
     * 
     * @param expansions A comma separated list of fields to expand.
     * 
     * 
     * 
     * @param userfields A comma separated list of User fields to display.
     * 
     * 
     * 
     * @returns ListsGetUsersOwnedResponse Response data
     */
    async getUsersOwned(
        
        
        
        id: string,
        
        
        
        
        
        
        
        maxResults?: number,
        
        
        
        paginationToken?: string,
        
        
        
        listfields?: Array<any>,
        
        
        
        expansions?: Array<any>,
        
        
        
        userfields?: Array<any>,
        
        
        
        
    ): Promise<ListsGetUsersOwnedResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/owned_lists";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        if (maxResults !== undefined) {
            
            params.set("max_results", String(maxResults));
            
        }
        
        
        
        
        
        if (paginationToken !== undefined) {
            
            params.set("pagination_token", String(paginationToken));
            
        }
        
        
        
        
        
        if (listfields !== undefined) {
            
            params.set("list.fields", listfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            params.set("expansions", expansions.map(String).join(","));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            params.set("user.fields", userfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "GET",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsGetUsersOwnedResponse;
        
    }
    
    /**
     * Unfollow List
     * 
     * 
     * Causes the authenticated user to unfollow a specific List by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User that will unfollow the List.
     * 
     * 
     * 
     * @param listId The ID of the List to unfollow.
     * 
     * 
     * 
     * @returns ListsUnfollowResponse Response data
     */
    async unfollow(
        
        
        
        id: string,
        
        
        
        listId: string,
        
        
        
        
        
        
        
        
    ): Promise<ListsUnfollowResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/followed_lists/{list_id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        url = url.replace("{list_id}", String(listId));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "DELETE",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsUnfollowResponse;
        
    }
    
    /**
     * Create List
     * 
     * 
     * Creates a new List for the authenticated user.
     * 
     * 
     * 
     * 
     * 
     * 
     * 
     * 
     * @param body Request body
     * 
     * 
     * 
     * @returns ListsCreateResponse Response data
     */
    async create(
        
        
        
        
        
        
        
        
        body?: ListsCreateRequest,
        
    ): Promise<ListsCreateResponse> {
        let url = this.client.baseUrl + "/2/lists";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        

        

        const headers = new Headers();
        
        
        
        headers.set("Content-Type", "application/json");
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "POST",
            headers,
            
            body: body ? JSON.stringify(body) : undefined,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsCreateResponse;
        
    }
    
    /**
     * Unpin List
     * 
     * 
     * Causes the authenticated user to unpin a specific List by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User for whom to return results.
     * 
     * 
     * 
     * @param listId The ID of the List to unpin.
     * 
     * 
     * 
     * @returns ListsUnpinResponse Response data
     */
    async unpin(
        
        
        
        id: string,
        
        
        
        listId: string,
        
        
        
        
        
        
        
        
    ): Promise<ListsUnpinResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/pinned_lists/{list_id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        url = url.replace("{list_id}", String(listId));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "DELETE",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsUnpinResponse;
        
    }
    
    /**
     * Get pinned Lists
     * 
     * 
     * Retrieves a list of Lists pinned by the authenticated user.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User for whom to return results.
     * 
     * 
     * 
     * @param listfields A comma separated list of List fields to display.
     * 
     * 
     * 
     * @param expansions A comma separated list of fields to expand.
     * 
     * 
     * 
     * @param userfields A comma separated list of User fields to display.
     * 
     * 
     * 
     * @returns ListsGetUsersPinnedResponse Response data
     */
    async getUsersPinned(
        
        
        
        id: string,
        
        
        
        
        
        
        
        listfields?: Array<any>,
        
        
        
        expansions?: Array<any>,
        
        
        
        userfields?: Array<any>,
        
        
        
        
    ): Promise<ListsGetUsersPinnedResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/pinned_lists";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        if (listfields !== undefined) {
            
            params.set("list.fields", listfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            params.set("expansions", expansions.map(String).join(","));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            params.set("user.fields", userfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "GET",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsGetUsersPinnedResponse;
        
    }
    
    /**
     * Pin List
     * 
     * 
     * Causes the authenticated user to pin a specific List by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User that will pin the List.
     * 
     * 
     * 
     * 
     * 
     * 
     * 
     * @param body Request body
     * 
     * 
     * 
     * @returns ListsPinResponse Response data
     */
    async pin(
        
        
        
        id: string,
        
        
        
        
        body: ListsPinRequest,
        
        
        
        
        
    ): Promise<ListsPinResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/pinned_lists";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        headers.set("Content-Type", "application/json");
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "POST",
            headers,
            
            body: body ? JSON.stringify(body) : undefined,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsPinResponse;
        
    }
    
    /**
     * Add List member
     * 
     * 
     * Adds a User to a specific List by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the List for which to add a member.
     * 
     * 
     * 
     * 
     * 
     * 
     * 
     * @param body Request body
     * 
     * 
     * 
     * @returns ListsAddMemberResponse Response data
     */
    async addMember(
        
        
        
        id: string,
        
        
        
        
        
        
        
        
        body?: ListsAddMemberRequest,
        
    ): Promise<ListsAddMemberResponse> {
        let url = this.client.baseUrl + "/2/lists/{id}/members";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        headers.set("Content-Type", "application/json");
        

        // Make the request
        
        
        const response = await (this.client.oauth2Session || fetch)(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "POST",
            headers,
            
            body: body ? JSON.stringify(body) : undefined,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as ListsAddMemberResponse;
        
    }
    
} 