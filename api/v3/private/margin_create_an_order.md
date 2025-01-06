# Create A Margin Order

Create a margin order API, this endpoint supports limit, market, and stop-limit orders.

> 
After initiating an order, you can utilize the WebSocket streams for both [open orders](../../../ws/private/open_order_stream.md) and [history orders](../../../ws/private/history_order_stream.md) to continuously receive updated information about your orders in real-time.

# Api Request

**Rate Limit: `Allow `1200` requests per minute per IP & UID.`**

**`POST` /margin/orders/{pair}**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query | Type   | Required | Description                                                                                                               | Default | Range | Example   |
| :------------------ | :--- | :---- | :----- | :------- | :------------------------------------------------------------------------------------------------------------------------ | :------ | :---- | :-------- |
| X-BITOPRO-APIKEY    |      |       | string | Yes      | API Key                                                                                             |         |       |           |
| X-BITOPRO-PAYLOAD   |      |       | string | Yes      | Payload                                                                                         |         |       |           |
| X-BITOPRO-SIGNATURE |      |       | string | Yes      | Signature                                                                                     |         |       |           |
|                     | pair |       | string | Yes      | The trading pair in format {BASE}_{QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |         |       | bito\_eth |

**Request body:**

| Field     | Type    | Required | Description                                                           |
|:----------|:--------|:---------|:----------------------------------------------------------------------|
| action    | string  | Yes      | Order action: "buy" or "sell"                                         |
| price     | string  | Yes      | Order price                                                           |
| amount    | string  | Yes      | Order amount                                                          |
| condition | string  | No       | Condition for stop orders: ">=" or "<="                               |
| stopPrice | string  | No       | Stop price for stop orders                                            |
| timestamp | integer | Yes      | Current timestamp in milliseconds                                     |
| type      | string  | Yes      | Order type: "limit", "market", or "stop_limit"                        |
| clientId  | integer | No       | Client-defined order ID                                               |

**Request Example:**

```javascript
{
    "action": "buy",
    "price": "1",
    "amount": "100",
    "condition": ">=",
    "stopPrice": "1",
    "timestamp": {{nonce}},
    "type": "limit",
    "clientId": 123
}
```

# Api Response

**Response Fields:**

| Field       | Type    | Description                           |
|:------------|:--------|:--------------------------------------|
| orderId     | string  | Unique identifier for the order       |
| timestamp   | integer | Server timestamp in milliseconds      |
| action      | string  | Order action (BUY or SELL)            |
| amount      | string  | Order amount                          |
| price       | string  | Order price                           |
| timeInForce | string  | Time in force condition for the order |
| clientId    | integer | Client-defined order ID (if provided) |

**Response Example:**

```javascript
{
    "orderId": "9789414023",
    "timestamp": 1721376028000,
    "action": "BUY",
    "amount": "100",
    "price": "1",
    "timeInForce": "GTC",
    "clientId": 123
}
```

[Back](../summary.md)