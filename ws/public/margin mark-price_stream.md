# Margin Mark Price WebSocket Stream

This WebSocket stream provides real-time updates on the mark prices for margin trading.

## WebSocket Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/margin/mark-price**

## WebSocket Response

The response provides current mark prices for various cryptocurrencies used in margin trading.

### Response Fields:

| Field     | Type    | Description                                   |
|:----------|:--------|:----------------------------------------------|
| event     | string  | Event type (MARGIN_MARK_PRICE)                |
| timestamp | integer | Unix timestamp in milliseconds                |
| datetime  | string  | ISO 8601 formatted date and time              |
| data      | object  | Contains the mark prices for each currency    |

### Data Fields:

The `data` object contains key-value pairs where the key is the cryptocurrency code and the value is the current mark price as a string.

### Response Example:

```javascript
{
    "event": "MARGIN_MARK_PRICE",
    "timestamp": 1721723899655,
    "datetime": "2024-07-23T16:38:19.655Z",
    "data": {
        "BTC": "66913.43836165",
        "ETH": "3516.40409242",
        "USDT": "1"
    }
}
```

In this example:
- BTC has a mark price of approximately 66,913.44 USDT
- ETH has a mark price of approximately 3,516.40 USDT
- USDT has a mark price of 1 (as it's the reference currency)

[Back](../summary.md)