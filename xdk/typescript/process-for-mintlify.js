#!/usr/bin/env node

import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

console.log('🚀 Processing X API SDK Documentation for Mintlify...');

// Mintlify configuration
const MINTLIFY_CONFIG = {
  outputDir: 'mintlify-docs',
  baseUrl: 'https://your-mintlify-site.com', // Update this with your actual Mintlify URL
  title: 'X API SDK v2.152',
  description: 'TypeScript SDK for the X API with comprehensive pagination, authentication, and streaming support.',
  version: '2.152',
  githubUrl: 'https://github.com/your-org/x-api-sdk', // Update with your actual GitHub URL
  logo: {
    light: '/logo-light.svg',
    dark: '/logo-dark.svg'
  }
};

// Category mappings for better organization
const CATEGORY_MAPPINGS = {
  'Client': 'Getting Started',
  'Pagination': 'Core Features',
  'Streaming': 'Core Features',
  'Authentication': 'Authentication',
  'Models': 'API Reference',
  'Utilities': 'Utilities',
  'Other': 'API Reference'
};

// Method groupings for better navigation
const METHOD_GROUPS = {
  'users': 'Users',
  'posts': 'Posts',
  'lists': 'Lists',
  'bookmarks': 'Bookmarks',
  'communities': 'Communities',
  'spaces': 'Spaces',
  'trends': 'Trends',
  'media': 'Media',
  'webhooks': 'Webhooks',
  'compliance': 'Compliance',
  'usage': 'Usage',
  'general': 'General',
  'direct_messages': 'Direct Messages',
  'account_activity': 'Account Activity',
  'activity': 'Activity',
  'connections': 'Connections',
  'connection': 'Connection',
  'community_notes': 'Community Notes',
  'aaasubscriptions': 'AAA Subscriptions',
  'stream': 'Streaming'
};

// Helper function to generate Mintlify frontmatter
function generateFrontmatter(title, description, category = 'API Reference', tag = 'api', sidebarTitle = null) {
  // Clean up titles by removing generic type parameters for better readability
  const cleanTitle = (str) => {
    if (typeof str !== 'string') return str;
    return str
      .replace(/<.*?>/g, '')  // Remove all generic type parameters
      .replace(/Interface:\s+/, '')  // Remove "Interface:" prefix
      .replace(/Class:\s+/, '')  // Remove "Class:" prefix
      .replace(/\\/g, '')  // Remove any backslashes
      .replace(/\s+/g, ' ')  // Normalize whitespace
      .trim();
  };

  const frontmatter = {
    title: cleanTitle(title),
    description: cleanTitle(description)
  };
  
  if (sidebarTitle) {
    frontmatter.sidebarTitle = cleanTitle(sidebarTitle);
  }
  
  // Use simple quoted strings for clean frontmatter
  return `---
title: "${cleanTitle(title)}"
description: "${cleanTitle(description)}"
${sidebarTitle ? `sidebarTitle: "${cleanTitle(sidebarTitle)}"` : ''}
---

`;
}

