/**
 * Models for compliance operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getJobs
 * 
 * @public
 */
export type GetJobsResponse = Schemas.Get2ComplianceJobsResponse;
/**
 * Request for createJobs
 * 
 * @public
 */
export type CreateJobsRequest = Schemas.CreateComplianceJobRequest;
/**
 * Response for createJobs
 * 
 * @public
 */
export type CreateJobsResponse = Schemas.CreateComplianceJobResponse;
/**
 * Response for getJobsById
 * 
 * @public
 */
export type GetJobsByIdResponse = Schemas.Get2ComplianceJobsIdResponse;