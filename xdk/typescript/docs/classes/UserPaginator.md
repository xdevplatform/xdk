[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / UserPaginator

# Class: UserPaginator

Paginator for users

## Hierarchy

- [`Paginator`](Paginator.md)\<`any`\>

  ↳ **`UserPaginator`**

## Table of contents

### Constructors

- [constructor](UserPaginator.md#constructor)

### Accessors

- [items](UserPaginator.md#items)
- [meta](UserPaginator.md#meta)
- [includes](UserPaginator.md#includes)
- [errors](UserPaginator.md#errors)
- [done](UserPaginator.md#done)
- [rateLimited](UserPaginator.md#ratelimited)
- [users](UserPaginator.md#users)

### Methods

- [fetchNext](UserPaginator.md#fetchnext)
- [next](UserPaginator.md#next)
- [fetchPrevious](UserPaginator.md#fetchprevious)
- [previous](UserPaginator.md#previous)
- [fetchLast](UserPaginator.md#fetchlast)
- [reset](UserPaginator.md#reset)
- [[iterator]](UserPaginator.md#[iterator])
- [[asyncIterator]](UserPaginator.md#[asynciterator])

## Constructors

### constructor

• **new UserPaginator**(`fetchPage`): [`UserPaginator`](UserPaginator.md)

Creates a new paginator instance

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `fetchPage` | (`token?`: `string`) => `Promise`\<[`PaginatedResponse`](../interfaces/PaginatedResponse.md)\<`any`\>\> | Function that fetches a page of data given a pagination token |

#### Returns

[`UserPaginator`](UserPaginator.md)

#### Inherited from

[Paginator](Paginator.md).[constructor](Paginator.md#constructor)

#### Defined in

[paginator.ts:87](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L87)

## Accessors

### items

• `get` **items**(): `T`[]

Get all fetched items

#### Returns

`T`[]

#### Inherited from

Paginator.items

#### Defined in

[paginator.ts:94](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L94)

___

### meta

• `get` **meta**(): `any`

Get current pagination metadata

#### Returns

`any`

#### Inherited from

Paginator.meta

#### Defined in

[paginator.ts:101](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L101)

___

### includes

• `get` **includes**(): `undefined` \| `Record`\<`string`, `any`\>

Get current includes data

#### Returns

`undefined` \| `Record`\<`string`, `any`\>

#### Inherited from

Paginator.includes

#### Defined in

[paginator.ts:108](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L108)

___

### errors

• `get` **errors**(): `undefined` \| `any`[]

Get current errors

#### Returns

`undefined` \| `any`[]

#### Inherited from

Paginator.errors

#### Defined in

[paginator.ts:115](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L115)

___

### done

• `get` **done**(): `boolean`

Check if pagination is done

#### Returns

`boolean`

#### Inherited from

Paginator.done

#### Defined in

[paginator.ts:122](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L122)

___

### rateLimited

• `get` **rateLimited**(): `boolean`

Check if rate limit was hit

#### Returns

`boolean`

#### Inherited from

Paginator.rateLimited

#### Defined in

[paginator.ts:129](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L129)

___

### users

• `get` **users**(): `any`[]

#### Returns

`any`[]

#### Defined in

[paginator.ts:348](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L348)

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

#### Inherited from

[Paginator](Paginator.md).[fetchNext](Paginator.md#fetchnext)

#### Defined in

[paginator.ts:153](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L153)

___

### next

▸ **next**(): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get next page as a new instance

This method creates a new paginator instance that starts from the next page,
without affecting the current paginator's state.

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

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

#### Inherited from

[Paginator](Paginator.md).[next](Paginator.md#next)

#### Defined in

[paginator.ts:208](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L208)

___

### fetchPrevious

▸ **fetchPrevious**(): `Promise`\<`void`\>

Fetch previous page (if supported)

#### Returns

`Promise`\<`void`\>

#### Inherited from

[Paginator](Paginator.md).[fetchPrevious](Paginator.md#fetchprevious)

#### Defined in

[paginator.ts:222](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L222)

___

### previous

▸ **previous**(): `Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

Get previous page as a new instance

#### Returns

`Promise`\<[`Paginator`](Paginator.md)\<`any`\>\>

#### Inherited from

[Paginator](Paginator.md).[previous](Paginator.md#previous)

#### Defined in

[paginator.ts:257](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L257)

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

#### Inherited from

[Paginator](Paginator.md).[fetchLast](Paginator.md#fetchlast)

#### Defined in

[paginator.ts:271](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L271)

___

### reset

▸ **reset**(): `void`

Reset paginator to initial state

#### Returns

`void`

#### Inherited from

[Paginator](Paginator.md).[reset](Paginator.md#reset)

#### Defined in

[paginator.ts:285](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L285)

___

### [iterator]

▸ **[iterator]**(): `Iterator`\<`any`, `any`, `undefined`\>

Iterator for all fetched items

#### Returns

`Iterator`\<`any`, `any`, `undefined`\>

#### Inherited from

[Paginator](Paginator.md).[[iterator]](Paginator.md#[iterator])

#### Defined in

[paginator.ts:300](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L300)

___

### [asyncIterator]

▸ **[asyncIterator]**(): `AsyncIterator`\<`any`, `any`, `undefined`\>

Async iterator that fetches pages automatically

#### Returns

`AsyncIterator`\<`any`, `any`, `undefined`\>

#### Inherited from

[Paginator](Paginator.md).[[asyncIterator]](Paginator.md#[asynciterator])

#### Defined in

[paginator.ts:309](https://github.com/xdevplatform/xdk/blob/796140a044d14160471bbb8c39cc8eae5182b809/xdk/typescript/src/paginator.ts#L309)
