/**
 * Models for stream operations
 */
import type * as Schemas from '../schemas.js';





/**
 * Response for postsSample
 * 
 * @public
 */
export type PostsSampleResponse = Schemas.StreamingTweetResponse;
/**
 * Response for postsFirehoseEn
 * 
 * @public
 */
export type PostsFirehoseEnResponse = Schemas.StreamingTweetResponse;
/**
 * Response for postsSample10
 * 
 * @public
 */
export type PostsSample10Response = Schemas.Get2TweetsSample10StreamResponse;
/**
 * Response for likesFirehose
 * 
 * @public
 */
export type LikesFirehoseResponse = Schemas.StreamingLikeResponseV2;
/**
 * Response for getRuleCounts
 * 
 * @public
 */
export type GetRuleCountsResponse = Schemas.Get2TweetsSearchStreamRulesCountsResponse;
/**
 * Response for likesSample10
 * 
 * @public
 */
export type LikesSample10Response = Schemas.StreamingLikeResponseV2;
/**
 * Response for postsFirehose
 * 
 * @public
 */
export type PostsFirehoseResponse = Schemas.StreamingTweetResponse;
/**
 * Response for postsFirehoseKo
 * 
 * @public
 */
export type PostsFirehoseKoResponse = Schemas.StreamingTweetResponse;
/**
 * Response for getRules
 * 
 * @public
 */
export type GetRulesResponse = Schemas.RulesLookupResponse;
/**
 * Request for updateRules
 * 
 * @public
 */
export type UpdateRulesRequest = Schemas.AddOrDeleteRulesRequest;
/**
 * Response for updateRules
 * 
 * @public
 */
export type UpdateRulesResponse = Schemas.AddOrDeleteRulesResponse;
/**
 * Response for labelsCompliance
 * 
 * @public
 */
export type LabelsComplianceResponse = Schemas.TweetLabelStreamResponse;
/**
 * Response for postsCompliance
 * 
 * @public
 */
export type PostsComplianceResponse = Schemas.TweetComplianceStreamResponse;
/**
 * Response for usersCompliance
 * 
 * @public
 */
export type UsersComplianceResponse = Schemas.UserComplianceStreamResponse;
/**
 * Response for posts
 * 
 * @public
 */
export type PostsResponse = Schemas.FilteredStreamingTweetResponse;
/**
 * Response for likesCompliance
 * 
 * @public
 */
export type LikesComplianceResponse = Schemas.LikesComplianceStreamResponse;
/**
 * Response for postsFirehosePt
 * 
 * @public
 */
export type PostsFirehosePtResponse = Schemas.StreamingTweetResponse;
/**
 * Response for postsFirehoseJa
 * 
 * @public
 */
export type PostsFirehoseJaResponse = Schemas.StreamingTweetResponse;