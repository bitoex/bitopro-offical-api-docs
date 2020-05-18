# Withdraw

## `POST` /wallet/withdraw

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../authentication.md#signature) |  |  |  |
|  | currency |  | string | Yes | The currency to withdraw. Please follow the [link](https://www.bitopro.com/fees) to check the currency list. |  |  | twd |

## Request body

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| protocol | string | No | The protocol to send. Allowed values: MAIN, ERC20, OMNI. Default: MAIN. USDT have ERC20 and OMNI to choose. |
| address | string | No | The address or bank account to send fund. Required for non-TWD withdraw.|
| amount | string | Yes | The amount of fund to send. |
| message | string | No | The message or note to be attached with withdraw. For some currencies, it is required. For example EOS and BNB.|


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
      "total": "12368", //total amount deducted
      "message": "test" //may not be included 
    }
}
```

[Back](../rest.md)

