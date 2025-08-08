/**
 * Webhooks client for the X API.
 *
 * This module provides a client for interacting with the Webhooks endpoints of the X API.
 */

import { Client } from '../client.js';
import {
    
    
    WebhooksGetResponse,
    
    
    
    WebhooksCreateRequest,
    
    WebhooksCreateResponse,
    
    
    
    
    WebhooksValidateResponse,
    
    
    
    WebhooksDeleteResponse,
    
    
} from './models.js';

/**
 * Client for Webhooks operations
 */
export class WebhooksClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }

    
    /**
     * Get webhook
     * 
     * 
     * Get a list of webhook configs associated with a client app.
     * 
     * 
     * 
     * 
     * @param webhookConfigfields A comma separated list of WebhookConfig fields to display.
     * 
     * 
     * 
     * @returns WebhooksGetResponse Response data
     */
    async get(
        
        
        
        
        
        
        
        webhookConfigfields?: Array<any>,
        
        
        
        
    ): Promise<WebhooksGetResponse> {
        let url = this.client.baseUrl + "/2/webhooks";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        if (webhookConfigfields !== undefined) {
            
            params.set("webhook_config.fields", webhookConfigfields.map(String).join(","));
            
        }
        
        
        

        
        
        
        
        

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

        
        return responseData as WebhooksGetResponse;
        
    }
    
    /**
     * Create webhook
     * 
     * 
     * Creates a new webhook configuration.
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
     * @returns WebhooksCreateResponse Response data
     */
    async create(
        
        
        
        
        
        
        
        
        body?: WebhooksCreateRequest,
        
    ): Promise<WebhooksCreateResponse> {
        let url = this.client.baseUrl + "/2/webhooks";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        

        

        const headers = new Headers();
        
        
        
        headers.set("Content-Type", "application/json");
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
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

        
        return responseData as WebhooksCreateResponse;
        
    }
    
    /**
     * Validate webhook
     * 
     * 
     * Triggers a CRC check for a given webhook.
     * 
     * 
     * 
     * 
     * @param webhookId The ID of the webhook to check.
     * 
     * 
     * 
     * @returns WebhooksValidateResponse Response data
     */
    async validate(
        
        
        
        webhookId: string,
        
        
        
        
        
        
        
        
    ): Promise<WebhooksValidateResponse> {
        let url = this.client.baseUrl + "/2/webhooks/{webhook_id}";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{webhook_id}", String(webhookId));
        
        
        

        const headers = new Headers();
        
        
        
        
        
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "PUT",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as WebhooksValidateResponse;
        
    }
    
    /**
     * Delete webhook
     * 
     * 
     * Deletes an existing webhook configuration.
     * 
     * 
     * 
     * 
     * @param webhookId The ID of the webhook to delete.
     * 
     * 
     * 
     * @returns WebhooksDeleteResponse Response data
     */
    async delete(
        
        
        
        webhookId: string,
        
        
        
        
        
        
        
        
    ): Promise<WebhooksDeleteResponse> {
        let url = this.client.baseUrl + "/2/webhooks/{webhook_id}";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{webhook_id}", String(webhookId));
        
        
        

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

        
        return responseData as WebhooksDeleteResponse;
        
    }
    
} 