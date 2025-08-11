/**
 * Environment-aware HTTP client for the X API SDK.
 * 
 * This module provides a universal HTTP client that works in both Node.js and browser environments
 * without requiring manual polyfills.
 */

// Environment detection
const isNode =
  typeof process !== 'undefined' && process.versions && process.versions.node;
const isBrowser =
  typeof window !== 'undefined' && typeof window.fetch === 'function';

// Type definitions
export interface RequestOptions {
  method?: string;
  headers?: Record<string, string> | Headers;
  body?: string | Buffer | ArrayBuffer | ArrayBufferView;
  signal?: AbortSignal;
}

export interface HttpResponse {
  ok: boolean;
  status: number;
  statusText: string;
  headers: Headers;
  url: string;
  json(): Promise<any>;
  text(): Promise<string>;
  arrayBuffer(): Promise<ArrayBuffer>;
}

/**
 * Universal HTTP client that works in both Node.js and browser environments
 */
export class HttpClient {
  private fetch: any;
  private HeadersClass: any;

  constructor() {
    if (isNode) {
      // Node.js environment - dynamically import node-fetch
      this.initializeNodeEnvironment();
    } else if (isBrowser) {
      // Browser environment - use native APIs
      this.fetch = globalThis.fetch;
      this.HeadersClass = globalThis.Headers;
    } else {
      // Fallback for other environments (Deno, etc.)
      this.fetch = globalThis.fetch;
      this.HeadersClass = globalThis.Headers;
    }
  }

  private async initializeNodeEnvironment(): Promise<void> {
    try {
      // Try to use native Node.js fetch (Node 18+)
      if (typeof globalThis.fetch === 'function') {
        this.fetch = globalThis.fetch;
        this.HeadersClass = globalThis.Headers;
        return;
      }

      // Fallback to node-fetch for older Node.js versions
      try {
        const {
          default: nodeFetch,
          Headers: NodeHeaders,
        } = await import('node-fetch');
        // Use any type to avoid type conflicts
        this.fetch = nodeFetch as any;
        this.HeadersClass = NodeHeaders as any;
      } catch (importError) {
        // If node-fetch is not available, provide a helpful error
        throw new Error(
          'HTTP client requires either Node.js 18+ (with native fetch) or node-fetch package. ' +
            'Please install node-fetch: npm install node-fetch'
        );
      }
    } catch (error) {
      // If node-fetch is not available, provide a helpful error
      throw new Error(
        'HTTP client requires either Node.js 18+ (with native fetch) or node-fetch package. ' +
          'Please install node-fetch: npm install node-fetch'
      );
    }
  }

  /**
   * Create a new Headers instance
   */
  createHeaders(init?: Record<string, string> | Headers): Headers {
    return new this.HeadersClass(init) as Headers;
  }

  /**
   * Make an HTTP request
   */
  async request(
    url: string,
    options: RequestOptions = {}
  ): Promise<HttpResponse> {
    // Ensure fetch is initialized (for Node.js async initialization)
    if (!this.fetch) {
      await this.initializeNodeEnvironment();
    }

    // Convert body to string if it's a Buffer or ArrayBuffer
    let body = options.body;
    if (body && typeof body !== 'string') {
      if (Buffer.isBuffer(body)) {
        body = body.toString();
      } else if (body instanceof ArrayBuffer) {
        body = new TextDecoder().decode(body);
      } else if (ArrayBuffer.isView(body)) {
        body = new TextDecoder().decode(body);
      }
    }

    const response = await this.fetch(url, {
      method: options.method || 'GET',
      headers: options.headers as any,
      body: body as any,
      signal: options.signal,
    });

    return response as HttpResponse;
  }

  /**
   * Make a GET request
   */
  async get(
    url: string,
    headers?: Record<string, string>
  ): Promise<HttpResponse> {
    return this.request(url, {
      method: 'GET',
      headers,
    });
  }

  /**
   * Make a POST request
   */
  async post(
    url: string,
    body?: string,
    headers?: Record<string, string>
  ): Promise<HttpResponse> {
    return this.request(url, {
      method: 'POST',
      headers,
      body,
    });
  }

  /**
   * Make a PUT request
   */
  async put(
    url: string,
    body?: string,
    headers?: Record<string, string>
  ): Promise<HttpResponse> {
    return this.request(url, {
      method: 'PUT',
      headers,
      body,
    });
  }

  /**
   * Make a DELETE request
   */
  async delete(
    url: string,
    headers?: Record<string, string>
  ): Promise<HttpResponse> {
    return this.request(url, {
      method: 'DELETE',
      headers,
    });
  }

  /**
   * Make a PATCH request
   */
  async patch(
    url: string,
    body?: string,
    headers?: Record<string, string>
  ): Promise<HttpResponse> {
    return this.request(url, {
      method: 'PATCH',
      headers,
      body,
    });
  }
}

// Export a singleton instance
export const httpClient = new HttpClient();
