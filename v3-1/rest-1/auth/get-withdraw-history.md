# Get Withdraw History Information

## `GET` /wallet/withdrawHistory/{currency}

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../authentication.md#signature) |  |  |  |
|  | currency |  | string | Yes | The currency of the withdraw to get. Please follow the [link](https://www.bitopro.com/fees) to check the currency list. |  |  | twd |
|  | | startTimestamp | int | No | The start timestamp in unix timestap (miliesceond). | 90 days from the end timestamp | | 1592203563000 |
|  | | endTimestamp | int | No | The end timestamp in unix timestap (miliesceond).  | present timestamp | | 1592203563000 |
|  | | limit | int | No | The limit for the response. | 20 | min:1, max:100 | 30 |
|  |  | id | string | No | The id of the first data in the response. It can serve as an offset when it's sent as an id of the last data from the previous response. |  |  | 3255779687 |
|  |  | statuses | string | No | The status of the withdraw. It is multiple values that are concatenated by a comma. |  | | CANCELLED,WAIT_PROCESS |

- The start timestamp must be less than the end timestamp and the time between the start and end timestamp must be less and equal to 90 days.
- The withdraw status could be `PROCESSING`,`COMPLETE`,`EXPIRED`,`INVALID`,`WAIT_PROCESS`,`WAIT_CONFIRMATION`,`EMAIL_VERIFICATION`,`CANCELLED`.

## Response sample

```javascript
{
    "data": [
        {
            "serial": "20210126BW05262128",
            "timestamp": "1611660419000",
            "address": "2N7sfszCocGkDst3mULPP7JmdctgDWeCpGf",
            "amount": "200000000",
            "fee": "0",
            "total": "200000000",
            "status": "WAIT_PROCESS",
            "txid": "00d618f6ecb5697c674a47cd1a40edf399c99eaeb045f0ff7ab3ee2be6f5",
            "message": "test", //may not be included 
            "protocol": "MAIN",
            "id": "3255779687"
        },
        {
            "serial": "20210126BW21101833",
            "timestamp": "1611660400000",
            "address": "2N7sfszCocGkDst3mULPP7JmdctgDWeCpGf",
            "amount": "300000000",
            "fee": "0",
            "total": "300000000",
            "status": "WAIT_PROCESS",
            "txid": "00e1d6aec3cb40080bace4ec70a3e4ad95af1ca7ca68ef7be02a3f59fcf9",
            "protocol": "MAIN",
            "id": "8378921292"
        },
        {
            "serial": "20210126BW16517260",
            "timestamp": "1611648549000",
            "address": "2N1LFhSACBKCY4cWQoNr11JJzPmWMUXzp3k",
            "amount": "300000000",
            "fee": "0",
            "total": "300000000",
            "status": "WAIT_PROCESS",
            "txid": "02b3309db5b615d77a5658d7426e4a8fcd919b1456afcba025be0b50a523",
            "protocol": "MAIN",
            "id": "3994629320"
        },
        {
            "serial": "20210126BW01177362",
            "timestamp": "1611648540000",
            "address": "2N1LFhSACBKCY4cWQoNr11JJzPmWMUXzp3k",
            "amount": "200000000",
            "fee": "0",
            "total": "200000000",
            "status": "WAIT_PROCESS",
            "txid": "095bf1437f2c0e18e02fba593cec3b0c2588ef1fe256d068371ba7e259ed",
            "protocol": "MAIN",
            "id": "9117770925"
        },
        {
            "serial": "20210126BW66914816",
            "timestamp": "1611648161000",
            "address": "2N1LFhSACBKCY4cWQoNr11JJzPmWMUXzp3k",
            "amount": "100000000",
            "fee": "0",
            "total": "100000000",
            "status": "CANCELLED",
            "txid": "14d7bf233251703cdca17a23a26094b49ab6e209382efa3a14d5efa52470",
            "protocol": "MAIN",
            "id": "4240912531"
        }
    ]
}
```

[Back](../rest.md)

