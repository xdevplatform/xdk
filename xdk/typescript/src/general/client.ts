/**
 * General client for the X API.
 *
 * This module provides a client for interacting with the General endpoints of the X API.
 */

import { Client } from '../client.js';

import {
    GeneralGetOpenApiSpecResponse,
} from './models.js';
/**
 * Client for General operations
 */

export class GeneralClient {
    private client: Client;
    constructor(client: Client) {
        this.client = client;
    }
    /**
     * Get OpenAPI Spec.
     * 

     * Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)



     * @returns GeneralGetOpenApiSpecResponse Response data
     */

    async getOpenApiSpec(
    ): Promise<GeneralGetOpenApiSpecResponse> {
        let url = this.client.baseUrl + "/2/openapi.json";
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
        return responseData as GeneralGetOpenApiSpecResponse;
    }
} 