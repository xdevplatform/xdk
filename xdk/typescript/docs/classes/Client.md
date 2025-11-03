[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / Client

# Class: Client

Main client class for the X API

This is the primary entry point for interacting with the X API. It provides
access to all API endpoints through specialized client modules and handles
authentication, request configuration, and error handling.

**`Example`**

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

## Table of contents

### Constructors

- [constructor](Client.md#constructor)

### Properties

- [baseUrl](Client.md#baseurl)
- [bearerToken](Client.md#bearertoken)
- [accessToken](Client.md#accesstoken)
- [oauth1](Client.md#oauth1)
- [headers](Client.md#headers)
- [timeout](Client.md#timeout)
- [retry](Client.md#retry)
- [maxRetries](Client.md#maxretries)
- [userAgent](Client.md#useragent)
- [httpClient](Client.md#httpclient)
- [compliance](Client.md#compliance)
- [spaces](Client.md#spaces)
- [webhooks](Client.md#webhooks)
- [activity](Client.md#activity)
- [users](Client.md#users)
- [trends](Client.md#trends)
- [communityNotes](Client.md#communitynotes)
- [directMessages](Client.md#directmessages)
- [usage](Client.md#usage)
- [accountActivity](Client.md#accountactivity)
- [lists](Client.md#lists)
- [communities](Client.md#communities)
- [media](Client.md#media)
- [connections](Client.md#connections)
- [stream](Client.md#stream)
- [general](Client.md#general)
- [posts](Client.md#posts)

### Methods

- [request](Client.md#request)
- [isTokenExpired](Client.md#istokenexpired)
- [refreshToken](Client.md#refreshtoken)
- [isAuthenticated](Client.md#isauthenticated)
- [mapSecuritySchemeToAuthTypes](Client.md#mapsecurityschemetoauthtypes)
- [validateAuthentication](Client.md#validateauthentication)
- [getAvailableAuthTypes](Client.md#getavailableauthtypes)

## Constructors

### constructor

• **new Client**(`config`): [`Client`](Client.md)

Creates a new X API client instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `config` | `any` | Configuration options for the client |

#### Returns

[`Client`](Client.md)

**`Example`**

```typescript
// Bearer token authentication
const client = new Client({
  bearerToken: 'your-bearer-token'
});

// OAuth2 authentication
const client = new Client({
  accessToken: 'your-access-token'
});

// OAuth1 authentication
const client = new Client({
  oauth1: oauth1Instance
});
```

#### Defined in

[client.ts:306](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L306)

## Properties

### baseUrl

• `Readonly` **baseUrl**: `string`

Base URL for API requests

#### Defined in

[client.ts:209](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L209)

___

### bearerToken

• `Optional` `Readonly` **bearerToken**: `string`

Bearer token for authentication

#### Defined in

[client.ts:211](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L211)

___

### accessToken

• `Optional` `Readonly` **accessToken**: `string`

OAuth2 access token

#### Defined in

[client.ts:213](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L213)

___

### oauth1

• `Optional` `Readonly` **oauth1**: `any`

OAuth1 instance for authentication

#### Defined in

[client.ts:215](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L215)

___

### headers

• `Readonly` **headers**: `Headers`

Headers for requests

#### Defined in

[client.ts:217](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L217)

___

### timeout

• `Readonly` **timeout**: `number`

Request timeout in milliseconds

#### Defined in

[client.ts:219](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L219)

___

### retry

• `Readonly` **retry**: `boolean`

Whether to automatically retry failed requests

#### Defined in

[client.ts:221](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L221)

___

### maxRetries

• `Readonly` **maxRetries**: `number`

Maximum number of retry attempts

#### Defined in

[client.ts:223](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L223)

___

### userAgent

• `Readonly` **userAgent**: `string`

User agent string

#### Defined in

[client.ts:225](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L225)

___

### httpClient

• `Readonly` **httpClient**: [`HttpClient`](HttpClient.md) = `httpClient`

HTTP client for making requests

#### Defined in

[client.ts:228](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L228)

___

### compliance

• `Readonly` **compliance**: [`ComplianceClient`](ComplianceClient.md)

compliance client

#### Defined in

[client.ts:232](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L232)

___

### spaces

• `Readonly` **spaces**: [`SpacesClient`](SpacesClient.md)

spaces client

#### Defined in

[client.ts:235](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L235)

___

### webhooks

• `Readonly` **webhooks**: [`WebhooksClient`](WebhooksClient.md)

webhooks client

#### Defined in

[client.ts:238](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L238)

___

### activity

• `Readonly` **activity**: [`ActivityClient`](ActivityClient.md)

activity client

#### Defined in

[client.ts:241](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L241)

___

### users

• `Readonly` **users**: [`UsersClient`](UsersClient.md)

users client

#### Defined in

[client.ts:244](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L244)

___

### trends

• `Readonly` **trends**: [`TrendsClient`](TrendsClient.md)

trends client

#### Defined in

[client.ts:247](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L247)

___

### communityNotes

• `Readonly` **communityNotes**: [`CommunityNotesClient`](CommunityNotesClient.md)

community notes client

#### Defined in

[client.ts:250](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L250)

___

### directMessages

• `Readonly` **directMessages**: [`DirectMessagesClient`](DirectMessagesClient.md)

direct messages client

#### Defined in

[client.ts:253](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L253)

___

### usage

• `Readonly` **usage**: [`UsageClient`](UsageClient.md)

usage client

#### Defined in

[client.ts:256](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L256)

___

### accountActivity

• `Readonly` **accountActivity**: [`AccountActivityClient`](AccountActivityClient.md)

account activity client

#### Defined in

[client.ts:259](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L259)

___

### lists

• `Readonly` **lists**: [`ListsClient`](ListsClient.md)

lists client

#### Defined in

[client.ts:262](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L262)

___

### communities

• `Readonly` **communities**: [`CommunitiesClient`](CommunitiesClient.md)

communities client

#### Defined in

[client.ts:265](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L265)

___

### media

• `Readonly` **media**: [`MediaClient`](MediaClient.md)

media client

#### Defined in

[client.ts:268](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L268)

___

### connections

• `Readonly` **connections**: [`ConnectionsClient`](ConnectionsClient.md)

connections client

#### Defined in

[client.ts:271](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L271)

___

### stream

• `Readonly` **stream**: [`StreamClient`](StreamClient.md)

stream client

#### Defined in

[client.ts:274](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L274)

___

### general

• `Readonly` **general**: [`GeneralClient`](GeneralClient.md)

general client

#### Defined in

[client.ts:277](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L277)

___

### posts

• `Readonly` **posts**: [`PostsClient`](PostsClient.md)

posts client

#### Defined in

[client.ts:280](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L280)

## Methods

### request

▸ **request**\<`T`\>(`method`, `path`, `options?`): `Promise`\<`T`\>

Make an authenticated request to the X API

This method handles authentication, request formatting, and error handling
for all API requests. It automatically adds the appropriate authentication
headers based on the client configuration.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `method` | `string` | HTTP method (GET, POST, PUT, DELETE, etc.) |
| `path` | `string` | API endpoint path (e.g., '/2/users/by/username/username') |
| `options` | [`RequestOptions`](../interfaces/RequestOptions.md) | Request options including timeout, headers, and body |

#### Returns

`Promise`\<`T`\>

Promise that resolves to the parsed response data

**`Example`**

```typescript
// GET request
const user = await client.request('GET', '/2/users/by/username/username', {
  timeout: 5000
});

// POST request with body
const result = await client.request('POST', '/2/tweets', {
  body: JSON.stringify({ text: 'Hello World!' })
});
```

**`Throws`**

When the API returns an error response

#### Defined in

[client.ts:400](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L400)

___

### isTokenExpired

▸ **isTokenExpired**(): `boolean`

Check if the OAuth2 token is expired

#### Returns

`boolean`

#### Defined in

[client.ts:494](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L494)

___

### refreshToken

▸ **refreshToken**(): `Promise`\<`void`\>

Refresh the OAuth2 token

#### Returns

`Promise`\<`void`\>

#### Defined in

[client.ts:502](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L502)

___

### isAuthenticated

▸ **isAuthenticated**(): `boolean`

Get the current authentication status

#### Returns

`boolean`

#### Defined in

[client.ts:509](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L509)

___

### mapSecuritySchemeToAuthTypes

▸ **mapSecuritySchemeToAuthTypes**(`securitySchemeName`): `string`[]

Map OpenAPI security scheme names to internal authentication types

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `securitySchemeName` | `string` | The security scheme name from OpenAPI |

#### Returns

`string`[]

Array of internal authentication types

#### Defined in

[client.ts:518](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L518)

___

### validateAuthentication

▸ **validateAuthentication**(`requiredAuthTypes`, `operationName`): `void`

Validate that the required authentication method is available

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `requiredAuthTypes` | `string`[] | Array of required authentication types (OpenAPI security scheme names) |
| `operationName` | `string` | Name of the operation for error messages |

#### Returns

`void`

#### Defined in

[client.ts:540](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L540)

___

### getAvailableAuthTypes

▸ **getAvailableAuthTypes**(): `string`[]

Get available authentication types

#### Returns

`string`[]

#### Defined in

[client.ts:582](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/client.ts#L582)
