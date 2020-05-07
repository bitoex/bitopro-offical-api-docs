# Withdraw

## `POST` /wallet/withdraw

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY |  |  | string | Yes | [API Key](../authentication.md#api-key) |  |  |  |
| X-BITOPRO-PAYLOAD |  |  | string | Yes | [Payload](../authentication.md#payload) |  |  |  |
| X-BITOPRO-SIGNATURE |  |  | string | Yes | [Signature](../authentication.md#signature) |  |  |  |


## Request body

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| currency | string | Yes | The currency to send.|
| protocol | string | No | The protocol to send. Allowed values: MAIN, ERC20, OMNI, BNB. Default: MAIN. USDT have ERC20 and OMNI to choose. |
| address | string | Yes | The address or bank account to send fund. |
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
      "amount": "12353",
      "message": "test" //may not be included 
    }
}
```

[Back](../rest.md)

