# Margin Active Orders WebSocket Stream

This WebSocket stream provides real-time updates on active margin orders.

## WebSocket Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/auth/margin/orders**

## Authentication

You need to authenticate to access this private WebSocket stream. Please refer to the [authentication document](../../../README.md#api-security-protocol) for details on how to create the necessary headers.

## WebSocket Response

The response provides information about currently active margin orders. If there are no active orders, an empty data object will be returned.

### Response Fields:

| Field     | Type    | Description                                   |
|:----------|:--------|:----------------------------------------------|
| event     | string  | Event type (ACTIVE_ORDERS)                    |
| timestamp | integer | Unix timestamp in milliseconds                |
| datetime  | string  | ISO 8601 formatted date and time              |
| data      | object  | Contains active orders grouped by trading pair|

### Order Fields:

| Field              | Type    | Description                                        |
|:-------------------|:--------|:---------------------------------------------------|
| id                 | string  | Unique identifier for the order                    |
| pair               | string  | Trading pair                                       |
| price              | string  | Order price                                        |
| avgExecutionPrice  | string  | Average execution price                            |
| action             | string  | Order action (BUY or SELL)                         |
| type               | string  | Order type (e.g., LIMIT)                           |
| timestamp          | integer | Unix timestamp of the order                        |
| status             | integer | Order status                                       |
| originalAmount     | string  | Original order amount                              |
| remainingAmount    | string  | Remaining amount to be executed                    |
| executedAmount     | string  | Amount that has been executed                      |
| fee                | string  | Fee amount                                         |
| feeSymbol          | string  | Symbol of the fee currency                         |
| bitoFee            | string  | Bito fee amount                                    |
| total              | string  | Total order value                                  |
| seq                | string  | Order sequence number                              |
| timeInForce        | string  | Time in force condition                            |
| createdTimestamp   | integer | Unix timestamp when the order was created          |
| updatedTimestamp   | integer | Unix timestamp when the order was last updated     |
| accountType        | integer | Account type (5 for margin)                        |

### Response Example (With Active Orders):

```javascript
{
    "event": "ACTIVE_ORDERS",
    "timestamp": 1721381602242,
    "datetime": "2024-07-19T17:33:22.242Z",
    "data": {
        "btc_usdt": [
            {
                "id": "2696006730",
                "pair": "btc_usdt",
                "price": "0.01",
                "avgExecutionPrice": "0",
                "action": "BUY",
                "type": "LIMIT",
                "timestamp": 1721381581000,
                "status": 0,
                "originalAmount": "2",
                "remainingAmount": "2",
                "executedAmount": "0",
                "fee": "0",
                "feeSymbol": "btc",
                "bitoFee": "0",
                "total": "0",
                "seq": "BTCUSDT768422940",
                "timeInForce": "GTC",
                "createdTimestamp": 1721381581000,
                "updatedTimestamp": 1721381581000,
                "accountType": 5
            }
        ]
    }
}
```

### Response Example (No Active Orders):

```javascript
{
    "event": "ACTIVE_ORDERS",
    "timestamp": 1721381496944,
    "datetime": "2024-07-19T17:31:36.944Z",
    "data": {}
}
```

[Back](../summary.md)