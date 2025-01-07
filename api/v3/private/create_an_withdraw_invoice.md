# Create Withdraw Invoice

Submit withdraw request. Before using this api, you have to setup your withdraw address from this [webpage](https://www.bitopro.com/address).

# Api Request

**Rate limit:**

Allow `60` requests per minute per IP.

**`POST` /wallet/withdraw/{currency}**

**Parameters:**

You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| X-BITOPRO-APIKEY | | | string | Yes | API Key | | | |
| X-BITOPRO-PAYLOAD | | | string | Yes | Payload | | | |
| X-BITOPRO-SIGNATURE | | | string | Yes | Signature | | | |
| | currency | | string | Yes | The currency to withdraw. Please follow the [link](https://www.bitopro.com/fees) to check the currency list. Please provide only currency name without protocol, you can define protocol in request body. | | | twd, usdt, btc or eth |

**Request body:**

| Field | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| protocol | string | No | The protocol to send. USDT have `ERC20`, `OMNI` and `TRX` to choose. | `MAIN` | `MAIN`, `ERC20`, `OMNI`, `TRX`, `BSC`, `POLYGON` | `ERC20` |
| address | string | No | The address or bank account to send fund. Required for non-TWD withdraw. | | | |
| amount | string | Yes | The amount of fund to send. | | | |
| message | string | No | The message or note to be attached with withdraw. For some currencies, it is required, for example, EOS and BNB. | | | |
| bankAccountSerial | string | No | Bank account number for TWD withdrawal | Default to the verified bank account | | 1020000286850710 |
| bankSerial | string | No | Bank code for TWD withdrawal | Default to the verified bank account | | 805 |

# Api Response

**Response Example:**

```javascript
{
  "data": {
    "serial": "20200417TW51258295",
    "currency": "TWD",
    "protocol": "MAIN",
    "address": "64382xx3234",
    "amount": "12353", //amount actually sent
    "fee": "15", //fee deducted from initial amount
    "total": "12368", //total amount deducted
    "message": "test", //may not be included 
    "id": "12368"
  }
}
```

**Response Fields:**

| Field | Type | Description |
| :--- | :--- | :--- |
| serial | string | The unique identifier for the withdrawal transaction |
| currency | string | The currency of the withdrawal |
| protocol | string | The protocol used for the withdrawal |
| address | string | The recipient's address or bank account |
| amount | string | The amount actually sent |
| fee | string | The fee deducted from the initial amount |
| total | string | The total amount deducted (amount + fee) |
| message | string | The attached message (may not be included) |
| id | string | Withdrawal transaction ID |

[Back](../summary.md)