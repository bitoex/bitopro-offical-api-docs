# Trade Stream
Trade pushed full data when updated.

# Ws Request
**`GET` wss://stream.bitopro.com:443/ws/v1/pub/trades/{pair}**

**Request**

| Path | Query | Type   | Description                                                                            |
| :--- | :---- | :----- | :------------------------------------------------------------------------------------- |
| pair |       | string | Uppercase string literal of a pair. e.g. `BTC_TWD`                                     |
|      | pairs | string | The same with `pair`, multi pairs are comma-delimited. e.g. `BTC_TWD,ETH_TWD,BITO_ETH` |

# Ws Response

**Response**

| \#   | Field     | Type         | Description                                                           |
| :--- | :-------- | :----------- | :-------------------------------------------------------------------- |
| 0    | event     | string       | String literal for event name                                         |
| 0    | eventID   | string       | event id for debug usage |
| 0    | pair      | string       | Uppercase string underscore-delimited literal of a pair of currencies |
| 0    | timestamp | long integer | Unix Timestamp in milliseconds (seconds * 1000)                       |
| 0    | datetime  | string       | ISO8601 datetime string with milliseconds                             |
| 0    | data      | object array |                                                                       |
| 1    | timestamp | long integer | Unix Timestamp in milliseconds                                        |
| 1    | price     | string       |                                                                       |
| 1    | amount    | string       |                                                                       |
| 1    | isBuyer   | boolean      |                                                                       |



**Response Example with Pair:**

```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/trades/BTC_TWD

{
  "event": "TRADE",
  "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
  "pair": "BTC_TWD",
  "timestamp": 1136185445000,
  "datetime": "2006-01-02T15:04:05.700Z",
  "data": [
    {
      "timestamp": 1136185445,
      "price": "1",
      "amount": "1",
      "isBuyer": false
    },
    {
      "timestamp": 1136185445,
      "price": "1",
      "amount": "1",
      "isBuyer": true
    }
    ...
  ]
}
```

**Response Example with Multiple Pairs:**

```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/trades?pairs=BTC_TWD,BITO_ETH

{
    "event": "TRADE",
    "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
    "pair": "BTC_TWD",
    "timestamp": 1136185445000,
    "datetime": "2006-01-02T15:04:05.700Z",
    "data": [
      {
        "timestamp": 1136185445,
        "price": "1",
        "amount": "1",
        "isBuyer": false
      },
      {
        "timestamp": 1136185445,
        "price": "1",
        "amount": "1",
        "isBuyer": true
      }
      ...
    ]
  },
  {
    "event": "TRADE",
    "eventID": "88038887-1de1-4521-b411-93440156cb41",
    "pair": "BITO_ETH",
    "timestamp": 1136185445000,
    "datetime": "2006-01-02T15:04:05.700Z",
    "data": [
      {
        "timestamp": 1136185445,
        "price": "1",
        "amount": "1",
        "isBuyer": false
      },
      {
        "timestamp": 1136185445,
        "price": "1",
        "amount": "1",
        "isBuyer": true
      }
      ...
    ]
  }
```
[Back](../summary.md)