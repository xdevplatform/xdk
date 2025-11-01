/**
 * Main client for the X API.
 *
 * This module provides the main client class for interacting with the X API.
 */

import { httpClient } from "./http-client.js";
import { 
  Paginator, 
  PostPaginator, 
  UserPaginator, 
  EventPaginator
} from "./paginator.js";



import { ListsClient } from "./lists/index.js";



import { DirectMessagesClient } from "./direct_messages/index.js";



import { UsageClient } from "./usage/index.js";



import { WebhooksClient } from "./webhooks/index.js";



import { TrendsClient } from "./trends/index.js";



import { CommunityNotesClient } from "./community_notes/index.js";



import { StreamClient } from "./stream/client.js";



import { CommunitiesClient } from "./communities/index.js";



import { MediaClient } from "./media/index.js";



import { ConnectionsClient } from "./connections/index.js";



import { ComplianceClient } from "./compliance/index.js";



import { GeneralClient } from "./general/index.js";



import { UsersClient } from "./users/index.js";



import { ActivityClient } from "./activity/index.js";



import { AccountActivityClient } from "./account_activity/index.js";



import { PostsClient } from "./posts/index.js";



import { SpacesClient } from "./spaces/index.js";



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
  /** OAuth1 instance for authentication */
  oauth1?: any;
  /** Custom headers to include in requests */
  headers?: Record<string, string>;
  /** Request timeout in milliseconds */
  timeout?: number;
  /** Whether to automatically retry failed requests */
  retry?: boolean;
  /** Maximum number of retry attempts */
  maxRetries?: number;
  /** User agent string */
  userAgent?: string;
}

/**
 * API Error class for handling X API errors
 */
export class ApiError extends Error {
  public readonly status: number;
  public readonly statusText: string;
  public readonly headers: Headers;
  public readonly data?: any;

  constructor(message: string, status: number, statusText: string, headers: Headers, data?: any) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.statusText = statusText;
    this.headers = headers;
    this.data = data;
  }
}

/**
 * Request options for API calls
 */
export interface RequestOptions {
  /** Request timeout in milliseconds */
  timeout?: number;
  /** Additional headers */
  headers?: Record<string, string>;
  /** Request signal for cancellation */
  signal?: AbortSignal;
  /** Request body */
  body?: string;
  /** Return raw HTTP wrapper instead of parsed body */
  raw?: boolean;
}

/**
 * Response wrapper with metadata
 */
export interface ApiResponse<T = any> {
  /** Response body */
  body: T;
  /** Response headers */
  headers: Headers;
  /** HTTP status code */
  status: number;
  /** HTTP status text */
  statusText: string;
  /** Response URL */
  url: string;
}

/**
 * Pagination metadata
 */
export interface PaginationMeta {
  /** Next page token */
  next_token?: string;
  /** Previous page token */
  previous_token?: string;
  /** Total count */
  total_count?: number;
  /** Result count */
  result_count?: number;
}


/**
 * Main client class for the X API
 * 
 * This is the primary entry point for interacting with the X API. It provides
 * access to all API endpoints through specialized client modules and handles
 * authentication, request configuration, and error handling.
 * 
 * @example
 * ```typescript
 * import { Client } from 'x-api-sdk';
 * 
 * const client = new Client({
 *   bearerToken: 'your-bearer-token'
 * });
 * 
 * // Get user information
 * const user = await client.users.getUser('783214');
 * 
 * // Get followers with pagination
 * const followers = await client.users.getFollowers('783214', {
 *   maxResults: 10,
 *   userFields: ['id', 'name', 'username']
 * });
 * 
 * // Iterate through followers
 * for await (const follower of followers) {
 *   console.log(follower.username);
 * }
 * ```
 * 
 * @category Client
 */
export class Client {
  /** Base URL for API requests */
  readonly baseUrl: string;
  /** Bearer token for authentication */
  readonly bearerToken?: string;
  /** OAuth2 access token */
  readonly accessToken?: string;
  /** OAuth1 instance for authentication */
  readonly oauth1?: any;
  /** Headers for requests */
  readonly headers: Headers;
  /** Request timeout in milliseconds */
  readonly timeout: number;
  /** Whether to automatically retry failed requests */
  readonly retry: boolean;
  /** Maximum number of retry attempts */
  readonly maxRetries: number;
  /** User agent string */
  readonly userAgent: string;

  /** HTTP client for making requests */
  readonly httpClient = httpClient;


  /** lists client */
  readonly lists: ListsClient;

  /** direct messages client */
  readonly directMessages: DirectMessagesClient;

  /** usage client */
  readonly usage: UsageClient;

  /** webhooks client */
  readonly webhooks: WebhooksClient;

  /** trends client */
  readonly trends: TrendsClient;

