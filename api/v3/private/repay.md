# Margin Repay

This API allows users to repay borrowed funds in the margin trading system.

# Api Request

**`POST` /margin/repay**

**Request Body Parameters:**

| Field       | Type   | Required | Description                                 |
|:------------|:-------|:---------|:--------------------------------------------|
| currency    | string | Yes      | The currency code to repay (e.g., "usdt")   |
| repayAmount | string | Yes      | The amount to repay                         |

**Request Example:**

```javascript
{
    "currency": "usdt",
    "repayAmount": "1"
}
```

# Api Response

**Response Fields:**

| Field     | Type   | Description                           |
|:----------|:-------|:--------------------------------------|
| invoiceID | string | The invoice ID for the repay transaction |

**Response Example:**

```javascript
{
    "invoiceID": "5418000015"
}
```

[Back](../summary.md)