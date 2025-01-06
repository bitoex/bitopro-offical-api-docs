# Get Margin Order Trades

This API retrieves the trade history for margin orders of a specific trading pair.

# Api Request

**`GET` /margin/orders/trades/{pair}**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header              | Path | Query          | Type   | Required | Description                                                                                                                               | Default                        | Range           | Example       |
| :------------------ | :--- | :------------- | :----- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- | :-------------- | :------------ |
| X-BITOPRO-APIKEY    |      |                | string | Yes      | API Key                                                                                                             |                                |                 |               |
| X-BITOPRO-PAYLOAD   |      |                | string | Yes      | Payload                                                                                                             |                                |                 |               |
| X-BITOPRO-SIGNATURE |      |                | string | Yes      | Signature                                                                                                         |                                |                 |               |
|                     | pair |                | string | Yes      | The trading pair in format ${BASE}\_${QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list.              |                                |                 | btc_usdt      |
|                     |      | startTimestamp | int64  | No       | The start timestamp in unix timestap (miliesceond).                                                                                       | 90 days from the end timestamp |                 | 1592203563000 |
|                     |      | endTimestamp   | int64  | No       | The end timestamp in unix timestap (miliesceond).                                                                                         | present timestamp              |                 | 1592203563000 |
|                     |      | orderId        | string | No       | The id of the order.                                                                                                                      |                                |                 | 6995795641    |
|                     |      | tradeId        | string | No       | The id of the first trade in the response. It can serve as an offset when it's sent as an id of the last data from the previous response. If this parameter is included, the response will comprise data with IDs less than or equal to the tradeId provided. |                                |                 | 8473494907    |
|                     |      | limit          | int64  | No       | The limit for the response.                                                                                                               | 100                            | min:0, max:1000 | 100           |

# Api Response

**Response Fields:**

| Field             | Type    | Description                                        |
|:------------------|:--------|:---------------------------------------------------|
| tradeId           | string  | Unique identifier for the trade                    |
| orderId           | string  | Identifier of the order                            |
| price             | string  | Price at which the trade occurred                  |
| action            | string  | Action of the trade (BUY or SELL)                  |
| baseAmount        | string  | Amount of base currency traded                     |
| quoteAmount       | string  | Amount of quote currency traded                    |
| fee               | string  | Fee amount for the trade                           |
| feeSymbol         | string  | Symbol of the currency in which fee was paid       |
| isTaker           | boolean | Whether the trade was a taker order                |
| timestamp         | integer | Timestamp of the trade (deprecated)                |
| createdTimestamp  | integer | Timestamp of when the trade was created            |

**Response Example:**

```javascript
{
    "data": [
        {
            "tradeId": "2567799214",
            "orderId": "6683089851",
            "price": "4",
            "action": "SELL",
            "baseAmount": "1",
            "quoteAmount": "4",
            "fee": "0",
            "feeSymbol": "usdt",
            "isTaker": false,
            "timestamp": 1720680330858,
            "createdTimestamp": 1720680330858
        },
        {
            "tradeId": "3060365636",
            "orderId": "7861191918",
            "price": "1",
            "action": "BUY",
            "baseAmount": "0.00004695",
            "quoteAmount": "0.00004695",
            "fee": "0",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1720680169045,
            "createdTimestamp": 1720680169045
        },
        // ... more trade entries ...
    ]
}
```

[Back](../summary.md)