/**
 * Models for Account activity operations
 */
/**
 * Response for getSubscriptions

 */

export interface AccountActivityGetSubscriptionsResponse {
    /** The list of active subscriptions for a specified webhook */

    data: Record<string, any>;



    errors?: Array<any>;


}









/**
 * Response for createReplayJob

 * Confirmation that the replay job request was accepted.

 */

export interface AccountActivityCreateReplayJobResponse {
    /** The UTC timestamp indicating when the replay job was created. */

    createdAt?: string;



    /** The unique identifier for the initiated replay job. */

    jobId?: string;


}









/**
 * Response for deleteSubscription

 */

export interface AccountActivityDeleteSubscriptionResponse {
    data?: Record<string, any>;
    errors?: Array<any>;
}
/**
 * Response for getSubscriptionCount

 */

export interface AccountActivityGetSubscriptionCountResponse {
    /** The count of active subscriptions across all webhooks */

    data: Record<string, any>;



    errors?: Array<any>;


}









/**
 * Response for validateSubscription

 */

export interface AccountActivityValidateSubscriptionResponse {
    data?: Record<string, any>;
    errors?: Array<any>;
}