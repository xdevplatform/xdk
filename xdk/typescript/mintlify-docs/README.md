---
title: "TypeScript SDK"
description: "TypeScript SDK for the X API with comprehensive pagination, authentication, and streaming support."
---

# TypeScript SDK

A comprehensive TypeScript SDK for the X API (formerly Twitter API) with advanced features including:

- **🔄 Smart Pagination**: Automatic pagination with async iteration support
- **🔐 Multiple Authentication**: OAuth1, OAuth2, and Bearer token support
- **📡 Real-time Streaming**: Event-driven streaming with automatic reconnection
- **📚 Full Type Safety**: Complete TypeScript definitions for all endpoints
- **🎯 20+ API Modules**: Users, Posts, Lists, Bookmarks, Communities, and more

## Quick Start

```typescript
import { Client } from 'x-api-sdk';

const client = new Client({
  bearerToken: 'your-bearer-token'
});

// Get user information
const user = await client.users.getUser('783214');

// Get followers with pagination
const followers = await client.users.getFollowers('783214', {
  maxResults: 10,
  userFields: ['id', 'name', 'username']
});

// Iterate through followers
for await (const follower of followers) {
  console.log(follower.username);
}
```

## Installation

```bash
npm install x-api-sdk
```

## Features

### 🔄 Smart Pagination
The SDK provides intelligent pagination that automatically handles API pagination tokens and provides multiple ways to iterate through data:

```typescript
// Automatic iteration
for await (const follower of client.users.getFollowers('783214')) {
  console.log(follower.username);
}

// Manual control
const followers = await client.users.getFollowers('783214');
await followers.fetchNext();
console.log(followers.items.length);
```

### 📡 Real-time Streaming
Connect to real-time streams with automatic reconnection and error handling:

```typescript
const stream = await client.stream.postsFirehose({
  tweetFields: ['id', 'text', 'created_at']
});

stream.on('data', (tweet) => {
  console.log('New tweet:', tweet.text);
});
```

### 🔐 Authentication
Support for all X API authentication methods:

```typescript
// Bearer token
const client = new Client({ bearerToken: 'your-token' });

// OAuth2
const client = new Client({ accessToken: 'your-access-token' });

// OAuth1
const client = new Client({ oauth1: oauth1Instance });
```

## API Reference

Explore the complete API reference in the sidebar. The SDK includes clients for all major X API endpoints:

- **Users**: User management, followers, following, search
- **Posts**: Tweet management, search, analytics
- **Lists**: List creation, management, members
- **Bookmarks**: Bookmark management and retrieval
- **Communities**: Community management and moderation
- **Spaces**: Live audio spaces management
- **Media**: Media upload and management
- **Webhooks**: Webhook management and validation
- **Compliance**: Data compliance and deletion
- **Usage**: API usage and rate limit information

## Support

- **GitHub**: [https://github.com/your-org/x-api-sdk](https://github.com/your-org/x-api-sdk)
- **Documentation**: This site
- **Issues**: [Report issues on GitHub](https://github.com/your-org/x-api-sdk/issues)

## License

MIT License - see the [GitHub repository](https://github.com/your-org/x-api-sdk) for details.
