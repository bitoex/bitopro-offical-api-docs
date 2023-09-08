# Order Matches Stream
This channel pushes messages with history orders.

Note: When you initially establish a websocket connection, you will receive active orders from all trading pairs. After that, the websocket server will only push the updated history orders from the single trading pair.

# Ws Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/auth/user-trades**

**Authentication For Private Websocket Connection**

    | Security scheme | Header parameter    |
    | :-------------- | :------------------ |
    | API Key         | X-BITOPRO-APIKEY    |
    | Payload         | X-BITOPRO-PAYLOAD   |
    | Signature       | X-BITOPRO-SIGNATURE |
You can find how to create payload and signature from [authentication document](../../README.md#api-security-protocol).

# Ws Response

**Response:**

| 0    | Field             | Type    | Description                                                                         |
| :--- | :---------------- | :------ | :---------------------------------------------------------------------------------- |
| 0    | event             | string  | String literal for event name                                                       |
| 0    | timestamp         | integer | Unix Timestamp in milliseconds (seconds * 1000)                                     |
| 0    | datetime          | string  | ISO8601 datetime string with milliseconds                                           |
| 1    | id                | string  |                                                                                     |
| 1    | side              | string  | BUY or SELL                                                                         |
| 1    | price             | string  |                                                                                     |
| 1    | volume            | string  |                                                                                     |
| 1    | fee              | string  | LIMIT, Market or STOP_LIMIT                                                         |
| 1    | feeCurrency  | integer | Unix Timestamp in milliseconds (seconds * 1000)                                     |
| 1    | transactionTimestamp  | integer | Unix Timestamp in milliseconds (seconds * 1000)                                     |
| 1    | eventTimestamp            | integer | [see order status](../../model.md#order-status-explanation)                                      |
| 1    | orderID    | string  |                                                                                     |
| 1    | orderType   | string  |                                                                                     |
| 1    | matchID    | string  |                                                                                     |
| 1    | isMarket         | string  |                                                                                     |
| 1    | isMaker         | string  | stop limit trigger condition                                                        |
 

**Response Example:**

```javascript
{
  "event": "USER_TRADE",
  "timestamp": 1639552073346,
  "datetime": "2021-12-15T07:07:53.346Z",
  "data": {
    "base": "yfi",
    "quote": "twd",
    "side": "ask",
    "price": "50",
    "volume": "0.0001",
    "fee": "0",
    "feeCurrency": "twd",
    "transactionTimestamp": 1690950154,
    "eventTimestamp": 1690950154,
    "orderID": 306553356,
    "orderType": "LIMIT",
    "matchID": "00bac524-223c-44af-8390-73ac43178840",
    "isMarket": false,
    "isMaker": false
  }
}
```
[Back](README.md)