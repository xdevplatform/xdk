import { Client, OAuth1 } from 'x-api-sdk';

async function testOAuth1() {
    try {
        console.log('🔧 Testing OAuth1 signature generation...\n');
        
        const oauth1 = new OAuth1({
            apiKey: 'XIS9eNeCsJKzBvF7Fg6vWflXO',
            apiSecret: '9jzr6n4l8tvvvV2wyctAQFATNws2JDEYj8XDOYY6uMFvu1IkHX',
            accessToken: '1716450569358098432-9SAPOATAh9xN88K4cvMjBZfHVxfUMS',
            accessTokenSecret: 'MIRy56xmBCkQlAkFT5dDLGoRKCZruX5jCWZg6IERReIsM',
        });

        console.log('✅ OAuth1 instance created');
        console.log('📝 Access Token:', oauth1.accessToken?.accessToken);
        console.log('🔑 Access Token Secret:', oauth1.accessToken?.accessTokenSecret);
        
        // Test building a request header
        const method = 'GET';
        const url = 'https://api.x.com/2/tweets/20';
        const body = '';
        
        console.log('\n🔍 Building OAuth1 header for:');
        console.log('  Method:', method);
        console.log('  URL:', url);
        console.log('  Body:', body);
        
        const authHeader = await oauth1.buildRequestHeader(method, url, body);
        console.log('\n✅ Generated OAuth1 Header:');
        console.log(authHeader);
        
        // Now test with the client
        console.log('\n🚀 Testing with Client...');
        const client = new Client(oauth1);
        
        console.log('✅ Client created with OAuth1');
        
        // Make a simple request to see what happens
        console.log('\n📡 Making API request...');
        const res = await client.posts.getById('20');
        
        console.log('✅ API request successful!');
        console.log('📊 Response:', res);
        
    } catch (error) {
        console.error('\n❌ Error occurred:');
        console.error('Message:', error.message);
        console.error('Status:', error.status);
        console.error('Stack:', error.stack);
        
        if (error.response) {
            console.error('Response details:', {
                status: error.response.status,
                statusText: error.response.statusText,
                headers: Object.fromEntries(error.response.headers.entries())
            });
        }
    }
}

testOAuth1().catch(console.error); 