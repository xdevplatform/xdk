X API SDK v2.152 / [Exports](modules.md)

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

## Documentation

### 📚 API Reference

- **HTML Documentation**: [View Online](https://your-docs-site.com) | [Generate Locally](#generating-documentation)
- **TypeScript Definitions**: Full type definitions included
- **JSDoc Comments**: Comprehensive inline documentation

### 🔧 Generating Documentation

To generate documentation locally:

```bash
# Install dependencies
npm install

# Generate HTML documentation
npm run docs:build

# Generate and serve documentation locally
npm run docs:serve

# Watch for changes and regenerate
npm run docs:watch
```

The documentation will be generated in the `docs/` directory:
- `docs/html/` - HTML documentation with search and navigation
- `docs/markdown/` - Markdown documentation for GitHub/GitLab
- `docs/api/` - Minimal API reference

### 📖 Documentation Features

- **Interactive Examples**: Copy-paste ready code samples
- **Type Information**: Full TypeScript type definitions
- **Search**: Find methods, classes, and interfaces quickly
- **Categories**: Organized by functionality (Authentication, Pagination, etc.)
- **Cross-References**: Links between related methods and types

## Quick Start

```typescript
import { Client } from 'x-api-sdk';

// Create a client instance - no polyfills needed!
const client = new Client({
    bearerToken: 'your-bearer-token'
});

// Example: Get user details by ID
const user = await client.users.getById('12345');

// Example: Get user details by username with specific fields
const userByUsername = await client.users.getByUsername('username', {
  userFields: ['id', 'name', 'username', 'created_at'],
  expansions: ['pinned_tweet_id']
});

// Example: Get multiple users by IDs with options
const users = await client.users.getByIds(['12345', '67890'], {
  userFields: ['id', 'name', 'username'],
  requestOptions: { raw: true }
});

// Example: Search for users with pagination
const searchResults = await client.users.search('query', {
  maxResults: 10,
  userFields: ['id', 'name', 'username']
});

console.log(user);
```

## Ergonomic API Design

The SDK provides an ergonomic default behavior that returns the parsed API response body directly, avoiding the need for `res.data.data` patterns:

```typescript
// ✅ Default behavior - returns parsed body directly with exact types
const user = await client.users.getById('12345');
console.log(user.data); // Direct access to API response data
// Type: Promise<UsersGetByIdResponse>

// ✅ Raw HTTP wrapper when needed with exact types
const response = await client.users.getById('12345', { 
  requestOptions: { raw: true } 
});
console.log(response.body.data); // Access to full API response
console.log(response.status); // HTTP status code
console.log(response.headers); // Response headers
// Type: Promise<ApiResponse<UsersGetByIdResponse>>
```

### Response Structure

- **Default**: Returns the parsed API response body directly with exact TypeScript types
- **Raw mode** (`{ requestOptions: { raw: true } }`): Returns the full HTTP wrapper with `body`, `status`, `headers`, etc.

### Type Safety

The SDK uses function overloading to provide exact types based on the `raw` option:

```typescript
// ✅ Explicit type assignment works perfectly
const res: PostsGetByIdResponse = await client.posts.getById(postId);
const post = res.data; // ✅ Direct access, no manual checking

const res: ApiResponse<PostsGetByIdResponse> = await client.posts.getById(postId, { 
  requestOptions: { raw: true } 
});
const post = res.body.data; // ✅ Direct access, no manual checking

// ✅ TypeScript knows the exact return type automatically
const user = await client.users.getById('12345');
console.log(user.data); // ✅ Direct access to API data

const response = await client.users.getById('12345', { 
  requestOptions: { raw: true } 
});
console.log(response.body.data); // ✅ Access to wrapped response data
console.log(response.status); // ✅ HTTP status code
console.log(response.headers); // ✅ Response headers

// ❌ TypeScript prevents these errors at compile time:
// console.log(user.status); // Error: Property 'status' does not exist
// console.log(response.data); // Error: Property 'data' does not exist
```

**No Manual Runtime Checking Needed!** The function overloading ensures TypeScript knows the exact return type, eliminating the need for `if ('body' in result)` checks.

## Options Object Pattern

The SDK uses an options object pattern for all optional parameters, making the API more ergonomic and maintainable:

```typescript
// ✅ Clean, readable calls with named parameters
const user = await client.users.getById('12345', {
  userFields: ['id', 'name', 'username', 'created_at'],
  expansions: ['pinned_tweet_id'],
  requestOptions: { raw: true }
});

// ✅ Easy to add new options without breaking existing code
const posts = await client.posts.getById('12345', {
  tweetFields: ['text', 'created_at', 'public_metrics'],
  expansions: ['author_id'],
  userFields: ['name', 'username']
});

// ✅ No need to pass undefined for unused parameters
const simpleUser = await client.users.getById('12345'); // Just the ID
```

### Benefits

- **Named parameters**: No more positional parameter confusion
- **Optional by default**: Only specify what you need
- **Type safety**: Full TypeScript support with autocomplete
- **Future-proof**: Adding new options won't break existing code
- **Readable**: Clear intent at the call site

## Importing Types

All types are available directly from the main SDK import - no need to import from separate paths:

```typescript
// ✅ All types available from main import
import { 
  Client, 
  type ClientConfig,
  type ApiResponse,
  type PostsGetByIdResponse,
  type UsersGetMeResponse,
  type UsersGetByIdResponse
} from 'x-api-sdk';

// ❌ No need for separate imports like this:
// import type { PostsGetByIdResponse } from 'x-api-sdk/src/posts/models.js';
// import type { UsersGetMeResponse } from 'x-api-sdk/src/users/models.js';
```

## Authentication

The SDK supports multiple authentication methods:

### Bearer Token (App-only)
```typescript
import { Client } from 'x-api-sdk';

const client = new Client({
    bearerToken: 'your-bearer-token'
});

const user = await client.users.getById('12345');

console.log(user.data);
```

### OAuth2.0 (User-context) - With Client Secret
```typescript
import { Client, OAuth2 } from 'x-api-sdk';

const oauth2 = new OAuth2({
   clientId: 'your-client-id',
   clientSecret: 'your-client-secret', // Server-side applications
   redirectUri: 'your-redirect-uri',
   scope: ['tweet.read', 'users.read']
});

const authUrl = await oauth2.getAuthorizationUrl();

const tokens = await oauth2.exchangeCode('authorization-code');

const client = new Client({
   accessToken: tokens.access_token
});
```

### OAuth2.0 (User-context) - Public Client
```typescript
import { Client, OAuth2 } from 'x-api-sdk';

const oauth2 = new OAuth2({
   clientId: 'your-client-id',
   // No clientSecret - automatically treated as public client
   redirectUri: 'your-redirect-uri',
   scope: ['tweet.read', 'users.read']
});

const authUrl = await oAuth2.getAuthorizationUrl();

const tokens = await oauth2.exchangeCode('authorization-code');

const client = new Client({
   accessToken: tokens.access_token
});
```

### OAuth2.0 with PKCE (Recommended for Public Clients)
```typescript
import { Client, OAuth2, generateCodeVerifier, generateCodeChallenge } from 'x-api-sdk';

const oauth2 = new OAuth2({
   clientId: 'your-client-id',
   // No clientSecret - automatically treated as public client
   redirectUri: 'your-redirect-uri',
   scope: ['tweet.read', 'users.read']
});

// Generate PKCE parameters
const codeVerifier = generateCodeVerifier();
const codeChallenge = await generateCodeChallenge(codeVerifier);

// Build authorization URL with PKCE parameters
const authUrl = `https://x.com/i/oauth2/authorize?` + new URLSearchParams({
   response_type: 'code',
   client_id: 'your-client-id',
   redirect_uri: 'your-redirect-uri',
   scope: 'tweet.read users.read',
   code_challenge: codeChallenge,
   code_challenge_method: 'S256'
}).toString();

