# Cancel All Margin Orders

Cancel all open margin orders. 

> 
After cancelling an order, you can utilize the WebSocket streams for order history to continuously receive updated information about your orders in real-time.

# Api Request

**Rate Limit: `Allow `2` requests per second per IP & UID.`**

**`DELETE` /margin/orders/all or /v3/margin/orders/{pair}**

If you send a request to /v3/margin/orders/all API, it will cancel all your active margin orders of all pairs.

**Rate limit:**
Allow `1` request per second per IP.

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query | Type   | Required | Description                                                                                                               | Default | Range | Example   |
| :------------------ | :--- | :---- | :----- | :------- | :------------------------------------------------------------------------------------------------------------------------ | :------ | :---- | :-------- |
| X-BITOPRO-APIKEY    |      |       | string | Yes      | API Key                                                                                             |         |       |           |
| X-BITOPRO-PAYLOAD   |      |       | string | Yes      | Payload                                    |         |       |           |
| X-BITOPRO-SIGNATURE |      |       | string | Yes      | Signature                              |         |       |           |
|                     | pair |       | string | No       | The trading pair in format {BASE}_{QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |         |       | BTC_USDT |

# Api Response

The response will be a JSON object containing a "data" field. The "data" field will contain key-value pairs where the key is the trading pair and the value is an array of successfully cancelled order ids.

**Response Example:**

```javascript
{
    "data": {
        "BTC_USDT": [
            "9050564390",
            "3927422785"
        ]
    }
}
```
[Back](../summary.md)