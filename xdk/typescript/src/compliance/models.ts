/**
 * Models for compliance operations
 */

/**
 * Response for getJobsById
 */
export interface GetJobsByIdResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getJobs
 */
export interface GetJobsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createJobs
 * A request to create a new batch compliance job.
 */
export interface CreateJobsRequest {
  /** User-provided name for a compliance job. */
  name?: string;
  /** If true, this endpoint will return a pre-signed URL with resumable uploads enabled. */
  resumable?: boolean;
  /** Type of compliance job to list. */
  type?: string;
}

/**
 * Response for createJobs
 */
export interface CreateJobsResponse {
  data: Record<string, any>;
  errors?: Array<any>;
}
