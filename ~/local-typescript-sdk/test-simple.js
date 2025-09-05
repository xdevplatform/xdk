import { Client, OAuth1 } from 'x-api-sdk';

async function testSimple() {
    try {
        console.log('🔧 Testing simple OAuth1 request...\n');
        
        const oauth1 = new OAuth1({
            apiKey: 'XIS9eNeCsJKzBvF7Fg6vWflXO',
            apiSecret: '9jzr6n4l8tvvvV2wyctAQFATNws2JDEYj8XDOYY6uMFvu1IkHX',
            accessToken: '1716450569358098432-9SAPOATAh9xN88K4cvMjBZfHVxfUMS',
            accessTokenSecret: 'MIRy56xmBCkQlAkFT5dDLGoRKCZruX5jCWZg6IERReIsM',
        });

        console.log('✅ OAuth1 instance created');
        
        // Test building a request header
        const method = 'GET';
        const url = 'https://api.x.com/2/tweets/20';
        const body = '';
        
        console.log('🔍 Building OAuth1 header...');
        const authHeader = await oauth1.buildRequestHeader(method, url, body);
        console.log('✅ Generated OAuth1 Header:');
        console.log(authHeader);
        
        // Now test with the client
        console.log('\n🚀 Testing with Client...');
        const client = new Client(oauth1);
        
        console.log('✅ Client created with OAuth1');
        
        // Make a simple request to see what happens
        console.log('\n📡 Making API request...');
        
        // Try a different endpoint first
        console.log('Trying users/me endpoint...');
        try {
            const userRes = await client.users.getMe();
            console.log('✅ Users/me successful:', userRes);
        } catch (userError) {
            console.log('❌ Users/me failed:', userError.message);
        }
        
        // Now try the posts endpoint
        console.log('\nTrying posts endpoint...');
        const res = await client.posts.getById('20');
        
        console.log('✅ API request successful!');
        console.log('📊 Response:', res);
        
    } catch (error) {
        console.error('\n❌ Error occurred:');
        console.error('Message:', error.message);
        console.error('Status:', error.status);
        
        if (error.response) {
            console.error('Response details:', {
                status: error.response.status,
                statusText: error.response.statusText,
                headers: Object.fromEntries(error.response.headers.entries())
            });
            
            try {
                const errorBody = await error.response.text();
                console.error('Response Body:', errorBody);
            } catch (e) {
                console.error('Could not read response body:', e.message);
            }
        }
    }
}

testSimple().catch(console.error); 