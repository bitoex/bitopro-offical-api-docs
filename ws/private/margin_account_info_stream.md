# Margin Account Info WebSocket Stream

This WebSocket stream provides real-time updates on the margin account information.

## WebSocket Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/auth/margin/account-info**

## Authentication

You need to authenticate to access this private WebSocket stream. Please refer to the [authentication document](../../../README.md#api-security-protocol) for details on how to create the necessary headers.

## WebSocket Response

The response provides comprehensive information about the margin account status, including the account-to-debt ratio, account balances, and total asset and debt amounts.

### Response Fields:

| Field     | Type    | Description                                        |
|:----------|:--------|:---------------------------------------------------|
| event     | string  | Event type (MARGIN_BALANCE_INFO)                   |
| timestamp | integer | Unix timestamp in milliseconds                     |
| datetime  | string  | ISO 8601 formatted date and time                   |
| data      | object  | Contains the margin account information            |

### Data Fields:

| Field            | Type    | Description                                        |
|:-----------------|:--------|:---------------------------------------------------|
| adRatio          | string  | Account-to-debt ratio                              |
| adRatioLabel     | string  | Label indicating the safety level of the AD ratio  |
| accountID        | string  | Unique identifier for the account                  |
| accountStatus    | integer | Status of the account                              |
| marginStatus     | integer | Status of margin trading for this account          |
| balances         | object  | Contains balance information for each currency     |
| calculateUnit    | string  | The unit used for calculations (e.g., "USDT")      |
| totalAssetAmount | string  | Total value of assets in the account               |
| totalDebtAmount  | string  | Total debt in the account                          |
| action           | string  | Action type (e.g., "MARGIN_INIT")                  |
| timestamp        | integer | Unix timestamp in milliseconds                     |

### Balance Fields for Each Currency:

| Field                | Type   | Description                             |
|:---------------------|:-------|:----------------------------------------|
| borrowAmount         | string | The amount borrowed                     |
| borrowInterestAmount | string | The accumulated interest on borrowed amount |

### Response Example:

```javascript
{
    "event": "MARGIN_BALANCE_INFO",
    "timestamp": 1721381296166,
    "datetime": "2024-07-19T17:28:16.166Z",
    "data": {
        "adRatio": "55.70",
        "adRatioLabel": "SAFETY_THRESHOLD",
        "accountID": "5411716254",
        "accountStatus": 1,
        "marginStatus": 1,
        "balances": {
            "BTC": {
                "borrowAmount": "2.00008624",
                "borrowInterestAmount": "0.00242282"
            },
            "ETH": {
                "borrowAmount": "0.00000000",
                "borrowInterestAmount": "0.00000000"
            },
            "USDT": {
                "borrowAmount": "14.00078403",
                "borrowInterestAmount": "0.00038376"
            }
        },
        "calculateUnit": "USDT",
        "totalAssetAmount": "7134740.15231776",
        "totalDebtAmount": "128079.84498910",
        "action": "MARGIN_INIT",
        "timestamp": 1721381296166
    }
}
```

[Back](../summary.md)