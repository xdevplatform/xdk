/**
 * Compliance client for the X API.
 *
 * This module provides a client for interacting with the Compliance endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  ComplianceGetJobsByIdResponse,
  ComplianceGetJobsResponse,
  ComplianceCreateJobsRequest,
  ComplianceCreateJobsResponse,
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
     * Get Compliance Job by ID
     * Retrieves details of a specific Compliance Job by its ID.
     * @param id The ID of the Compliance Job to retrieve.
     * @param complianceJobfields A comma separated list of ComplianceJob fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getJobsById(
    id: string,
    complianceJobfields?: Array<any>,
    options?: RequestOptions
  ): Promise<ApiResponse<ComplianceGetJobsByIdResponse>> {
    const params = new URLSearchParams();

    if (complianceJobfields !== undefined) {
      params.set('compliance_job.fields', String(complianceJobfields));
    }

    const path = `/2/compliance/jobs/{id}`.replace('{id}', String(id));

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ComplianceGetJobsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Get Compliance Jobs
     * Retrieves a list of Compliance Jobs filtered by job type and optional status.
     * @param type Type of Compliance Job to list.
     * @param status Status of Compliance Job to list.
     * @param complianceJobfields A comma separated list of ComplianceJob fields to display.* @param options Additional request options
     * @returns Promise with the API response
     */
  async getJobs(
    type: string,
    complianceJobfields?: Array<any>,
    status?: string,
    options?: RequestOptions
  ): Promise<ApiResponse<ComplianceGetJobsResponse>> {
    const params = new URLSearchParams();

    if (type !== undefined) {
      params.set('type', String(type));
    }

    if (status !== undefined) {
      params.set('status', String(status));
    }

    if (complianceJobfields !== undefined) {
      params.set('compliance_job.fields', String(complianceJobfields));
    }

    const path = `/2/compliance/jobs`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},
      },
    };

    return this.client.request<ComplianceGetJobsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }

  /**
     * Create Compliance Job
     * Creates a new Compliance Job for the specified job type.* @param body A request to create a new batch compliance job.* @param options Additional request options
     * @returns Promise with the API response
     */
  async createJobs(
    body: ComplianceCreateJobsRequest,
    options?: RequestOptions
  ): Promise<ApiResponse<ComplianceCreateJobsResponse>> {
    const params = new URLSearchParams();

    const path = `/2/compliance/jobs`;

    const requestOptions: RequestOptions = {
      ...options,
      headers: {
        ...options && options.headers ? options.headers : {},

        'Content-Type': 'application/json',
      },
    };

    if (body) {
      requestOptions.body = JSON.stringify(body);
    }

    return this.client.request<ComplianceCreateJobsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      requestOptions
    );
  }
}
