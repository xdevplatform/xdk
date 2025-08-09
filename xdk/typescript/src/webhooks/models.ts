/**
 * Models for Webhooks operations
 */

/**
 * Response for validate
 */
export interface WebhooksValidateResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for delete
 */
export interface WebhooksDeleteResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for get
 */
export interface WebhooksGetResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Request body for create
 */
export interface WebhooksCreateRequest {
  url?: string;
}

/**
 * Response for create
 * A Webhook Configuration
 */
export interface WebhooksCreateResponse {
  createdAt?: string;
  /** The unique identifier of this webhook config. */
  id?: string;
  /** The callback URL of the webhook. */
  url?: string;
  valid?: boolean;
}
