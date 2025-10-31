/**
 * Models for account activity operations
 */

/**
 * Response for getSubscriptionCount
 */
export interface GetSubscriptionCountResponse {
  /** The count of active subscriptions across all webhooks */
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for getSubscriptions
 */
export interface GetSubscriptionsResponse {
  /** The list of active subscriptions for a specified webhook */
  data: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for createReplayJob
 * Confirmation that the replay job request was accepted.
 */
export interface CreateReplayJobResponse {
  /** The UTC timestamp indicating when the replay job was created. */
  createdAt?: string;
  /** The unique identifier for the initiated replay job. */
  jobId?: string;
}

/**
 * Response for deleteSubscription
 */
export interface DeleteSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Response for validateSubscription
 */
export interface ValidateSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}

/**
 * Request body for createSubscription
 */
export interface CreateSubscriptionRequest {}

/**
 * Response for createSubscription
 */
export interface CreateSubscriptionResponse {
  data?: Record<string, any>;
  errors?: Array<any>;
}
