/**
 * X API SDK
 *
 * A modern TypeScript/JavaScript SDK for interacting with the X API.
 * Built with full TypeScript support, React hooks, and Next.js integration.
 */

// Main client
export { Client } from './client.js';
export type { ClientConfig } from './client.js';

// Error handling
export { ApiError } from './client.js';
export type { RequestOptions, ApiResponse, PaginatedResponse, PaginationMeta } from './client.js';

// HTTP client
export { httpClient, HttpClient } from './http-client.js';
export type { RequestOptions as HttpClientRequestOptions, HttpResponse } from './http-client.js';

// Authentication
export { OAuth2Auth } from './oauth2_auth.js';
export type { OAuth2Config } from './oauth2_auth.js';

// Client modules

export * from './media/index.js';

export * from './trends/index.js';

export * from './aaasubscriptions/index.js';

export * from './spaces/index.js';

export * from './stream/index.js';

export * from './general/index.js';

export * from './communities/index.js';

export * from './compliance/index.js';

export * from './users/index.js';

export * from './lists/index.js';

export * from './direct_messages/index.js';

export * from './community_notes/index.js';

export * from './usage/index.js';

export * from './posts/index.js';

export * from './webhooks/index.js';

export * from './bookmarks/index.js';

export * from './account_activity/index.js';

export * from './connection/index.js';


// Utilities
export * from './paginator.js'; 