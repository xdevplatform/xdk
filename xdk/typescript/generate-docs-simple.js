#!/usr/bin/env node

/**
 * Simple documentation generation script for X API SDK
 * 
 * This script generates documentation for the core SDK files,
 * excluding problematic stream client files.
 */

import { execSync } from 'child_process';
import { existsSync, mkdirSync } from 'fs';
import { join } from 'path';

const DOCS_DIR = 'docs';

console.log('📚 Generating X API SDK Documentation (Simple)...\n');

// Create docs directory
if (!existsSync(DOCS_DIR)) {
    mkdirSync(DOCS_DIR, { recursive: true });
}

try {
    // Generate HTML documentation for core files only
    console.log('🔨 Generating HTML documentation for core files...');
    
    const coreFiles = [
        'src/index.ts',
        'src/client.ts',
        'src/paginator.ts',
        'src/http-client.ts',
        'src/oauth2_auth.ts',
        'src/oauth1_auth.ts',
        'src/crypto_utils.ts',
        'src/users/client.ts',
        'src/posts/client.ts',
        'src/lists/client.ts',
        'src/bookmarks/client.ts',
        'src/trends/client.ts',
        'src/spaces/client.ts',
        'src/media/client.ts',
        'src/direct_messages/client.ts',
        'src/webhooks/client.ts',
        'src/communities/client.ts',
        'src/community_notes/client.ts',
        'src/compliance/client.ts',
        'src/account_activity/client.ts',
        'src/aaasubscriptions/client.ts',
        'src/connection/client.ts',
        'src/general/client.ts',
        'src/usage/client.ts'
    ].join(' ');

    execSync(`npx typedoc --entryPoints ${coreFiles} --out docs --name "X API SDK" --readme README.md --theme default --includeVersion true --excludePrivate true --excludeProtected true --excludeExternals true --excludeInternal true --searchInComments true --cleanOutputDir true`, { stdio: 'inherit' });
    
    console.log('✅ HTML documentation generated in docs/');
    console.log('\n📁 Generated documentation:');
    console.log('   • HTML docs: docs/index.html');
    console.log('\n🚀 You can now open docs/index.html in your browser to view the documentation.');

} catch (error) {
    console.error('❌ Error generating documentation:', error.message);
    process.exit(1);
}
