# Get Open Margin Orders

Fetches all open margin orders, descending ordered by updated time.

If you need real-time updates to obtain unfilled orders, we recommend using the WebSocket open orders API. For more details, please refer to this [link](../../../ws/private/open_orders_stream.md).

# Api Request

**Rate Limit: `Allow `5` requests per second per IP & UID.`**

**`GET` /margin/orders/orders/open**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query | Type   | Required | Description                                                                                                                | Default | Range | Example   |
|:--------------------|:-----|:------|:-------|:---------|:---------------------------------------------------------------------------------------------------------------------------|:--------|:------|:----------|
| X-BITOPRO-APIKEY    |      |       | string | Yes      | API Key                                                                                                                    |         |       |           |
| X-BITOPRO-PAYLOAD   |      |       | string | Yes      | Payload                                                                                                                    |         |       |           |
| X-BITOPRO-SIGNATURE |      |       | string | Yes      | Signature                                                                                                                  |         |       |           |
|                     |      | pair  | string | No       | The trading pair in format ${BASE}_${QUOTE}. Please follow the [link](https://www.bitopro.com/fees) to check the pair list. Response all pair orders if pair is empty. |         |       | btc_usdt  |

# Api Response

To get detailed order model explanation, refer to [order model explanation.](../../../model.md#order-model-explanation)

**Response Example:**
```javascript
{
    "data": [
        {
            "action": "BUY",
            "avgExecutionPrice": "0",
            "bitoFee": "0",
            "executedAmount": "0",
            "id": "8804281179",
            "originalAmount": "100",
            "pair": "btc_usdt",
            "price": "1",
            "remainingAmount": "100",
            "seq": "BTCUSDT1441070115",
            "status": 0,
            "createdTimestamp": 1721377215,
            "updatedTimestamp": 1721377215,
            "total": "0",
            "type": "LIMIT",
            "timeInForce": "GTC",
            "clientId": 123,
            "condition": "",
            "stopPrice": ""
        }
    ]
}
```
[Back](../summary.md)