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
    this.initializeEnvironment();
  }

  private initializeEnvironment(): void {
    if (isNode) {
      // Node.js environment - set up polyfills synchronously
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

  private initializeNodeEnvironment(): void {
    // Check if native fetch is available (Node.js 18+)
    if (
      typeof globalThis.fetch === 'function' &&
      typeof globalThis.Headers === 'function'
    ) {
      this.fetch = globalThis.fetch;
      this.HeadersClass = globalThis.Headers;
      return;
    }

    // Try to use node-fetch for older Node.js versions
    try {
      const nodeFetch = require('node-fetch');
      const { Headers: NodeHeaders } = nodeFetch;

      this.fetch = nodeFetch.default || nodeFetch;
      this.HeadersClass = NodeHeaders;
    } catch (error) {
      // If node-fetch is not available, provide a helpful error
      throw new Error(
        'X API SDK: node-fetch not found. For Node.js environments, please install node-fetch:\n' +
          'npm install node-fetch\n' +
          'Or upgrade to Node.js 18+ for native fetch support.'
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
