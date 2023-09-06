# Get User Balance

Fetch your spot wallet balances.

> If you require real-time updates or a high-frequency trading environment, we recommend using the websocket account balance api. For more details, please refer to this [link](web-socket-api_V3.md/#account-balance-stream).


# Api Request

**`GET` /accounts/balance**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../README.md#api-security-protocol).

| Header              | Path | Query | Type   | Required | Description                       | Default | Range | Example |
| :------------------ | :--- | :---- | :----- | :------- | :-------------------------------- | :------ | :---- | :------ |
| X-BITOPRO-APIKEY    |      |       | string | Yes      | API Key     |         |       |         |
| X-BITOPRO-PAYLOAD   |      |       | string | Yes      | Payload     |         |       |         |
| X-BITOPRO-SIGNATURE |      |       | string | Yes      | Signature |         |       |         |

# Api Response

**Response Example:**
```javascript
{
  "data": [
    {
      "amount": "10001",
      "available": "1.0",
      "currency": "bito",
      "stake": "10000",
      "tradable": true
    },
    {
      "amount": "0.0",
      "available": "1.0",
      "currency": "btc",
      "stake": "0",
      "tradable": true
    },
    {
      "amount": "3.0",
      "available": "0.01",
      "currency": "eth",
      "stake": "0",
      "tradable": true
    },
    {
      "amount": "30000",
      "available": "2500",
      "currency": "twd",
      "stake": "0",
      "tradable": true
    },
    {
      "amount": "30000",
      "available": "2500",
      "currency": "npxs",
      "stake": "0",
      "tradable": false
    }
  ]
}
```
[Back](../summary.md)
