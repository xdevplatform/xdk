# TypeScript SDK Navigation Structure

Add this to your existing mintlify.json tabs array:

```json
{
  "tab": "TypeScript SDK",
  "hidden": true,
  "pages": [
    "xdks/typescript/overview",
    "xdks/typescript/install",
    "xdks/typescript/authentication",
    "xdks/typescript/pagination",
    "xdks/typescript/streaming",
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
        "xdks/typescript/reference/AccountActivityClient",
        "xdks/typescript/reference/ActivityClient",
        "xdks/typescript/reference/CommunitiesClient",
        "xdks/typescript/reference/CommunityNotesClient",
        "xdks/typescript/reference/ComplianceClient",
        "xdks/typescript/reference/ConnectionsClient",
        "xdks/typescript/reference/DirectMessagesClient",
        "xdks/typescript/reference/GeneralClient",
        "xdks/typescript/reference/HttpClient",
        "xdks/typescript/reference/ListsClient",
        "xdks/typescript/reference/MediaClient",
        "xdks/typescript/reference/PostsClient",
        "xdks/typescript/reference/SpacesClient",
        "xdks/typescript/reference/TrendsClient",
        "xdks/typescript/reference/UsageClient"
      ]
    },
    {
      "group": "Pagination",
      "pages": [
        "xdks/typescript/reference/EventPaginator",
        "xdks/typescript/reference/PostPaginator",
        "xdks/typescript/reference/UserPaginator"
      ]
    },
    {
      "group": "Streaming",
      "pages": [
        "xdks/typescript/reference/EventDrivenStream",
        "xdks/typescript/reference/StreamClient",
        "xdks/typescript/reference/ActivityStreamOptions",
        "xdks/typescript/reference/ActivityStreamResponse",
        "xdks/typescript/reference/StreamDataEvent",
        "xdks/typescript/reference/StreamErrorEvent",
        "xdks/typescript/reference/StreamGetRuleCountsResponse",
        "xdks/typescript/reference/StreamGetRuleCountsStreamingOptions"
      ]
    },
    {
      "group": "Types & Interfaces",
      "pages": [
        "xdks/typescript/reference/ApiError",
        "xdks/typescript/reference/AccountActivityCreateReplayJobResponse",
        "xdks/typescript/reference/AccountActivityCreateSubscriptionOptions",
        "xdks/typescript/reference/AccountActivityCreateSubscriptionRequest",
        "xdks/typescript/reference/AccountActivityCreateSubscriptionResponse",
        "xdks/typescript/reference/AccountActivityDeleteSubscriptionResponse",
        "xdks/typescript/reference/AccountActivityGetSubscriptionCountResponse",
        "xdks/typescript/reference/AccountActivityGetSubscriptionsResponse",
        "xdks/typescript/reference/AccountActivityValidateSubscriptionResponse",
        "xdks/typescript/reference/ActivityCreateSubscriptionOptions",
        "xdks/typescript/reference/ActivityCreateSubscriptionRequest",
        "xdks/typescript/reference/ActivityCreateSubscriptionResponse",
        "xdks/typescript/reference/ActivityDeleteSubscriptionResponse",
        "xdks/typescript/reference/ActivityGetSubscriptionsResponse",
        "xdks/typescript/reference/ActivityUpdateSubscriptionOptions"
      ]
    }
  ]
}
```

## Integration Instructions

1. **Copy the navigation structure above** into your existing mintlify.json tabs array
2. **Copy the generated files** from the xdk/ directory to your Mintlify site
3. **Deploy** - Mintlify will automatically use the sidebarTitle from each file's frontmatter

## File Structure

The generated files should be placed in your Mintlify site as:
- `xdks/typescript/reference/` - All API reference pages
- `xdks/typescript/guides/` - Guide pages (currently empty)
- `xdks/typescript/assets/` - Static assets

## How It Works

- **Tab Structure**: The TypeScript SDK appears as a tab in your Mintlify site
- **Grouped Navigation**: Pages are organized into logical groups within the tab
- **Sidebar Titles**: Each file's frontmatter includes `sidebarTitle` for clean sidebar display
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
- Page titles in the sidebar come from the `sidebarTitle` frontmatter field
- The tab structure provides clean separation from your other documentation
- Groups help organize related functionality for better discoverability
