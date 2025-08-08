/**
 * Main client for the X API.
 *
 * This module provides the main client class for interacting with the X API.
 */

import { AaasubscriptionsClient } from './aaasubscriptions/index.js';

import { ComplianceClient } from './compliance/index.js';

import { GeneralClient } from './general/index.js';

import { MediaClient } from './media/index.js';

import { CommunityNotesClient } from './community_notes/index.js';

import { BookmarksClient } from './bookmarks/index.js';

import { UsageClient } from './usage/index.js';

import { WebhooksClient } from './webhooks/index.js';

import { PostsClient } from './posts/index.js';

import { ListsClient } from './lists/index.js';

import { SpacesClient } from './spaces/index.js';

import { ConnectionClient } from './connection/index.js';

import { CommunitiesClient } from './communities/index.js';

import { AccountActivityClient } from './account_activity/index.js';

import { TrendsClient } from './trends/index.js';

import { StreamClient } from './stream/index.js';

import { UsersClient } from './users/index.js';

import { DirectMessagesClient } from './direct_messages/index.js';
/**
 * Configuration options for the X API client
 */

export interface ClientConfig {
    /** Base URL for API requests */
    baseUrl?: string;
    /** Bearer token for authentication */
    bearerToken?: string;
    /** OAuth2 access token */
    accessToken?: string;
    /** Custom headers to include in requests */
    headers?: Record<string, string>;
}

/**
 * Main client class for the X API
 */

export class Client {
    /** Base URL for API requests */
    readonly baseUrl: string;
    /** Bearer token for authentication */
    readonly bearerToken?: string;
    /** OAuth2 access token */
    readonly accessToken?: string;
    /** Headers for requests */
    readonly headers: Headers;
    /** OAuth2 session for requests */
    readonly oauth2Session?: typeof fetch;
    /** OAuth2 authentication instance */
    readonly oauth2Auth?: any;
    /** OAuth2 token */
    readonly token?: any;


    /** aaasubscriptions operations */
    readonly aaasubscriptions: AaasubscriptionsClient;

    /** compliance operations */
    readonly compliance: ComplianceClient;

    /** general operations */
    readonly general: GeneralClient;

    /** media operations */
    readonly media: MediaClient;

    /** community notes operations */
    readonly communityNotes: CommunityNotesClient;

    /** bookmarks operations */
    readonly bookmarks: BookmarksClient;

    /** usage operations */
    readonly usage: UsageClient;

    /** webhooks operations */
    readonly webhooks: WebhooksClient;

    /** posts operations */
    readonly posts: PostsClient;

    /** lists operations */
    readonly lists: ListsClient;

    /** spaces operations */
    readonly spaces: SpacesClient;

    /** connection operations */
    readonly connection: ConnectionClient;

    /** communities operations */
    readonly communities: CommunitiesClient;

    /** account activity operations */
    readonly accountActivity: AccountActivityClient;

    /** trends operations */
    readonly trends: TrendsClient;

    /** stream operations */
    readonly stream: StreamClient;

    /** users operations */
    readonly users: UsersClient;

    /** direct messages operations */
    readonly directMessages: DirectMessagesClient;


    constructor(config: ClientConfig = {}) {
        this.baseUrl = config.baseUrl || 'https://api.twitter.com/2';
        this.bearerToken = config.bearerToken;
        this.accessToken = config.accessToken;
        this.headers = new Headers(config.headers);


        this.aaasubscriptions = new AaasubscriptionsClient(this);

        this.compliance = new ComplianceClient(this);

        this.general = new GeneralClient(this);

        this.media = new MediaClient(this);

        this.communityNotes = new CommunityNotesClient(this);

        this.bookmarks = new BookmarksClient(this);

        this.usage = new UsageClient(this);

        this.webhooks = new WebhooksClient(this);

        this.posts = new PostsClient(this);

        this.lists = new ListsClient(this);

        this.spaces = new SpacesClient(this);

        this.connection = new ConnectionClient(this);

        this.communities = new CommunitiesClient(this);

        this.accountActivity = new AccountActivityClient(this);

        this.trends = new TrendsClient(this);

        this.stream = new StreamClient(this);

        this.users = new UsersClient(this);

        this.directMessages = new DirectMessagesClient(this);

    }

    /**
     * Check if the OAuth2 token is expired
     */
    isTokenExpired(): boolean {
        // TODO: Implement token expiration check
        return false;
    }
    /**
     * Refresh the OAuth2 token
     */

    async refreshToken(): Promise<void> {
        // TODO: Implement token refresh
    }
} 