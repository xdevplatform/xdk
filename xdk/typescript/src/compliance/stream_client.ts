/**
 * Stream client for the X API.
 *
 * This module provides a client for interacting with the streaming endpoints of the X API.
 */

import { Client, ApiResponse, RequestOptions } from '../client.js';
import { EventDrivenStream, StreamEvent } from './event_driven_stream.js';
import {
  ComplianceGetJobsResponse,
  ComplianceCreateJobsResponse,
  ComplianceGetJobsByIdResponse,
} from './models.js';

/**
 * Options for getJobs method
 */
export interface ComplianceGetJobsStreamingOptions {
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
 */
export interface ComplianceCreateJobsStreamingOptions {
  /** Additional request options */
  requestOptions?: RequestOptions;
  /** Additional headers */
  headers?: Record<string, string>;
  /** AbortSignal for cancelling the request */
  signal?: AbortSignal;
}
/**
 * Options for getJobsById method
 */
export interface ComplianceGetJobsByIdStreamingOptions {
  /** A comma separated list of ComplianceJob fields to display. */
  complianceJobfields?: Array<any>;

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
     * Get Compliance Jobs
     * Retrieves a list of Compliance Jobs filtered by job type and optional status.
     * 
     * @returns Promise with the API response
     */
  async getJobs(
    type: string,
    options: ComplianceGetJobsStreamingOptions = {}
  ): Promise<ComplianceGetJobsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getJobs');

    // Destructure options with defaults

    const {
      status = undefined,

      complianceJobfields = [],

      requestOptions: requestOptions = {},
    } = options;

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

    // Build path parameters
    let path = `/2/compliance/jobs`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<ComplianceGetJobsResponse>(
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
    options: ComplianceCreateJobsStreamingOptions = {}
  ): Promise<ComplianceCreateJobsResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'createJobs');

    // Destructure options with defaults

    const requestOptions = {};

    // Build query parameters
    const params = new URLSearchParams();

    // Build path parameters
    let path = `/2/compliance/jobs`;

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      body: JSON.stringify(body),

      ...options,
    };

    // Make the request
    return this.client.request<ComplianceCreateJobsResponse>(
      'POST',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }

  /**
     * Get Compliance Job by ID
     * Retrieves details of a specific Compliance Job by its ID.
     * 
     * @returns Promise with the API response
     */
  async getJobsById(
    id: string,
    options: ComplianceGetJobsByIdStreamingOptions = {}
  ): Promise<ComplianceGetJobsByIdResponse> {
    // Validate authentication requirements

    const requiredAuthTypes = [];

    requiredAuthTypes.push('BearerToken');

    this.client.validateAuthentication(requiredAuthTypes, 'getJobsById');

    // Destructure options with defaults

    const {
      complianceJobfields = [],

      requestOptions: requestOptions = {},
    } = options;

    // Build query parameters
    const params = new URLSearchParams();

    if (complianceJobfields !== undefined) {
      params.append('compliance_job.fields', complianceJobfields.join(','));
    }

    // Build path parameters
    let path = `/2/compliance/jobs/{id}`;

    path = path.replace(`{${'id'}}`, String(id));

    // Prepare request options
    const finalRequestOptions: RequestOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      signal: options.signal,

      ...options,
    };

    // Make the request
    return this.client.request<ComplianceGetJobsByIdResponse>(
      'GET',
      path + (params.toString() ? `?${params.toString()}` : ''),
      finalRequestOptions
    );
  }
}
