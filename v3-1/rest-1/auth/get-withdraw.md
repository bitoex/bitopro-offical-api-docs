# Get Withdraw Information

## `GET` /wallet/withdraw/{currency}/{serial}

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../authentication.md#signature) |  |  |  |
|  | currency |  | string | Yes | The currency of the withdraw to get. Please follow the [link](https://www.bitopro.com/fees) to check the currency list. |  |  | twd |
|  | serial |  | string | Yes | The serial of the withdraw. |  |  | 20200417TW51258295 |




## Response sample

```javascript
{
  "data": 
    {
      "serial": "20200417TW51258295",
      "currency": "TWD",
      "protocol": "MAIN",
      "address": "64382xx3234",
      "amount": "12353", //amount actually sent
      "fee": "15", //fee deducted from initial amount
      "total": "12368",
      "message": "test" //may not be included 
    }
}
```

[Back](../rest.md)

