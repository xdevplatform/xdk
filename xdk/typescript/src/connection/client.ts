/**
 * Connection client for the X API.
 *
 * This module provides a client for interacting with the Connection endpoints of the X API.
 */

import { Client } from '../client.js';

import {
    ConnectionDeleteAllResponse,
} from './models.js';
/**
 * Client for Connection operations
 */

export class ConnectionClient {
    private client: Client;
    constructor(client: Client) {
        this.client = client;
    }
    /**
     * Terminate all connections
     * 

     * Terminates all active streaming connections for the authenticated application.



     * @returns ConnectionDeleteAllResponse Response data
     */

    async deleteAll(
    ): Promise<ConnectionDeleteAllResponse> {
        let url = this.client.baseUrl + "/2/connections/all";
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        const params = new URLSearchParams();
        const headers = new Headers();
        // Make the request
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "DELETE",
            headers,
        });
        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // Parse the response data
        const responseData = await response.json();
        return responseData as ConnectionDeleteAllResponse;
    }
} 