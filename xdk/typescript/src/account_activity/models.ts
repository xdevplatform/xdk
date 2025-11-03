/**
 * Models for account activity operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getSubscriptions
 * 
 * @public
 */
export type GetSubscriptionsResponse = Schemas.SubscriptionsListGetResponse;
/**
 * Response for createReplayJob
 * 
 * @public
 */
export type CreateReplayJobResponse = Schemas.ReplayJobCreateResponse;
/**
 * Response for validateSubscription
 * 
 * @public
 */
export type ValidateSubscriptionResponse = Schemas.SubscriptionsGetResponse;
/**
 * Request for createSubscription
 * 
 * @public
 */
export type CreateSubscriptionRequest = Schemas.SubscriptionsCreateRequest;
/**
 * Response for createSubscription
 * 
 * @public
 */
export type CreateSubscriptionResponse = Schemas.SubscriptionsCreateResponse;
/**
 * Response for deleteSubscription
 * 
 * @public
 */
export type DeleteSubscriptionResponse = Schemas.SubscriptionsDeleteResponse;
/**
 * Response for getSubscriptionCount
 * 
 * @public
 */
export type GetSubscriptionCountResponse = Schemas.SubscriptionsCountGetResponse;