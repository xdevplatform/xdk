/**
 * Usage client for the X API.
 *
 * This module provides a client for interacting with the Usage endpoints of the X API.
 */

import { Client } from '../client.js';

import {
    UsageGetResponse,
} from './models.js';
/**
 * Client for Usage operations
 */

export class UsageClient {
    private client: Client;
    constructor(client: Client) {
        this.client = client;
    }
    /**
     * Get usage
     * 

     * Retrieves usage statistics for Posts over a specified number of days.



     * @param days The number of days for which you need usage for.



     * @param usagefields A comma separated list of Usage fields to display.



     * @returns UsageGetResponse Response data
     */

    async get(
        days?: number,
        usagefields?: Array<any>,
    ): Promise<UsageGetResponse> {
        let url = this.client.baseUrl + "/2/usage/tweets";
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        const params = new URLSearchParams();
        if (days !== undefined) {
            params.set("days", String(days));
        }
        if (usagefields !== undefined) {
            params.set("usage.fields", usagefields.map(String).join(","));
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
        return responseData as UsageGetResponse;
    }
} 