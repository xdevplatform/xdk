[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / Paginator

# Class: Paginator\<T\>

X API paginator with rich functionality

This class provides comprehensive pagination support for the X API, including:
- Automatic iteration with `for await...of` loops
- Manual page control with `fetchNext()` and `fetchPrevious()`
- Metadata access for pagination tokens and counts
- Error handling and rate limit detection
- Support for both forward and backward pagination

**`Example`**

```typescript
// Automatic iteration
const followers = await client.users.getFollowers('783214');
for await (const follower of followers) {
  console.log(follower.username);
}

// Manual control
const followers = await client.users.getFollowers('783214');
await followers.fetchNext();
console.log(followers.items.length); // Number of followers
console.log(followers.meta.next_token); // Next page token

// Check status
if (!followers.done) {
  await followers.fetchNext();
}
```

## Type parameters

| Name | Description |
| :------ | :------ |
| `T` | The type of items being paginated |

## Hierarchy

- **`Paginator`**

  ↳ [`PostPaginator`](PostPaginator.md)

  ↳ [`UserPaginator`](UserPaginator.md)

  ↳ [`EventPaginator`](EventPaginator.md)

## Implements

- `AsyncIterable`\<`T`\>

## Table of contents

### Constructors

- [constructor](Paginator.md#constructor)

### Accessors

- [items](Paginator.md#items)
- [meta](Paginator.md#meta)
- [includes](Paginator.md#includes)
- [errors](Paginator.md#errors)
- [done](Paginator.md#done)
- [rateLimited](Paginator.md#ratelimited)

### Methods

- [fetchNext](Paginator.md#fetchnext)
- [next](Paginator.md#next)
- [fetchPrevious](Paginator.md#fetchprevious)
- [previous](Paginator.md#previous)
- [fetchLast](Paginator.md#fetchlast)
- [reset](Paginator.md#reset)
- [[iterator]](Paginator.md#[iterator])
- [[asyncIterator]](Paginator.md#[asynciterator])

## Constructors

### constructor

• **new Paginator**\<`T`\>(`fetchPage`): [`Paginator`](Paginator.md)\<`T`\>

Creates a new paginator instance

#### Type parameters

| Name |
| :------ |
| `T` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `fetchPage` | (`token?`: `string`) => `Promise`\<[`PaginatedResponse`](../interfaces/PaginatedResponse.md)\<`T`\>\> | Function that fetches a page of data given a pagination token |

#### Returns

[`Paginator`](Paginator.md)\<`T`\>

#### Defined in

[paginator.ts:87](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L87)

## Accessors

### items

• `get` **items**(): `T`[]

Get all fetched items

#### Returns

`T`[]

#### Defined in

[paginator.ts:94](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L94)

___

### meta

• `get` **meta**(): `any`

Get current pagination metadata

#### Returns

`any`

#### Defined in

[paginator.ts:101](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L101)

___

### includes

• `get` **includes**(): `undefined` \| `Record`\<`string`, `any`\>

Get current includes data

#### Returns

`undefined` \| `Record`\<`string`, `any`\>

#### Defined in

[paginator.ts:108](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L108)

___

### errors

• `get` **errors**(): `undefined` \| `any`[]

Get current errors

#### Returns

`undefined` \| `any`[]

#### Defined in

[paginator.ts:115](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L115)

___

### done

• `get` **done**(): `boolean`

Check if pagination is done

#### Returns

`boolean`

#### Defined in

[paginator.ts:122](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L122)

___

### rateLimited

• `get` **rateLimited**(): `boolean`

Check if rate limit was hit

#### Returns

`boolean`

#### Defined in

[paginator.ts:129](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L129)

## Methods

### fetchNext

▸ **fetchNext**(): `Promise`\<`void`\>

Fetch the next page and add items to current instance

This method fetches the next page of data and appends the items to the
current paginator instance. It updates the pagination state and metadata.

#### Returns

`Promise`\<`void`\>

**`Example`**

```typescript
const followers = await client.users.getFollowers('783214');
await followers.fetchNext(); // Fetch first page
console.log(followers.items.length); // Number of followers

if (!followers.done) {
  await followers.fetchNext(); // Fetch second page
  console.log(followers.items.length); // Total followers across pages
}
```

**`Throws`**

When the API request fails

#### Defined in

[paginator.ts:153](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L153)

___

### next

▸ **next**(): `Promise`\<[`Paginator`](Paginator.md)\<`T`\>\>

Get next page as a new instance

This method creates a new paginator instance that starts from the next page,
without affecting the current paginator's state.

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`T`\>\>

New paginator instance for the next page

**`Example`**

```typescript
const followers = await client.users.getFollowers('783214');
await followers.fetchNext(); // Fetch first page

if (!followers.done) {
  const nextPage = await followers.next(); // Get next page as new instance
  console.log(followers.items.length); // Still first page
  console.log(nextPage.items.length); // Second page
}
```

#### Defined in

[paginator.ts:208](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L208)

___

### fetchPrevious

▸ **fetchPrevious**(): `Promise`\<`void`\>

Fetch previous page (if supported)

#### Returns

`Promise`\<`void`\>

#### Defined in

[paginator.ts:222](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L222)

___

### previous

▸ **previous**(): `Promise`\<[`Paginator`](Paginator.md)\<`T`\>\>

Get previous page as a new instance

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`T`\>\>

#### Defined in

[paginator.ts:257](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L257)

___

### fetchLast

▸ **fetchLast**(`count`): `Promise`\<`void`\>

Fetch up to a specified number of additional items

#### Parameters

| Name | Type |
| :------ | :------ |
| `count` | `number` |

#### Returns

`Promise`\<`void`\>

#### Defined in

[paginator.ts:271](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L271)

___

### reset

▸ **reset**(): `void`

Reset paginator to initial state

#### Returns

`void`

#### Defined in

[paginator.ts:285](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L285)

___

### [iterator]

▸ **[iterator]**(): `Iterator`\<`T`, `any`, `undefined`\>

Iterator for all fetched items

#### Returns

`Iterator`\<`T`, `any`, `undefined`\>

#### Defined in

[paginator.ts:300](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L300)

___

### [asyncIterator]

▸ **[asyncIterator]**(): `AsyncIterator`\<`T`, `any`, `undefined`\>

Async iterator that fetches pages automatically

#### Returns

`AsyncIterator`\<`T`, `any`, `undefined`\>

#### Implementation of

AsyncIterable.[asyncIterator]

#### Defined in

[paginator.ts:309](https://github.com/xdevplatform/xdk/blob/ad4172ef5f68f089e0f077a190b271016dd35bf7/xdk/typescript/src/paginator.ts#L309)
