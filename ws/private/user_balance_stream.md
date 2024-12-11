# Account Balance Stream
This channel pushes account balance message.

Note: When you initially establish a websocket connection, you will receive balance from all currencies. After that, the websocket server will only push the updated balance.

# Ws Request

**`GET` wss://stream.bitopro.com:443/ws/v1/pub/auth/account-balance**

**Authentication For Private Websocket Connection**

    | Security scheme | Header parameter    |
    | :-------------- | :------------------ |
    | API Key         | X-BITOPRO-APIKEY    |
    | Payload         | X-BITOPRO-PAYLOAD   |
    | Signature       | X-BITOPRO-SIGNATURE |
You can find how to create payload and signature from [authentication document](../../README.md#api-security-protocol).



# Ws Response
**Response:**

| 0    | Field     | Type    | Description                                     |
| :--- | :-------- | :------ | :---------------------------------------------- |
| 0    | event     | string  | String literal for event name                   |
| 0    | eventID           | string  | event id for debug usage |
| 0    | timestamp | integer | Unix Timestamp in milliseconds (seconds * 1000) |
| 0    | datetime  | string  | ISO8601 datetime string with milliseconds       |
| 1    | currency  | string  | uppercase string                                |
| 1    | amount    | string  | Total amount                                    |
| 1    | available | string  |                                                 |
| 1    | stake     | string  |                                                 |
| 1    | tradable  | bool    |                                                 |



```javascript
// first message for all currencies
{
    "event": "ACCOUNT_BALANCE",
    "eventID": "dadf4ac1-665a-4f39-a139-ab95da102374",
    "timestamp": 1639553303365,
    "datetime": "2021-12-15T07:28:23.365Z",
    "data": {
        "ADA": {
            "currency": "ADA",
            "amount": "999999999999.99999999",
            "available": "999999999999.99999999",
            "stake": "0",
            "tradable": true
        },
        "ALLN": {
            "currency": "ALLN",
            "amount": "0",
            "available": "0",
            "stake": "0",
            "tradable": false
        },
        "BCD": {
            "currency": "BCD",
            "amount": "0",
            "available": "0",
            "stake": "0",
            "tradable": true
        },
        "BCH": {
            "currency": "BCH",
            "amount": "0",
            "available": "0",
            "stake": "0",
            "tradable": true
        },
        "BCHSV": {
            "currency": "BCHSV",
            "amount": "0",
            "available": "0",
            "stake": "0",
            "tradable": true
        },
        "BITO": {
            "currency": "BITO",
            "amount": "9999799",
            "available": "9999799",
            "stake": "0",
            "tradable": true
        },
        "BNB": {
            "currency": "BNB",
            "amount": "8500",
            "available": "8500",
            "stake": "0",
            "tradable": true
        },
        "BTC": {
            "currency": "BTC",
            "amount": "999999999999.99999999",
            "available": "999999999999.99999999",
            "stake": "0",
            "tradable": true
        },
        "DOGE": {
            "currency": "DOGE",
            "amount": "999999999999.99999999",
            "available": "999999999999.99999999",
            "stake": "0",
            "tradable": true
        },
        "EOS": {
            "currency": "EOS",
            "amount": "0",
            "available": "0",
            "stake": "0",
            "tradable": true
        },
        "MITH": {
            "currency": "MITH",
            "amount": "0",
            "available": "0",
            "stake": "0",
            "tradable": false
        },
        ...
    }
}
// second message for updated balance
{
    "event": "ACCOUNT_BALANCE",
    "eventID": "88038887-1de1-4521-b411-93440156cb41",
    "timestamp": 1639553303365,
    "datetime": "2021-12-15T07:28:23.365Z",
    "data": {
        "ADA": {
            "currency": "ADA",
            "amount": "999999999999.99999999",
            "available": "0",
            "stake": "0",
            "tradable": true
        }
    }
}
```
[Back](../summary.md)