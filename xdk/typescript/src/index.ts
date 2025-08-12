/**
 * X API SDK
 *
 * A modern TypeScript/JavaScript SDK for interacting with the X API.
 * Built with full TypeScript support, React hooks, and Next.js integration.
 */

// Automatic polyfill setup for Node.js environments
if (typeof process !== 'undefined' && process.versions && process.versions.node) {
  // Node.js environment - set up polyfills if needed
  if (typeof globalThis.fetch === 'undefined' || typeof globalThis.Headers === 'undefined') {
    try {
      // Try to use native Node.js fetch (Node 18+)
      if (typeof globalThis.fetch === 'function' && typeof globalThis.Headers === 'function') {
        // Native APIs are available, no polyfills needed
      } else {
        // Need to set up polyfills for older Node.js versions
        const nodeFetch = require('node-fetch');
        const { Headers: NodeHeaders } = nodeFetch;
        
        if (typeof globalThis.fetch === 'undefined') {
          (globalThis as any).fetch = nodeFetch.default || nodeFetch;
        }
        if (typeof globalThis.Headers === 'undefined') {
          (globalThis as any).Headers = NodeHeaders;
        }
      }
    } catch (error) {
      // If node-fetch is not available, provide a helpful error
      console.warn(
        'X API SDK: node-fetch not found. For Node.js environments, please install node-fetch:\n' +
        'npm install node-fetch\n' +
        'Or upgrade to Node.js 18+ for native fetch support.'
      );
    }
  }
}

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

// Client modules and their types

export * from './general/index.js';

export * from './webhooks/index.js';

export * from './account_activity/index.js';

export * from './usage/index.js';

export * from './community_notes/index.js';

export * from './compliance/index.js';

export * from './communities/index.js';

export * from './trends/index.js';

export * from './direct_messages/index.js';

export * from './stream/index.js';

export * from './connection/index.js';

export * from './bookmarks/index.js';

export * from './spaces/index.js';

export * from './media/index.js';

export * from './lists/index.js';

export * from './users/index.js';

export * from './posts/index.js';

export * from './aaasubscriptions/index.js';


// Utilities
export * from './paginator.js'; 