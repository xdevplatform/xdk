# Mintlify Documentation Processing

This directory contains scripts and tools for processing the X API SDK documentation for deployment on Mintlify.

## Quick Start

```bash
# Generate Mintlify-ready documentation
npm run docs:mintlify
```

This will:
1. Generate TypeDoc documentation
2. Process markdown files for Mintlify
3. Create proper frontmatter and navigation
4. Output to `mintlify-docs/` directory

## What Gets Generated

### File Structure
```
mintlify-docs/
├── README.md                 # Main landing page
├── mintlify.json            # Mintlify configuration
├── DEPLOYMENT.md            # Deployment instructions
├── assets/                  # Static assets
│   └── favicon.svg         # Placeholder favicon
└── reference/              # API reference pages
    ├── Client.md           # Main client documentation
    ├── Paginator.md        # Pagination utilities
    ├── UsersClient.md      # Users API client
    └── ...                 # 300+ other API pages
```

### Key Features

**🎨 Professional Styling**
- X/Twitter brand colors (#1DA1F2)
- Proper typography and spacing
- Code syntax highlighting
- Responsive design

**📚 Comprehensive Navigation**
- Organized by categories (Getting Started, Core Features, API Reference)
- Grouped by functionality (Clients, Paginators, Streaming, Types)
- Search functionality
- Cross-references between pages

**🔧 Mintlify Integration**
- Proper frontmatter for all pages
- Category and tag organization
- SEO-friendly URLs
- GitHub integration ready

## Deployment

### Option 1: GitHub Repository (Recommended)
1. Copy the `mintlify-docs/` folder to your Mintlify GitHub repository
2. Update `mintlify.json` with your project details:
   - `name`: Your project name
   - `logo`: Path to your logo files
   - `colors`: Your brand colors
   - `topbarLinks`: Your GitHub repository URL
3. Push to your main branch
4. Mintlify will automatically deploy

### Option 2: Direct Upload
1. Zip the `mintlify-docs/` folder
2. Upload to Mintlify dashboard
3. Configure your domain and settings

## Customization

### Branding
Edit `mintlify.json` to customize:
- Colors and logo
- Navigation structure
- Topbar links
- Footer social links

### Content
- Edit individual markdown files in `reference/`
- Add custom pages in the root directory
- Include images and diagrams in `assets/`

### Navigation
Modify the `navigation` array in `mintlify.json` to:
- Reorder pages
- Create custom groupings
- Add external links

## Script Details

### `process-for-mintlify.js`
Main processing script that:
- Generates TypeDoc documentation
- Processes markdown files
- Adds Mintlify frontmatter
- Creates navigation structure
- Generates configuration files

### Configuration
The script uses these mappings:
- **Categories**: Getting Started, Core Features, API Reference, Authentication, Utilities
- **Method Groups**: Users, Posts, Lists, Bookmarks, Communities, etc.
- **Tags**: Automatic tagging based on content type

## Advanced Features

### Search
Mintlify provides automatic search across all documentation.

### Code Examples
All code examples are syntax-highlighted and copy-paste ready.

### API Explorer
Mintlify can generate an interactive API explorer from your OpenAPI spec.

### Analytics
Enable Mintlify analytics to track usage and popular pages.

## Troubleshooting

### Common Issues
1. **Missing files**: Ensure TypeDoc generation completed successfully
2. **Broken links**: Check that all reference files were processed
3. **Navigation issues**: Verify `mintlify.json` structure

### Debug Mode
Add `console.log` statements to `process-for-mintlify.js` to debug processing issues.

## Support

- [Mintlify Documentation](https://mintlify.com/docs)
- [Mintlify Discord](https://discord.gg/6W7x5n4S3x)
- [Mintlify GitHub](https://github.com/mintlify/mintlify)

## Examples

### Before (TypeDoc)
```markdown
# Class: Client
Main client class for the X API
```

### After (Mintlify)
```markdown
---
title: "Client"
description: "Main client class for the X API"
category: "Getting Started"
tags: ["client"]
---

# Client

Main client class for the X API
```

The processed documentation is ready for professional deployment on Mintlify! 🚀
