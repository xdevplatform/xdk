/**
 * Main client for the X API.
 *
 * This module provides the main client class for interacting with the X API.
 */


import { BookmarksClient } from './bookmarks/index.js';

import { ComplianceClient } from './compliance/index.js';

import { WebhooksClient } from './webhooks/index.js';

import { CommunityNotesClient } from './community_notes/index.js';

import { ListsClient } from './lists/index.js';

import { UsersClient } from './users/index.js';

import { AaasubscriptionsClient } from './aaasubscriptions/index.js';

import { GeneralClient } from './general/index.js';

import { UsageClient } from './usage/index.js';

import { SpacesClient } from './spaces/index.js';

import { StreamClient } from './stream/index.js';

import { AccountActivityClient } from './account_activity/index.js';

import { DirectMessagesClient } from './direct_messages/index.js';

import { ConnectionClient } from './connection/index.js';

import { CommunitiesClient } from './communities/index.js';

import { TrendsClient } from './trends/index.js';

import { PostsClient } from './posts/index.js';

import { MediaClient } from './media/index.js';


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

    
    /** bookmarks operations */
    readonly bookmarks: BookmarksClient;
    
    /** compliance operations */
    readonly compliance: ComplianceClient;
    
    /** webhooks operations */
    readonly webhooks: WebhooksClient;
    
    /** community notes operations */
    readonly communityNotes: CommunityNotesClient;
    
    /** lists operations */
    readonly lists: ListsClient;
    
    /** users operations */
    readonly users: UsersClient;
    
    /** aaasubscriptions operations */
    readonly aaasubscriptions: AaasubscriptionsClient;
    
    /** general operations */
    readonly general: GeneralClient;
    
    /** usage operations */
    readonly usage: UsageClient;
    
    /** spaces operations */
    readonly spaces: SpacesClient;
    
    /** stream operations */
    readonly stream: StreamClient;
    
    /** account activity operations */
    readonly accountActivity: AccountActivityClient;
    
    /** direct messages operations */
    readonly directMessages: DirectMessagesClient;
    
    /** connection operations */
    readonly connection: ConnectionClient;
    
    /** communities operations */
    readonly communities: CommunitiesClient;
    
    /** trends operations */
    readonly trends: TrendsClient;
    
    /** posts operations */
    readonly posts: PostsClient;
    
    /** media operations */
    readonly media: MediaClient;
    

    constructor(config: ClientConfig = {}) {
        this.baseUrl = config.baseUrl || 'https://api.twitter.com/2';
        this.bearerToken = config.bearerToken;
        this.accessToken = config.accessToken;
        this.headers = new Headers(config.headers);

        
        this.bookmarks = new BookmarksClient(this);
        
        this.compliance = new ComplianceClient(this);
        
        this.webhooks = new WebhooksClient(this);
        
        this.communityNotes = new CommunityNotesClient(this);
        
        this.lists = new ListsClient(this);
        
        this.users = new UsersClient(this);
        
        this.aaasubscriptions = new AaasubscriptionsClient(this);
        
        this.general = new GeneralClient(this);
        
        this.usage = new UsageClient(this);
        
        this.spaces = new SpacesClient(this);
        
        this.stream = new StreamClient(this);
        
        this.accountActivity = new AccountActivityClient(this);
        
        this.directMessages = new DirectMessagesClient(this);
        
        this.connection = new ConnectionClient(this);
        
        this.communities = new CommunitiesClient(this);
        
        this.trends = new TrendsClient(this);
        
        this.posts = new PostsClient(this);
        
        this.media = new MediaClient(this);
        
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