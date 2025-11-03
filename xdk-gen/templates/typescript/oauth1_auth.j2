/**
 * OAuth1 authentication utilities for the X API.
 */

import { CryptoUtils, generateNonce, generateTimestamp } from './crypto_utils.js';

/**
 * OAuth1 configuration options
 */
export interface OAuth1Config {
  /** API Key (Consumer Key) */
  apiKey: string;
  /** API Secret (Consumer Secret) */
  apiSecret: string;
  /** Callback URL for OAuth flow */
  callback: string;
  /** Access Token (if already obtained) */
  accessToken?: string;
  /** Access Token Secret (if already obtained) */
  accessTokenSecret?: string;
}

/**
 * OAuth1 request token response
 */
export interface OAuth1RequestToken {
  /** OAuth token */
  oauthToken: string;
  /** OAuth token secret */
  oauthTokenSecret: string;
}

/**
 * OAuth1 access token response
 */
export interface OAuth1AccessToken {
  /** Access token */
  accessToken: string;
  /** Access token secret */
  accessTokenSecret: string;
}

/**
 * OAuth1 authentication handler
 */
export class OAuth1 {
  private config: OAuth1Config;
  public requestToken?: OAuth1RequestToken;
  public accessToken?: OAuth1AccessToken;

  constructor(config: OAuth1Config) {
    this.config = config;
    
    // If access token is provided, set it
    if (config.accessToken && config.accessTokenSecret) {
      this.accessToken = {
        accessToken: config.accessToken,
        accessTokenSecret: config.accessTokenSecret
      };
    }
  }

  /**
   * Get the authorization URL for OAuth1 flow
   * @param loginWithX Whether to use "Log in with X" flow
   * @returns Authorization URL
   */
  getAuthorizationUrl(loginWithX: boolean = false): string {
    if (!this.requestToken) {
      throw new Error('Request token not obtained. Call getRequestToken() first.');
    }

    const baseUrl = loginWithX 
      ? 'https://x.com/i/oauth/authenticate'
      : 'https://x.com/oauth/authorize';

    const params = new URLSearchParams({
      oauth_token: this.requestToken.oauthToken
    });

    return `${baseUrl}?${params.toString()}`;
  }

  /**
   * Get request token to start OAuth1 flow
   * @returns Promise with request token
   */
  async getRequestToken(): Promise<OAuth1RequestToken> {
    const url = 'https://api.x.com/oauth/request_token';
    
    const params = new URLSearchParams({
      oauth_callback: this.config.callback
    });

    const response = await fetch(`${url}?${params.toString()}`, {
      method: 'POST',
      headers: {
        'Authorization': await this._buildOAuthHeader('POST', url, params.toString())
      }
    });

    if (!response.ok) {
      throw new Error(`Failed to get request token: ${response.status} ${response.statusText}`);
    }

    const responseText = await response.text();
    const responseParams = new URLSearchParams(responseText);
    
    this.requestToken = {
      oauthToken: responseParams.get('oauth_token')!,
      oauthTokenSecret: responseParams.get('oauth_token_secret')!
    };

    return this.requestToken;
  }

  /**
   * Exchange verifier for access token
   * @param verifier OAuth verifier from callback or PIN
   * @returns Promise with access token
   */
  async getAccessToken(verifier: string): Promise<OAuth1AccessToken> {
    if (!this.requestToken) {
      throw new Error('Request token not obtained. Call getRequestToken() first.');
    }

    const url = 'https://api.x.com/oauth/access_token';
    
    const params = new URLSearchParams({
      oauth_token: this.requestToken.oauthToken,
      oauth_verifier: verifier
    });

    const response = await fetch(`${url}?${params.toString()}`, {
      method: 'POST',
      headers: {
        'Authorization': await this._buildOAuthHeader('POST', url, params.toString())
      }
    });

    if (!response.ok) {
      throw new Error(`Failed to get access token: ${response.status} ${response.statusText}`);
    }

    const responseText = await response.text();
    const responseParams = new URLSearchParams(responseText);
    
    this.accessToken = {
      accessToken: responseParams.get('oauth_token')!,
      accessTokenSecret: responseParams.get('oauth_token_secret')!
    };

    return this.accessToken;
  }

