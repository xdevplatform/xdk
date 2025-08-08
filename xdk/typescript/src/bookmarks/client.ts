/**
 * Bookmarks client for the X API.
 *
 * This module provides a client for interacting with the Bookmarks endpoints of the X API.
 */

import { Client } from '../client.js';
import {
    
    
    BookmarksGetUsersResponse,
    
    
    
    BookmarksCreateUsersRequest,
    
    BookmarksCreateUsersResponse,
    
    
    
    
    BookmarksGetUsersFoldersResponse,
    
    
    
    BookmarksGetUsersByFolderIdResponse,
    
    
    
    BookmarksDeleteUsersResponse,
    
    
} from './models.js';

/**
 * Client for Bookmarks operations
 */
export class BookmarksClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }

    
    /**
     * Get Bookmarks
     * 
     * 
     * Retrieves a list of Posts bookmarked by the authenticated user.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User for whom to return results.
     * 
     * 
     * 
     * @param maxResults The maximum number of results.
     * 
     * 
     * 
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * 
     * 
     * 
     * @param tweetfields A comma separated list of Tweet fields to display.
     * 
     * 
     * 
     * @param expansions A comma separated list of fields to expand.
     * 
     * 
     * 
     * @param mediafields A comma separated list of Media fields to display.
     * 
     * 
     * 
     * @param pollfields A comma separated list of Poll fields to display.
     * 
     * 
     * 
     * @param userfields A comma separated list of User fields to display.
     * 
     * 
     * 
     * @param placefields A comma separated list of Place fields to display.
     * 
     * 
     * 
     * @returns BookmarksGetUsersResponse Response data
     */
    async getUsers(
        
        
        
        id: string,
        
        
        
        
        
        
        
        maxResults?: number,
        
        
        
        paginationToken?: string,
        
        
        
        tweetfields?: Array<any>,
        
        
        
        expansions?: Array<any>,
        
        
        
        mediafields?: Array<any>,
        
        
        
        pollfields?: Array<any>,
        
        
        
        userfields?: Array<any>,
        
        
        
        placefields?: Array<any>,
        
        
        
        
    ): Promise<BookmarksGetUsersResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/bookmarks";

        

        
        
        
        
        
        
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
        
        
        
        
        
        if (tweetfields !== undefined) {
            
            params.set("tweet.fields", tweetfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (expansions !== undefined) {
            
            params.set("expansions", expansions.map(String).join(","));
            
        }
        
        
        
        
        
        if (mediafields !== undefined) {
            
            params.set("media.fields", mediafields.map(String).join(","));
            
        }
        
        
        
        
        
        if (pollfields !== undefined) {
            
            params.set("poll.fields", pollfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (userfields !== undefined) {
            
            params.set("user.fields", userfields.map(String).join(","));
            
        }
        
        
        
        
        
        if (placefields !== undefined) {
            
            params.set("place.fields", placefields.map(String).join(","));
            
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

        
        return responseData as BookmarksGetUsersResponse;
        
    }
    
    /**
     * Create Bookmark
     * 
     * 
     * Adds a post to the authenticated user’s bookmarks.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User for whom to add bookmarks.
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
     * @returns BookmarksCreateUsersResponse Response data
     */
    async createUsers(
        
        
        
        id: string,
        
        
        
        
        body: BookmarksCreateUsersRequest,
        
        
        
        
        
    ): Promise<BookmarksCreateUsersResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/bookmarks";

        

        
        
        
        
        
        
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

        
        return responseData as BookmarksCreateUsersResponse;
        
    }
    
    /**
     * Get Bookmark folders
     * 
     * 
     * Retrieves a list of Bookmark folders created by the authenticated user.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User for whom to return results.
     * 
     * 
     * 
     * @param maxResults The maximum number of results.
     * 
     * 
     * 
     * @param paginationToken This parameter is used to get the next 'page' of results.
     * 
     * 
     * 
     * @returns BookmarksGetUsersFoldersResponse Response data
     */
    async getUsersFolders(
        
        
        
        id: string,
        
        
        
        
        
        
        
        maxResults?: number,
        
        
        
        paginationToken?: string,
        
        
        
        
    ): Promise<BookmarksGetUsersFoldersResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/bookmarks/folders";

        

        
        
        
        
        
        
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

        
        return responseData as BookmarksGetUsersFoldersResponse;
        
    }
    
    /**
     * Get Bookmarks by folder ID
     * 
     * 
     * Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User for whom to return results.
     * 
     * 
     * 
     * @param folderId The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.
     * 
     * 
     * 
     * @returns BookmarksGetUsersByFolderIdResponse Response data
     */
    async getUsersByFolderId(
        
        
        
        id: string,
        
        
        
        folderId: string,
        
        
        
        
        
        
        
        
    ): Promise<BookmarksGetUsersByFolderIdResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/bookmarks/folders/{folder_id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        url = url.replace("{folder_id}", String(folderId));
        
        
        

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

        
        return responseData as BookmarksGetUsersByFolderIdResponse;
        
    }
    
    /**
     * Delete Bookmark
     * 
     * 
     * Removes a Post from the authenticated user’s Bookmarks by its ID.
     * 
     * 
     * 
     * 
     * @param id The ID of the authenticated source User whose bookmark is to be removed.
     * 
     * 
     * 
     * @param tweetId The ID of the Post that the source User is removing from bookmarks.
     * 
     * 
     * 
     * @returns BookmarksDeleteUsersResponse Response data
     */
    async deleteUsers(
        
        
        
        id: string,
        
        
        
        tweetId: string,
        
        
        
        
        
        
        
        
    ): Promise<BookmarksDeleteUsersResponse> {
        let url = this.client.baseUrl + "/2/users/{id}/bookmarks/{tweet_id}";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        
        

        
        
        
        url = url.replace("{id}", String(id));
        
        
        
        
        
        url = url.replace("{tweet_id}", String(tweetId));
        
        
        

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

        
        return responseData as BookmarksDeleteUsersResponse;
        
    }
    
} 