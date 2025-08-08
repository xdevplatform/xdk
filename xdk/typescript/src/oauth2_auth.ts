/**
 * OAuth2 authentication utilities for the X API.
 */

/**
 * OAuth2 configuration options
 */
export interface OAuth2Config {
    /** Client ID */
    clientId: string;
    /** Client secret */
    clientSecret: string;
    /** Redirect URI */
    redirectUri: string;
    /** Authorization URL */
    authUrl?: string;
    /** Token URL */
    tokenUrl?: string;
    /** Scopes to request */
    scopes?: string[];
}

/**
 * OAuth2 token response
 */
export interface OAuth2Token {
    /** Access token */
    accessToken: string;
    /** Token type */
    tokenType: string;
    /** Expiration time in seconds */
    expiresIn: number;
    /** Refresh token */
    refreshToken?: string;
    /** Scopes granted */
    scope?: string;
}

/**
 * OAuth2 authentication handler
 */
export class OAuth2Auth {
    private config: OAuth2Config;
    private token?: OAuth2Token;

    constructor(config: OAuth2Config) {
        this.config = {
            authUrl: 'https://twitter.com/i/oauth2/authorize',
            tokenUrl: 'https://api.twitter.com/2/oauth2/token',
            scopes: ['tweet.read', 'users.read'],
            ...config
        };
    }

    /**
     * Get the authorization URL
     */
    getAuthorizationUrl(state?: string): string {
        const params = new URLSearchParams({
            response_type: 'code',
            client_id: this.config.clientId,
            redirect_uri: this.config.redirectUri,
            scope: this.config.scopes?.join(' ') || '',
            state: state || ''
        });

        return `${this.config.authUrl}?${params.toString()}`;
    }

    /**
     * Exchange authorization code for tokens
     */
    async exchangeCode(code: string): Promise<OAuth2Token> {
        const params = new URLSearchParams({
            grant_type: 'authorization_code',
            code,
            redirect_uri: this.config.redirectUri,
            client_id: this.config.clientId,
            client_secret: this.config.clientSecret
        });

        const response = await fetch(this.config.tokenUrl!, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: params.toString()
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        this.token = {
            accessToken: data.access_token,
            tokenType: data.token_type,
            expiresIn: data.expires_in,
            refreshToken: data.refresh_token,
            scope: data.scope
        };

        return this.token;
    }

    /**
     * Refresh the access token
     */
    async refreshToken(): Promise<OAuth2Token> {
        if (!this.token?.refreshToken) {
            throw new Error('No refresh token available');
        }

        const params = new URLSearchParams({
            grant_type: 'refresh_token',
            refresh_token: this.token.refreshToken,
            client_id: this.config.clientId,
            client_secret: this.config.clientSecret
        });

        const response = await fetch(this.config.tokenUrl!, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: params.toString()
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        this.token = {
            accessToken: data.access_token,
            tokenType: data.token_type,
            expiresIn: data.expires_in,
            refreshToken: data.refresh_token || this.token.refreshToken,
            scope: data.scope
        };

        return this.token;
    }

    /**
     * Get the current token
     */
    getToken(): OAuth2Token | undefined {
        return this.token;
    }
} 