  /** community notes client */
  readonly communityNotes: CommunityNotesClient;

  /** stream client */
  readonly stream: StreamClient;

  /** communities client */
  readonly communities: CommunitiesClient;

  /** media client */
  readonly media: MediaClient;

  /** connections client */
  readonly connections: ConnectionsClient;

  /** compliance client */
  readonly compliance: ComplianceClient;

  /** general client */
  readonly general: GeneralClient;

  /** users client */
  readonly users: UsersClient;

  /** activity client */
  readonly activity: ActivityClient;

  /** account activity client */
  readonly accountActivity: AccountActivityClient;

  /** posts client */
  readonly posts: PostsClient;

  /** spaces client */
  readonly spaces: SpacesClient;


  /**
   * Creates a new X API client instance
   * 
   * @param config - Configuration options for the client
   * 
   * @example
   * ```typescript
   * // Bearer token authentication
   * const client = new Client({
   *   bearerToken: 'your-bearer-token'
   * });
   * 
   * // OAuth2 authentication
   * const client = new Client({
   *   accessToken: 'your-access-token'
   * });
   * 
   * // OAuth1 authentication
   * const client = new Client({
   *   oauth1: oauth1Instance
   * });
   * ```
   */
  constructor(config: ClientConfig | any) {
    // Handle OAuth1 instance passed directly
    if (config && typeof config === 'object' && config.accessToken && config.accessToken.accessToken && config.accessToken.accessTokenSecret) {
      // This is an OAuth1 instance
      this.oauth1 = config;
      this.baseUrl = "https://api.x.com";
    } else {
      // This is a regular config object
      const clientConfig = config as ClientConfig;
      this.baseUrl = clientConfig.baseUrl || "https://api.x.com";
      this.bearerToken = clientConfig.bearerToken;
      this.accessToken = clientConfig.accessToken;
      this.oauth1 = clientConfig.oauth1;
    }
    
    this.timeout = (config as ClientConfig).timeout || 30000;
    this.retry = (config as ClientConfig).retry ?? true;
    this.maxRetries = (config as ClientConfig).maxRetries || 3;
    this.userAgent = (config as ClientConfig).userAgent || "x-api-sdk/1.0.0";
    
    // Initialize headers
    const defaultHeaders: Record<string, string> = {
      'User-Agent': this.userAgent,
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      ...((config as ClientConfig).headers || {}),
    };
    
    this.headers = httpClient.createHeaders(defaultHeaders);


    this.lists = new ListsClient(this);

    this.directMessages = new DirectMessagesClient(this);

    this.usage = new UsageClient(this);

    this.webhooks = new WebhooksClient(this);

    this.trends = new TrendsClient(this);

    this.communityNotes = new CommunityNotesClient(this);

    this.stream = new StreamClient(this);

    this.communities = new CommunitiesClient(this);

    this.media = new MediaClient(this);

    this.connections = new ConnectionsClient(this);

    this.compliance = new ComplianceClient(this);

    this.general = new GeneralClient(this);

    this.users = new UsersClient(this);

    this.activity = new ActivityClient(this);

    this.accountActivity = new AccountActivityClient(this);

    this.posts = new PostsClient(this);

    this.spaces = new SpacesClient(this);

  }

