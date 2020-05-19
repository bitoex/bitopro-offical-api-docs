# Create batch limit/market orders

## Create batch limit/market orders

Up to 10 limit/market orders can be created at a time.

## Rate limit

Allow `60` requests per minute per IP.

### `POST` /orders/batch

### Headers

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../authentication.md#signature) |  |  |  |
|

## Parameters

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| action | string | Yes | The action type of the order, should only be `BUY` or `SELL`. |
| amount | string | Yes | The amount of the order for the trading pair, please follow the [link](https://www.bitopro.com/fees) to see the limitations. |
| price | string | Yes | The price of the order for the trading pair. |
| timestamp | integer | Yes | The client timestamp in millisecond. |
| type | string | Yes | The order type, should only be `LIMIT`, `MARKET`. |
|

## Request sample

```javascript
[{
  pair: "BTC_TWD",
  action: "BUY",
  type: "LIMIT",
  price: "210000",
  amount: "1",
  timestamp: 1504262258000
}, {
  pair: "BTC_TWD",
  action: "SELL",
  type: "MARKET",
  amount: "2",
  timestamp: 1504262258000
}]
```

### Response sample

```javascript
{
  "data": [{
    "orderId": 1234567890,
    "action": "BUY",
    "price": "210000",
    "amount": "1",
    "timestamp": 1504262258000
  }, {
    "orderId": 3234567891,
    "action": "SELL",
    "amount": "2",
    "timestamp": 1504262258000
  }]
}
```

[Back](../rest.md)

