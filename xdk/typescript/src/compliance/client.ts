/**
 * compliance client for the X API.
 *
 * This module provides a client for interacting with the compliance endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import {
  Paginator,
  PostPaginator,
  UserPaginator,
  EventPaginator,
} from '../paginator.js';
import {
  GetJobsByIdResponse,
  GetJobsResponse,
  CreateJobsRequest,
  CreateJobsResponse,
} from './models.js';

/**
 * Options for getJobs method
 */
export interface GetJobsOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
}

/**
 * Client for compliance operations
 * 
 * This client provides methods for interacting with the compliance endpoints
 * of the X API. It handles authentication, request formatting, and response
 * parsing for all compliance related operations.
 * 
 * @category compliance
 */
export class ComplianceClient {
  private client: Client;

  /**
     * Creates a new compliance client instance
     * 
     * @param client - The main X API client instance
     */
  constructor(client: Client) {
    this.client = client;
  }

  /**
   * Get Compliance Job by ID
   * Retrieves details of a specific Compliance Job by its ID.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getJobsById(): Promise<GetJobsByIdResponse> {
    // Destructure options

    const requestOptions = {};

    // Build the path with path parameters
    let path = '/2/compliance/jobs/{id}';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      // No optional parameters, using empty request options
    };

    return this.client.request<GetJobsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
   * Get Compliance Jobs
   * Retrieves a list of Compliance Jobs filtered by job type and optional status.




   * @returns Promise with the API response
   */
  // Overload 1: Default behavior (unwrapped response)
  async getJobs(options: GetJobsOptions = {}): Promise<GetJobsResponse> {
    // Destructure options

    const { requestOptions: requestOptions = {} } = options;

    // Build the path with path parameters
    let path = '/2/compliance/jobs';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      ...requestOptions,
    };

    return this.client.request<GetJobsResponse>(
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
  async createJobs(body: CreateJobsRequest): Promise<CreateJobsResponse> {
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

    return this.client.request<CreateJobsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
