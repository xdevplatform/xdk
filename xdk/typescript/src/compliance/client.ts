/**
 * Compliance client for the X API.
 *
 * This module provides a client for interacting with the Compliance endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  ComplianceGetJobsResponse,
  ComplianceCreateJobsRequest,
  ComplianceCreateJobsResponse,
  ComplianceGetJobsByIdResponse,
} from './models.js';

/**
 * Options for getJobs method
 */
export interface ComplianceGetJobsOptions {
  /** Status of Compliance Job to list. */
  status?: string;

  /** A comma separated list of ComplianceJob fields to display. */
  complianceJobfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Options for getJobsById method
 */
export interface ComplianceGetJobsByIdOptions {
  /** A comma separated list of ComplianceJob fields to display. */
  complianceJobfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for Compliance operations
 * 
 * This client provides methods for interacting with the Compliance endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all Compliance related operations.
 * 
 * @category Compliance
 */
export class ComplianceClient {
  private client: Client;

  /**
     * Creates a new Compliance client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get Compliance Jobs
   * Retrieves a list of Compliance Jobs filtered by job type and optional status.


   * @param type Type of Compliance Job to list.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getJobs(
    type: string,
    options: ComplianceGetJobsOptions = {}
  ): Promise<ComplianceGetJobsResponse> {
    // Destructure options

    const {
      status = undefined,

      complianceJobfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/compliance/jobs';

    // Build query parameters
    const params = new URLSearchParams();

    if (type !== undefined) {
      params.append('type', String(type));
    }

    if (status !== undefined) {
      params.append('status', String(status));
    }

    if (complianceJobfields !== undefined) {
      params.append('compliance_job.fields', complianceJobfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<ComplianceGetJobsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Create Compliance Job
   * Creates a new Compliance Job for the specified job type.


   * @param body A request to create a new batch compliance job.

   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async createJobs(
    body: ComplianceCreateJobsRequest
  ): Promise<ComplianceCreateJobsResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/compliance/jobs';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      body: JSON.stringify(body || {}),

      // No optional parameters, using empty request options
    };

    return this.client.request<ComplianceCreateJobsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Compliance Job by ID
   * Retrieves details of a specific Compliance Job by its ID.


   * @param id The ID of the Compliance Job to retrieve.



   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getJobsById(
    id: string,
    options: ComplianceGetJobsByIdOptions = {}
  ): Promise<ComplianceGetJobsByIdResponse> {
    // Destructure options

    const {
      complianceJobfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build the path with path parameters
    let path = '/2/compliance/jobs/{id}';

    path = path.replace('{id}', encodeURIComponent(String(id)));

    // Build query parameters
    const params = new URLSearchParams();

    if (complianceJobfields !== undefined) {
      params.append('compliance_job.fields', complianceJobfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<ComplianceGetJobsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