// After user authorizes and you get the authorization code:
const tokens = await oauth2.exchangeCode('authorization-code', codeVerifier);

const client = new Client({
   accessToken: tokens.access_token
});
```

### 3-legged OAuth (OAuth1.0)
```typescript
import { Client, OAuth1 } from 'x-api-sdk';

const oauth1 = new OAuth1({
   apiKey: 'your-consumer-key',
   apiSecret: 'your-consumer-secret',
   callback: 'your-callback-url',
});

const authUrl = oauth1.getAuthorizationUrl();

// Or To use Log in with X / Sign in with X, you can set the loginWithX parameter when getting the authorization URL:
const authUrl = oauth1.getAuthorizationUrl(loginWithX=true);

// This can be used to have a user authenticate your app. Once they've done so, they'll be redirected to the Callback / Redirect URI / URL you provided, with oauth_token and oauth_verifier parameters.
// You can then use the verifier to get the access token and secret:
const { accessToken, accessTokenSecret } = await oauth1.getAccessToken("Verifier (oauth_verifier) here");

// If you need to reinitialize OAuth1, you can set the request token and secret afterward, before using the verifier to get the access token and secret:
const oauthToken = oauth1.requestToken.oauthToken;
const oauthTokenSecret = oauth1.requestToken.oauthTokenSecret;

