# TypeScript XDK

A comprehensive TypeScript SDK for the X API (formerly Twitter API) with advanced features including smart pagination, multiple authentication methods, real-time streaming, and full type safety.

## Key Features

- **🔐 Authentication**: User Context (OAuth1.0a, OAuth2.0), and App-Only (Bearer token) authentication
- **🔄 Pagination**: Automatic pagination with async iteration support
- **📡 Streaming**: Event-driven streaming with automatic reconnection
- **📚 Type Safety**: Complete TypeScript definitions for all endpoints and parameters
- **🎯 Full X API Support**: Users, Posts, Lists, Bookmarks, Communities, and more

## Install

### npm

```bash
npm install @xdevplatform/xdk
```

### yarn

```bash
yarn add @xdevplatform/xdk
```

### pnpm

```bash
pnpm add @xdevplatform/xdk
```

### TypeScript Support

The SDK is written in TypeScript and includes full type definitions. No additional type packages are required.

### Requirements

- Node.js 16+ 
- TypeScript 4.5+ (if using TypeScript)

## Quick Start

```typescript
import { 
  Client, 
  type ClientConfig,
  type UsersGetByUsernameResponse
} from '@xdevplatform/xdk';

const config: ClientConfig = { bearerToken: 'your-bearer-token' };

const client: Client = new Client(config);

async function main(): Promise<void> {
  const userResponse: UsersGetByUsernameResponse = await client.users.getByUsername('XDevelopers');
  const username: string = userResponse.data?.username!;
  console.log(username);
}

main();
```

## Authentication

The TypeScript SDK supports multiple authentication methods for different use cases.

### Bearer Token (App-Only Auth)

For read-only operations and public data access:

```typescript
import { 
  Client, 
  type ClientConfig,
  type Users
} from '@xdevplatform/xdk';

const config: ClientConfig = { bearerToken: 'your-bearer-token' };

const client: Client = new Client(config);

async function main(): Promise<void> {
  const userResponse: Users.GetByUsernameResponse = await client.users.getByUsername('XDevelopers');
  const username: string = userResponse.data?.username!;
  console.log(username);
}

main();
```

### OAuth 1.0a (User Context)

For legacy applications or specific use cases:

```typescript
import { 
  Client, 
  OAuth1,
  type OAuth1Config,
  type ClientConfig,
  type Users
} from '@xdevplatform/xdk';

const oauth1Config: OAuth1Config = {
  apiKey: 'your-api-key',
  apiSecret: 'your-api-secret',
  accessToken: 'user-access-token',
  accessTokenSecret: 'user-access-token-secret'
};

const oauth1: OAuth1 = new OAuth1(oauth1Config);

const config: ClientConfig = {
  oauth1: oauth1,
};

const client: Client = new Client(config);

async function main(): Promise<void> {
  const response: Users.GetMeResponse = await client.users.getMe();

  const me = response.data;
  console.log(me);
}

main();

```

### OAuth 2.0 (User Context)

For user-specific operations:

```typescript
import { 
  Client, 
  OAuth2,
  generateCodeVerifier,
  generateCodeChallenge,
  type OAuth2Config,
  type ClientConfig,
  type OAuth2Token
} from '@xdevplatform/xdk';

(async (): Promise<void> => {
  const oauth2Config: OAuth2Config = {
    clientId: 'your-client-id',
    clientSecret: 'your-client-secret',
    redirectUri: 'https://example.com',
    scope: ['tweet.read', 'users.read', 'offline.access'],
  };

  const oauth2: OAuth2 = new OAuth2(oauth2Config);

  const state: string = 'example-state';
  const codeVerifier: string = generateCodeVerifier();
  const codeChallenge: string = await generateCodeChallenge(codeVerifier);
  
  oauth2.setPkceParameters(codeVerifier, codeChallenge);
  
  const authUrl: string = await oauth2.getAuthorizationUrl(state);

  const tokens: OAuth2Token = await oauth2.exchangeCode(authCode, codeVerifier);

  const config: ClientConfig = {
    accessToken: tokens.access_token,
  };

  const client: Client = new Client(config);
});

```

