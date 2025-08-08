/**
 * Communities client for the X API.
 *
 * This module provides a client for interacting with the Communities endpoints of the X API.
 */

import { Client } from '../client.js';
import {
    
    
    CommunitiesSearchResponse,
    
    
    
    CommunitiesGetByIdResponse,
    
    
} from './models.js';

/**
 * Client for Communities operations
 */
export class CommunitiesClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }

    
    /**
     * Search Communities
     * 
     * 
     * Retrieves a list of Communities matching the specified search query.
     * 
     * 
     * 
     * 
     * @param query Query to search communities.
     * 
     * 
     * 
     * @param maxResults The maximum number of search results to be returned by a request.
     * 
     * 
     * 
     * @param nextToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * 
     * 
     * 
     * @param paginationToken This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
     * 
     * 
     * 
     * @param communityfields A comma separated list of Community fields to display.
     * 
     * 
     * 
     * @returns CommunitiesSearchResponse Response data
     */
    async search(
        
        
        
        query: string,
        
        
        
        
        
        
        
        maxResults?: number,
        
        
        
        nextToken?: string,
        
        
        
        paginationToken?: string,
        
        
        
        communityfields?: Array<any>,
        
        
        
        
    ): Promise<CommunitiesSearchResponse> {
        let url = this.client.baseUrl + "/2/communities/search";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        if (query !== undefined) {
            
            params.set("query", String(query));
            
        }
        
        
        
        
        
        if (maxResults !== undefined) {
            
            params.set("max_results", String(maxResults));
            
        }
        
        
        
        
        
        if (nextToken !== undefined) {
            
            params.set("next_token", String(nextToken));
            
        }
        
        
        
        
        
        if (paginationToken !== undefined) {
            
            params.set("pagination_token", String(paginationToken));
            
        }
        
        
        
        
        
        if (communityfields !== undefined) {
            
            params.set("community.fields", communityfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

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

        
        return responseData as CommunitiesSearchResponse;
        
    }
    
    /**
     * Get Community by ID
     * 
     * 
     * Retrieves details of a specific Community by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the Community.
     * 
     * 
     * 
     * @param communityfields A comma separated list of Community fields to display.
     * 
     * 
     * 
     * @returns CommunitiesGetByIdResponse Response data
     */
    async getById(
        
        
        
        id: string,
        
        
        
        
        
        
        
        communityfields?: Array<any>,
        
        
        
        
    ): Promise<CommunitiesGetByIdResponse> {
        let url = this.client.baseUrl + "/2/communities/{id}";

        

        
        
        
        
        
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
        
        
        
        
        
        
        
        if (communityfields !== undefined) {
            
            params.set("community.fields", communityfields.map(String).join(","));
            
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

        
        return responseData as CommunitiesGetByIdResponse;
        
    }
    
} 