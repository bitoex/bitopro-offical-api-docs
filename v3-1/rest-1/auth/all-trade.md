# Get trade list

### `GET` /orders/trades/{pair}

### Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../authentication.md#signature) |  |  |  |
|  | pair |  | string | Yes | The trading pair in format ${BASE}\_${QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |  |  | bito\_eth |
|  |  | startTimestamp | integer | No | The start timestamp in unix timestap (miliesceond). | 90 days from the end timestamp  |  | 1592203563000 |
|  |  | endTimestamp | integer | No | The end timestamp in unix timestap (miliesceond). | present timestamp  | | 1592203563000 |
|  |  | orderId | string | No | The id of the order.	 | | | 6995795641 |
|  |  | tradeId | string | No | The id of the first trade in the response. It can serve as an offset when it's sent as an id of the last data from the previous response. | | | 8473494907 |
|  |  | limit | integer | No | The limit for the response. | 100 | min:0, max:1000 | 100 |

### Response sample

```javascript
{
    "data": [
        {
            "tradeId": "8473494907",
            "orderId": "6995795641",
            "price": "10000",
            "action": "BUY",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "0.00015",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1611040629306
        },
        {
            "tradeId": "8473494907",
            "orderId": "1872654036",
            "price": "10000",
            "action": "SELL",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "5.5",
            "feeSymbol": "btc",
            "isTaker": true,
            "timestamp": 1611040629306
        },
        {
            "tradeId": "3350353302",
            "orderId": "6995795641",
            "price": "10000",
            "action": "BUY",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "0.00015",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1611042308542
        },
        {
            "tradeId": "3350353302",
            "orderId": "6749512430",
            "price": "10000",
            "action": "SELL",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "5.5",
            "feeSymbol": "btc",
            "isTaker": true,
            "timestamp": 1611042308542
        },
        {
            "tradeId": "8227211696",
            "orderId": "1626370825",
            "price": "10000",
            "action": "BUY",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "0.00015",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1611298410074
        },
        {
            "tradeId": "8227211696",
            "orderId": "6503229219",
            "price": "10000",
            "action": "SELL",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "5.5",
            "feeSymbol": "btc",
            "isTaker": true,
            "timestamp": 1611298410074
        },
        {
            "tradeId": "3104070091",
            "orderId": "6256946008",
            "price": "30000",
            "action": "BUY",
            "baseAmount": "0.2",
            "quoteAmount": "6000",
            "fee": "0.00006",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1611298671831
        },
        {
            "tradeId": "3104070091",
            "orderId": "1133804403",
            "price": "30000",
            "action": "SELL",
            "baseAmount": "0.2",
            "quoteAmount": "6000",
            "fee": "6.6",
            "feeSymbol": "btc",
            "isTaker": true,
            "timestamp": 1611298671831
        },
        {
            "tradeId": "2857786880",
            "orderId": "6256946008",
            "price": "30000",
            "action": "BUY",
            "baseAmount": "0.8",
            "quoteAmount": "24000",
            "fee": "0.00024",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1611808383670
        },
        {
            "tradeId": "2793300274",
            "orderId": "1380087614",
            "price": "20000",
            "action": "BUY",
            "baseAmount": "1",
            "quoteAmount": "20000",
            "fee": "0.0003",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1615195177461
        },
        {
            "tradeId": "7670158668",
            "orderId": "1626370825",
            "price": "10000",
            "action": "BUY",
            "baseAmount": "0.5",
            "quoteAmount": "5000",
            "fee": "0.00015",
            "feeSymbol": "btc",
            "isTaker": false,
            "timestamp": 1615195177461
        }
    ]
}
```

[Back](../rest.md)

