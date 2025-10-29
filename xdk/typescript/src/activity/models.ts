/**
 * Models for Activity operations
 */

/**
 * Request body for updateSubscription
 */
export interface ActivityUpdateSubscriptionRequest {
  tag?: string;
  /** The unique identifier of this webhook config. */
  webhookId?: string;
}

/**
 * Response for updateSubscription
 */
export interface ActivityUpdateSubscriptionResponse {
  data?: Record<string, any>;
}

/**
 * Response for deleteSubscription
 */
export interface ActivityDeleteSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for getSubscriptions
 */
export interface ActivityGetSubscriptionsResponse {
  data?: Array<any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Request body for createSubscription
 */
export interface ActivityCreateSubscriptionRequest {
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
export interface ActivityCreateSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
  meta?: Record<string, any>;
}

/**
 * Response for stream
 * An activity event or error that can be returned by the x activity streaming API.
 */
export interface ActivityStreamResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