// Helper function to clean and format markdown content
function processMarkdownContent(content, title) {
  // Remove TypeDoc-specific elements that don't work well in Mintlify
  content = content
    // Remove TypeDoc navigation elements
    .replace(/\[\[include:.*?\]\]/g, '')
    .replace(/\[\[include-start:.*?\]\]/g, '')
    .replace(/\[\[include-end:.*?\]\]/g, '')
    
    // Fix code block formatting
    .replace(/```typescript\n/g, '```typescript\n')
    .replace(/```javascript\n/g, '```javascript\n')
    
    // Fix internal links (convert to Mintlify format with xdks/typescript prefix)
    .replace(/\[([^\]]+)\]\(\.\/([^)]+)\)/g, (match, text, link) => {
      // Convert relative links to proper Mintlify paths
      const cleanLink = link.replace('.md', '').replace('classes/', '').replace('interfaces/', '');
      return `[${text}](/xdks/typescript/reference/${cleanLink})`;
    })
    
    // Fix method signatures
    .replace(/### (.*?)\(/g, '### `$1`(')
    
    // Add proper spacing
    .replace(/\n\n\n+/g, '\n\n')
    
    // Fix parameter formatting
    .replace(/\*\*@param\s+(\w+)\s+(.*?)\*\*/g, '**@param** `$1` - $2')
    .replace(/\*\*@returns\s+(.*?)\*\*/g, '**@returns** $1')
    .replace(/\*\*@throws\s+(.*?)\*\*/g, '**@throws** $1');

  return content;
}

// Helper function to determine category from file path
function getCategoryFromPath(filePath) {
  if (filePath.includes('classes/Client')) return 'Getting Started';
  if (filePath.includes('classes/Paginator')) return 'Core Features';
  if (filePath.includes('stream_client')) return 'Core Features';
  if (filePath.includes('interfaces/')) return 'API Reference';
  
  // Check for specific modules
  for (const [module, category] of Object.entries(METHOD_GROUPS)) {
    if (filePath.includes(module)) {
      return 'API Reference';
    }
  }
  
  return 'API Reference';
}

// Helper function to generate a single tag from file path
function generateTag(filePath, title) {
  if (filePath.includes('Paginator')) return 'pagination';
  if (filePath.includes('Client')) return 'client';
  if (filePath.includes('stream')) return 'streaming';
  if (filePath.includes('auth')) return 'authentication';
  if (filePath.includes('interface')) return 'types';
  
  // Add module-specific tags
  for (const module of Object.keys(METHOD_GROUPS)) {
    if (filePath.includes(module)) {
      return module.replace('_', '-');
    }
  }
  
  return 'api';
}

// Main processing function
async function processDocs() {
  try {
    // First, try to generate the documentation, but skip if it fails (e.g., Node version mismatch)
    console.log('📚 Generating documentation...');
    try {
      execSync('npm run docs:build', { stdio: 'inherit' });
    } catch (error) {
      console.log('⚠️  TypeDoc generation failed (likely Node version issue), using existing docs if available...');
      if (!fs.existsSync('docs') || fs.readdirSync('docs').length === 0) {
        throw new Error('No documentation found and TypeDoc generation failed. Please upgrade Node.js to 16+ or generate docs manually.');
      }
      console.log('✅ Using existing documentation files');
    }
    
    // Create output directory
    const outputDir = MINTLIFY_CONFIG.outputDir;
    if (fs.existsSync(outputDir)) {
      fs.rmSync(outputDir, { recursive: true });
    }
    fs.mkdirSync(outputDir, { recursive: true });
    
    // Create subdirectories with xdks/typescript prefix
    fs.mkdirSync(path.join(outputDir, 'xdks', 'typescript', 'reference'), { recursive: true });
    fs.mkdirSync(path.join(outputDir, 'xdks', 'typescript', 'guides'), { recursive: true });
    fs.mkdirSync(path.join(outputDir, 'xdks', 'typescript', 'assets'), { recursive: true });
    
    console.log('📝 Processing markdown files...');
    
    // Process all markdown files recursively
    const docsDir = 'docs';
    function getAllFiles(dir, fileList = []) {
      const files = fs.readdirSync(dir);
      files.forEach(file => {
        const filePath = path.join(dir, file);
        if (fs.statSync(filePath).isDirectory()) {
          getAllFiles(filePath, fileList);
        } else if (file.endsWith('.md')) {
          // Store relative path from docsDir
          fileList.push(path.relative(docsDir, filePath));
        }
      });
      return fileList;
    }
    const files = getAllFiles(docsDir);
    
    const processedFiles = [];
    const navigation = {
      'Getting Started': [],
      'Core Features': [],
      'API Reference': [],
      'Authentication': [],
      'Utilities': []
    };
    
    for (const file of files) {
      if (file.endsWith('.md') && file !== 'README.md') {
        const filePath = path.join(docsDir, file);
        const content = fs.readFileSync(filePath, 'utf8');
        
        // Extract title from content or filename
        let title = path.basename(file, '.md');
        const titleMatch = content.match(/^#\s+(.+)$/m);
        if (titleMatch) {
          title = titleMatch[1];
        }
        
        // Clean up title
        title = title
          .replace(/^Class\s+/, '')
          .replace(/^Interface\s+/, '')
          .replace(/^Type\s+/, '')
          .replace(/([A-Z])/g, ' $1')
          .trim();
        
        const category = getCategoryFromPath(file);
        const tag = generateTag(file, title);
        const processedContent = processMarkdownContent(content, title);
        
    // Generate frontmatter with sidebarTitle
    const frontmatter = generateFrontmatter(title, `Documentation for ${title}`, category, tag, title);
        const finalContent = frontmatter + processedContent;
        
        // Determine output path with xdks/typescript prefix
        let outputPath;
        if (file.includes('classes/')) {
          const className = path.basename(file, '.md');
          outputPath = path.join(outputDir, 'xdks', 'typescript', 'reference', `${className}.mdx`);
        } else if (file.includes('interfaces/')) {
          const interfaceName = path.basename(file, '.md');
          outputPath = path.join(outputDir, 'xdks', 'typescript', 'reference', `${interfaceName}.mdx`);
        } else {
          const baseName = path.basename(file, '.md');
          outputPath = path.join(outputDir, 'xdks', 'typescript', 'reference', `${baseName}.mdx`);
        }
        
        // Write processed file
        fs.writeFileSync(outputPath, finalContent);
        processedFiles.push({
          title,
          category,
          path: outputPath,
          originalPath: file
        });
        
        // Add to navigation with xdks/typescript prefix
        if (navigation[category]) {
          navigation[category].push({
            title,
            url: `xdks/typescript/reference/${path.basename(outputPath, '.mdx')}`
          });
        }
      }
    }
    
    // Create high-level documentation pages
    console.log('📄 Creating high-level documentation pages...');
    
    // Overview page
    const overviewContent = `---
title: "Overview"
description: "TypeScript SDK for the X API - Comprehensive guide to getting started"
sidebarTitle: "Overview"
---

# TypeScript SDK for X API

A comprehensive TypeScript SDK for the X API (formerly Twitter API) with advanced features including smart pagination, multiple authentication methods, real-time streaming, and full type safety.

## Key Features

- **🔄 Smart Pagination**: Automatic pagination with async iteration support
- **🔐 Multiple Authentication**: OAuth1, OAuth2, and Bearer token support  
- **📡 Real-time Streaming**: Event-driven streaming with automatic reconnection
- **📚 Full Type Safety**: Complete TypeScript definitions for all endpoints
- **🎯 20+ API Modules**: Users, Posts, Lists, Bookmarks, Communities, and more

## Quick Start

\`\`\`typescript
import { Client } from '@your-org/x-api-sdk';

const client = new Client({
  bearerToken: 'your-bearer-token'
});

// Get user information
const user = await client.users.getMe();
console.log(user.data.username);
\`\`\`

## What's Next?

- [Installation Guide](/xdks/typescript/install) - Set up the SDK in your project
- [Authentication](/xdks/typescript/authentication) - Learn about different auth methods
- [Pagination](/xdks/typescript/pagination) - Master data pagination
- [Streaming](/xdks/typescript/streaming) - Real-time data streaming
- [API Reference](/xdks/typescript/reference/Client) - Complete API documentation
`;

    fs.writeFileSync(path.join(outputDir, 'xdks', 'typescript', 'overview.mdx'), overviewContent);

    // Install page
    const installContent = `---
title: "Installation"
description: "Install and set up the TypeScript SDK for X API"
sidebarTitle: "Installation"
---

# Installation

Get started with the TypeScript SDK for X API in your project.

## Install via npm

\`\`\`bash
npm install @your-org/x-api-sdk
\`\`\`

## Install via yarn

\`\`\`bash
yarn add @your-org/x-api-sdk
\`\`\`

## Install via pnpm

\`\`\`bash
pnpm add @your-org/x-api-sdk
\`\`\`

## TypeScript Support

The SDK is written in TypeScript and includes full type definitions. No additional type packages are required.

## Requirements

- Node.js 16+ 
- TypeScript 4.5+ (if using TypeScript)

## Next Steps

- [Authentication](/xdks/typescript/authentication) - Set up authentication
- [Quick Start](/xdks/typescript/overview) - Your first API call
`;

    fs.writeFileSync(path.join(outputDir, 'xdks', 'typescript', 'install.mdx'), installContent);

    // Authentication page
    const authContent = `---
title: "Authentication"
description: "Authentication methods and setup for the TypeScript SDK"
sidebarTitle: "Authentication"
---

# Authentication

The TypeScript SDK supports multiple authentication methods for different use cases.

## Bearer Token (App-Only Auth)

For read-only operations and public data access:

\`\`\`typescript
import { Client } from '@your-org/x-api-sdk';

const client = new Client({
  bearerToken: 'your-bearer-token'
});

// Get public tweets
const tweets = await client.posts.searchRecent({
  query: 'typescript'
});
\`\`\`

## OAuth 2.0 (User Context)

For user-specific operations:

\`\`\`typescript
import { Client, OAuth2Auth } from '@your-org/x-api-sdk';

const auth = new OAuth2Auth({
  clientId: 'your-client-id',
  clientSecret: 'your-client-secret',
  redirectUri: 'http://localhost:3000/callback'
});

// Get authorization URL
const authUrl = auth.getAuthorizationUrl();

// After user authorization, exchange code for token
const token = await auth.getAccessToken(authorizationCode);

const client = new Client({
  auth
});

// Access user-specific data
const user = await client.users.getMe();
\`\`\`

## OAuth 1.0a (User Context)

For legacy applications or specific use cases:

\`\`\`typescript
import { Client, OAuth1Auth } from '@your-org/x-api-sdk';

const auth = new OAuth1Auth({
  apiKey: 'your-api-key',
  apiSecret: 'your-api-secret',
  accessToken: 'user-access-token',
  accessTokenSecret: 'user-access-token-secret'
});

const client = new Client({
  auth
});
\`\`\`

## Environment Variables

Store sensitive credentials in environment variables:

\`\`\`bash
# .env
X_API_BEARER_TOKEN=your-bearer-token
X_API_CLIENT_ID=your-client-id
X_API_CLIENT_SECRET=your-client-secret
\`\`\`

\`\`\`typescript
import { Client } from '@your-org/x-api-sdk';

const client = new Client({
  bearerToken: process.env.X_API_BEARER_TOKEN
});
\`\`\`
`;

    fs.writeFileSync(path.join(outputDir, 'xdks', 'typescript', 'authentication.mdx'), authContent);

    // Pagination page
    const paginationContent = `---
title: "Pagination"
description: "Learn how to use pagination in the TypeScript SDK"
sidebarTitle: "Pagination"
---

# Pagination

The TypeScript SDK provides powerful pagination capabilities for efficiently handling large datasets.

## Basic Pagination

Most endpoints that return lists support pagination:

\`\`\`typescript
import { Client } from '@your-org/x-api-sdk';

const client = new Client({
  bearerToken: 'your-bearer-token'
});

// Get followers with pagination
const followersPaginator = await client.users.getFollowers({
  userId: 'user-id',
  maxResults: 100
});

// Access pagination metadata
console.log('Has more pages:', !followersPaginator.done);
console.log('Next token:', followersPaginator.meta?.next_token);
\`\`\`

## Async Iteration

Iterate through all pages automatically:

\`\`\`typescript
// Get all followers
for await (const follower of followersPaginator) {
  console.log(follower.username);
}
\`\`\`

## Manual Page Control

Control pagination manually:

\`\`\`typescript
// Get first page
await followersPaginator.fetchNext();
console.log('First page:', followersPaginator.items);

// Get next page
if (!followersPaginator.done) {
  await followersPaginator.fetchNext();
  console.log('Second page:', followersPaginator.items);
}
\`\`\`

## Pagination Types

Different endpoints return different paginator types:

\`\`\`typescript
// User paginator for user-related endpoints
const userPaginator = await client.users.getFollowers({ userId: 'user-id' });
// userPaginator.users - array of User objects

// Post paginator for tweet/post endpoints  
const postPaginator = await client.posts.getUserTweets({ userId: 'user-id' });
// postPaginator.posts - array of Post objects

// Event paginator for DM/event endpoints
const eventPaginator = await client.directMessages.getDmEvents({ userId: 'user-id' });
// eventPaginator.events - array of DmEvent objects
\`\`\`

## Error Handling

Handle pagination errors gracefully:

\`\`\`typescript
try {
  for await (const follower of followersPaginator) {
    console.log(follower.username);
  }
} catch (error) {
  if (followersPaginator.rateLimited) {
    console.log('Rate limited, waiting...');
    // Handle rate limiting
  } else {
    console.error('Pagination error:', error);
  }
}
\`\`\`
`;

    fs.writeFileSync(path.join(outputDir, 'xdks', 'typescript', 'pagination.mdx'), paginationContent);

    // Streaming page
    const streamingContent = `---
title: "Streaming"
description: "Real-time streaming with the TypeScript SDK"
sidebarTitle: "Streaming"
---

# Streaming

The TypeScript SDK provides real-time streaming capabilities for live data feeds.

## Basic Streaming

Connect to real-time streams:

\`\`\`typescript
import { Client } from '@your-org/x-api-sdk';

const client = new Client({
  bearerToken: 'your-bearer-token'
});

// Stream tweets in real-time
const stream = await client.stream.getTweetsStream({
  tweetFields: ['created_at', 'author_id', 'text']
});

// Listen for tweets
stream.on('tweet', (tweet) => {
  console.log('New tweet:', tweet.text);
});

// Handle errors
stream.on('error', (error) => {
  console.error('Stream error:', error);
});

// Start streaming
await stream.connect();
\`\`\`

## Event-Driven Streaming

Use the event-driven approach for better control:

\`\`\`typescript
import { EventDrivenStream } from '@your-org/x-api-sdk';

const stream = new EventDrivenStream({
  endpoint: 'tweets/sample/stream',
  bearerToken: 'your-bearer-token'
});

// Set up event handlers
stream.onTweet((tweet) => {
  console.log('Tweet received:', tweet.text);
});

stream.onError((error) => {
  console.error('Stream error:', error);
});

stream.onConnect(() => {
  console.log('Connected to stream');
});

stream.onDisconnect(() => {
  console.log('Disconnected from stream');
});

// Connect to stream
await stream.connect();
\`\`\`

## Stream Management

Control stream lifecycle:

\`\`\`typescript
// Connect to stream
await stream.connect();

// Check connection status
console.log('Connected:', stream.isConnected());

// Disconnect from stream
await stream.disconnect();

// Reconnect after disconnect
await stream.reconnect();
\`\`\`

## Filtering Streams

Apply filters to streams:

\`\`\`typescript
// Stream with specific rules
const filteredStream = await client.stream.getTweetsStream({
  tweetFields: ['created_at', 'author_id', 'text'],
  expansions: ['author_id'],
  userFields: ['username', 'name']
});

// Add filtering rules
await client.stream.addRules({
  add: [
    { value: 'typescript', tag: 'typescript-tweets' },
    { value: 'javascript', tag: 'js-tweets' }
  ]
});
\`\`\`

## Error Handling

Handle streaming errors and reconnections:

\`\`\`typescript
stream.on('error', (error) => {
  if (error.code === 'ECONNRESET') {
    console.log('Connection lost, reconnecting...');
    stream.reconnect();
  } else {
    console.error('Stream error:', error);
  }
});

// Handle rate limiting
stream.on('rate_limit', (rateLimitInfo) => {
  console.log('Rate limited, backing off...');
  // Implement backoff strategy
});
\`\`\`
`;

    fs.writeFileSync(path.join(outputDir, 'xdks', 'typescript', 'streaming.mdx'), streamingContent);
    
    // Create main README.md for integration
    console.log('📄 Creating main README.md...');
    const mainReadme = `---
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

\`\`\`typescript
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
\`\`\`

## Installation

\`\`\`bash
npm install x-api-sdk
\`\`\`

## Features

### 🔄 Smart Pagination
The SDK provides intelligent pagination that automatically handles API pagination tokens and provides multiple ways to iterate through data:

\`\`\`typescript
// Automatic iteration
for await (const follower of client.users.getFollowers('783214')) {
  console.log(follower.username);
}

// Manual control
const followers = await client.users.getFollowers('783214');
await followers.fetchNext();
console.log(followers.items.length);
\`\`\`

### 📡 Real-time Streaming
Connect to real-time streams with automatic reconnection and error handling:

\`\`\`typescript
const stream = await client.stream.postsFirehose({
  tweetFields: ['id', 'text', 'created_at']
});

stream.on('data', (tweet) => {
  console.log('New tweet:', tweet.text);
});
\`\`\`

### 🔐 Authentication
Support for all X API authentication methods:

\`\`\`typescript
// Bearer token
const client = new Client({ bearerToken: 'your-token' });

// OAuth2
const client = new Client({ accessToken: 'your-access-token' });

// OAuth1
const client = new Client({ oauth1: oauth1Instance });
\`\`\`

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

- **GitHub**: [${MINTLIFY_CONFIG.githubUrl}](${MINTLIFY_CONFIG.githubUrl})
- **Documentation**: This site
- **Issues**: [Report issues on GitHub](${MINTLIFY_CONFIG.githubUrl}/issues)

## License

MIT License - see the [GitHub repository](${MINTLIFY_CONFIG.githubUrl}) for details.
`;

    fs.writeFileSync(path.join(outputDir, 'README.md'), mainReadme);
    
    // Create navigation structure for integration into existing Mintlify site
    console.log('⚙️ Creating navigation structure...');
    
    // Generate the TypeScript SDK navigation tab with groups
    const typescriptSdkNavigation = {
      tab: 'TypeScript SDK',
      hidden: true,
      pages: [
        'xdks/typescript/overview',
        'xdks/typescript/install',
        'xdks/typescript/authentication',
        'xdks/typescript/pagination',
        'xdks/typescript/streaming',
        'xdks/typescript/reference/Client',
        {
          group: 'Core Features',
          pages: navigation['Core Features'].slice(0, 5).map(item => item.url)
        },
        {
          group: 'API Clients',
          pages: navigation['API Reference'].filter(item => 
            item.title.includes('Client') && !item.title.includes('Stream')
          ).slice(0, 15).map(item => item.url)
        },
        {
          group: 'Pagination',
          pages: navigation['API Reference'].filter(item => 
            item.title.includes('Paginator')
          ).map(item => item.url)
        },
        {
          group: 'Streaming',
          pages: navigation['API Reference'].filter(item => 
            item.title.includes('Stream')
          ).slice(0, 8).map(item => item.url)
        },
        {
          group: 'Types & Interfaces',
          pages: navigation['API Reference'].filter(item => 
            !item.title.includes('Client') && 
            !item.title.includes('Paginator') && 
            !item.title.includes('Stream')
          ).slice(0, 15).map(item => item.url)
        }
      ]
    };
    
    // Create a navigation snippet file
    const navigationSnippet = `# TypeScript SDK Navigation Structure

Add this to your existing mintlify.json tabs array:

\`\`\`json
${JSON.stringify(typescriptSdkNavigation, null, 2)}
\`\`\`

## Integration Instructions

1. **Copy the navigation structure above** into your existing mintlify.json tabs array
2. **Copy the generated files** from the xdk/ directory to your Mintlify site
3. **Deploy** - Mintlify will automatically use the sidebarTitle from each file's frontmatter

## File Structure

The generated files should be placed in your Mintlify site as:
- \`xdks/typescript/reference/\` - All API reference pages
- \`xdks/typescript/guides/\` - Guide pages (currently empty)
- \`xdks/typescript/assets/\` - Static assets

## How It Works

- **Tab Structure**: The TypeScript SDK appears as a tab in your Mintlify site
- **Grouped Navigation**: Pages are organized into logical groups within the tab
- **Sidebar Titles**: Each file's frontmatter includes \`sidebarTitle\` for clean sidebar display
- **Mixed Structure**: Pages array can contain both URL strings and group objects
- **Automatic Organization**: Mintlify automatically organizes pages by their frontmatter

## Customization

You can modify the navigation by:
- Reordering the groups and URLs in the pages array
- Adding or removing specific page URLs from groups
- Adding new groups or removing existing ones
- Modifying the sidebarTitle in individual file frontmatter

## Notes

- All internal links are already configured for the /xdks/typescript/ path structure
- Page titles in the sidebar come from the \`sidebarTitle\` frontmatter field
- The tab structure provides clean separation from your other documentation
- Groups help organize related functionality for better discoverability
`;

    fs.writeFileSync(
      path.join(outputDir, 'NAVIGATION_INTEGRATION.md'), 
      navigationSnippet
    );
    
    // Also create a JSON file for easy copy-paste
    fs.writeFileSync(
      path.join(outputDir, 'typescript-sdk-navigation.json'), 
      JSON.stringify(typescriptSdkNavigation, null, 2)
    );
    
    // Create a deployment guide
    console.log('📋 Creating deployment guide...');
    const deploymentGuide = `# TypeScript SDK Integration Guide

## Integration into Existing Mintlify Site

This guide shows how to integrate the TypeScript SDK documentation into your existing Mintlify site.

### Step 1: Copy Files

1. **Copy the xdk/ directory**: Copy the entire \`xdk/\` folder to your existing Mintlify site
2. **Maintain directory structure**: Keep the \`xdks/typescript/\` structure intact

### Step 2: Update Navigation

1. **Open your existing mintlify.json**
2. **Add the TypeScript SDK tab**: Copy the content from \`typescript-sdk-navigation.json\`
3. **Insert into your tabs array**: Add it alongside your other tabs

Example:
\`\`\`json
{
  "tabs": [
    {
      "name": "Your Existing Tab",
      "url": "/your-existing-page"
    },
    // Add the TypeScript SDK tab here
    {
      "tab": "TypeScript SDK",
      "pages": [
        "xdks/typescript/reference/Client",
        {
          "group": "Core Features",
          "pages": [
            "xdks/typescript/reference/Paginator"
          ]
        },
        {
          "group": "API Clients",
          "pages": [
            "xdks/typescript/reference/UsersClient",
            "xdks/typescript/reference/PostsClient"
          ]
        }
      ]
    }
  ]
}
\`\`\`

### Step 3: Deploy

1. **Commit changes**: Add the new files to your repository
2. **Push to main branch**: Mintlify will automatically deploy the updates
3. **Verify**: Check that the TypeScript SDK section appears in your sidebar

## File Structure

\`\`\`
mintlify-docs/
├── README.md                 # Main landing page
├── mintlify.json            # Mintlify configuration
├── xdk/                     # XDK documentation root
│   └── typescript/          # TypeScript SDK documentation
│       ├── reference/       # API reference pages
│       │   ├── client.md   # Main client documentation
│       │   ├── paginator.md # Pagination utilities
│       │   ├── usersclient.md # Users API client
│       │   └── ...         # Other API clients
│       ├── guides/         # Guide pages
│       └── assets/         # Static assets (logos, images)
└── DEPLOYMENT.md            # This deployment guide
\`\`\`

## Customization

### Branding
- Update \`mintlify.json\` with your colors and logo
- Add your favicon to the \`assets/\` folder
- Update the main README.md with your specific information

### Navigation
- Modify the \`navigation\` array in \`mintlify.json\`
- Reorder pages or create custom groupings
- Add external links to your topbar

### Content
- Edit individual markdown files in \`reference/\`
- Add custom pages in the root directory
- Include images and diagrams in the \`assets/\` folder

## Advanced Features

### Search
Mintlify automatically provides search functionality across all your documentation.

### Code Examples
All code examples are syntax-highlighted and copy-paste ready.

### API Explorer
Mintlify can automatically generate an API explorer from your OpenAPI spec.

### Analytics
Enable Mintlify analytics to track usage and popular pages.

## Support

- [Mintlify Documentation](https://mintlify.com/docs)
- [Mintlify Discord](https://discord.gg/6W7x5n4S3x)
- [Mintlify GitHub](https://github.com/mintlify/mintlify)
`;

    fs.writeFileSync(path.join(outputDir, 'DEPLOYMENT.md'), deploymentGuide);
    
    // Create a simple favicon placeholder
    console.log('🎨 Creating placeholder assets...');
    const faviconSvg = `<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="32" height="32" rx="8" fill="#1DA1F2"/>
<path d="M8 12h16v8H8z" fill="white"/>
<circle cx="12" cy="16" r="2" fill="#1DA1F2"/>
<circle cx="20" cy="16" r="2" fill="#1DA1F2"/>
</svg>`;
    fs.writeFileSync(path.join(outputDir, 'xdks', 'typescript', 'assets', 'favicon.svg'), faviconSvg);
    
    console.log('✅ TypeScript SDK documentation processed successfully!');
    console.log(`📁 Output directory: ${outputDir}/`);
    console.log(`📊 Processed ${processedFiles.length} files`);
    console.log('\n🚀 Integration steps:');
    console.log('1. Copy the \'xdk/\' folder to your existing Mintlify site');
    console.log('2. Add the navigation structure from \'typescript-sdk-navigation.json\' to your mintlify.json');
    console.log('3. Push to your main branch to deploy');
    console.log('\n📋 See INTEGRATION_GUIDE.md for detailed instructions');
    console.log('📄 See NAVIGATION_INTEGRATION.md for navigation setup');
    
  } catch (error) {
    console.error('❌ Error processing documentation:', error.message);
    process.exit(1);
  }
}

// Run the processing
processDocs();
