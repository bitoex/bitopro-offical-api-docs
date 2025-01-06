# List User Liquidations

This API retrieves the user's liquidation history in the margin trading system.

# Api Request

**`GET` /margin/user-liquidations**

# Api Response

The response provides a list of liquidation records and the total number of liquidation transactions.

**Response Fields:**

| Field              | Type    | Description                                     |
|:-------------------|:--------|:------------------------------------------------|
| liquidations       | array   | List of liquidation records                     |
| liquidationsAmount | integer | Total number of liquidation transactions        |

**Liquidation Record Fields:**

| Field            | Type    | Description                                                                              |
|:-----------------|:--------|:-----------------------------------------------------------------------------------------|
| serial           | integer | Unique identifier for the liquidation transaction                                        |
| debtCurrency     | string  | The currency code of the debt                                                            |
| debtAmount       | string  | The amount of debt liquidated                                                            |
| assetCurrency    | string  | The currency code of the asset (if applicable)                                           |
| assetAmount      | string  | The amount of asset liquidated (if applicable)                                           |
| feeAmount        | string  | The fee amount for the liquidation                                                       |
| adRatio          | string  | The Account-to-Debt ratio before liquidation                                             |
| afterAdRatio     | string  | The Account-to-Debt ratio after liquidation                                              |
| status           | integer | Status of the liquidation (2: finished)                                                  |
| type             | integer | Type of liquidation (1: repay - original currency repayment, 2: sell - forced liquidation)|
| finishTimestamp  | integer | Unix timestamp of when the liquidation was completed                                     |

**Response Example:**

```javascript
{
    "liquidations": [
        {
            "serial": 3704048445,
            "debtCurrency": "USDT",
            "debtAmount": "9,904.38493339",
            "feeAmount": "100.04429225",
            "adRatio": "0.15",
            "afterAdRatio": "0",
            "status": 2,
            "type": 1,
            "finishTimestamp": 1714754343
        },
        {
            "serial": 8580906839,
            "debtCurrency": "BTC",
            "debtAmount": "15.72249574",
            "assetCurrency": "USDT",
            "assetAmount": "1,000,104.57077436",
            "feeAmount": "0.15881308",
            "adRatio": "0.15",
            "afterAdRatio": "0",
            "status": 2,
            "type": 2,
            "finishTimestamp": 1714754343
        },
        // ... more liquidation records ...
    ],
    "liquidationsAmount": 15
}
```

[Back](../summary.md)