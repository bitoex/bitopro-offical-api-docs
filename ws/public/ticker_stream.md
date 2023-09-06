# Ticker Data Stream
Ticker pushed 24hr rollwing window statistics when updated.

# Ws Request
**`GET` wss://stream.bitopro.com:443/ws/v1/pub/tickers/{pair}**

**Request:**

| Path | Query | Type   | Description                                                                            |
| :--- | :---- | :----- | :------------------------------------------------------------------------------------- |
| pair |       | string | Uppercase string literal of a pair. e.g. `BTC_TWD`                                     |
|      | pairs | string | The same with `pair`, multi pairs are comma-delimited. e.g. `BTC_TWD,ETH_TWD,BITO_ETH` |

# Ws Response

**Response:**

| Field           | Type         | Description                                                           |
| :-------------- | :----------- | :-------------------------------------------------------------------- |
| event           | string       | String literal for event name                                         |
| pair            | string       | Uppercase string underscore-delimited literal of a pair of currencies |
| isBuyer         | boolean      |                                                                       |
| priceChange24hr | string       |                                                                       |
| volume24hr      | string       |                                                                       |
| high24hr        | string       |                                                                       |
| low24hr         | string       |                                                                       |
| timestamp       | long integer | Unix Timestamp in milliseconds (seconds * 1000)                       |
| datetime        | string       | ISO8601 datetime string with milliseconds                             |

**Response Example with Pair:**
```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/tickers/BTC_TWD

{
  "event": "TICKER",
  "pair": "BTC_TWD",
  "lastPrice": "1",
  "isBuyer": true,
  "priceChange24hr": "1",
  "volume24hr": "1",
  "high24hr": "1",
  "low24hr": "1",
  "timestamp": 1136185445000,
  "datetime": "2006-01-02T15:04:05.700Z"
}
```

**Response Example with Multiple Pair:**
```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/tickers?pairs=BTC_TWD,BITO_ETH

{
    "event": "TICKER",
    "pair": "BTC_TWD",
    "lastPrice": "1",
    "isBuyer": true,
    "priceChange24hr": "1",
    "volume24hr": "1",
    "high24hr": "1",
    "low24hr": "1",
    "timestamp": 1136185445000,
    "datetime": "2006-01-02T15:04:05.700Z"
  },
  {
    "event": "TICKER",
    "pair": "BITO_ETH",
    "lastPrice": "1",
    "isBuyer": true,
    "priceChange24hr": "1",
    "volume24hr": "1",
    "high24hr": "1",
    "low24hr": "1",
    "timestamp": 1136185445000,
    "datetime": "2006-01-02T15:04:05.700Z"
  }
```
[Back](../summary.md)
