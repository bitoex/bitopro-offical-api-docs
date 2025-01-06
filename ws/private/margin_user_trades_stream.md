# Margin User Trades WebSocket Stream

This WebSocket stream provides real-time updates on the user's margin trade executions.

## WebSocket Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/auth/margin/margin/user-trades**

## Authentication

You need to authenticate to access this private WebSocket stream. Please refer to the [authentication document](../../../README.md#api-security-protocol) for details on how to create the necessary headers.

## WebSocket Response

The response provides information about each margin trade execution as it occurs.

### Response Fields:

| Field     | Type    | Description                                   |
|:----------|:--------|:----------------------------------------------|
| event     | string  | Event type (USER_TRADE)                       |
| timestamp | integer | Unix timestamp of the event in milliseconds   |
| datetime  | string  | ISO 8601 formatted date and time              |
| data      | object  | Contains details of the trade execution       |

### Trade Data Fields:

| Field                 | Type    | Description                                        |
|:----------------------|:--------|:---------------------------------------------------|
| base                  | string  | Base currency of the trading pair                  |
| quote                 | string  | Quote currency of the trading pair                 |
| side                  | string  | Trade side (ask for sell, bid for buy)             |
| price                 | string  | Execution price                                    |
| volume                | string  | Executed volume                                    |
| fee                   | string  | Fee amount                                         |
| feeCurrency           | string  | Currency in which the fee was paid                 |
| transactionTimestamp  | integer | Unix timestamp of the trade execution              |
| eventTimestamp        | integer | Unix timestamp of the event processing             |
| orderID               | string  | ID of the order that was executed                  |
| orderType             | string  | Type of the order (e.g., LIMIT, MARKET)            |
| matchID               | string  | Unique identifier for the trade match (if any)     |
| isMarket              | boolean | Indicates if it was a market order                 |
| isMaker               | boolean | Indicates if the trade was executed as a maker     |

### Response Example:

```javascript
{
    "event": "USER_TRADE",
    "timestamp": 1721387560580,
    "datetime": "2024-07-19T19:12:40.580Z",
    "data": {
        "base": "btc",
        "quote": "usdt",
        "side": "ask",
        "price": "1",
        "volume": "1",
        "fee": "0",
        "feeCurrency": "usdt",
        "transactionTimestamp": 1721387560,
        "eventTimestamp": 1721387560,
        "orderID": "479457831",
        "orderType": "LIMIT",
        "matchID": "",
        "isMarket": false,
        "isMaker": false
    }
}
```

This example shows a margin trade execution where 1 BTC was sold at a price of 1 USDT. The trade was executed as a taker (isMaker: false) with a LIMIT order type.

[Back](../summary.md)