  /**
   * Build OAuth1 authorization header
   * @param method HTTP method
   * @param url Request URL
   * @param body Request body
   * @returns Promise that resolves to OAuth1 authorization header string
   */
  private async _buildOAuthHeader(method: string, url: string, body: string): Promise<string> {
    const timestamp = generateTimestamp();
    const nonce = generateNonce();
    
    const oauthParams: Record<string, string> = {
      oauth_consumer_key: this.config.apiKey,
      oauth_nonce: nonce,
      oauth_signature_method: 'HMAC-SHA1',
      oauth_timestamp: timestamp,
      oauth_version: '1.0'
    };

    // Add request token if available
    if (this.requestToken) {
      oauthParams['oauth_token'] = this.requestToken.oauthToken;
    }

    // Add access token if available
    if (this.accessToken) {
      oauthParams['oauth_token'] = this.accessToken.accessToken;
    }

    // Build signature base string
    const paramString = this._buildParamString(oauthParams, body);
    const signatureBase = `${method.toUpperCase()}&${this._encode(url)}&${this._encode(paramString)}`;
    
    // Generate signature
    const signingKey = `${this._encode(this.config.apiSecret)}&${this._encode(
      this.requestToken?.oauthTokenSecret || this.accessToken?.accessTokenSecret || ''
    )}`;
    
    const signature = await CryptoUtils.hmacSha1(signingKey, signatureBase);
    oauthParams['oauth_signature'] = signature;

    // Build authorization header
    const headerParams = Object.entries(oauthParams)
      .map(([key, value]) => `${key}="${this._encode(value)}"`)
      .join(', ');

    return `OAuth ${headerParams}`;
  }

  /**
   * Build parameter string for OAuth signature
   * @param oauthParams OAuth parameters
   * @param body Request body
   * @returns Parameter string
   */
  private _buildParamString(oauthParams: Record<string, string>, body: string): string {
    const allParams = { ...oauthParams };
    
    // Parse body parameters if present
    if (body) {
      try {
        const bodyParams = new URLSearchParams(body);
        bodyParams.forEach((value, key) => {
          allParams[key] = value;
        });
      } catch (error) {
        // If body parsing fails, ignore it
        console.warn('Failed to parse body parameters:', error);
      }
    }

    // Sort parameters alphabetically
    const sortedParams = Object.entries(allParams).sort(([a], [b]) => a.localeCompare(b));
    
    return sortedParams
      .map(([key, value]) => `${this._encode(key)}=${this._encode(value)}`)
      .join('&');
  }

  /**
   * URL encode string according to OAuth1 specification
   * @param str String to encode
   * @returns Encoded string
   */
  private _encode(str: string): string {
    return encodeURIComponent(str)
      .replace(/!/g, '%21')
      .replace(/\*/g, '%2A')
      .replace(/'/g, '%27')
      .replace(/\(/g, '%28')
      .replace(/\)/g, '%29')
      .replace(/%7E/g, '~');
  }

  /**
   * Convenience method to start the OAuth1 flow
   * @param loginWithX Whether to use "Log in with X" flow
   * @returns Promise that resolves to the authorization URL
   */
  async startOAuthFlow(loginWithX: boolean = false): Promise<string> {
    await this.getRequestToken();
    return this.getAuthorizationUrl(loginWithX);
  }

  /**
   * Build OAuth1 authorization header for API requests
   * @param method HTTP method
   * @param url Request URL
   * @param body Request body
   * @returns Promise that resolves to OAuth1 authorization header string
   */
  async buildRequestHeader(method: string, url: string, body: string = ''): Promise<string> {
    if (!this.accessToken) {
      throw new Error('Access token not available. Complete OAuth1 flow first.');
    }

    // Extract query parameters from URL if present
    let urlWithoutQuery = url;
    let queryParams = '';
    
    try {
      const urlObj = new URL(url);
      if (urlObj.search) {
        queryParams = urlObj.search.substring(1); // Remove the '?' prefix
        urlWithoutQuery = urlObj.origin + urlObj.pathname;
      }
    } catch (error) {
      // If URL parsing fails, use the original URL
      console.warn('Failed to parse URL for OAuth1:', error);
    }

    // Combine query parameters with body parameters
    let allParams = '';
    if (queryParams && body) {
      allParams = `${queryParams}&${body}`;
    } else if (queryParams) {
      allParams = queryParams;
    } else if (body) {
      allParams = body;
    }

    return this._buildOAuthHeader(method, urlWithoutQuery, allParams);
  }
} 