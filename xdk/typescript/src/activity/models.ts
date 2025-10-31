/**
 * Models for activity operations
 */

/**
 * Request body for updateSubscription
 */
export interface UpdateSubscriptionRequest {
  tag?: string;
  /** The unique identifier of this webhook config. */
  webhookId?: string;
}

/**
 * Response for updateSubscription
 */
export interface UpdateSubscriptionResponse {
  data?: Record<string, any>;
}

/**
 * Response for deleteSubscription
 */
export interface DeleteSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getSubscriptions
 */
export interface GetSubscriptionsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createSubscription
 */
export interface CreateSubscriptionRequest {
  eventType?: string;
  /** An XAA subscription. */
  filter?: Record<string, any>;
  tag?: string;
  /** The unique identifier of this webhook config. */
  webhookId?: string;
}

/**
 * Response for createSubscription
 */
export interface CreateSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for stream
 * An activity event or error that can be returned by the x activity streaming API.
 */
export interface StreamResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
