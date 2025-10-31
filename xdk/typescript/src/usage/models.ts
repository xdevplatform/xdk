/**
 * Models for usage operations
 */

/**
 * Response for get
 */
export interface GetResponse {
  /** Usage per client app */
  data?: Record<string, any>;
  errors?: Array<any>;
}
