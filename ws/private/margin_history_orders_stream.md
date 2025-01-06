# Margin History Orders WebSocket Stream

This WebSocket stream provides real-time updates on the history of margin orders.

## WebSocket Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/auth/margin/orders/histories**

## Authentication

You need to authenticate to access this private WebSocket stream. Please refer to the [authentication document](../../../README.md#api-security-protocol) for details on how to create the necessary headers.

## WebSocket Response

The response provides information about recent margin order history, grouped by trading pairs.

### Response Fields:

| Field     | Type    | Description                                   |
|:----------|:--------|:----------------------------------------------|
| event     | string  | Event type (RECENT_HISTORY_ORDERS)            |
| timestamp | integer | Unix timestamp in milliseconds                |
| datetime  | string  | ISO 8601 formatted date and time              |
| data      | object  | Contains order history grouped by trading pair|

### Order Fields:

| Field              | Type    | Description                                        |
|:-------------------|:--------|:---------------------------------------------------|
| id                 | string  | Unique identifier for the order                    |
| pair               | string  | Trading pair                                       |
| price              | string  | Order price                                        |
| avgExecutionPrice  | string  | Average execution price                            |
| action             | string  | Order action (BUY or SELL)                         |
| type               | string  | Order type (e.g., LIMIT, STOP_LIMIT)               |
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
| clientID           | integer | Client-defined ID (if provided)                    |
| accountType        | integer | Account type (5 for margin)                        |
| stopPrice          | string  | Stop price for STOP_LIMIT orders (if applicable)   |
| condition          | string  | Condition for STOP_LIMIT orders (if applicable)    |

### Response Example:

```javascript
{
    "event": "RECENT_HISTORY_ORDERS",
    "timestamp": 1721381693260,
    "datetime": "2024-07-19T17:34:53.260Z",
    "data": {
        "btc_usdt": [
            {
                "id": "8804281179",
                "pair": "btc_usdt",
                "price": "1",
                "avgExecutionPrice": "1",
                "action": "BUY",
                "type": "LIMIT",
                "timestamp": 1721379365000,
                "status": 2,
                "originalAmount": "100",
                "remainingAmount": "0",
                "executedAmount": "100",
                "fee": "0",
                "feeSymbol": "btc",
                "bitoFee": "0",
                "total": "100",
                "seq": "BTCUSDT1441070115",
                "timeInForce": "GTC",
                "createdTimestamp": 1721377215000,
                "updatedTimestamp": 1721379365000,
                "clientID": 123,
                "accountType": 5
            },
            // ... more order entries ...
        ]
    }
}
```

Note: The response may include multiple orders for each trading pair, showing the recent history of margin orders.

[Back](../summary.md)