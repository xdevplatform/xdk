/**
 * Models for webhooks operations
 */

/**
 * Response for createStreamLink
 */
export interface CreateStreamLinkResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for deleteStreamLink
 */
export interface DeleteStreamLinkResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getStreamLinks
 */
export interface GetStreamLinksResponse {
  /** The list of active webhook links for a given stream */
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for get
 */
export interface GetResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Request body for create
 */
export interface CreateRequest {
  url?: string;
}

/**
 * Response for create
 * A Webhook Configuration
 */
export interface CreateResponse {
  createdAt?: string;
  /** The unique identifier of this webhook config. */
  id?: string;
  /** The callback URL of the webhook. */
  url?: string;
  valid?: boolean;
}

/**
 * Response for validate
 */
export interface ValidateResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for delete
 */
export interface DeleteResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
