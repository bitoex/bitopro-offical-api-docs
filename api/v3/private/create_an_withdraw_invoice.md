# Create Withdraw Invoice API

## Overview

- **API Name**: Create Withdraw Invoice
- **Type**: RESTful
- **Endpoint**: POST /v3/wallet/withdraw/{currency}

Submit withdraw request. Before using this api, you have to setup your withdraw address from this [webpage](https://www.bitopro.com/address).

## Request Details

### Rate Limit

Allow 60 requests per minute per IP.

### Endpoint

```
POST /wallet/withdraw/{currency}
```

### Headers

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| X-BITOPRO-APIKEY | string | Yes | API Key |
| X-BITOPRO-PAYLOAD | string | Yes | Payload |
| X-BITOPRO-SIGNATURE | string | Yes | Signature |

Note: You can find how to create payload and signature from [authentication document](../../../README.md#api-security-protocol).

### Path Parameters

| Parameter | Type | Required | Description | Possible Values |
|-----------|------|----------|-------------|-----------------|
| currency | string | Yes | The currency to withdraw. Please follow the [link](https://www.bitopro.com/fees) to check the currency list. Provide only the currency name without protocol; you can define protocol in request body. | twd, usdt, btc, eth |

### Request Body

| Field | Type | Required | Description | Default | Possible Values | Example |
|-------|------|----------|-------------|---------|-----------------|---------|
| protocol | string | No | The protocol to send. USDT has `ERC20`, `OMNI`, and `TRX` to choose from. | `MAIN` | `MAIN`, `ERC20`, `OMNI`, `TRX`, `BSC`, `POLYGON` | `ERC20` |
| address | string | No | The address or bank account to send funds. Required for non-TWD withdrawals. | | | |
| amount | string | Yes | The amount of funds to send. | | | |
| message | string | No | The message or note to be attached to the withdrawal. Required for some currencies (e.g., EOS and BNB). | | | |
| bankAccountSerial | string | No | Bank account number for TWD withdrawal | Default to the verified bank account | | 0000028506119385 |
| bankSerial | string | No | Bank code for TWD withdrawal | Default to the verified bank account | | 004 |

## Response

### Response Example

```javascript
{
  "data": {
    "serial": "20200417TW51258295",
    "currency": "TWD",
    "protocol": "MAIN",
    "address": "64382xx3234",
    "amount": "12353", // amount actually sent
    "fee": "15", // fee deducted from initial amount
    "total": "12368", // total amount deducted
    "message": "test", // may not be included 
    "id": "12368"
  }
}
```

### Response Fields

| Field | Description |
|-------|-------------|
| serial | The unique identifier for the withdrawal transaction |
| currency | The currency of the withdrawal |
| protocol | The protocol used for the withdrawal |
| address | The recipient's address or bank account |
| amount | The amount actually sent |
| fee | The fee deducted from the initial amount |
| total | The total amount deducted (amount + fee) |
| message | The attached message (may not be included) |
| id | Withdrawal transaction ID |

[Back](../summary.md)