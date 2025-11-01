/**
 * OpenAPI Schema Types
 * Auto-generated from OpenAPI components/schemas
 */

/**
The unique identifier of an Activity event.
 *
 * @public
 */
export type ActivityEventId = string; /**
An activity event or error that can be returned by the x activity streaming API.
 *
 * @public
 */
export interface ActivityStreamingResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
An XActivity subscription.
 *
 * @public
 */
export interface ActivitySubscription {
  /** none */ createdAt: string;
  /** none */ eventType: string;
  filter: ActivitySubscriptionFilter;
  subscriptionId: ActivitySubscriptionId;
  /** none */ tag?: string;
  /** none */ updatedAt: string;
  webhookId?: WebhookConfigId;
} /**
Schema type for ActivitySubscriptionCreateRequest
 *
 * @public
 */
export interface ActivitySubscriptionCreateRequest {
  /** none */ eventType:
    | 'ProfileBioUpdate'
    | 'ProfilePictureUpdate'
    | 'ProfileBannerPictureUpdate'
    | 'ProfileScreennameUpdate'
    | 'ProfileGeoUpdate'
    | 'ProfileUrlUpdate'
    | 'ProfileVerifiedBadgeUpdate';
  filter: ActivitySubscriptionFilter;
  /** none */ tag?: string;
  webhookId?: WebhookConfigId;
} /**
Schema type for ActivitySubscriptionCreateResponse
 *
 * @public
 */
export interface ActivitySubscriptionCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for ActivitySubscriptionDeleteResponse
 *
 * @public
 */
export interface ActivitySubscriptionDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
An XAA subscription.
 *
 * @public
 */
export interface ActivitySubscriptionFilter {
  userId?: UserId;
} /**
Schema type for ActivitySubscriptionGetResponse
 *
 * @public
 */
export interface ActivitySubscriptionGetResponse {
  /** none */ data?: Array<ActivitySubscription>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
The unique identifier of this subscription.
 *
 * @public
 */
export type ActivitySubscriptionId = string; /**
Schema type for ActivitySubscriptionUpdateRequest
 *
 * @public
 */
export interface ActivitySubscriptionUpdateRequest {
  /** none */ tag?: string;
  webhookId?: WebhookConfigId;
} /**
Schema type for ActivitySubscriptionUpdateResponse
 *
 * @public
 */
export interface ActivitySubscriptionUpdateResponse {
  /** none */ data?: Record<string, any>;
}
/**
Schema type for AddOrDeleteRulesRequest
 *
 * @public
 */
export type AddOrDeleteRulesRequest = any; /**
A response from modifying user-specified stream filtering rules.
 *
 * @public
 */
export interface AddOrDeleteRulesResponse {
  /** All user-specified stream filtering rules that were created. */ data?: Array<
    Rule
  >;
  /** none */ errors?: Array<Problem>;
  meta: RulesResponseMetadata;
} /**
A request to add a user-specified stream filtering rule.
 *
 * @public
 */
export interface AddRulesRequest {
  /** none */ add: Array<RuleNoId>;
} /**
The sum of results returned in this response.
 *
 * @public
 */
export type Aggregate = number; /**
Schema type for AllowDownloadStatus
 *
 * @public
 */
export interface AllowDownloadStatus {
  /** none */ allowDownload?: boolean;
} /**
Client App Rule Counts for all applications in the project
 *
 * @public
 */
export type AllProjectClientApps = Array<
  AppRulesCount
>; /**
Schema type for AltText
 *
 * @public
 */
export interface AltText {
  /** Description of media ( <= 1000 characters ) */ text: string;
} /**
Schema type for Analytics
 *
 * @public
 */
export interface Analytics {
  /** none */ data?: Array<Record<string, any>>;
  /** none */ errors?: Array<Problem>;
}
/**
Schema type for AnimatedGif
 *
 * @public
 */
export type AnimatedGif = any; /**
A count of user-provided stream filtering rules at the client application level.
 *
 * @public
 */
export interface AppRulesCount {
  clientAppId?: ClientAppId;
  /** Number of rules for client application */ ruleCount?: number;
} /**
Schema type for AudiencePolicy
 *
 * @public
 */
export interface AudiencePolicy {
  /** none */ creatorSubscriptions?: Array<'Any'>;
  /** none */ xSubscriptions?: Array<'Any'>;
} /**
Schema type for BookmarkAddRequest
 *
 * @public
 */
export interface BookmarkAddRequest {
  tweetId: TweetId;
} /**
The unique identifier of this Bookmark folder.
 *
 * @public
 */
export type BookmarkFolderId = string; /**
Schema type for BookmarkFolderPostsResponse
 *
 * @public
 */
export interface BookmarkFolderPostsResponse {
  /** none */ data?: Array<Record<string, any>>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for BookmarkFoldersResponse
 *
 * @public
 */
export interface BookmarkFoldersResponse {
  /** none */ data?: Array<Record<string, any>>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for BookmarkMutationResponse
 *
 * @public
 */
export interface BookmarkMutationResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
}
/**
Schema type for CashtagEntity
 *
 * @public
 */
export type CashtagEntity = any; /**
Represent the portion of text recognized as a Cashtag, and its start and end position within the text.
 *
 * @public
 */
export interface CashtagFields {
  /** none */ tag: string;
} /**
The ID of the client application
 *
 * @public
 */
export type ClientAppId = string; /**
Usage per client app
 *
 * @public
 */
export interface ClientAppUsage {
  /** The unique identifier for this project */ clientAppId?: string;
  /** The usage value */ usage?: Array<UsageFields>;
  /** The number of results returned */ usageResultCount?: number;
}
/**
Your client has gone away.
 *
 * @public
 */
export type ClientDisconnectedProblem = any;
/**
A problem that indicates your client is forbidden from making this request.
 *
 * @public
 */
export type ClientForbiddenProblem = any; /**
A X Community is a curated group of Posts.
 *
 * @public
 */
export interface Community {
  /** none */ createdAt?: string;
  id: CommunityId;
  /** The name of this Community. */ name: string;
} /**
The unique identifier of this Community.
 *
 * @public
 */
export type CommunityId = string; /**
Schema type for ComplianceJob
 *
 * @public
 */
export interface ComplianceJob {
  createdAt: CreatedAt;
  downloadExpiresAt: DownloadExpiration;
  downloadUrl: DownloadUrl;
  id: JobId;
  name?: ComplianceJobName;
  status: ComplianceJobStatus;
  type: ComplianceJobType;
  uploadExpiresAt: UploadExpiration;
  uploadUrl: UploadUrl;
} /**
User-provided name for a compliance job.
 *
 * @public
 */
export type ComplianceJobName = string; /**
Status of a compliance job.
 *
 * @public
 */
export type ComplianceJobStatus =
  | 'created'
  | 'in_progress'
  | 'failed'
  | 'complete'
  | 'expired'; /**
Type of compliance job to list.
 *
 * @public
 */
export type ComplianceJobType = 'tweets' | 'users';
/**
You cannot create a new job if one is already in progress.
 *
 * @public
 */
export type ConflictProblem = any;
/**
A problem that indicates something is wrong with the connection.
 *
 * @public
 */
export type ConnectionExceptionProblem = any; /**
Schema type for ContentExpiration
 *
 * @public
 */
export interface ContentExpiration {
  /** Expiration time for content as a Unix timestamp in seconds */ timestampSec: number;
} /**
Annotation inferred from the Tweet text.
 *
 * @public
 */
export interface ContextAnnotation {
  domain: ContextAnnotationDomainFields;
  entity: ContextAnnotationEntityFields;
} /**
Represents the data for the context annotation domain.
 *
 * @public
 */
export interface ContextAnnotationDomainFields {
  /** Description of the context annotation domain. */ description?: string;
  /** The unique id for a context annotation domain. */ id: string;
  /** Name of the context annotation domain. */ name?: string;
} /**
Represents the data for the context annotation entity.
 *
 * @public
 */
export interface ContextAnnotationEntityFields {
  /** Description of the context annotation entity. */ description?: string;
  /** The unique id for a context annotation entity. */ id: string;
  /** Name of the context annotation entity. */ name?: string;
} /**
A two-letter ISO 3166-1 alpha-2 country code.
 *
 * @public
 */
export type CountryCode = string; /**
Schema type for CreateAttachmentsMessageRequest
 *
 * @public
 */
export interface CreateAttachmentsMessageRequest {
  attachments: DmAttachments;
  /** Text of the message. */ text?: string;
} /**
A request to create a new batch compliance job.
 *
 * @public
 */
export interface CreateComplianceJobRequest {
  name?: ComplianceJobName;
  /** If true, this endpoint will return a pre-signed URL with resumable uploads enabled. */ resumable?: boolean;
  /** Type of compliance job to list. */ type: 'tweets' | 'users';
} /**
Schema type for CreateComplianceJobResponse
 *
 * @public
 */
export interface CreateComplianceJobResponse {
  data?: ComplianceJob;
  /** none */ errors?: Array<Problem>;
} /**
Creation time of the compliance job.
 *
 * @public
 */
export type CreatedAt = string; /**
Schema type for CreateDmConversationRequest
 *
 * @public
 */
export interface CreateDmConversationRequest {
  /** The conversation type that is being created. */ conversationType: 'Group';
  message: CreateMessageRequest;
  participantIds: DmParticipants;
} /**
Schema type for CreateDmEventResponse
 *
 * @public
 */
export interface CreateDmEventResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
}
/**
Schema type for CreateMessageRequest
 *
 * @public
 */
export type CreateMessageRequest = any; /**
Schema type for CreateNoteRequest
 *
 * @public
 */
export interface CreateNoteRequest {
  info: NoteInfo;
  postId: TweetId;
  /** If true, the note being submitted is only for testing the capability of the bot, and won't be publicly visible. If false, the note being submitted will be a new proposed note on the product. */ testMode: boolean;
} /**
Schema type for CreateNoteResponse
 *
 * @public
 */
export interface CreateNoteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for CreateTextMessageRequest
 *
 * @public
 */
export interface CreateTextMessageRequest {
  attachments?: DmAttachments;
  /** Text of the message. */ text: string;
} /**
Schema type for DeleteDmResponse
 *
 * @public
 */
export interface DeleteDmResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for DeleteNoteResponse
 *
 * @public
 */
export interface DeleteNoteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
A response from deleting user-specified stream filtering rules.
 *
 * @public
 */
export interface DeleteRulesRequest {
  /** IDs and values of all deleted user-specified stream filtering rules. */ delete: Record<
    string,
    any
  >;
}
/**
A problem that indicates that the resource requested violates the precepts of this API.
 *
 * @public
 */
export type DisallowedResourceProblem = any; /**
Represent a boundary range (start and end zero-based indices) for the portion of text that is displayed for a post. `start` must be smaller than `end`. The start index is inclusive, the end index is exclusive.
 *
 * @public
 */
export type DisplayTextRange = Array<
  number
>; /**
Attachments to a DM Event.
 *
 * @public
 */
export type DmAttachments = Array<
  DmMediaAttachment
>; /**
Unique identifier of a DM conversation. This can either be a numeric string, or a pair of numeric strings separated by a '-' character in the case of one-on-one DM Conversations.
 *
 * @public
 */
export type DmConversationId = string; /**
Schema type for DmEvent
 *
 * @public
 */
export interface DmEvent {
  /** Specifies the type of attachments (if any) present in this DM. */ attachments?: Record<
    string,
    any
  >;
  /** none */ cashtags?: Array<CashtagEntity>;
  /** none */ createdAt?: string;
  dmConversationId?: DmConversationId;
  /** none */ eventType: string;
  /** none */ hashtags?: Array<HashtagEntity>;
  id: DmEventId;
  /** none */ mentions?: Array<MentionEntity>;
  /** A list of participants for a ParticipantsJoin or ParticipantsLeave event_type. */ participantIds?: Array<
    UserId
  >;
  /** A list of Posts this DM refers to. */ referencedTweets?: Array<
    Record<string, any>
  >;
  senderId?: UserId;
  /** none */ text?: string;
  /** none */ urls?: Array<UrlEntityDm>;
} /**
Unique identifier of a DM Event.
 *
 * @public
 */
export type DmEventId = string; /**
Schema type for DmMediaAttachment
 *
 * @public
 */
export interface DmMediaAttachment {
  mediaId: MediaId;
} /**
Participants for the DM Conversation.
 *
 * @public
 */
export type DmParticipants = Array<
  UserId
>; /**
Schema type for DomainRestrictions
 *
 * @public
 */
export interface DomainRestrictions {
  /** List of whitelisted domains */ whitelist: Array<string>;
} /**
Expiration time of the download URL.
 *
 * @public
 */
export type DownloadExpiration = string; /**
URL from which the user will retrieve their compliance results.
 *
 * @public
 */
export type DownloadUrl = string;
/**
The rule you have submitted is a duplicate.
 *
 * @public
 */
export type DuplicateRuleProblem = any; /**
The end time of the bucket.
 *
 * @public
 */
export type End = string; /**
An Engagement Api Response.
 *
 * @public
 */
export interface Engagement {
  /** none */ errors?: Array<Record<string, any>>;
  /** none */ measurement?: Record<string, any>;
} /**
Represent a boundary range (start and end index) for a recognized entity (for example a hashtag or a mention). `start` must be smaller than `end`.  The start index is inclusive, the end index is exclusive.
 *
 * @public
 */
export interface EntityIndicesInclusiveExclusive {
  /** Index (zero-based) at which position this entity ends.  The index is exclusive. */ end: number;
  /** Index (zero-based) at which position this entity starts.  The index is inclusive. */ start: number;
} /**
Represent a boundary range (start and end index) for a recognized entity (for example a hashtag or a mention). `start` must be smaller than `end`.  The start index is inclusive, the end index is inclusive.
 *
 * @public
 */
export interface EntityIndicesInclusiveInclusive {
  /** Index (zero-based) at which position this entity ends.  The index is inclusive. */ end: number;
  /** Index (zero-based) at which position this entity starts.  The index is inclusive. */ start: number;
} /**
Schema type for Error
 *
 * @public
 */
export interface Error {
  /** none */ code: number;
  /** none */ message: string;
} /**
Schema type for EvaluateNoteRequest
 *
 * @public
 */
export interface EvaluateNoteRequest {
  /** Text for the community note. */ noteText: string;
  postId: TweetId;
} /**
Schema type for EvaluateNoteResponse
 *
 * @public
 */
export interface EvaluateNoteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Expansions
 *
 * @public
 */
export interface Expansions {
  /** none */ media?: Array<Media>;
  /** none */ places?: Array<Place>;
  /** none */ polls?: Array<Poll>;
  /** none */ topics?: Array<Topic>;
  /** none */ tweets?: Array<Tweet>;
  /** none */ users?: Array<User>;
}
/**
A problem that indicates that you are not allowed to see a particular field on a Tweet, User, etc.
 *
 * @public
 */
export type FieldUnauthorizedProblem = any; /**
A Tweet or error that can be returned by the streaming Tweet API. The values returned with a successful streamed Tweet includes the user provided rules that the Tweet matched.
 *
 * @public
 */
export interface FilteredStreamingTweetResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** The list of rules which matched the Tweet */ matchingRules?: Array<
    Record<string, any>
  >;
} /**
Schema type for FoundMediaOrigin
 *
 * @public
 */
