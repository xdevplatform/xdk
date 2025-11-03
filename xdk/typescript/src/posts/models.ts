/**
 * Models for posts operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for getInsights28hr
 * 
 * @public
 */
export type GetInsights28hrResponse = Schemas.Get2Insights28hrResponse;
/**
 * Response for searchRecent
 * 
 * @public
 */
export type SearchRecentResponse = Schemas.Get2TweetsSearchRecentResponse;
/**
 * Response for getRepostedBy
 * 
 * @public
 */
export type GetRepostedByResponse = Schemas.Get2TweetsIdRetweetedByResponse;
/**
 * Response for getLikingUsers
 * 
 * @public
 */
export type GetLikingUsersResponse = Schemas.Get2TweetsIdLikingUsersResponse;
/**
 * Response for getInsightsHistorical
 * 
 * @public
 */
export type GetInsightsHistoricalResponse = Schemas.Get2InsightsHistoricalResponse;
/**
 * Response for getReposts
 * 
 * @public
 */
export type GetRepostsResponse = Schemas.Get2TweetsIdRetweetsResponse;
/**
 * Request for hideReply
 * 
 * @public
 */
export type HideReplyRequest = Schemas.TweetHideRequest;
/**
 * Response for hideReply
 * 
 * @public
 */
export type HideReplyResponse = Schemas.TweetHideResponse;
/**
 * Response for getCountsRecent
 * 
 * @public
 */
export type GetCountsRecentResponse = Schemas.Get2TweetsCountsRecentResponse;
/**
 * Response for getByIds
 * 
 * @public
 */
export type GetByIdsResponse = Schemas.Get2TweetsResponse;
/**
 * Request for create
 * 
 * @public
 */
export type CreateRequest = Schemas.TweetCreateRequest;
/**
 * Response for create
 * 
 * @public
 */
export type CreateResponse = Schemas.TweetCreateResponse;
/**
 * Response for getById
 * 
 * @public
 */
export type GetByIdResponse = Schemas.Get2TweetsIdResponse;
/**
 * Response for delete
 * 
 * @public
 */
export type DeleteResponse = Schemas.TweetDeleteResponse;
/**
 * Response for getAnalytics
 * 
 * @public
 */
export type GetAnalyticsResponse = Schemas.Analytics;
/**
 * Response for getCountsAll
 * 
 * @public
 */
export type GetCountsAllResponse = Schemas.Get2TweetsCountsAllResponse;
/**
 * Response for getQuoted
 * 
 * @public
 */
export type GetQuotedResponse = Schemas.Get2TweetsIdQuoteTweetsResponse;
/**
 * Response for searchAll
 * 
 * @public
 */
export type SearchAllResponse = Schemas.Get2TweetsSearchAllResponse;