let newOauth1 = new OAuth1({
   apiKey: 'your-consumer-key',
   apiSecret: 'your-consumer-secret',
   callback: 'your-callback-url',
});

newOauth1.requestToken = {
    "oauthToken": oauthToken,
    "oauthTokenSecret": oauthTokenSecret
};

const { accessToken, accessTokenSecret } = await newOauth1.getAccessToken("Verifier (oauth_verifier) here");

// Otherwise, you can simply use the old instance of OAuth1.
// You can then use this instance of OAuth1 to initialize the client
const client = new Client(oauth1);

// You can also use the access_token and access_token_secret to initialize a new instance of OAuth1
const oauth1 = new OAuth1({
   apiKey: 'your-api-key',
   apiSecret: 'your-api-secret',
   accessToken: 'your-access-token',
   accessTokenSecret: 'your-access-token-secret',
});

const client = new Client(oauth1);
```

### PIN-based OAuth (OAuth1.0)
The PIN-based OAuth flow can be used by setting the callback parameter to "oob":

```typescript
let oauth1 = new OAuth1({
   apiKey: 'your-api-key',
   apiSecret: 'your-api-secret',
   callback: 'oob',
});

// You can then get the authorization URL the same way:
const authUrl = oauth1.getAuthorizationUrl();

// When the user authenticates with this URL, they'll be provided a PIN. You can retrieve this PIN from the user to use as the verifier:
const verifier = (get user verifier from user input);

const { accessToken, accessTokenSecret } = await oauth1.getAccessToken(verifier);

// You can then use the instance of OAuth1 and/or the accessToken and accessTokenSecret.
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
// Get tweet by ID
const tweet = await client.tweets.getById('12345', ['id', 'text', 'author_id']);

// Search recent tweets
const searchResults = await client.tweets.tweetsRecentSearch('query', 10);

// Post a tweet
const newTweet = await client.tweets.postTweets({
  text: 'Hello, world!'
});

// Get user's tweets
const userTweets = await client.tweets.usersIdTweets('12345', 100);
```

### Lists API
```typescript
// Get list by ID
const list = await client.lists.getById('12345', ['id', 'name', 'description']);

// Get list members
const members = await client.lists.getMembers('12345', 100);

// Create a new list
const newList = await client.lists.postLists({
  name: 'My List',
  description: 'A list of interesting accounts'
});
```

### Media API
```typescript
// Upload media
const media = await client.media.mediaUpload({
  media_category: 'tweet_image',
  media_data: 'base64_encoded_image_data'
});

