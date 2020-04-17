# Cancel multiple orders

## `PUT` /orders

Send a json format request to cancel multiple orders at a time.

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](https://github.com/bitoex/bitopro-offical-api-docs/tree/a48e38825359359965a45c42a035431d6379e53d/v3/rest/authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](https://github.com/bitoex/bitopro-offical-api-docs/tree/a48e38825359359965a45c42a035431d6379e53d/v3/rest/authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](https://github.com/bitoex/bitopro-offical-api-docs/tree/a48e38825359359965a45c42a035431d6379e53d/v3/rest/authentication.md#signature) |  |  |  |
|  | pair |  | string | Yes | The trading pair in format ${BASE}\_${QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |  |  | bito\_eth |
|  | orderId |  | string | Yes | The id of the order. |  |  | 2959906694 |

## Request sample

```javascript
{
  "BTC_USDT": [
    "12234566",
    "12234567"
  ],
  "ETH_USDT": [
    "44566712",
    "24552212"
  ]
}
```

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