### Environment Variables

Store sensitive credentials in environment variables:

```bash
# .env
X_API_BEARER_TOKEN=your-bearer-token
X_API_CLIENT_ID=your-client-id
X_API_CLIENT_SECRET=your-client-secret
```

```typescript
import { Client } from '@xdevplatform/xdk';

const client = new Client({ bearerToken: process.env.X_API_BEARER_TOKEN });
```

## Pagination

The SDK provides generic paginator utilities you can use with any endpoint that returns paginated responses. Methods return plain responses; you wrap them with a paginator.

### Basic Pagination

```typescript
import { Client, UserPaginator, PaginatedResponse, Schemas } from '@xdevplatform/xdk';

const client: Client = new Client({ bearerToken: 'your-bearer-token' });

// Wrap any list endpoint with proper typing
const followers: UserPaginator = new UserPaginator(
  async (token?: string): Promise<PaginatedResponse<Schemas.User>> => {
    const res = await client.users.getFollowers('<userId>', {
      maxResults: 100,
      paginationToken: token,
      userfields: ['id','name','username'],
    });
    return { 
      data: res.data ?? [], 
      meta: res.meta, 
      includes: res.includes, 
      errors: res.errors 
    };
  }
);
```

### Manual paging

```typescript
import { UserPaginator, Schemas } from '@xdevplatform/xdk';

await followers.fetchNext();          // first page
while (!followers.done) {
  await followers.fetchNext();        // subsequent pages
}

const userCount: number = followers.users.length;  // all fetched users
const firstUser: Schemas.User | undefined = followers.users[0];
const nextToken: string | undefined = followers.meta?.next_token;
```

### Async iteration

```typescript
import { Schemas } from '@xdevplatform/xdk';

for await (const user of followers) {
  const typedUser: Schemas.User = user;
  console.log(typedUser.username);  // fully typed access
}
```

### Next page as a new instance

```typescript
import { UserPaginator } from '@xdevplatform/xdk';

await followers.fetchNext();
if (!followers.done) {
  const page2: UserPaginator = await followers.next(); // independent paginator starting at next page
  await page2.fetchNext();
  console.log(page2.users.length);  // items from second page
}
```

### Error handling and rate limits

```typescript
import { UserPaginator, Schemas } from '@xdevplatform/xdk';

try {
  for await (const item of followers) {
    const user: Schemas.User = item;
    // process user...
  }
} catch (err: unknown) {
  if (followers.rateLimited) {
    console.error('Rate limited, backoff required');
    // backoff / retry later
  } else {
    console.error('Pagination error:', err);
    throw err;
  }
}
```

## Streaming

The TypeScript SDK provides real-time streaming capabilities for live data feeds.

### Basic Streaming

Connect to real-time sampled posts:

```typescript
import { Client } from '@xdevplatform/xdk';

const client: Client = new Client({ bearerToken: 'your-bearer-token' });

// 1% sampled public posts
const stream = await client.stream.postsSample({
  tweetfields: ['id','text','created_at'],
  expansions: ['author_id'],
  userfields: ['id','username','name']
});

// Listen to events
stream.on('data', (event) => {
  // event is the parsed JSON line (data/includes/matching_rules)
  console.log('New data:', event);
});

stream.on('error', (e) => console.error('Stream error:', e));
stream.on('close', () => console.log('Stream closed'));
```

### Async Iteration

Consume the stream with async iteration:

```typescript
const stream = await client.stream.postsSample();
for await (const event of stream) {
  // Each event is a parsed JSON line (data/includes/matching_rules)
  console.log(event);
}
```

### Stream Management

Control lifecycle from the event-driven stream:

```typescript
// Close the stream
stream.close();

// Auto-reconnect (if enabled by your wrapper)
// The default EventDrivenStream exposes basic reconnect hooks
```

### Error Handling

Handle streaming errors and reconnections:

```typescript
stream.on('error', (event) => {
  const err = event.error || event;
  console.error('Stream error:', err);
});

stream.on('keepAlive', () => {
  // heartbeat event
});
```