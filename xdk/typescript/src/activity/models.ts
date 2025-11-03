/**
 * Models for activity operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for stream
 * 
 * @public
 */
export type StreamResponse = Schemas.ActivityStreamingResponse;
/**
 * Request for updateSubscription
 * 
 * @public
 */
export type UpdateSubscriptionRequest = Schemas.ActivitySubscriptionUpdateRequest;
/**
 * Response for updateSubscription
 * 
 * @public
 */
export type UpdateSubscriptionResponse = Schemas.ActivitySubscriptionUpdateResponse;
/**
 * Response for deleteSubscription
 * 
 * @public
 */
export type DeleteSubscriptionResponse = Schemas.ActivitySubscriptionDeleteResponse;
/**
 * Response for getSubscriptions
 * 
 * @public
 */
export type GetSubscriptionsResponse = Schemas.ActivitySubscriptionGetResponse;
/**
 * Request for createSubscription
 * 
 * @public
 */
export type CreateSubscriptionRequest = Schemas.ActivitySubscriptionCreateRequest;
/**
 * Response for createSubscription
 * 
 * @public
 */
export type CreateSubscriptionResponse = Schemas.ActivitySubscriptionCreateResponse;