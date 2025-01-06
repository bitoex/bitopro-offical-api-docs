# Margin Transfer

This API allows users to transfer funds between different account types within the margin system.

# Api Request

**`POST` /margin/transfer**

**Request Body Parameters:**

| Field           | Type    | Required | Description                                                           |
|:----------------|:--------|:---------|:----------------------------------------------------------------------|
| currency        | string  | Yes      | The currency code to transfer (e.g., "usdt")                          |
| amount          | string  | Yes      | The amount to transfer                                                |
| fromBalanceKind | integer | Yes      | The source account type (e.g., 0 for spot account)                    |
| toBalanceKind   | integer | Yes      | The destination account type (e.g., 5 for margin account)             |

**Request Example:**

```javascript
{
    "currency": "usdt",
    "amount": "10",
    "fromBalanceKind": 0,
    "toBalanceKind": 5
}
```

# Api Response

**Response Fields:**

| Field         | Type   | Description                                   |
|:--------------|:-------|:----------------------------------------------|
| fromInvoiceID | string | The invoice ID for the source account         |
| toInvoiceID   | string | The invoice ID for the destination account    |

**Response Example:**

```javascript
{
    "fromInvoiceID": "8183753651",
    "toInvoiceID": "1932659838"
}
```

[Back](../summary.md)