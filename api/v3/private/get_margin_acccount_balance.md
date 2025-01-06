# Get Margin Account Balance

This API retrieves the current margin account balance and related information.

# Api Request

**`GET` /margin/balances**

# Api Response

The response provides a comprehensive overview of the margin account status, including the account-to-debt ratio, account status, and detailed balance information for each supported cryptocurrency.

**Response Fields:**

| Field           | Type    | Description                                                        |
|:----------------|:--------|:-------------------------------------------------------------------|
| adRatio         | string  | The current account-to-debt ratio                                  |
| adRatioLabel    | string  | The label indicating the safety level of the current AD ratio      |
| accountID       | string  | The unique identifier for the margin account                       |
| accountStatus   | integer | The status of the account                                          |
| marginStatus    | integer | The status of margin trading for this account                      |
| balances        | object  | Detailed balance information for each supported cryptocurrency     |
| calculateUnit   | string  | The unit used for calculations (e.g., "USDT")                      |
| totalAssetAmount| string  | The total value of assets in the account, in the calculation unit  |
| totalDebtAmount | string  | The total debt in the account, in the calculation unit             |

**Balance Fields for Each Currency:**

| Field                | Type    | Description                                                     |
|:---------------------|:--------|:----------------------------------------------------------------|
| availableAmount      | string  | The amount available for trading                                |
| tradedAmount         | string  | The amount currently in open orders                             |
| borrowAmount         | string  | The amount borrowed                                             |
| borrowInterestAmount | string  | The accumulated interest on borrowed amount                     |
| borrowStatus         | integer | The status of borrowing for this currency                       |
| transferStatus       | integer | The status of transfers for this currency                       |
| totalAmount          | string  | The total amount (available + traded)                           |

**Response Example:**

```javascript
{
    "adRatio": "5.76",
    "adRatioLabel": "SAFETY_THRESHOLD",
    "accountID": "5411716254",
    "accountStatus": 1,
    "marginStatus": 1,
    "balances": {
        "BTC": {
            "availableAmount": "9.99990000",
            "tradedAmount": "0.00000000",
            "borrowAmount": "2.00008624",
            "borrowInterestAmount": "0.00236786",
            "borrowStatus": 1,
            "transferStatus": 1,
            "totalAmount": "9.99990000"
        },
        "ETH": {
            "availableAmount": "0.00000000",
            "tradedAmount": "0.00000000",
            "borrowAmount": "0.00000000",
            "borrowInterestAmount": "0.00000000",
            "borrowStatus": 1,
            "transferStatus": 1,
            "totalAmount": "0.00000000"
        },
        "USDT": {
            "availableAmount": "100041.50010000",
            "tradedAmount": "0.00000000",
            "borrowAmount": "15.00078403",
            "borrowInterestAmount": "0.00000000",
            "borrowStatus": 1,
            "transferStatus": 1,
            "totalAmount": "100041.50010000"
        }
    },
    "calculateUnit": "USDT",
    "totalAssetAmount": "748279.60832069",
    "totalDebtAmount": "129823.00462234"
}
```

[Back](../summary.md)