// Get media by ID
const mediaInfo = await client.media.getById('12345');
```

## Advanced Features

### Pagination
Many API endpoints support pagination with rich functionality:

```typescript
// Get all followers (handles pagination automatically)
const followersPaginator = client.users.getFollowers('12345', {
  maxResults: 100,
  userFields: ['id', 'name', 'username']
});

// Iterate through all followers
for await (const follower of followersPaginator) {
  console.log('Follower:', follower.name);
}

// Access fetched items directly
console.log('Total followers:', followersPaginator.users.length);

// Check pagination status
console.log('Done:', followersPaginator.done);
console.log('Rate limited:', followersPaginator.rateLimited);

// Manual pagination control
while (!followersPaginator.done) {
  await followersPaginator.fetchNext();
  console.log('Fetched more followers:', followersPaginator.users.length);
}

// Get next page as separate instance
const nextPage = await followersPaginator.next();
console.log('Next page followers:', nextPage.users);

// Fetch specific number of additional items
await followersPaginator.fetchLast(500); // Fetch up to 500 more items

// Access metadata and includes
console.log('Meta:', followersPaginator.meta);
console.log('Includes:', followersPaginator.includes);
console.log('Errors:', followersPaginator.errors);
```

### Error Handling
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

### Custom Headers
You can add custom headers to your requests:

```typescript
const client = new Client({
  bearerToken: 'your-token',
  headers: {
    'X-Custom-Header': 'custom-value'
  }
});
```

## Configuration

The client supports various configuration options:

```typescript
const client = new Client({
  baseUrl: 'https://api.x.com',
  bearerToken: 'your-bearer-token',
  timeout: 30000,
  retry: true,
  maxRetries: 3,
  userAgent: 'my-app/1.0.0'
});
```

## Authentication Validation

The SDK automatically validates that you have the correct authentication method for each API endpoint based on the OpenAPI specification:

```typescript
// ✅ This will work - bearer token is valid for public endpoints
const client = new Client({ bearerToken: 'your-bearer-token' });
const user = await client.users.getById('12345');

// ❌ This will throw an error - OAuth1 required for this endpoint
const client = new Client({ bearerToken: 'your-bearer-token' });
await client.users.getMe(); // Throws: "Authentication required for getMe. Required: UserToken. Available: bearer_token."

// ✅ This will work - OAuth1 is configured
const oauth1 = new OAuth1({ /* ... */ });
const client = new Client(oauth1);
const me = await client.users.getMe();
```

### Available Authentication Types

- **`bearer_token`** - App-only OAuth2.0 (Bearer Token)
- **`oauth2_user_context`** - OAuth2.0 User Context (Access Token)
- **`oauth1`** - OAuth1.0a (User Context)

### Error Messages

When authentication validation fails, you'll get clear error messages:

```
Authentication required for getMe. 
Required: UserToken. 
Available: bearer_token. 
Please configure the appropriate authentication method.
```

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

## Features

- 🌐 **Zero-config polyfills** - works in Node.js and browsers automatically
- 🔒 **Multiple authentication methods** - Bearer token, OAuth2.0, and OAuth1.0a
- 🛡️ **Automatic authentication validation** - validates correct auth method for each endpoint
- 🎯 **Ergonomic API design** - returns parsed body by default, raw wrapper when needed
- 📝 **Options object pattern** - named parameters for better readability and maintainability
- 🎯 **Function overloading** - exact TypeScript types based on `raw` option, no runtime checking needed
- 📄 **Comprehensive API coverage** - all X API endpoints
- 🚨 **Robust error handling** with detailed error messages
- 📦 **Tree-shakeable** - only import what you use
- ⚡ **Minimal dependencies** - lightweight and fast
- 🔧 **Auto-generated** - always up to date with the latest API changes

## License

This project is licensed under the MIT License - see the LICENSE file for details.
