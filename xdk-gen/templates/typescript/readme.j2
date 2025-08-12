# X API SDK

A modern TypeScript/JavaScript SDK for interacting with the X API. Built with full TypeScript support and comprehensive API coverage.

## Installation

```bash
# Using npm
npm install x-api-sdk

# Using yarn
yarn add x-api-sdk

# Using pnpm (recommended)
pnpm add x-api-sdk
```

## Quick Start

```typescript
import { Client } from 'x-api-sdk';

// Create a client instance - no polyfills needed!
const client = new Client({
    bearerToken: 'your-bearer-token'
});

// Example: Get user details by ID
const user = await client.users.getById('12345');

// Example: Get user details by username
const userByUsername = await client.users.getByUsername('username');

// Example: Get multiple users by IDs
const users = await client.users.getByIds(['12345', '67890']);

// Example: Search for users
const searchResults = await client.users.search('query', 10);

console.log(user.data);
```

## Authentication

The SDK supports multiple authentication methods:

### Bearer Token (App-only)
```typescript
import { Client } from 'x-api-sdk';

const client = new Client({
    bearerToken: 'your-bearer-token'
});
```

### OAuth 2.0 (User authentication)
```typescript
import { Client, OAuth2Auth } from 'x-api-sdk';

const oauth2 = new OAuth2Auth({
    clientId: 'your-client-id',
    clientSecret: 'your-client-secret',
    redirectUri: 'your-redirect-uri'
});

// Get authorization URL
const authUrl = oauth2.getAuthorizationUrl();

// After user authorizes, exchange code for tokens
const tokens = await oauth2.exchangeCodeForTokens('authorization-code');

const client = new Client({
    accessToken: tokens.access_token
});
```

## API Examples

### Users API
```typescript
// Get user by ID
const user = await client.users.getById('12345', ['id', 'name', 'username']);

// Get user by username
const userByUsername = await client.users.getByUsername('username');

// Get multiple users
const users = await client.users.getByIds(['12345', '67890']);

// Search users
const searchResults = await client.users.search('query', 10);

// Get user's followers
const followers = await client.users.getFollowers('12345', 100);

// Get user's following
const following = await client.users.getFollowing('12345', 100);
```

### Tweets API
```typescript
// Get user's tweets
const tweets = await client.tweets.getUserTweets('12345', 10);

// Get tweet by ID
const tweet = await client.tweets.getById('tweet-id');

// Get multiple tweets
const tweets = await client.tweets.getByIds(['tweet1', 'tweet2']);

// Search tweets
const searchResults = await client.tweets.search('query', 10);
```

### Lists API
```typescript
// Get user's lists
const lists = await client.lists.getUserOwnedLists('12345');

// Get list by ID
const list = await client.lists.getById('list-id');

// Get list members
const members = await client.lists.getMembers('list-id', 100);
```

## Environment Support

The SDK automatically handles polyfills and works in all environments:

### Node.js 18+ (Native Fetch)
```javascript
import { Client } from 'x-api-sdk';
// Works immediately - no polyfills needed
const client = new Client({ bearerToken: 'token' });
```

### Node.js 16-17 (with node-fetch)
```javascript
import { Client } from 'x-api-sdk';
// Works automatically - SDK sets up polyfills internally
const client = new Client({ bearerToken: 'token' });
```

### Modern Browsers
```javascript
import { Client } from 'x-api-sdk';
// Works immediately - uses native browser APIs
const client = new Client({ bearerToken: 'token' });
```

### Requirements
- **Node.js**: 16.14+ (18+ recommended for native fetch support)
- **Browsers**: Modern browsers with fetch support
- **Dependencies**: `node-fetch` is automatically included for Node.js environments

## Features

- ✨ **Full TypeScript support** with complete type definitions
- 🔄 **Dual ESM/CommonJS support** for maximum compatibility
- 🌐 **Zero-config polyfills** - works in Node.js and browsers automatically
- 🔒 **OAuth2 authentication** with PKCE support
- 📄 **Comprehensive API coverage** - all X API endpoints
- 🚨 **Robust error handling** with detailed error messages
- 📦 **Tree-shakeable** - only import what you use
- ⚡ **Minimal dependencies** - lightweight and fast
- 🔧 **Auto-generated** - always up to date with the latest API changes

## Type Safety

The SDK is written in TypeScript and provides full type safety:

```typescript
// All methods have complete type definitions
const user = await client.users.getById('12345', ['id', 'name', 'username']);

// TypeScript knows the exact structure of the response
console.log(user.data?.name); // ✅ Fully typed
console.log(user.data?.id);   // ✅ Fully typed

// Autocomplete and type checking work out of the box
const searchResults = await client.users.search(
    'query',     // ✅ Type checked
    10,          // ✅ Type checked
    undefined,   // ✅ Optional parameters
    ['id', 'name'] // ✅ Type checked array
);
```

## Error Handling

The SDK provides comprehensive error handling:

```typescript
try {
    const user = await client.users.getById('invalid-id');
} catch (error) {
    if (error instanceof ApiError) {
        console.log('API Error:', error.status, error.message);
        console.log('Response:', error.response);
    } else {
        console.log('Network Error:', error.message);
    }
}
```

## Pagination

Many API endpoints support pagination:

```typescript
// Get all followers (handles pagination automatically)
const allFollowers = [];
for await (const follower of client.users.getFollowersAll('12345')) {
    allFollowers.push(follower);
    console.log('Follower:', follower.name);
}
```

## Configuration

The client supports various configuration options:

```typescript
const client = new Client({
    bearerToken: 'your-bearer-token',
    baseUrl: 'https://api.twitter.com', // Optional: custom base URL
    timeout: 30000, // Optional: request timeout in milliseconds
    retries: 3, // Optional: number of retry attempts
});
```

## Development

```bash
# Install dependencies
npm install

# Build the SDK
npm run build

# Run tests
npm test

# Lint code
npm run lint

# Format code
npm run format

# Type checking
npm run type-check
```

## API Reference

The SDK provides access to all X API endpoints:

- **Users API** - User management and lookup
- **Tweets API** - Tweet creation, retrieval, and search
- **Lists API** - List management and operations
- **Spaces API** - Audio spaces functionality
- **Direct Messages API** - DM management
- **Bookmarks API** - Bookmark operations
- **Compliance API** - Data compliance and deletion
- **Media API** - Media upload and management
- **Trends API** - Trending topics and places
- **Stream API** - Real-time data streaming

For detailed API documentation, visit the [X API Documentation](https://developer.twitter.com/en/docs/twitter-api).

## Contributing

This SDK is auto-generated from the X API OpenAPI specification. To contribute:

1. Fork the repository
2. Make your changes to the generator templates
3. Run the generation process
4. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details. 