export interface FoundMediaOrigin {
  /** Unique Identifier of media within provider ( <= 24 characters )) */ id: string;
  /** The media provider (e.g., 'giphy') that sourced the media ( <= 8 Characters ) */ provider: string;
} /**
Schema type for FullTextEntities
 *
 * @public
 */
export interface FullTextEntities {
  /** none */ annotations?: Array<any>;
  /** none */ cashtags?: Array<CashtagEntity>;
  /** none */ hashtags?: Array<HashtagEntity>;
  /** none */ mentions?: Array<MentionEntity>;
  /** none */ urls?: Array<UrlEntity>;
}
/**
A generic problem with no additional information beyond that provided by the HTTP status code.
 *
 * @public
 */
export type GenericProblem = any; /**
Schema type for Geo
 *
 * @public
 */
export interface Geo {
  /** none */ bbox: Array<number>;
  geometry?: Point;
  /** none */ properties: Record<string, any>;
  /** none */ type: 'Feature';
}
/**
Schema type for GeoRestrictions
 *
 * @public
 */
export type GeoRestrictions = any; /**
Schema type for Get2CommunitiesIdResponse
 *
 * @public
 */
export interface Get2CommunitiesIdResponse {
  data?: Community;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2CommunitiesSearchResponse
 *
 * @public
 */
export interface Get2CommunitiesSearchResponse {
  /** none */ data?: Array<Community>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2ComplianceJobsIdResponse
 *
 * @public
 */
export interface Get2ComplianceJobsIdResponse {
  data?: ComplianceJob;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2ComplianceJobsResponse
 *
 * @public
 */
export interface Get2ComplianceJobsResponse {
  /** none */ data?: Array<ComplianceJob>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2DmConversationsIdDmEventsResponse
 *
 * @public
 */
export interface Get2DmConversationsIdDmEventsResponse {
  /** none */ data?: Array<DmEvent>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2DmConversationsWithParticipantIdDmEventsResponse
 *
 * @public
 */
export interface Get2DmConversationsWithParticipantIdDmEventsResponse {
  /** none */ data?: Array<DmEvent>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2DmEventsEventIdResponse
 *
 * @public
 */
export interface Get2DmEventsEventIdResponse {
  data?: DmEvent;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2DmEventsResponse
 *
 * @public
 */
export interface Get2DmEventsResponse {
  /** none */ data?: Array<DmEvent>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2FdxAccountsAccountidContactResponse
 *
 * @public
 */
export interface Get2FdxAccountsAccountidContactResponse {
  data?: PlaidAccountContact;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2FdxAccountsAccountidPayment-networksResponse
 *
 * @public
 */
export interface Get2FdxAccountsAccountidPayment_networksResponse {
  /** none */ data?: Array<PlaidAccountPaymentNetwork>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2FdxAccountsAccountidResponse
 *
 * @public
 */
export interface Get2FdxAccountsAccountidResponse {
  data?: PlaidAccount;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2FdxAccountsAccountidTransactionsResponse
 *
 * @public
 */
export interface Get2FdxAccountsAccountidTransactionsResponse {
  /** none */ data?: Array<PlaidAccountTransaction>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2FdxCustomersCurrentResponse
 *
 * @public
 */
export interface Get2FdxCustomersCurrentResponse {
  data?: PlaidCustomer;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2Insights28hrResponse
 *
 * @public
 */
export interface Get2Insights28hrResponse {
  /** none */ data?: Array<Engagement>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2InsightsHistoricalResponse
 *
 * @public
 */
export interface Get2InsightsHistoricalResponse {
  /** none */ data?: Array<Engagement>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2LikesFirehoseStreamResponse
 *
 * @public
 */
export interface Get2LikesFirehoseStreamResponse {
  data?: LikeWithTweetAuthor;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2LikesSample10StreamResponse
 *
 * @public
 */
export interface Get2LikesSample10StreamResponse {
  data?: LikeWithTweetAuthor;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2ListsIdFollowersResponse
 *
 * @public
 */
export interface Get2ListsIdFollowersResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2ListsIdMembersResponse
 *
 * @public
 */
export interface Get2ListsIdMembersResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2ListsIdResponse
 *
 * @public
 */
export interface Get2ListsIdResponse {
  data?: List;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2ListsIdTweetsResponse
 *
 * @public
 */
export interface Get2ListsIdTweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2MediaAnalyticsResponse
 *
 * @public
 */
export interface Get2MediaAnalyticsResponse {
  data?: MediaAnalytics;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2MediaMediaKeyResponse
 *
 * @public
 */
export interface Get2MediaMediaKeyResponse {
  data?: Media;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2MediaResponse
 *
 * @public
 */
export interface Get2MediaResponse {
  /** none */ data?: Array<Media>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2NotesSearchNotesWrittenResponse
 *
 * @public
 */
export interface Get2NotesSearchNotesWrittenResponse {
  /** none */ data?: Array<Note>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2NotesSearchPostsEligibleForNotesResponse
 *
 * @public
 */
export interface Get2NotesSearchPostsEligibleForNotesResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2SpacesByCreatorIdsResponse
 *
 * @public
 */
export interface Get2SpacesByCreatorIdsResponse {
  /** none */ data?: Array<Space>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2SpacesIdBuyersResponse
 *
 * @public
 */
export interface Get2SpacesIdBuyersResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2SpacesIdResponse
 *
 * @public
 */
export interface Get2SpacesIdResponse {
  data?: Space;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2SpacesIdTweetsResponse
 *
 * @public
 */
export interface Get2SpacesIdTweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2SpacesResponse
 *
 * @public
 */
export interface Get2SpacesResponse {
  /** none */ data?: Array<Space>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2SpacesSearchResponse
 *
 * @public
 */
export interface Get2SpacesSearchResponse {
  /** none */ data?: Array<Space>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TrendsByWoeidWoeidResponse
 *
 * @public
 */
export interface Get2TrendsByWoeidWoeidResponse {
  /** none */ data?: Array<Trend>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2TweetsAnalyticsResponse
 *
 * @public
 */
export interface Get2TweetsAnalyticsResponse {
  data?: Analytics;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2TweetsCountsAllResponse
 *
 * @public
 */
export interface Get2TweetsCountsAllResponse {
  /** none */ data?: Array<SearchCount>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsCountsRecentResponse
 *
 * @public
 */
export interface Get2TweetsCountsRecentResponse {
  /** none */ data?: Array<SearchCount>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsFirehoseStreamLangEnResponse
 *
 * @public
 */
export interface Get2TweetsFirehoseStreamLangEnResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsFirehoseStreamLangJaResponse
 *
 * @public
 */
export interface Get2TweetsFirehoseStreamLangJaResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsFirehoseStreamLangKoResponse
 *
 * @public
 */
export interface Get2TweetsFirehoseStreamLangKoResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsFirehoseStreamLangPtResponse
 *
 * @public
 */
export interface Get2TweetsFirehoseStreamLangPtResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsFirehoseStreamResponse
 *
 * @public
 */
export interface Get2TweetsFirehoseStreamResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsIdLikingUsersResponse
 *
 * @public
 */
export interface Get2TweetsIdLikingUsersResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsIdQuoteTweetsResponse
 *
 * @public
 */
export interface Get2TweetsIdQuoteTweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsIdResponse
 *
 * @public
 */
export interface Get2TweetsIdResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsIdRetweetedByResponse
 *
 * @public
 */
export interface Get2TweetsIdRetweetedByResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsIdRetweetsResponse
 *
 * @public
 */
export interface Get2TweetsIdRetweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsResponse
 *
 * @public
 */
export interface Get2TweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsSample10StreamResponse
 *
 * @public
 */
export interface Get2TweetsSample10StreamResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsSampleStreamResponse
 *
 * @public
 */
export interface Get2TweetsSampleStreamResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsSearchAllResponse
 *
 * @public
 */
export interface Get2TweetsSearchAllResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsSearchRecentResponse
 *
 * @public
 */
export interface Get2TweetsSearchRecentResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2TweetsSearchStreamResponse
 *
 * @public
 */
export interface Get2TweetsSearchStreamResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2TweetsSearchStreamRulesCountsResponse
 *
 * @public
 */
export interface Get2TweetsSearchStreamRulesCountsResponse {
  data?: RulesCount;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2UsageTweetsResponse
 *
 * @public
 */
export interface Get2UsageTweetsResponse {
  data?: Usage;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2UsersByResponse
 *
 * @public
 */
export interface Get2UsersByResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2UsersByUsernameUsernameResponse
 *
 * @public
 */
export interface Get2UsersByUsernameUsernameResponse {
  data?: User;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2UsersIdBlockingResponse
 *
 * @public
 */
export interface Get2UsersIdBlockingResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdBookmarksResponse
 *
 * @public
 */
export interface Get2UsersIdBookmarksResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdFollowedListsResponse
 *
 * @public
 */
export interface Get2UsersIdFollowedListsResponse {
  /** none */ data?: Array<List>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdFollowersResponse
 *
 * @public
 */
export interface Get2UsersIdFollowersResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdFollowingResponse
 *
 * @public
 */
export interface Get2UsersIdFollowingResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdLikedTweetsResponse
 *
 * @public
 */
export interface Get2UsersIdLikedTweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdListMembershipsResponse
 *
 * @public
 */
export interface Get2UsersIdListMembershipsResponse {
  /** none */ data?: Array<List>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdMentionsResponse
 *
 * @public
 */
export interface Get2UsersIdMentionsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdMutingResponse
 *
 * @public
 */
export interface Get2UsersIdMutingResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdOwnedListsResponse
 *
 * @public
 */
export interface Get2UsersIdOwnedListsResponse {
  /** none */ data?: Array<List>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdPinnedListsResponse
 *
 * @public
 */
export interface Get2UsersIdPinnedListsResponse {
  /** none */ data?: Array<List>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdResponse
 *
 * @public
 */
export interface Get2UsersIdResponse {
  data?: User;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2UsersIdTimelinesReverseChronologicalResponse
 *
 * @public
 */
export interface Get2UsersIdTimelinesReverseChronologicalResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersIdTweetsResponse
 *
 * @public
 */
export interface Get2UsersIdTweetsResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersMeResponse
 *
 * @public
 */
export interface Get2UsersMeResponse {
  data?: User;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2UsersPersonalizedTrendsResponse
 *
 * @public
 */
export interface Get2UsersPersonalizedTrendsResponse {
  /** none */ data?: Array<PersonalizedTrend>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Get2UsersRepostsOfMeResponse
 *
 * @public
 */
export interface Get2UsersRepostsOfMeResponse {
  /** none */ data?: Array<Tweet>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2UsersResponse
 *
 * @public
 */
export interface Get2UsersResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for Get2UsersSearchResponse
 *
 * @public
 */
export interface Get2UsersSearchResponse {
  /** none */ data?: Array<User>;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
  /** none */ meta?: Record<string, any>;
} /**
Schema type for Get2WebhooksResponse
 *
 * @public
 */
export interface Get2WebhooksResponse {
  /** none */ data?: Array<WebhookConfig>;
  /** none */ errors?: Array<Problem>;
  /** none */ meta?: Record<string, any>;
}
/**
Schema type for HashtagEntity
 *
 * @public
 */
export type HashtagEntity = any; /**
Represent the portion of text recognized as a Hashtag, and its start and end position within the text.
 *
 * @public
 */
export interface HashtagFields {
  /** The text of the Hashtag. */ tag: string;
} /**
HTTP Status Code.
 *
 * @public
 */
export type HttpStatusCode = number;
/**
A problem that indicates this request is invalid.
 *
 * @public
 */
export type InvalidRequestProblem = any;
/**
The rule you have submitted is invalid.
 *
 * @public
 */
export type InvalidRuleProblem = any; /**
Compliance Job ID.
 *
 * @public
 */
export type JobId = string; /**
Schema type for KillAllConnectionsResponse
 *
 * @public
 */
export interface KillAllConnectionsResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for LikeComplianceSchema
 *
 * @public
 */
export interface LikeComplianceSchema {
  delete: UnlikeComplianceSchema;
} /**
The unique identifier of this Like.
 *
 * @public
 */
export type LikeId = string;
/**
Likes compliance stream events.
 *
 * @public
 */
export type LikesComplianceStreamResponse = any; /**
A Like event, with the tweet author user and the tweet being liked
 *
 * @public
 */
export interface LikeWithTweetAuthor {
  /** Creation time of the Tweet. */ createdAt?: string;
  id?: LikeId;
  likedTweetId?: TweetId;
  /** Timestamp in milliseconds of creation. */ timestampMs?: number;
  tweetAuthorId?: UserId;
} /**
A X List is a curated group of accounts.
 *
 * @public
 */
export interface List {
  /** none */ createdAt?: string;
  /** none */ description?: string;
  /** none */ followerCount?: number;
  id: ListId;
  /** none */ memberCount?: number;
  /** The name of this List. */ name: string;
  ownerId?: UserId;
  /** none */ private?: boolean;
} /**
Schema type for ListAddUserRequest
 *
 * @public
 */
export interface ListAddUserRequest {
  userId: UserId;
} /**
Schema type for ListCreateRequest
 *
 * @public
 */
export interface ListCreateRequest {
  /** none */ description?: string;
  /** none */ name: string;
  /** none */ private?: boolean;
} /**
Schema type for ListCreateResponse
 *
 * @public
 */
export interface ListCreateResponse {
  /** A X List is a curated group of accounts. */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for ListDeleteResponse
 *
 * @public
 */
export interface ListDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for ListFollowedRequest
 *
 * @public
 */
export interface ListFollowedRequest {
  listId: ListId;
} /**
Schema type for ListFollowedResponse
 *
 * @public
 */
export interface ListFollowedResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
The unique identifier of this List.
 *
 * @public
 */
export type ListId = string; /**
Schema type for ListMutateResponse
 *
 * @public
 */
export interface ListMutateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for ListPinnedRequest
 *
 * @public
 */
export interface ListPinnedRequest {
  listId: ListId;
} /**
Schema type for ListPinnedResponse
 *
 * @public
 */
export interface ListPinnedResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for ListUnpinResponse
 *
 * @public
 */
export interface ListUnpinResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for ListUpdateRequest
 *
 * @public
 */
export interface ListUpdateRequest {
  /** none */ description?: string;
  /** none */ name?: string;
  /** none */ private?: boolean;
} /**
Schema type for ListUpdateResponse
 *
 * @public
 */
export interface ListUpdateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for ManagementInfo
 *
 * @public
 */
export interface ManagementInfo {
  /** Indicates if the media is managed by Media Studio */ managed: boolean;
} /**
Schema type for Media
 *
 * @public
 */
export interface Media {
  height?: MediaHeight;
  mediaKey?: MediaKey;
  /** none */ type: string;
  width?: MediaWidth;
} /**
Schema type for MediaAnalytics
 *
 * @public
 */
export interface MediaAnalytics {
  /** none */ data?: Array<Record<string, any>>;
  /** none */ errors?: Array<Problem>;
} /**
A string enum value which identifies a media use-case. This identifier is used to enforce use-case specific constraints (e.g. file size, video duration) and enable advanced features.
 *
 * @public
 */
export type MediaCategory =
  | 'amplify_video'
  | 'tweet_gif'
  | 'tweet_image'
  | 'tweet_video'
  | 'dm_gif'
  | 'dm_image'
  | 'dm_video'
  | 'subtitles'; /**
A string enum value which identifies a media use-case. This identifier is used to enforce use-case specific constraints (e.g. file size) and enable advanced features.
 *
 * @public
 */
export type MediaCategoryOneShot =
  | 'tweet_image'
  | 'dm_image'
  | 'subtitles'; /**
The media category of uploaded media to which subtitles should be added/deleted
 *
 * @public
 */
export type MediaCategorySubtitles =
  | 'AmplifyVideo'
  | 'TweetVideo'; /**
The height of the media in pixels.
 *
 * @public
 */
export type MediaHeight = number; /**
The unique identifier of this Media.
 *
 * @public
 */
export type MediaId = string; /**
The Media Key identifier for this attachment.
 *
 * @public
 */
export type MediaKey = string; /**
Schema type for MediaMetrics
 *
 * @public
 */
export interface MediaMetrics {
  /** Tracks the number of clicks on a call-to-action URL */ ctaUrlClicks?: number;
  /** Tracks the number of clicks to watch a video or media content */ ctaWatchClicks?: number;
  /** Tracks the number of times a video or media is played from a user tap */ playFromTap?: number;
  /** Tracks the number of times a video reaches 25% of its duration */ playback25?: number;
  /** Tracks the number of times a video reaches 50% of its duration */ playback50?: number;
  /** Tracks the number of times a video reaches 75% of its duration */ playback75?: number;
  /** Tracks the number of times a video is played to completion */ playbackComplete?: number;
  /** Tracks the number of times a video playback is initiated */ playbackStart?: number;
  /** Tracks the number of times a video is viewed */ videoViews?: number;
  /** Tracks the total time spent watching a video, measured in milliseconds */ watchTimeMs?: number;
} /**
The file to upload.
 *
 * @public
 */
export type MediaPayloadBinary = string; /**
The file to upload.
 *
 * @public
 */
export type MediaPayloadByte = string;
/**
Schema type for MediaSegments
 *
 * @public
 */
export type MediaSegments = any; /**
Schema type for MediaTimestampedMetrics
 *
 * @public
 */
export interface MediaTimestampedMetrics {
  metrics?: MediaMetrics;
  /** ISO8601 Time */ timestamp?: string;
}
/**
Schema type for MediaUploadAppendRequest
 *
 * @public
 */
export type MediaUploadAppendRequest = any; /**
A response from getting a media upload request status.
 *
 * @public
 */
export interface MediaUploadAppendResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for MediaUploadConfigRequest
 *
 * @public
 */
export interface MediaUploadConfigRequest {
  /** none */ additionalOwners?: Array<UserId>;
  mediaCategory?: MediaCategory;
  /** The type of media. */ mediaType?:
    | 'video/mp4'
    | 'video/webm'
    | 'video/mp2t'
    | 'video/quicktime'
    | 'text/srt'
    | 'text/vtt'
    | 'image/jpeg'
    | 'image/gif'
    | 'image/bmp'
    | 'image/png'
    | 'image/webp'
    | 'image/pjpeg'
    | 'image/tiff'
    | 'model/gltf-binary'
    | 'model/vnd.usdz+zip';
  /** Whether this media is shared or not. */ shared?: boolean;
  /** The total size of the media upload in bytes. */ totalBytes?: number;
} /**
Schema type for MediaUploadRequestOneShot
 *
 * @public
 */
export interface MediaUploadRequestOneShot {
  /** none */ additionalOwners?: Array<UserId>;
  /** none */ media: any;
  mediaCategory: MediaCategoryOneShot;
  /** The type of image or subtitle. */ mediaType?:
    | 'text/srt'
    | 'text/vtt'
    | 'image/jpeg'
    | 'image/bmp'
    | 'image/png'
    | 'image/webp'
    | 'image/pjpeg'
    | 'image/tiff';
  /** Whether this media is shared or not. */ shared?: boolean;
} /**
A response from getting a media upload request status.
 *
 * @public
 */
export interface MediaUploadResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
The width of the media in pixels.
 *
 * @public
 */
export type MediaWidth = number;
/**
Schema type for MentionEntity
 *
 * @public
 */
export type MentionEntity = any; /**
Represent the portion of text recognized as a User mention, and its start and end position within the text.
 *
 * @public
 */
export interface MentionFields {
  id?: UserId;
  username: UserName;
} /**
Schema type for MetadataCreateRequest
 *
 * @public
 */
export interface MetadataCreateRequest {
  id: MediaId;
  /** none */ metadata?: Record<string, any>;
} /**
Schema type for MetadataCreateResponse
 *
 * @public
 */
export interface MetadataCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for Metrics
 *
 * @public
 */
export interface Metrics {
  /** Tracks number of App Install Attempts */ appInstallAttempts?: number;
  /** Tracks number of App opens */ appOpens?: number;
  /** Tracks number of Detail expands */ detailExpands?: number;
  /** Tracks number of Email Tweet actions */ emailTweet?: number;
  /** Tracks total Engagements */ engagements?: number;
  /** Tracks number of Follows */ follows?: number;
  /** Tracks number of Hashtag clicks */ hashtagClicks?: number;
  /** Tracks number of Impressions */ impressions?: number;
  /** Tracks number of Likes */ likes?: number;
  /** Tracks number of Link clicks */ linkClicks?: number;
  /** Tracks number of Media engagements */ mediaEngagements?: number;
  /** Tracks number of Media views */ mediaViews?: number;
  /** Tracks number of Permalink clicks */ permalinkClicks?: number;
  /** Tracks number of Profile visits */ profileVisits?: number;
  /** Tracks number of Quote Tweets */ quoteTweets?: number;
  /** Tracks number of Replies */ replies?: number;
  /** Tracks number of Retweets */ retweets?: number;
  /** Tracks number of URL clicks */ urlClicks?: number;
  /** Tracks number of User Profile clicks */ userProfileClicks?: number;
} /**
Community Note misleading tags type.
 *
 * @public
 */
export type MisleadingTags =
  | 'disputed_claim_as_fact'
  | 'factual_error'
  | 'manipulated_media'
  | 'misinterpreted_satire'
  | 'missing_important_context'
  | 'other'
  | 'outdated_information'; /**
Schema type for MuteUserMutationResponse
 *
 * @public
 */
export interface MuteUserMutationResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for MuteUserRequest
 *
 * @public
 */
export interface MuteUserRequest {
  targetUserId: UserId;
} /**
The newest id in this response.
 *
 * @public
 */
export type NewestId = string; /**
The next token.
 *
 * @public
 */
export type NextToken = string;
/**
A problem that indicates the user's rule set is not compliant.
 *
 * @public
 */
export type NonCompliantRulesProblem = any; /**
A X Community Note is a note on a Post.
 *
 * @public
 */
export interface Note {
  id: NoteId;
  info?: NoteInfo;
  postId: TweetId;
  status?: NoteRatingStatus;
  testResult?: NoteTestResult;
} /**
Community Note classification type.
 *
 * @public
 */
export type NoteClassification =
  | 'misinformed_or_potentially_misleading'
  | 'not_misleading'; /**
The unique identifier of this Community Note.
 *
 * @public
 */
export type NoteId = string; /**
A X Community Note is a note on a Post.
 *
 * @public
 */
export interface NoteInfo {
  classification: NoteClassification;
  /** none */ misleadingTags: Array<MisleadingTags>;
  /** The text summary in the Community Note. */ text: string;
  /** Whether the note provided trustworthy links. */ trustworthySources: boolean;
} /**
Community Note rating status
 *
 * @public
 */
export type NoteRatingStatus =
  | 'currently_rated_helpful'
  | 'currently_rated_not_helpful'
  | 'firm_reject'
  | 'insufficient_consensus'
  | 'minimum_ratings_not_met'
  | 'needs_more_ratings'
  | 'needs_your_help'; /**
The evaluation result of a community note.
 *
 * @public
 */
export interface NoteTestResult {
  /** Score bucket from the evaluator result. */ evaluatorScoreBucket?: string;
  /** The type of the evaluator. */ evaluatorType?: string;
} /**
The note content of the Tweet.
 *
 * @public
 */
export type NoteTweetText = string;
/**
A problem that indicates your client application does not have the required OAuth1 permissions for the requested endpoint.
 *
 * @public
 */
export type Oauth1PermissionsProblem = any; /**
The oldest id in this response.
 *
 * @public
 */
export type OldestId = string;
/**
You have been disconnected for operational reasons.
 *
 * @public
 */
export type OperationalDisconnectProblem = any; /**
A base32 pagination token.
 *
 * @public
 */
export type PaginationToken32 = string; /**
A base36 pagination token.
 *
 * @public
 */
export type PaginationToken36 = string; /**
A 'long' pagination token.
 *
 * @public
 */
export type PaginationTokenLong = string; /**
A trend.
 *
 * @public
 */
export interface PersonalizedTrend {
  /** Category of this trend. */ category?: string;
  /** Number of posts pertaining to this trend. */ postCount?: number;
  /** Name of the trend. */ trendName?: string;
  /** Time since this is trending. */ trendingSince?: string;
}
/**
Schema type for Photo
 *
 * @public
 */
export type Photo = any; /**
Schema type for Place
 *
 * @public
 */
export interface Place {
  /** none */ containedWithin?: Array<PlaceId>;
  /** The full name of the county in which this place exists. */ country?: string;
  countryCode?: CountryCode;
  /** The full name of this place. */ fullName: string;
  geo?: Geo;
  id: PlaceId;
  /** The human readable name of this place. */ name?: string;
  placeType?: PlaceType;
} /**
The identifier for this place.
 *
 * @public
 */
export type PlaceId = string; /**
Schema type for PlaceType
 *
 * @public
 */
export type PlaceType =
  | 'poi'
  | 'neighborhood'
  | 'city'
  | 'admin'
  | 'country'
  | 'unknown'; /**
Descriptor for a Plaid account.
 *
 * @public
 */
export interface PlaidAccount {
  /** The category of the account (e.g., personal, business). */ accountCategory: string;
  /** The Plaid account ID. */ accountId: string;
  /** The last 2-4 digits of the account number. */ accountNumberDisplay: string;
  /** The type of the account (e.g., checking, savings). */ accountType: string;
  /** The available balance of the account. */ availableBalance?: number;
  currency: PlaidCurrency;
  /** The current balance of the account. */ currentBalance?: number;
  /** The nickname of the account. */ nickname?: string;
  /** The name of the product associated with the account. */ productName: string;
  /** The status of the account. */ status: string;
} /**
Contact information associated with a Plaid account.
 *
 * @public
 */
export interface PlaidAccountContact {
  /** List of addresses associated with the account holder. */ addresses: Array<
    PlaidAddress
  >;
  /** List of email addresses associated with the account holder. */ emails: Array<
    string
  >;
  name: PlaidName;
  /** Relationship of the contact to the account. */ relationship?: string;
  /** List of telephone numbers associated with the account holder. */ telephones: Array<
    PlaidTelephone
  >;
} /**
Payment network details associated with the account.
 *
 * @public
 */
export interface PlaidAccountPaymentNetwork {
  /** The bank ID associated with the account. */ bankId: string;
  /** The payment network identifier. */ identifier: string;
  /** Indicates if transfers into the account are supported. */ transferIn: boolean;
  /** Indicates if transfers out of the account are supported. */ transferOut: boolean;
  /** The type of payment network (e.g., ACH, SEPA). */ type: string;
} /**
Descriptor for a Plaid account.
 *
 * @public
 */
export interface PlaidAccountTransaction {
  /** The category of the account (e.g., personal, business). */ accountCategory: string;
  /** The amount transacted. */ amount: number;
  /** Memo for transaction (e.g. CREDIT) */ debitCreditMemo: string;
  /** The transaction description */ description: string;
  /** The timestamp when the transaction was posted. */ postedTimestamp?: string;
  /** The status of the transaction. */ status: string;
  /** The identifier for the transaction. */ transactionId: string;
  /** The timestamp when the transaction occurred. */ transactionTimestamp: string;
} /**
Address information for the account holder.
 *
 * @public
 */
export interface PlaidAddress {
  /** The city of the address. */ city: string;
  /** The country of the address (ISO 3166-1 alpha-2 code). */ country: string;
  /** The first line of the address. */ line1: string;
  /** The second line of the address. */ line2?: string;
  /** The postal code of the address. */ postalCode?: string;
  /** The region or state of the address. */ region?: string;
} /**
Currency information.
 *
 * @public
 */
export interface PlaidCurrency {
  /** The ISO 4217 currency code. */ currencyCode: string;
} /**
A user id for the plaid customer
 *
 * @public
 */
export interface PlaidCustomer {
  customerId?: UserId;
} /**
Name information for the account holder.
 *
 * @public
 */
export interface PlaidName {
  /** The first name of the account holder. */ first: string;
  /** The last name of the account holder. */ last: string;
} /**
Telephone information for the account holder.
 *
 * @public
 */
export interface PlaidTelephone {
  /** The country code for the phone number (e.g., '+1'). */ country: string;
  /** The phone number. */ number: string;
  /** The type of phone number (e.g., 'mobile'). */ type: string;
} /**
A [GeoJson Point](https://tools.ietf.org/html/rfc7946#section-3.1.2) geometry object.
 *
 * @public
 */
export interface Point {
  coordinates: Position;
  /** none */ type: 'Point';
} /**
Represent a Poll attached to a Tweet.
 *
 * @public
 */
export interface Poll {
  /** none */ durationMinutes?: number;
  /** none */ endDatetime?: string;
  id: PollId;
  /** none */ options: Array<PollOption>;
  /** none */ votingStatus?: 'open' | 'closed';
} /**
Unique identifier of this poll.
 *
 * @public
 */
export type PollId = string; /**
Describes a choice in a Poll object.
 *
 * @public
 */
export interface PollOption {
  label: PollOptionLabel;
  /** Position of this choice in the poll. */ position: number;
  /** Number of users who voted for this choice. */ votes: number;
} /**
The text of a poll choice.
 *
 * @public
 */
export type PollOptionLabel = string; /**
A [GeoJson Position](https://tools.ietf.org/html/rfc7946#section-3.1.1) in the format `[longitude,latitude]`.
 *
 * @public
 */
export type Position = Array<
  number
>; /**
Schema type for PreviewImage
 *
 * @public
 */
export interface PreviewImage {
  /** none */ mediaKey: Record<string, any>;
} /**
The previous token.
 *
 * @public
 */
export type PreviousToken = string; /**
An HTTP Problem Details object, as defined in IETF RFC 7807 (https://tools.ietf.org/html/rfc7807).
 *
 * @public
 */
export interface Problem {
  /** none */ detail?: string;
  /** none */ status?: number;
  /** none */ title: string;
  /** none */ type: string;
} /**
Schema type for ProcessingInfo
 *
 * @public
 */
export interface ProcessingInfo {
  /** Number of seconds to check again for status */ checkAfterSecs?: number;
  /** Percent of upload progress */ progressPercent?: number;
  /** State of upload */ state?:
    | 'succeeded'
    | 'in_progress'
    | 'pending'
    | 'failed';
} /**
Confirmation that the replay job request was accepted.
 *
 * @public
 */
export interface ReplayJobCreateResponse {
  /** The UTC timestamp indicating when the replay job was created. */ createdAt: string;
  /** The unique identifier for the initiated replay job. */ jobId: string;
} /**
Shows who can reply a Tweet. Fields returned are everyone, mentioned_users, and following.
 *
 * @public
 */
export type ReplySettings =
  | 'everyone'
  | 'mentionedUsers'
  | 'following'
  | 'other'; /**
Shows who can reply a Tweet. Fields returned are everyone, mentioned_users, subscribers, verified and following.
 *
 * @public
 */
export type ReplySettingsWithVerifiedUsers =
  | 'everyone'
  | 'mentionedUsers'
  | 'following'
  | 'other'
  | 'subscribers'
  | 'verified';
/**
A problem that indicates that a given Tweet, User, etc. does not exist.
 *
 * @public
 */
export type ResourceNotFoundProblem = any;
/**
A problem that indicates you are not allowed to see a particular Tweet, User, etc.
 *
 * @public
 */
export type ResourceUnauthorizedProblem = any;
/**
A problem that indicates a particular Tweet, User, etc. is not available to you.
 *
 * @public
 */
export type ResourceUnavailableProblem = any; /**
The number of results returned in this response.
 *
 * @public
 */
export type ResultCount = number; /**
A user-provided stream filtering rule.
 *
 * @public
 */
export interface Rule {
  id?: RuleId;
  tag?: RuleTag;
  value: RuleValue;
} /**
Unique identifier of this rule.
 *
 * @public
 */
export type RuleId = string; /**
A user-provided stream filtering rule.
 *
 * @public
 */
export interface RuleNoId {
  tag?: RuleTag;
  value: RuleValue;
}
/**
You have exceeded the maximum number of rules.
 *
 * @public
 */
export type RulesCapProblem = any; /**
A count of user-provided stream filtering rules at the application and project levels.
 *
 * @public
 */
export interface RulesCount {
  allProjectClientApps?: AllProjectClientApps;
  /** Cap of number of rules allowed per client application */ capPerClientApp?: number;
  /** Cap of number of rules allowed per project */ capPerProject?: number;
  clientAppRulesCount?: AppRulesCount;
  /** Number of rules for project */ projectRulesCount?: number;
} /**
Schema type for RulesLookupResponse
 *
 * @public
 */
export interface RulesLookupResponse {
  /** none */ data?: Array<Rule>;
  meta: RulesResponseMetadata;
}
/**
Schema type for RulesRequestSummary
 *
 * @public
 */
export type RulesRequestSummary = any; /**
Schema type for RulesResponseMetadata
 *
 * @public
 */
export interface RulesResponseMetadata {
  nextToken?: NextToken;
  /** Number of Rules in result set. */ resultCount?: number;
  /** none */ sent: string;
  summary?: RulesRequestSummary;
} /**
A tag meant for the labeling of user provided rules.
 *
 * @public
 */
export type RuleTag = string; /**
The filterlang value of the rule.
 *
 * @public
 */
export type RuleValue = string; /**
Represent a Search Count Result.
 *
 * @public
 */
export interface SearchCount {
  end: End;
  start: Start;
  tweetCount: TweetCount;
} /**
Schema type for SensitiveMediaWarning
 *
 * @public
 */
export interface SensitiveMediaWarning {
  /** Indicates if the content contains adult material */ adultContent?: boolean;
  /** Indicates if the content depicts graphic violence */ graphicViolence?: boolean;
  /** Indicates if the content has other sensitive characteristics */ other?: boolean;
} /**
Schema type for SharedInfo
 *
 * @public
 */
export interface SharedInfo {
  /** Indicates if the media is shared in direct messages */ shared: boolean;
} /**
Schema type for Space
 *
 * @public
 */
export interface Space {
  /** Creation time of the Space. */ createdAt?: string;
  creatorId?: UserId;
  /** End time of the Space. */ endedAt?: string;
  /** The user ids for the hosts of the Space. */ hostIds?: Array<UserId>;
  id: SpaceId;
  /** An array of user ids for people who were invited to a Space. */ invitedUserIds?: Array<
    UserId
  >;
  /** Denotes if the Space is a ticketed Space. */ isTicketed?: boolean;
  /** The language of the Space. */ lang?: string;
  /** The number of participants in a Space. */ participantCount?: number;
  /** A date time stamp for when a Space is scheduled to begin. */ scheduledStart?: string;
  /** An array of user ids for people who were speakers in a Space. */ speakerIds?: Array<
    UserId
  >;
  /** When the Space was started as a date string. */ startedAt?: string;
  /** The current state of the Space. */ state: 'live' | 'scheduled' | 'ended';
  /** The number of people who have either purchased a ticket or set a reminder for this Space. */ subscriberCount?: number;
  /** The title of the Space. */ title?: string;
  /** The topics of a Space, as selected by its creator. */ topics?: Array<
    Record<string, any>
  >;
  /** When the Space was last updated. */ updatedAt?: string;
} /**
The unique identifier of this Space.
 *
 * @public
 */
export type SpaceId = string; /**
The start time of the bucket.
 *
 * @public
 */
export type Start = string; /**
Schema type for Sticker
 *
 * @public
 */
export interface Sticker {
  /** width-to-height ratio of the media */ aspectRatio?: number;
  /** A unique identifier for the group of annotations associated with the media */ groupAnnotationId?: number;
  /** Unique identifier for sticker */ id?: string;
  /** A unique identifier for the sticker set associated with the media */ stickerSetAnnotationId?: number;
  /** Scale or rotate the media on the x-axis */ transformA?: number;
  /** Skew the media on the x-axis */ transformB?: number;
  /** Skew the media on the y-axis */ transformC?: number;
  /** Scale or rotate the media on the y-axis */ transformD?: number;
  /** Scale or rotate the media on the x-axis */ transformTx?: number;
  /** The vertical translation (shift) value for the media */ transformTy?: number;
} /**
Schema type for StickerInfo
 *
 * @public
 */
export interface StickerInfo {
  /** Stickers list must not be empty and should not exceed 25 */ stickers: Array<
    Sticker
  >;
} /**
Schema type for StreamingLikeResponseV2
 *
 * @public
 */
export interface StreamingLikeResponseV2 {
  data?: LikeWithTweetAuthor;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for StreamingTweetResponse
 *
 * @public
 */
export interface StreamingTweetResponse {
  data?: Tweet;
  /** none */ errors?: Array<Problem>;
  includes?: Expansions;
} /**
Schema type for SubscriptionsCountGetResponse
 *
 * @public
 */
export interface SubscriptionsCountGetResponse {
  /** The count of active subscriptions across all webhooks */ data?: Record<
    string,
    any
  >;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for SubscriptionsCreateRequest
 *
 * @public
 */
export type SubscriptionsCreateRequest = Record<
  string,
  any
>; /**
Schema type for SubscriptionsCreateResponse
 *
 * @public
 */
export interface SubscriptionsCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for SubscriptionsDeleteResponse
 *
 * @public
 */
export interface SubscriptionsDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for SubscriptionsGetResponse
 *
 * @public
 */
export interface SubscriptionsGetResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for SubscriptionsListGetResponse
 *
 * @public
 */
export interface SubscriptionsListGetResponse {
  /** The list of active subscriptions for a specified webhook */ data?: Record<
    string,
    any
  >;
  /** none */ errors?: Array<Problem>;
} /**
The language code should be a BCP47 code (e.g. 'EN", "SP")
 *
 * @public
 */
export type SubtitleLanguageCode = string; /**
Schema type for Subtitles
 *
 * @public
 */
export interface Subtitles {
  /** Language name in a human readable form */ displayName?: string;
  id?: MediaId;
  languageCode?: SubtitleLanguageCode;
} /**
Schema type for SubtitlesCreateRequest
 *
 * @public
 */
export interface SubtitlesCreateRequest {
  id?: MediaId;
  mediaCategory?: MediaCategorySubtitles;
  subtitles?: Subtitles;
} /**
Schema type for SubtitlesCreateResponse
 *
 * @public
 */
export interface SubtitlesCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for SubtitlesDeleteRequest
 *
 * @public
 */
export interface SubtitlesDeleteRequest {
  id?: MediaId;
  languageCode?: SubtitleLanguageCode;
  mediaCategory?: MediaCategorySubtitles;
} /**
Schema type for SubtitlesDeleteResponse
 *
 * @public
 */
export interface SubtitlesDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for TimestampedMetrics
 *
 * @public
 */
export interface TimestampedMetrics {
  metrics?: Metrics;
  /** ISO8601 Time */ timestamp?: string;
} /**
The topic of a Space, as selected by its creator.
 *
 * @public
 */
export interface Topic {
  /** The description of the given topic. */ description?: string;
  id: TopicId;
  /** The name of the given topic. */ name: string;
} /**
Unique identifier of this Topic.
 *
 * @public
 */
export type TopicId = string; /**
A trend.
 *
 * @public
 */
export interface Trend {
  /** Name of the trend. */ trendName?: string;
  /** Number of Posts in this trend. */ tweetCount?: number;
} /**
Schema type for Tweet
 *
 * @public
 */
export interface Tweet {
  /** Specifies the type of attachments (if any) present in this Tweet. */ attachments?: Record<
    string,
    any
  >;
  authorId?: UserId;
  communityId?: CommunityId;
  /** none */ contextAnnotations?: Array<ContextAnnotation>;
  conversationId?: TweetId;
  /** Creation time of the Tweet. */ createdAt?: string;
  displayTextRange?: DisplayTextRange;
  /** none */ editControls?: Record<string, any>;
  /** A list of Tweet Ids in this Tweet chain. */ editHistoryTweetIds?: Array<
    TweetId
  >;
  entities?: FullTextEntities;
  /** The location tagged on the Tweet, if the user provided one. */ geo?: Record<
    string,
    any
  >;
  id?: TweetId;
  inReplyToUserId?: UserId;
  /** Language of the Tweet, if detected by X. Returned as a BCP47 language tag. */ lang?: string;
  /** Nonpublic engagement metrics for the Tweet at the time of the request. */ nonPublicMetrics?: Record<
    string,
    any
  >;
  /** The full-content of the Tweet, including text beyond 280 characters. */ noteTweet?: Record<
    string,
    any
  >;
  /** Organic nonpublic engagement metrics for the Tweet at the time of the request. */ organicMetrics?: Record<
    string,
    any
  >;
  /** Indicates if this Tweet contains URLs marked as sensitive, for example content suitable for mature audiences. */ possiblySensitive?: boolean;
  /** Promoted nonpublic engagement metrics for the Tweet at the time of the request. */ promotedMetrics?: Record<
    string,
    any
  >;
  /** Engagement metrics for the Tweet at the time of the request. */ publicMetrics?: Record<
    string,
    any
  >;
  /** A list of Posts this Tweet refers to. For example, if the parent Tweet is a Retweet, a Quoted Tweet or a Reply, it will include the related Tweet referenced to by its parent. */ referencedTweets?: Array<
    Record<string, any>
  >;
  replySettings?: ReplySettingsWithVerifiedUsers;
  /** The scopes for this tweet */ scopes?: Record<string, any>;
  /** This is deprecated. */ source?: string;
  /** none */ suggestedSourceLinks?: Array<UrlEntity>;
  text?: TweetText;
  username?: UserName;
  withheld?: TweetWithheld;
}
/**
Tweet compliance data.
 *
 * @public
 */
export type TweetComplianceData = any; /**
Schema type for TweetComplianceSchema
 *
 * @public
 */
export interface TweetComplianceSchema {
  /** Event time. */ eventAt: string;
  quoteTweetId?: TweetId;
  /** none */ tweet: Record<string, any>;
}
/**
Tweet compliance stream events.
 *
 * @public
 */
export type TweetComplianceStreamResponse = any; /**
The count for the bucket.
 *
 * @public
 */
export type TweetCount = number; /**
Schema type for TweetCreateRequest
 *
 * @public
 */
export interface TweetCreateRequest {
  /** Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link. */ cardUri?: string;
  communityId?: CommunityId;
  /** Link to take the conversation from the public timeline to a private Direct Message. */ directMessageDeepLink?: string;
  /** Options for editing an existing Post. When provided, this request will edit the specified Post instead of creating a new one. */ editOptions?: Record<
    string,
    any
  >;
  /** Exclusive Tweet for super followers. */ forSuperFollowersOnly?: boolean;
  /** Place ID being attached to the Tweet for geo location. */ geo?: Record<
    string,
    any
  >;
  /** Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI. */ media?: Record<
    string,
    any
  >;
  /** Nullcasted (promoted-only) Posts do not appear in the public timeline and are not served to followers. */ nullcast?: boolean;
  /** Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI. */ poll?: Record<
    string,
    any
  >;
  quoteTweetId?: TweetId;
  /** Tweet information of the Tweet being replied to. */ reply?: Record<
    string,
    any
  >;
  /** Settings to indicate who can reply to the Tweet. */ replySettings?:
    | 'following'
    | 'mentionedUsers'
    | 'subscribers'
    | 'verified';
  /** Share community post with followers too. */ shareWithFollowers?: boolean;
  text?: TweetText;
} /**
Schema type for TweetCreateResponse
 *
 * @public
 */
export interface TweetCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for TweetDeleteComplianceSchema
 *
 * @public
 */
export interface TweetDeleteComplianceSchema {
  delete: TweetComplianceSchema;
} /**
Schema type for TweetDeleteResponse
 *
 * @public
 */
export interface TweetDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for TweetDropComplianceSchema
 *
 * @public
 */
export interface TweetDropComplianceSchema {
  drop: TweetComplianceSchema;
} /**
Schema type for TweetEditComplianceObjectSchema
 *
 * @public
 */
export interface TweetEditComplianceObjectSchema {
  /** none */ editTweetIds: Array<TweetId>;
  /** Event time. */ eventAt: string;
  initialTweetId: TweetId;
  /** none */ tweet: Record<string, any>;
} /**
Schema type for TweetEditComplianceSchema
 *
 * @public
 */
export interface TweetEditComplianceSchema {
  tweetEdit: TweetEditComplianceObjectSchema;
} /**
Schema type for TweetHideRequest
 *
 * @public
 */
export interface TweetHideRequest {
  /** none */ hidden: boolean;
} /**
Schema type for TweetHideResponse
 *
 * @public
 */
export interface TweetHideResponse {
  /** none */ data?: Record<string, any>;
} /**
Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
 *
 * @public
 */
export type TweetId = string;
/**
Tweet label data.
 *
 * @public
 */
export type TweetLabelData = any;
/**
Tweet label stream events.
 *
 * @public
 */
export type TweetLabelStreamResponse = any; /**
Schema type for TweetNotice
 *
 * @public
 */
export interface TweetNotice {
  /** If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’. */ application: string;
  /** Information shown on the Tweet label */ details?: string;
  /** Event time. */ eventAt: string;
  /** The type of label on the Tweet */ eventType: string;
  /** Link to more information about this kind of label */ extendedDetailsUrl?: string;
  /** Title/header of the Tweet label */ labelTitle?: string;
  /** none */ tweet: Record<string, any>;
} /**
Schema type for TweetNoticeSchema
 *
 * @public
 */
export interface TweetNoticeSchema {
  publicTweetNotice: TweetNotice;
} /**
Schema type for TweetTakedownComplianceSchema
 *
 * @public
 */
export interface TweetTakedownComplianceSchema {
  /** Event time. */ eventAt: string;
  quoteTweetId?: TweetId;
  /** none */ tweet: Record<string, any>;
  /** none */ withheldInCountries: Array<CountryCode>;
} /**
The content of the Tweet.
 *
 * @public
 */
export type TweetText = string; /**
Schema type for TweetUndropComplianceSchema
 *
 * @public
 */
export interface TweetUndropComplianceSchema {
  undrop: TweetComplianceSchema;
} /**
Schema type for TweetUnviewable
 *
 * @public
 */
export interface TweetUnviewable {
  /** If the label is being applied or removed. Possible values are ‘apply’ or ‘remove’. */ application: string;
  /** Event time. */ eventAt: string;
  /** none */ tweet: Record<string, any>;
} /**
Schema type for TweetUnviewableSchema
 *
 * @public
 */
export interface TweetUnviewableSchema {
  publicTweetUnviewable: TweetUnviewable;
} /**
Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).
 *
 * @public
 */
export interface TweetWithheld {
  /** Indicates if the content is being withheld for on the basis of copyright infringement. */ copyright: boolean;
  /** Provides a list of countries where this content is not available. */ countryCodes: Array<
    CountryCode
  >;
  /** Indicates whether the content being withheld is the `tweet` or a `user`. */ scope?:
    | 'tweet'
    | 'user';
} /**
Schema type for TweetWithheldComplianceSchema
 *
 * @public
 */
export interface TweetWithheldComplianceSchema {
  withheld: TweetTakedownComplianceSchema;
} /**
Schema type for UnlikeComplianceSchema
 *
 * @public
 */
export interface UnlikeComplianceSchema {
  /** Event time. */ eventAt: string;
  /** none */ favorite: Record<string, any>;
}
/**
A problem that indicates that the authentication used is not supported.
 *
 * @public
 */
export type UnsupportedAuthenticationProblem = any; /**
Expiration time of the upload URL.
 *
 * @public
 */
export type UploadExpiration = string; /**
Schema type for UploadSource
 *
 * @public
 */
export interface UploadSource {
  /** Records the source (e.g., app, device) from which the media was uploaded */ uploadSource: string;
} /**
URL to which the user will upload their Tweet or user IDs.
 *
 * @public
 */
export type UploadUrl = string; /**
A validly formatted URL.
 *
 * @public
 */
export type Url = string;
/**
Represent the portion of text recognized as a URL, and its start and end position within the text.
 *
 * @public
 */
export type UrlEntity = any;
/**
Represent the portion of text recognized as a URL, and its start and end position within the text.
 *
 * @public
 */
export type UrlEntityDm = any; /**
Represent the portion of text recognized as a URL.
 *
 * @public
 */
export interface UrlFields {
  /** Description of the URL landing page. */ description?: string;
  /** The URL as displayed in the X client. */ displayUrl?: string;
  expandedUrl?: Url;
  /** none */ images?: Array<UrlImage>;
  mediaKey?: MediaKey;
  status?: HttpStatusCode;
  /** Title of the page the URL points to. */ title?: string;
  /** Fully resolved url. */ unwoundUrl?: string;
  url: Url;
} /**
Represent the information for the URL image.
 *
 * @public
 */
export interface UrlImage {
  height?: MediaHeight;
  url?: Url;
  width?: MediaWidth;
} /**
Usage per client app
 *
 * @public
 */
export interface Usage {
  /** Number of days left for the Tweet cap to reset */ capResetDay?: number;
  /** The daily usage breakdown for each Client Application a project */ dailyClientAppUsage?: Array<
    ClientAppUsage
  >;
  /** The daily usage breakdown for a project */ dailyProjectUsage?: Record<
    string,
    any
  >;
  /** Total number of Posts that can be read in this project per month */ projectCap?: number;
  /** The unique identifier for this project */ projectId?: string;
  /** The number of Posts read in this project */ projectUsage?: number;
}
/**
A problem that indicates that a usage cap has been exceeded.
 *
 * @public
 */
export type UsageCapExceededProblem = any; /**
Represents the data for Usage
 *
 * @public
 */
export interface UsageFields {
  /** The time period for the usage */ date?: string;
  /** The usage value */ usage?: number;
} /**
The X User object.
 *
 * @public
 */
export interface User {
  /** Metadata about a user's affiliation. */ affiliation?: Record<string, any>;
  /** Returns detailed information about the relationship between two users. */ connectionStatus?: Array<
    | 'follow_request_received'
    | 'follow_request_sent'
    | 'blocking'
    | 'followed_by'
    | 'following'
    | 'muting'
  >;
  /** Creation time of this User. */ createdAt?: string;
  /** The text of this User's profile description (also known as bio), if the User provided one. */ description?: string;
  /** A list of metadata found in the User's profile description. */ entities?: Record<
    string,
    any
  >;
  id: UserId;
  /** The location specified in the User's profile, if the User provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries. */ location?: string;
  mostRecentTweetId?: TweetId;
  /** The friendly name of this User, as shown on their profile. */ name: string;
  pinnedTweetId?: TweetId;
  /** The URL to the profile banner for this User. */ profileBannerUrl?: string;
  /** The URL to the profile image for this User. */ profileImageUrl?: string;
  /** Indicates if this User has chosen to protect their Posts (in other words, if this User's Posts are private). */ protected?: boolean;
  /** A list of metrics for this User. */ publicMetrics?: Record<string, any>;
  /** Indicates if you can send a DM to this User */ receivesYourDm?: boolean;
  /** The X Blue subscription type of the user, eg: Basic, Premium, PremiumPlus or None. */ subscriptionType?:
    | 'Basic'
    | 'Premium'
    | 'PremiumPlus'
    | 'None';
  /** The URL specified in the User's profile. */ url?: string;
  username: UserName;
  /** Indicate if this User is a verified X User. */ verified?: boolean;
  /** The X Blue verified type of the user, eg: blue, government, business or none. */ verifiedType?:
    | 'blue'
    | 'government'
    | 'business'
    | 'none';
  withheld?: UserWithheld;
}
/**
User compliance data.
 *
 * @public
 */
export type UserComplianceData = any; /**
Schema type for UserComplianceSchema
 *
 * @public
 */
export interface UserComplianceSchema {
  /** Event time. */ eventAt: string;
  /** none */ user: Record<string, any>;
}
/**
User compliance stream events.
 *
 * @public
 */
export type UserComplianceStreamResponse = any; /**
Schema type for UserDeleteComplianceSchema
 *
 * @public
 */
export interface UserDeleteComplianceSchema {
  userDelete: UserComplianceSchema;
} /**
Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
 *
 * @public
 */
export type UserId = string; /**
Unique identifier of this User. The value must be the same as the authenticated user.
 *
 * @public
 */
export type UserIdMatchesAuthenticatedUser = string; /**
The X handle (screen name) of this user.
 *
 * @public
 */
export type UserName = string; /**
Schema type for UserProfileModificationComplianceSchema
 *
 * @public
 */
export interface UserProfileModificationComplianceSchema {
  userProfileModification: UserProfileModificationObjectSchema;
} /**
Schema type for UserProfileModificationObjectSchema
 *
 * @public
 */
export interface UserProfileModificationObjectSchema {
  /** Event time. */ eventAt: string;
  /** none */ newValue: string;
  /** none */ profileField: string;
  /** none */ user: Record<string, any>;
} /**
Schema type for UserProtectComplianceSchema
 *
 * @public
 */
export interface UserProtectComplianceSchema {
  userProtect: UserComplianceSchema;
} /**
Schema type for UserScrubGeoObjectSchema
 *
 * @public
 */
export interface UserScrubGeoObjectSchema {
  /** Event time. */ eventAt: string;
  upToTweetId: TweetId;
  /** none */ user: Record<string, any>;
} /**
Schema type for UserScrubGeoSchema
 *
 * @public
 */
export interface UserScrubGeoSchema {
  scrubGeo: UserScrubGeoObjectSchema;
} /**
Schema type for UsersDMBlockCreateResponse
 *
 * @public
 */
export interface UsersDMBlockCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UsersDMUnBlockCreateResponse
 *
 * @public
 */
export interface UsersDMUnBlockCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
The the search string by which to query for users.
 *
 * @public
 */
export type UserSearchQueryVnext = string; /**
Schema type for UsersFollowingCreateRequest
 *
 * @public
 */
export interface UsersFollowingCreateRequest {
  targetUserId: UserId;
} /**
Schema type for UsersFollowingCreateResponse
 *
 * @public
 */
export interface UsersFollowingCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UsersFollowingDeleteResponse
 *
 * @public
 */
export interface UsersFollowingDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UsersLikesCreateRequest
 *
 * @public
 */
export interface UsersLikesCreateRequest {
  tweetId: TweetId;
} /**
Schema type for UsersLikesCreateResponse
 *
 * @public
 */
export interface UsersLikesCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UsersLikesDeleteResponse
 *
 * @public
 */
export interface UsersLikesDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UsersRetweetsCreateRequest
 *
 * @public
 */
export interface UsersRetweetsCreateRequest {
  tweetId: TweetId;
} /**
Schema type for UsersRetweetsCreateResponse
 *
 * @public
 */
export interface UsersRetweetsCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UsersRetweetsDeleteResponse
 *
 * @public
 */
export interface UsersRetweetsDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for UserSuspendComplianceSchema
 *
 * @public
 */
export interface UserSuspendComplianceSchema {
  userSuspend: UserComplianceSchema;
} /**
Schema type for UserTakedownComplianceSchema
 *
 * @public
 */
export interface UserTakedownComplianceSchema {
  /** Event time. */ eventAt: string;
  /** none */ user: Record<string, any>;
  /** none */ withheldInCountries: Array<CountryCode>;
} /**
Schema type for UserUndeleteComplianceSchema
 *
 * @public
 */
export interface UserUndeleteComplianceSchema {
  userUndelete: UserComplianceSchema;
} /**
Schema type for UserUnprotectComplianceSchema
 *
 * @public
 */
export interface UserUnprotectComplianceSchema {
  userUnprotect: UserComplianceSchema;
} /**
Schema type for UserUnsuspendComplianceSchema
 *
 * @public
 */
export interface UserUnsuspendComplianceSchema {
  userUnsuspend: UserComplianceSchema;
} /**
Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).
 *
 * @public
 */
export interface UserWithheld {
  /** Provides a list of countries where this content is not available. */ countryCodes: Array<
    CountryCode
  >;
  /** Indicates that the content being withheld is a `user`. */ scope?: 'user';
} /**
Schema type for UserWithheldComplianceSchema
 *
 * @public
 */
export interface UserWithheldComplianceSchema {
  userWithheld: UserTakedownComplianceSchema;
} /**
Schema type for Variant
 *
 * @public
 */
export interface Variant {
  /** The bit rate of the media. */ bitRate?: number;
  /** The content type of the media. */ contentType?: string;
  /** The url to the media. */ url?: string;
} /**
An array of all available variants of the media.
 *
 * @public
 */
export type Variants = Array<Variant>;
/**
Schema type for Video
 *
 * @public
 */
export type Video = any; /**
A Webhook Configuration
 *
 * @public
 */
export interface WebhookConfig {
  /** none */ createdAt: string;
  id: WebhookConfigId;
  /** The callback URL of the webhook. */ url: string;
  /** none */ valid: boolean;
} /**
Schema type for WebhookConfigCreateRequest
 *
 * @public
 */
export interface WebhookConfigCreateRequest {
  /** none */ url: string;
} /**
A Webhook Configuration
 *
 * @public
 */
export interface WebhookConfigCreateResponse {
  /** none */ createdAt: string;
  id: WebhookConfigId;
  /** The callback URL of the webhook. */ url: string;
  /** none */ valid: boolean;
} /**
Schema type for WebhookConfigDeleteResponse
 *
 * @public
 */
export interface WebhookConfigDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
The unique identifier of this webhook config.
 *
 * @public
 */
export type WebhookConfigId = string; /**
Schema type for WebhookConfigPutResponse
 *
 * @public
 */
export interface WebhookConfigPutResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for WebhookLinksCreateResponse
 *
 * @public
 */
export interface WebhookLinksCreateResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for WebhookLinksDeleteResponse
 *
 * @public
 */
export interface WebhookLinksDeleteResponse {
  /** none */ data?: Record<string, any>;
  /** none */ errors?: Array<Problem>;
} /**
Schema type for WebhookLinksGetResponse
 *
 * @public
 */
export interface WebhookLinksGetResponse {
  /** The list of active webhook links for a given stream */ data?: Record<
    string,
    any
  >;
  /** none */ errors?: Array<Problem>;
}
