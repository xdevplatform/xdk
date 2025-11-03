/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  GetJobsByIdResponse,
  GetJobsResponse,
  CreateJobsResponse,
} from './models.js';

/**
 * Options for getJobsById method
 * 
 * @public
 */
export interface GetJobsByIdStreamingOptions {
  /** A comma separated list of ComplianceJob fields to display. */
  complianceJobfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getJobs method
 * 
 * @public
 */
export interface GetJobsStreamingOptions {
  /** Status of Compliance Job to list. */
  status?: string;

  /** A comma separated list of ComplianceJob fields to display. */
  complianceJobfields?: Array<any>;

  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for createJobs method
 * 
 * @public
 */
export interface CreateJobsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}

export class ComplianceClient {
  private client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  /**
     * Get Compliance Job by ID
     * Retrieves details of a specific Compliance Job by its ID.
     * 
     * @returns Promise with the API response
     */
  async getJobsById(
    id: string,
    options: GetJobsByIdStreamingOptions = {}
  ): Promise<GetJobsByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getJobsById');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      complianceJobfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

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
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetJobsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Compliance Jobs
     * Retrieves a list of Compliance Jobs filtered by job type and optional status.
     * 
     * @returns Promise with the API response
     */
  async getJobs(
    type: string,
    options: GetJobsStreamingOptions = {}
  ): Promise<GetJobsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getJobs');

    // Destructure options (exclude path parameters, they're already function params)

    const {
      status = undefined,

      complianceJobfields = [],

      headers = {},
      signal,
      requestOptions: requestOptions = {},
    } =
      options || {};

    // Build the path with path parameters
    let path = '/2/compliance/jobs';

    // Build query parameters
    const params = new URLSearchParams();

    params.append('type', String(type));

    if (status !== undefined) {
      params.append('status', String(status));
    }

    if (complianceJobfields !== undefined) {
      params.append('compliance_job.fields', complianceJobfields.join(','));
    }

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      ...requestOptions,
    };

    // Make the request
    return this.client.request<GetJobsResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Create Compliance Job
     * Creates a new Compliance Job for the specified job type.
     * 
     * @returns Promise with the API response
     */
  async createJobs(
    body: any,
    options: CreateJobsStreamingOptions = {}
  ): Promise<CreateJobsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createJobs');

    // Destructure options (exclude path parameters, they're already function params)

    const { headers = {}, signal, requestOptions = {} } = options || {};

    // Build the path with path parameters
    let path = '/2/compliance/jobs';

    // Build query parameters
    const params = new URLSearchParams();

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...headers,
      },
      signal: signal,

      body: JSON.stringify(body),

      ...requestOptions,
    };

    // Make the request
    return this.client.request<CreateJobsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