  /**
   * Make an authenticated request to the X API
   * 
   * This method handles authentication, request formatting, and error handling
   * for all API requests. It automatically adds the appropriate authentication
   * headers based on the client configuration.
   * 
   * @param method - HTTP method (GET, POST, PUT, DELETE, etc.)
   * @param path - API endpoint path (e.g., '/2/users/by/username/username')
   * @param options - Request options including timeout, headers, and body
   * @returns Promise that resolves to the parsed response data
   * 
   * @example
   * ```typescript
   * // GET request
   * const user = await client.request('GET', '/2/users/by/username/username', {
   *   timeout: 5000
   * });
   * 
   * // POST request with body
   * const result = await client.request('POST', '/2/tweets', {
   *   body: JSON.stringify({ text: 'Hello World!' })
   * });
   * ```
   * 
   * @throws {ApiError} When the API returns an error response
   */
  async request<T = any>(
    method: string,
    path: string,
    options: RequestOptions = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${path}`;
    const headers = new Headers(this.headers);
    
    // Add authentication headers
    if (this.bearerToken) {
      headers.set('Authorization', `Bearer ${this.bearerToken}`);
    } else if (this.accessToken) {
      headers.set('Authorization', `Bearer ${this.accessToken}`);
    } else if (this.oauth1 && this.oauth1.accessToken) {
      // OAuth1 authentication - build proper OAuth1 header
      try {
        const oauthHeader = await this.oauth1.buildRequestHeader(method, url, options.body || '');
        headers.set('Authorization', oauthHeader);
        
        // Remove Content-Type for OAuth1 requests if it's application/json
        // OAuth1 typically expects application/x-www-form-urlencoded or no content type
        if (headers.get('Content-Type') === 'application/json') {
          headers.delete('Content-Type');
        }
      } catch (error) {
        throw new Error(`Failed to build OAuth1 header: ${error instanceof Error ? error.message : 'Unknown error'}`);
      }
    }
    
    // Add custom headers
    if (options.headers) {
      Object.entries(options.headers).forEach(([key, value]) => {
        headers.set(key, value);
      });
    }

    try {
      const response = await this.httpClient.request(url, {
        method,
        headers,
        signal: options.signal,
        body: options.body,
        timeout: options.timeout !== undefined ? options.timeout : this.timeout,
      });

      if (!response.ok) {
        let errorData: any;
        try {
          errorData = await response.json();
        } catch {
          errorData = await response.text();
        }
        
        throw new ApiError(
          errorData && errorData.message ? errorData.message : `HTTP ${response.status}: ${response.statusText}`,
          response.status,
          response.statusText,
          response.headers,
          errorData
        );
      }

      // For streaming requests, return the raw Response object
      if (options.raw) {
        return response as any; // Return the actual Response object for streaming
      }

      let data: T;
      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        data = await response.json();
      } else {
        data = await response.text() as T;
      }

      // Return parsed body for non-streaming requests
      return data;
    } catch (error) {
      if (error instanceof ApiError) {
        throw error;
      }
      throw new ApiError(
        error instanceof Error ? error.message : 'Request failed',
        0,
        'NETWORK_ERROR',
        new Headers(),
        error
      );
    }
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

  /**
   * Get the current authentication status
   */
  isAuthenticated(): boolean {
    return !!(this.bearerToken || this.accessToken || (this.oauth1 && this.oauth1.accessToken));
  }

  /**
   * Map OpenAPI security scheme names to internal authentication types
   * @param securitySchemeName The security scheme name from OpenAPI
   * @returns Array of internal authentication types
   */
  public mapSecuritySchemeToAuthTypes(securitySchemeName: string): string[] {
    // Mappings for X/Twitter API security schemes
    const schemeMapping: Record<string, string[]> = {
      'BearerToken': ['bearer_token'],           // App-only OAuth2.0
      'OAuth2UserToken': ['oauth2_user_context'], // OAuth2.0 User Context
      'UserToken': ['oauth1'],                   // OAuth1.0a User Context
      // Fallback mappings for common variations
      'OAuth2': ['bearer_token', 'oauth2_user_context'],
      'OAuth1': ['oauth1'],
      'Bearer': ['bearer_token'],
      'OAuth2User': ['oauth2_user_context'],
      'OAuth1User': ['oauth1'],
    };

    return schemeMapping[securitySchemeName] || [securitySchemeName.toLowerCase()];
  }

  /**
   * Validate that the required authentication method is available
   * @param requiredAuthTypes Array of required authentication types (OpenAPI security scheme names)
   * @param operationName Name of the operation for error messages
   */
  public validateAuthentication(requiredAuthTypes: string[], operationName: string): void {
    if (requiredAuthTypes.length === 0) {
      return; // No authentication required
    }

    const availableAuthTypes: string[] = [];
    
    if (this.bearerToken) {
      availableAuthTypes.push('bearer_token');
    }
    if (this.accessToken) {
      availableAuthTypes.push('oauth2_user_context');
    }
    if (this.oauth1 && this.oauth1.accessToken) {
      availableAuthTypes.push('oauth1');
    }

    // Map OpenAPI security schemes to internal auth types
    const mappedRequiredTypes = requiredAuthTypes.flatMap(scheme => 
      this.mapSecuritySchemeToAuthTypes(scheme)
    );

    // Check if any of the required auth types are available
    const hasRequiredAuth = mappedRequiredTypes.some(required => 
      availableAuthTypes.includes(required)
    );

    if (!hasRequiredAuth) {
      const availableStr = availableAuthTypes.length > 0 ? availableAuthTypes.join(', ') : 'none';
      const requiredStr = requiredAuthTypes.join(', ');
      throw new Error(
        `Authentication required for ${operationName}. ` +
        `Required: ${requiredStr}. ` +
        `Available: ${availableStr}. ` +
        `Please configure the appropriate authentication method.`
      );
    }
  }

  /**
   * Get available authentication types
   */
  getAvailableAuthTypes(): string[] {
    const authTypes: string[] = [];
    if (this.bearerToken) authTypes.push('bearer_token');
    if (this.accessToken) authTypes.push('oauth2_user_context');
    if (this.oauth1 && this.oauth1.accessToken) authTypes.push('oauth1');
    return authTypes;
  }
} 