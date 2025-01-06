# Cancel Batch Margin Orders

Cancel multiple margin orders by given group of order ids.

# Api Request:
**`PUT` /margin/orders**

Send a json format request to cancel multiple margin orders at a time.

**Rate limit:**
Allow `2` requests per second per IP.

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query | Type   | Required | Description                       | Default | Range | Example |
| :------------------ | :--- | :---- | :----- | :------- | :-------------------------------- | :------ | :---- | :------ |
| X-BITOPRO-APIKEY    |      |       | string | Yes      | API Key     |         |       |         |
| X-BITOPRO-PAYLOAD   |      |       | string | Yes      | Payload    |         |       |         |
| X-BITOPRO-SIGNATURE |      |       | string | Yes      | Signature|         |       |         |

**Request Body:**

The request body should be a JSON object where each key is a trading pair, and the value is an array of order ids to be cancelled for that pair.

**Request Example:**

```javascript
{
    "BTC_USDT": [
        "4419989207",
        "9789414023"
    ]
}
```

# Api Response:

The response will be a JSON object containing a "data" field. The "data" field will contain key-value pairs where the key is the trading pair and the value is an array of successfully cancelled order ids.

**Response Example:**

```javascript
{
    "data": {
        "BTC_USDT": [
            "4419989207",
            "9789414023"
        ]
    }
}
```
[Back](../summary.md)