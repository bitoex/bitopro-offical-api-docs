# Cancel a Margin Order

Cancel a specific margin order by given order id.

> 
After cancelling an order, you can utilize the WebSocket streams for order history to continuously receive updated information about your orders in real-time.

# Api Request
**Rate Limit: `Allow `900` requests per minute per IP & UID.`**

**`DELETE` /margin/orders/{pair}/{orderId}**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path    | Query | Type   | Required | Description                                                                                                               | Default | Range | Example    |
| :------------------ | :------ | :---- | :----- | :------- | :------------------------------------------------------------------------------------------------------------------------ | :------ | :---- | :--------- |
| X-BITOPRO-APIKEY    |         |       | string | Yes      | API Key                                                                                              |         |       |            |
| X-BITOPRO-PAYLOAD   |         |       | string | Yes      | Payload                                                                                              |         |       |            |
| X-BITOPRO-SIGNATURE |         |       | string | Yes      | Signature                                                                                          |         |       |            |
|                     | pair    |       | string | Yes      | The trading pair in format {BASE}_{QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |         |       | btc_usdt   |
|                     | orderId |       | string | Yes      | The id of the order.                                                                                                      |         |       | 9543130812 |

# Api Response

**Response Fields:**

| Field     | Type    | Description                      |
|:----------|:--------|:---------------------------------|
| orderId   | string  | The id of the cancelled order    |
| action    | string  | The action of the order (BUY/SELL) |
| timestamp | integer | The timestamp of cancellation    |
| price     | string  | The price of the cancelled order |
| amount    | string  | The amount of the cancelled order|

**Response Example:**

```javascript
{
    "orderId": "9543130812",
    "action": "BUY",
    "timestamp": 1721376406650,
    "price": "1",
    "amount": "1"
}
```
[Back](../summary.md)