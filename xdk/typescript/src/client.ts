/**
 * Main client for the X API.
 *
 * This module provides the main client class for interacting with the X API.
 */

import { httpClient } from './http-client.js';

import { MediaClient } from './media/index.js';

import { TrendsClient } from './trends/index.js';

import { AaasubscriptionsClient } from './aaasubscriptions/index.js';

import { SpacesClient } from './spaces/index.js';

import { StreamClient } from './stream/index.js';

import { GeneralClient } from './general/index.js';

import { CommunitiesClient } from './communities/index.js';

import { ComplianceClient } from './compliance/index.js';

import { UsersClient } from './users/index.js';

import { ListsClient } from './lists/index.js';

import { DirectMessagesClient } from './direct_messages/index.js';

import { CommunityNotesClient } from './community_notes/index.js';

import { UsageClient } from './usage/index.js';

import { PostsClient } from './posts/index.js';

import { WebhooksClient } from './webhooks/index.js';

import { BookmarksClient } from './bookmarks/index.js';

import { AccountActivityClient } from './account_activity/index.js';

import { ConnectionClient } from './connection/index.js';

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

  constructor(
    message: string,
    status: number,
    statusText: string,
    headers: Headers,
    data?: any
  ) {
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
}

/**
 * Response wrapper with metadata
 */
export interface ApiResponse<T = any> {
  /** Response data */
  data: T;
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
 * Paginated response wrapper
 */
export interface PaginatedResponse<T = any> extends ApiResponse<T[]> {
  /** Pagination metadata */
  meta: PaginationMeta;
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
  /** Request timeout in milliseconds */
  readonly timeout: number;
  /** Whether to automatically retry failed requests */
  readonly retry: boolean;
  /** Maximum number of retry attempts */
  readonly maxRetries: number;
  /** User agent string */
  readonly userAgent: string;
  /** OAuth2 session for requests */
  readonly oauth2Session?: typeof fetch;
  /** OAuth2 authentication instance */
  readonly oauth2Auth?: any;
  /** OAuth2 token */
  readonly token?: any;

  /** HTTP client for making requests */
  readonly httpClient = httpClient;

  /** media client */
  readonly media: MediaClient;

  /** trends client */
  readonly trends: TrendsClient;

  /** aaasubscriptions client */
  readonly aaasubscriptions: AaasubscriptionsClient;

  /** spaces client */
  readonly spaces: SpacesClient;

  /** stream client */
  readonly stream: StreamClient;

  /** general client */
  readonly general: GeneralClient;

  /** communities client */
  readonly communities: CommunitiesClient;

  /** compliance client */
  readonly compliance: ComplianceClient;

  /** users client */
  readonly users: UsersClient;

  /** lists client */
  readonly lists: ListsClient;

  /** direct messages client */
  readonly direct_messages: DirectMessagesClient;

  /** community notes client */
  readonly community_notes: CommunityNotesClient;

  /** usage client */
  readonly usage: UsageClient;

  /** posts client */
  readonly posts: PostsClient;

  /** webhooks client */
  readonly webhooks: WebhooksClient;

  /** bookmarks client */
  readonly bookmarks: BookmarksClient;

  /** account activity client */
  readonly account_activity: AccountActivityClient;

  /** connection client */
  readonly connection: ConnectionClient;

  constructor(config: ClientConfig = {}) {
    this.baseUrl = config.baseUrl || 'https://api.x.com';
    this.bearerToken = config.bearerToken;
    this.accessToken = config.accessToken;
    this.timeout = config.timeout || 30000;
    this.retry = config.retry !== undefined ? config.retry : true;
    this.maxRetries = config.maxRetries || 3;
    this.userAgent = config.userAgent || 'x-api-sdk/1.0.0';

    // Initialize headers
    const defaultHeaders: Record<string, string> = {
      'User-Agent': this.userAgent,
      'Content-Type': 'application/json',
      Accept: 'application/json',
      ...config.headers,
    };

    this.headers = httpClient.createHeaders(defaultHeaders);

    this.media = new MediaClient(this);

    this.trends = new TrendsClient(this);

    this.aaasubscriptions = new AaasubscriptionsClient(this);

    this.spaces = new SpacesClient(this);

    this.stream = new StreamClient(this);

    this.general = new GeneralClient(this);

    this.communities = new CommunitiesClient(this);

    this.compliance = new ComplianceClient(this);

    this.users = new UsersClient(this);

    this.lists = new ListsClient(this);

    this.direct_messages = new DirectMessagesClient(this);

    this.community_notes = new CommunityNotesClient(this);

    this.usage = new UsageClient(this);

    this.posts = new PostsClient(this);

    this.webhooks = new WebhooksClient(this);

    this.bookmarks = new BookmarksClient(this);

    this.account_activity = new AccountActivityClient(this);

    this.connection = new ConnectionClient(this);
  }

  /**
   * Make an authenticated request to the API
   */
  async request<T = any>(
    method: string,
    path: string,
    options: RequestOptions = {}
  ): Promise<ApiResponse<T>> {
    const url = `${this.baseUrl}${path}`;
    const headers = new Headers(this.headers);

    // Add authentication headers
    if (this.bearerToken) {
      headers.set('Authorization', `Bearer ${this.bearerToken}`);
    } else if (this.accessToken) {
      headers.set('Authorization', `Bearer ${this.accessToken}`);
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
      });

      if (!response.ok) {
        let errorData: any;
        try {
          errorData = await response.json();
        } catch {
          errorData = await response.text();
        }

        throw new ApiError(
          errorData && errorData.message
            ? errorData.message
            : `HTTP ${response.status}: ${response.statusText}`,
          response.status,
          response.statusText,
          response.headers,
          errorData
        );
      }

      let data: T;
      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        data = await response.json();
      } else {
        data = (await response.text()) as T;
      }

      return {
        data,
        headers: response.headers,
        status: response.status,
        statusText: response.statusText,
        url: response.url || url,
      };
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
    return !!(this.bearerToken || this.accessToken);
  }
}
