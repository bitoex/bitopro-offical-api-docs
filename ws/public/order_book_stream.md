# OrderBook Stream
Order book pushed all data every second when updated. You can specifiy one or more pairs and the default limit is 5. Valid limit values are **1**, **5**, **10**, **20**, **30** or **50**.

# Ws Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/order-books/{pair}**

**Parameters:**
| Path | Query | Type   | Description                                                                                              |
| :--- | :---- | :----- | :------------------------------------------------------------------------------------------------------- |
| pair |       | string | Uppercase string literal of a pair, you can optionally a colon with limit. e.g. `BTC_TWD` or `BTC_TWD:5` |
|      | pairs | string | The same with `pair`, multi pairs are comma-delimited. e.g. `BTC_TWD:1,ETH_TWD:20,BITO_ETH`              |

# Ws Response
**Response:**

| 0    | Field     | Type         | Description                                                           |
| :--- | :-------- | :----------- | :-------------------------------------------------------------------- |
| 0    | event     | string       | String literal for event name                                         |
| 0    | eventID           | string  | event id for debug usage |
| 0    | pair      | string       | Uppercase string underscore-delimited literal of a pair of currencies |
| 0    | bids      | object array |                                                                       |
| 0    | asks      | object array |                                                                       |
| 0    | timestamp | long integer | Unix Timestamp in milliseconds (seconds * 1000)                       |
| 0    | datetime  | string       | ISO8601 datetime string with milliseconds                             |
| 1    | price     | string       |                                                                       |
| 1    | amount    | string       |                                                                       |
| 1    | count     | integer      |                                                                       |
| 1    | total     | string       | Total amount                                                          |


**Response Example With Pair:**

```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/order-books/BTC_TWD

{
  "event": "ORDER_BOOK",
  "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
  "pair": "BTC_TWD",
  "bids": [
    {
      "price": "1",
      "amount": "1",
      "count": 1,
      "total": "1"
    }
    ...
  ],
  "asks": [
    {
      "price": "0.9",
      "amount": "1",
      "count": 2,
      "total": "2"
    }
    ...
  ],
  "timestamp": 1136185445000,
  "datetime": "2006-01-02T15:04:05.700Z"
}
```

**Response Example With Multiple Pairs:**

```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/order-books?pairs=BTC_TWD,ETH_TWD

{
  "event": "ORDER_BOOK",
  "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
  "pair": "BTC_TWD",
  "bids": [
    {
      "price": "1",
      "amount": "1",
      "count": 1,
      "total": "1"
    }
    ...
  ],
  "asks": [
    {
      "price": "0.9",
      "amount": "1",
      "count": 2,
      "total": "2"
    }
    ...
  ],
  "timestamp": 1136185445000,
  "datetime": "2006-01-02T15:04:05.700Z"
},
{
  "event": "ORDER_BOOK",
  "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
  "pair": "ETH_TWD",
  "bids": [
    {
      "price": "1",
      "amount": "1",
      "count": 1,
      "total": "1"
    }
    ...
  ],
  "asks": [
    {
      "price": "0.9",
      "amount": "1",
      "count": 2,
      "total": "2"
    }
    ...
  ],
  "timestamp": 1136185445000,
  "datetime": "2006-01-02T15:04:05.700Z"
}
```

**Response Example With Pair And Limit:**

```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/order-books/BTC_TWD:1

{
  "event": "ORDER_BOOK",
  "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
  "pair": "BTC_TWD",
  "bids": [
    {
      "price": "1",
      "amount": "1",
      "count": 1,
      "total": "1"
    }
    ...
  ],
  "asks": [
    {
      "price": "0.9",
      "amount": "1",
      "count": 2,
      "total": "2"
    }
    ...
  ],
  "timestamp": 1136185445000,
  "datetime": "2006-01-02T15:04:05.700Z"
}
```

**Response Example With Multiple Pairs And Limit:**

```javascript
GET wss://stream.bitopro.com:443/ws/v1/pub/order-books?pairs=BTC_TWD:1,ETH_TWD:1

{
    "event": "ORDER_BOOK",
    "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
    "pair": "BTC_TWD",
    "bids": [
      {
        "price": "1",
        "amount": "1",
        "count": 1,
        "total": "1"
      }
      ...
    ],
    "asks": [
      {
        "price": "0.9",
        "amount": "1",
        "count": 2,
        "total": "2"
      }
      ...
    ],
    "timestamp": 1136185445000,
    "datetime": "2006-01-02T15:04:05.700Z"
  },
  {
    "event": "ORDER_BOOK",
    "eventID": "88038887-1de1-4521-b411-93440156cb41",
    "pair": "ETH_TWD",
    "bids": [
      {
        "price": "1",
        "amount": "1",
        "count": 1,
        "total": "1"
      }
      ...
    ],
    "asks": [
      {
        "price": "0.9",
        "amount": "1",
        "count": 2,
        "total": "2"
      }
      ...
    ],
    "timestamp": 1136185445000,
    "datetime": "2006-01-02T15:04:05.700Z"
  }
```
[Back](../summary.md)
