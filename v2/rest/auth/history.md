# ~Get order history~

# V2 End-of-life (2021-06-30)
**We have already stopped any mantainance support on v2 API. We have scheduled to remove v2 API completely on 2021-06-30. Please migrate your program to you v3 ASAP.**

## `GET` /orders/history

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key]() |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload]() |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature]() |  |  |  |

## Response sample

```javascript
{
  "data": [
    {
      "action": "BUY",
      "avgExecutionPrice": "100000.00000000",
      "bitoFee": "0.00000000",
      "executedAmount": "1.00000000",
      "fee": "0.00100000",
      "feeSymbol": "BTC",
      "id": "123",
      "originalAmount": "1.00000000",
      "pair": "btc_twd",
      "price": "100000.00000000",
      "remainingAmount": "0.00000000",
      "status": 2,
      "timestamp": 1508753757000,
      "type": "LIMIT",
      "total": "123.00"
    },
    {
      "action": "BUY",
      "avgExecutionPrice": "100000.00000000",
      "bitoFee": "0.00000000",
      "executedAmount": "1.00000000",
      "fee": "0.00200000",
      "feeSymbol": "BTC",
      "id": "456",
      "originalAmount": "1.00000000",
      "pair": "btc_twd",
      "price": "100000.00000000",
      "remainingAmount": "0.00000000",
      "status": 2,
      "timestamp": 1508753787000,
      "type": "LIMIT",
      "total": "123.00"
    }
  ]
}
```

[Back](../rest.md)

