/**
 * Compliance client for the X API.
 *
 * This module provides a client for interacting with the Compliance endpoints of the X API.
 */

import { Client } from '../client.js';

import {
    ComplianceGetJobsResponse,
    ComplianceCreateJobsRequest,
    ComplianceCreateJobsResponse,
    ComplianceGetJobsByIdResponse,
} from './models.js';
/**
 * Client for Compliance operations
 */

export class ComplianceClient {
    private client: Client;
    constructor(client: Client) {
        this.client = client;
    }
    /**
     * Get Compliance Jobs
     * 

     * Retrieves a list of Compliance Jobs filtered by job type and optional status.



     * @param type Type of Compliance Job to list.



     * @param status Status of Compliance Job to list.



     * @param complianceJobfields A comma separated list of ComplianceJob fields to display.



     * @returns ComplianceGetJobsResponse Response data
     */

    async getJobs(
        type: string,
        status?: string,
        complianceJobfields?: Array<any>,
    ): Promise<ComplianceGetJobsResponse> {
        let url = this.client.baseUrl + "/2/compliance/jobs";
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        const params = new URLSearchParams();
        if (type !== undefined) {
            params.set("type", String(type));
        }
        if (status !== undefined) {
            params.set("status", String(status));
        }
        if (complianceJobfields !== undefined) {
            params.set("compliance_job.fields", complianceJobfields.map(String).join(","));
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
        return responseData as ComplianceGetJobsResponse;
    }
    /**
     * Create Compliance Job
     * 

     * Creates a new Compliance Job for the specified job type.







     * @param body A request to create a new batch compliance job.



     * @returns ComplianceCreateJobsResponse Response data
     */

    async createJobs(
        body: ComplianceCreateJobsRequest,
    ): Promise<ComplianceCreateJobsResponse> {
        let url = this.client.baseUrl + "/2/compliance/jobs";
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
        return responseData as ComplianceCreateJobsResponse;
    }
    /**
     * Get Compliance Job by ID
     * 

     * Retrieves details of a specific Compliance Job by its ID.



     * @param id The ID of the Compliance Job to retrieve.



     * @param complianceJobfields A comma separated list of ComplianceJob fields to display.



     * @returns ComplianceGetJobsByIdResponse Response data
     */

    async getJobsById(
        id: string,
        complianceJobfields?: Array<any>,
    ): Promise<ComplianceGetJobsByIdResponse> {
        let url = this.client.baseUrl + "/2/compliance/jobs/{id}";
        if (this.client.bearerToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.bearerToken}`);
        } else if (this.client.accessToken) {
            this.client.headers.set("Authorization", `Bearer ${this.client.accessToken}`);
        }
        const params = new URLSearchParams();
        if (complianceJobfields !== undefined) {
            params.set("compliance_job.fields", complianceJobfields.map(String).join(","));
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
        return responseData as ComplianceGetJobsByIdResponse;
    }
} 