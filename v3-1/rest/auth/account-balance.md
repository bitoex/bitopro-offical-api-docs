# Get the account balance

## `GET` /accounts/balance

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../../../v2-1/rest/authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../../../v2-1/rest/authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../../../v2-1/rest/authentication.md#signature) |  |  |  |

## Response sample

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

[Back](../rest.md)

