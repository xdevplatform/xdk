[X API SDK v2.152 - v1.0.0](../README.md) / [Exports](../modules.md) / [Schemas](../modules/Schemas.md) / PlaidAccount

# Interface: PlaidAccount

[Schemas](../modules/Schemas.md).PlaidAccount

## Table of contents

### Properties

- [accountCategory](Schemas.PlaidAccount.md#accountcategory)
- [accountId](Schemas.PlaidAccount.md#accountid)
- [accountNumberDisplay](Schemas.PlaidAccount.md#accountnumberdisplay)
- [accountType](Schemas.PlaidAccount.md#accounttype)
- [availableBalance](Schemas.PlaidAccount.md#availablebalance)
- [currency](Schemas.PlaidAccount.md#currency)
- [currentBalance](Schemas.PlaidAccount.md#currentbalance)
- [nickname](Schemas.PlaidAccount.md#nickname)
- [productName](Schemas.PlaidAccount.md#productname)
- [status](Schemas.PlaidAccount.md#status)

## Properties

### accountCategory

• **accountCategory**: `string`

The category of the account (e.g., personal, business).

#### Defined in

[schemas.ts:1985](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1985)

___

### accountId

• **accountId**: `string`

The Plaid account ID.

#### Defined in

[schemas.ts:1986](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1986)

___

### accountNumberDisplay

• **accountNumberDisplay**: `string`

The last 2-4 digits of the account number.

#### Defined in

[schemas.ts:1987](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1987)

___

### accountType

• **accountType**: `string`

The type of the account (e.g., checking, savings).

#### Defined in

[schemas.ts:1988](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1988)

___

### availableBalance

• `Optional` **availableBalance**: `number`

The available balance of the account.

#### Defined in

[schemas.ts:1989](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1989)

___

### currency

• **currency**: [`PlaidCurrency`](Schemas.PlaidCurrency.md)

#### Defined in

[schemas.ts:1990](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1990)

___

### currentBalance

• `Optional` **currentBalance**: `number`

The current balance of the account.

#### Defined in

[schemas.ts:1991](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1991)

___

### nickname

• `Optional` **nickname**: `string`

The nickname of the account.

#### Defined in

[schemas.ts:1992](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1992)

___

### productName

• **productName**: `string`

The name of the product associated with the account.

#### Defined in

[schemas.ts:1993](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1993)

___

### status

• **status**: `string`

The status of the account.

#### Defined in

[schemas.ts:1994](https://github.com/xdevplatform/xdk/blob/70fb6a6cb23cd3c8ca2096a864d248dff75ed2ff/xdk/typescript/src/schemas.ts#L1994)
