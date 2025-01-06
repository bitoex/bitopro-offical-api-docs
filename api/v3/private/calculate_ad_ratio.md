# Calculate AD Ratio

This API calculates the Account-to-Debt (AD) Ratio for margin trading based on a hypothetical action.

# Api Request

**`POST` /margin/calculate/ad-ratio**

**Request Body Parameters:**

| Field    | Type    | Required | Description                                                           |
|:---------|:--------|:---------|:----------------------------------------------------------------------|
| action   | integer | Yes      | Action type: 1 (borrow), 2 (repay), 3 (transfer in), 4 (transfer out) |
| currency | string  | Yes      | The currency code for the action (e.g., "btc")                        |
| amount   | string  | Yes      | The amount for the action                                             |

**Request Example:**

```javascript
{
    "action": 1,
    "currency": "btc",
    "amount": "0.1"
}
```

# Api Response

**Response Fields:**

| Field             | Type    | Description                                               |
|:------------------|:--------|:----------------------------------------------------------|
| action            | integer | The action type used in the calculation                   |
| ADRatio           | string  | The calculated Account-to-Debt ratio                      |
| userBorrowAmounts | array   | List of borrowed amounts for each currency                |
| userAssetAmounts  | array   | List of asset amounts for each currency                   |
| usdtMarkPrices    | array   | List of USDT mark prices for each currency                |
| totalUSDTAsset    | string  | Total asset value in USDT                                 |
| totalUSDTDebt     | string  | Total debt value in USDT                                  |

**Response Example:**

```javascript
{
    "action": 1,
    "ADRatio": "54.96",
    "userBorrowAmounts": [
        {
            "currency": "BTC",
            "amount": "2.10273234"
        },
        {
            "currency": "USDT",
            "amount": "14.00271882"
        },
        {
            "currency": "ETH",
            "amount": "0"
        }
    ],
    "userAssetAmounts": [
        {
            "currency": "USDT",
            "amount": "99948.4796"
        },
        {
            "currency": "BTC",
            "amount": "114.1003"
        },
        {
            "currency": "ETH",
            "amount": "0"
        }
    ],
    "usdtMarkPrices": [
        {
            "currency": "BTC",
            "amount": "66918.9198052"
        },
        {
            "currency": "ETH",
            "amount": "3517.88647461"
        },
        {
            "currency": "USDT",
            "amount": "1"
        }
    ],
    "totalUSDTAsset": "7728725.41306874",
    "totalUSDTDebt": "134034.68757056"
}
```

[Back](../summary.md)