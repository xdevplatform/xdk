/**
 * Models for webhooks operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getStreamLinks
 * 
 * @public
 */
export type GetStreamLinksResponse = Schemas.WebhookLinksGetResponse;
/**
 * Response for createStreamLink
 * 
 * @public
 */
export type CreateStreamLinkResponse = Schemas.WebhookLinksCreateResponse;
/**
 * Response for deleteStreamLink
 * 
 * @public
 */
export type DeleteStreamLinkResponse = Schemas.WebhookLinksDeleteResponse;
/**
 * Response for validate
 * 
 * @public
 */
export type ValidateResponse = Schemas.WebhookConfigPutResponse;
/**
 * Response for delete
 * 
 * @public
 */
export type DeleteResponse = Schemas.WebhookConfigDeleteResponse;
/**
 * Response for get
 * 
 * @public
 */
export type GetResponse = Schemas.Get2WebhooksResponse;
/**
 * Request for create
 * 
 * @public
 */
export type CreateRequest = Schemas.WebhookConfigCreateRequest;
/**
 * Response for create
 * 
 * @public
 */
export type CreateResponse = Schemas.WebhookConfigCreateResponse;