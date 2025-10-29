# TypeScript SDK Integration Guide

## Integration into Existing Mintlify Site

This guide shows how to integrate the TypeScript SDK documentation into your existing Mintlify site.

### Step 1: Copy Files

1. **Copy the xdk/ directory**: Copy the entire `xdk/` folder to your existing Mintlify site
2. **Maintain directory structure**: Keep the `xdks/typescript/` structure intact

### Step 2: Update Navigation

1. **Open your existing mintlify.json**
2. **Add the TypeScript SDK tab**: Copy the content from `typescript-sdk-navigation.json`
3. **Insert into your tabs array**: Add it alongside your other tabs

Example:
```json
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
```

### Step 3: Deploy

1. **Commit changes**: Add the new files to your repository
2. **Push to main branch**: Mintlify will automatically deploy the updates
3. **Verify**: Check that the TypeScript SDK section appears in your sidebar

## File Structure

```
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
```

## Customization

### Branding
- Update `mintlify.json` with your colors and logo
- Add your favicon to the `assets/` folder
- Update the main README.md with your specific information

### Navigation
- Modify the `navigation` array in `mintlify.json`
- Reorder pages or create custom groupings
- Add external links to your topbar

### Content
- Edit individual markdown files in `reference/`
- Add custom pages in the root directory
- Include images and diagrams in the `assets/` folder

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
