# Batch Create Margin Orders

Create batch margin orders, this endpoint supports creating up to `10 limit or market orders at a time`.

> 
After initiating orders, you can utilize the WebSocket streams for both open orders and order history to continuously receive updated information about your orders in real-time.

# Api Request

**Rate Limit: `Allow `90` requests per minute per IP & UID.`**

**`POST` /margin/orders/batch**

**Headers:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query | Type   | Required | Description                       | Default | Range | Example |
| :------------------ | :--- | :---- | :----- | :------- | :-------------------------------- | :------ | :---- | :------ |
| X-BITOPRO-APIKEY    |      |       | string | Yes      | API Key     |         |       |         |
| X-BITOPRO-PAYLOAD   |      |       | string | Yes      | Payload    |         |       |         |
| X-BITOPRO-SIGNATURE |      |       | string | Yes      | Signature|         |       |         |

**Request Body Parameters:**

| Field       | Type   | Required | Description                                                                                                                  | Default | Range              | Example       |
| :---------- | :----- | :------- | :--------------------------------------------------------------------------------------------------------------------------- | :------ | :----------------- | :------------ |
| action      | string | Yes      | The action type of the order, should only be `buy` or `sell`.                                                                |         | `buy` or `sell`    | `buy`         |
| pair        | string | Yes      | The trading pair in format {BASE}_{QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list.    |         |                    | btc_usdt      |
| type        | string | Yes      | The order type, should only be `LIMIT`, `MARKET`.                                                                            |         | `LIMIT`, `MARKET`  | LIMIT         |
| price       | string | Yes      | The price of the order for the trading pair.                                                                                 |         | > 0                | 1             |
| amount      | string | Yes      | The base amount of the order for the trading pair. **However, when executing a market buy order, this field represents the order's quote value.** |         | > 0                | 1             |
| timestamp   | int64  | Yes      | The client timestamp in millisecond.                                                                                         |         |                    | 1721376172000 |
| timeInForce | string | No       | Time in force condition for orders. If type is `MARKET`, this will always be `GTC`.                                          | `GTC`   | `GTC`, `POST_ONLY` | GTC           |

**Request Example:**

```javascript
[
    {
        "action": "buy",
        "pair": "btc_usdt",
        "type": "LIMIT",
        "price": "1",
        "amount": "1",
        "timestamp": {{nonce}},
        "timeInForce": "GTC"
    },
    {
        "action": "buy",
        "pair": "btc_usdt",
        "type": "LIMIT",
        "price": "1",
        "amount": "1",
        "timestamp": {{nonce}},
        "timeInForce": "GTC"
    }
]
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

**Response Example:**

```javascript
{
    "data": [
        {
            "orderId": "9543130812",
            "timestamp": 1721376172000,
            "action": "BUY",
            "amount": "1",
            "price": "1",
            "timeInForce": "GTC"
        },
        {
            "orderId": "4419989207",
            "timestamp": 1721376172000,
            "action": "BUY",
            "amount": "1",
            "price": "1",
            "timeInForce": "GTC"
        }
    ]
}
```

[Back](../summary.md)