# Cancel All orders

## `DELETE` /orders/all or /orders/{pair}

If you send a request to /orders/all API. It will cancel all your active orders of all pairs.

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key]() |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload]() |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](https://github.com/bitoex/bitopro-offical-api-docs/tree/12ea3bcb802087dc9b1cfb281d9cfbfd0de9b670/v3/rest/rest/authentication.md#signature) |  |  |  |
|  | pair |  | string | No | The trading pair in format ${BASE}\_${QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |  |  | bito\_eth |

## Response sample

```javascript
{
  "data": {
    "BTC_USDT": [
      "12234566", // cancelled orders
      "12234567"
    ],
    "ETH_USDT": [
      "44566712",
      "24552212"
    ]
  }
}
```

[Back](../rest.md)

