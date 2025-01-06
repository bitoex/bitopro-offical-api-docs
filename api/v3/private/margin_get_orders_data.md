# Get Margin Order List

Fetches all margin orders of a specific pair within 90 days, ordered by create time in descending order.

If you need real-time updates to obtain unfilled orders, we recommend using the WebSocket open orders API. For more details, please refer to this [link](../../../ws/private/open_orders_stream.md).

# Api Request

**`GET` /margin/orders/all/{pair}**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query          | Type   | Required | Description                                                                                                                                                                                                                                    | Default           | Range                                 | Example       |
| :------------------ | :--- | :------------- | :----- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- | :------------------------------------ | :------------ |
| X-BITOPRO-APIKEY    |      |                | string | Yes      | API Key                                                                                                                                                                                                                   |                   |                                       |               |
| X-BITOPRO-PAYLOAD   |      |                | string | Yes      | Payload                                                                                                                                                                                                                  |                   |                                       |               |
| X-BITOPRO-SIGNATURE |      |                | string | Yes      | Signature                                                                                                                                                                                                              |                   |                                       |               |
|                     | pair |                | string | Yes      | The trading pair in format ${BASE}\_${QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list.                                                                                                                   |                   |                                       | btc_usdt      |

# Api Response

To get detailed order model explanation, refer to [order model explanation.](../../../model.md#order-model-explanation)

**Response Example:**
```javascript
{
    "data": [
        {
            "id": "3927422785",
            "pair": "btc_usdt",
            "price": "1",
            "avgExecutionPrice": "0",
            "action": "BUY",
            "type": "LIMIT",
            "createdTimestamp": 1721376814204,
            "updatedTimestamp": 1721376819350,
            "status": 4,
            "originalAmount": "1",
            "remainingAmount": "1",
            "executedAmount": "0",
            "fee": "0",
            "feeSymbol": "btc",
            "bitoFee": "0",
            "total": "0",
            "seq": "BTCUSDT9293586467",
            "timeInForce": "GTC"
        },
        {
            "id": "9050564390",
            "pair": "btc_usdt",
            "price": "1",
            "avgExecutionPrice": "0",
            "action": "BUY",
            "type": "LIMIT",
            "createdTimestamp": 1721376814204,
            "updatedTimestamp": 1721376819324,
            "status": 4,
            "originalAmount": "1",
            "remainingAmount": "1",
            "executedAmount": "0",
            "fee": "0",
            "feeSymbol": "btc",
            "bitoFee": "0",
            "total": "0",
            "seq": "BTCUSDT7146102820",
            "timeInForce": "GTC"
        },
        // ... more order entries ...
    ]
}
```

[Back](../summary.md)