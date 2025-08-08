/**
 * Account activity client for the X API.
 *
 * This module provides a client for interacting with the Account activity endpoints of the X API.
 */

import { Client } from '../client.js';
import {
    
    
    AccountActivityDeleteSubscriptionResponse,
    
    
    
    AccountActivityValidateSubscriptionResponse,
    
    
    
    AccountActivityCreateReplayJobResponse,
    
    
    
    AccountActivityGetSubscriptionsResponse,
    
    
    
    AccountActivityGetSubscriptionCountResponse,
    
    
} from './models.js';

/**
 * Client for Account activity operations
 */
export class AccountActivityClient {
    private client: Client;

    constructor(client: Client) {
        this.client = client;
    }

    
    /**
     * Delete subscription
     * 
     * 
     * Deletes an Account Activity subscription for the given webhook and user ID.
     * 
     * 
     * 
     * 
     * @param webhookId The webhook ID to check subscription against.
     * 
     * 
     * 
     * @param userId User ID to unsubscribe from.
     * 
     * 
     * 
     * @returns AccountActivityDeleteSubscriptionResponse Response data
     */
    async deleteSubscription(
        
        
        
        webhookId: string,
        
        
        
        userId: string,
        
        
        
        
        
        
        
        
    ): Promise<AccountActivityDeleteSubscriptionResponse> {
        let url = this.client.baseUrl + "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        
        

        
        
        
        url = url.replace("{webhook_id}", String(webhookId));
        
        
        
        
        
        url = url.replace("{user_id}", String(userId));
        
        
        

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

        
        return responseData as AccountActivityDeleteSubscriptionResponse;
        
    }
    
    /**
     * Validate subscription
     * 
     * 
     * Checks a user’s Account Activity subscription for a given webhook.
     * 
     * 
     * 
     * 
     * @param webhookId The webhook ID to check subscription against.
     * 
     * 
     * 
     * @returns AccountActivityValidateSubscriptionResponse Response data
     */
    async validateSubscription(
        
        
        
        webhookId: string,
        
        
        
        
        
        
        
        
    ): Promise<AccountActivityValidateSubscriptionResponse> {
        let url = this.client.baseUrl + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all";

        

        
        
        
        
        
        
        // Ensure we have a valid access token
        if (this.client.oauth2Auth && this.client.token) {
            // Check if token needs refresh
            if (this.client.isTokenExpired()) {
                await this.client.refreshToken();
            }
        }
        
        
        
        
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        

        
        
        
        url = url.replace("{webhook_id}", String(webhookId));
        
        
        

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

        
        return responseData as AccountActivityValidateSubscriptionResponse;
        
    }
    
    /**
     * Create replay job
     * 
     * 
     * Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.
     * 
     * 
     * 
     * 
     * @param webhookId The unique identifier for the webhook configuration.
     * 
     * 
     * 
     * @param fromDate The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format.
     * 
     * 
     * 
     * @param toDate The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format.
     * 
     * 
     * 
     * @returns AccountActivityCreateReplayJobResponse Response data
     */
    async createReplayJob(
        
        
        
        webhookId: string,
        
        
        
        fromDate: string,
        
        
        
        toDate: string,
        
        
        
        
        
        
        
        
    ): Promise<AccountActivityCreateReplayJobResponse> {
        let url = this.client.baseUrl + "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        

        const params = new URLSearchParams();
        
        
        
        
        
        
        
        if (fromDate !== undefined) {
            
            params.set("from_date", String(fromDate));
            
        }
        
        
        
        
        
        if (toDate !== undefined) {
            
            params.set("to_date", String(toDate));
            
        }
        
        
        

        
        
        
        url = url.replace("{webhook_id}", String(webhookId));
        
        
        
        
        
        
        
        
        
        
        

        const headers = new Headers();
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        // Make the request
        
        
        const response = await fetch(url + (params.toString() ? `?${params.toString()}` : ""), {
            method: "POST",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as AccountActivityCreateReplayJobResponse;
        
    }
    
    /**
     * Get subscriptions
     * 
     * 
     * Retrieves a list of all active subscriptions for a given webhook.
     * 
     * 
     * 
     * 
     * @param webhookId The webhook ID to pull subscriptions for.
     * 
     * 
     * 
     * @returns AccountActivityGetSubscriptionsResponse Response data
     */
    async getSubscriptions(
        
        
        
        webhookId: string,
        
        
        
        
        
        
        
        
    ): Promise<AccountActivityGetSubscriptionsResponse> {
        let url = this.client.baseUrl + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list";

        

        
        
        
        
        
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
            method: "GET",
            headers,
            
        });
        
        

        // Check for errors
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the response data
        const responseData = await response.json();

        
        return responseData as AccountActivityGetSubscriptionsResponse;
        
    }
    
    /**
     * Get subscription count
     * 
     * 
     * Retrieves a count of currently active Account Activity subscriptions.
     * 
     * 
     * 
     * 
     * @returns AccountActivityGetSubscriptionCountResponse Response data
     */
    async getSubscriptionCount(
        
        
        
        
        
        
        
        
    ): Promise<AccountActivityGetSubscriptionCountResponse> {
        let url = this.client.baseUrl + "/2/account_activity/subscriptions/count";

        

        
        
        
        
        
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        
        
        
        
        

        const params = new URLSearchParams();
        

        

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

        
        return responseData as AccountActivityGetSubscriptionCountResponse;
        
    }
    
} 