# Margin Borrow

This API allows users to borrow funds in the margin trading system.

# Api Request

**`POST` /margin/borrow**

**Request Body Parameters:**

| Field        | Type   | Required | Description                                  |
|:-------------|:-------|:---------|:---------------------------------------------|
| currency     | string | Yes      | The currency code to borrow (e.g., "usdt")   |
| borrowAmount | string | Yes      | The amount to borrow                         |

**Request Example:**

```javascript
{
    "currency": "usdt",
    "borrowAmount": "2"
}
```

# Api Response

**Response Fields:**

| Field     | Type   | Description                           |
|:----------|:-------|:--------------------------------------|
| invoiceID | string | The invoice ID for the borrow transaction |

**Response Example:**

```javascript
{
    "invoiceID": "4533900631"
}
```

[Back](../summary.md)