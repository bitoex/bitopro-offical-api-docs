# Get A Margin Order Data

Get a margin order information by given order id.

# Api Request
**`GET` /margin/orders/{pair}/{orderId}**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path    | Query | Type   | Required | Description                                                                                                               | Default | Range | Example    |
| :------------------ | :------ | :---- | :----- | :------- | :------------------------------------------------------------------------------------------------------------------------ | :------ | :---- | :--------- |
| X-BITOPRO-APIKEY    |         |       | string | Yes      | API Key                                                                                              |         |       |            |
| X-BITOPRO-PAYLOAD   |         |       | string | Yes      | Payload                                                                                             |         |       |            |
| X-BITOPRO-SIGNATURE |         |       | string | Yes      | Signature                                                                                         |         |       |            |
|                     | pair    |       | string | Yes      | The trading pair in format {BASE}_{QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |         |       | btc_usdt   |
|                     | orderId |       | string | Yes      | The id of the order.                                                                                                      |         |       | 9296847601 |

# Api Response

To get detailed order model explanation, refer to [order model explanation.](../../../model.md#order-model-explanation)

**Response Example:**
```javascript
{
    "id": "9296847601",
    "pair": "btc_usdt",
    "price": "1",
    "avgExecutionPrice": "0",
    "action": "BUY",
    "type": "LIMIT",
    "timestamp": 1721376759721,
    "status": 4,
    "originalAmount": "1",
    "remainingAmount": "1",
    "executedAmount": "0",
    "fee": "0",
    "feeSymbol": "btc",
    "bitoFee": "0",
    "total": "0",
    "seq": "BTCUSDT2851135526",
    "timeInForce": "GTC",
    "createdTimestamp": 1721376748298,
    "updatedTimestamp": 1721376759721
}
```
[Back](../summary.md)