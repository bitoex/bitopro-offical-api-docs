# List User Transfers

This API retrieves the user's transfer history between different account types.

## API Request

**`GET` /history/user-transfers**

## API Response

The response provides a list of transfer records and the total number of transfer transactions.

### Response Fields:

| Field                  | Type    | Description                                     |
|:-----------------------|:--------|:------------------------------------------------|
| transferInvoices       | array   | List of transfer records                        |
| transferInvoicesAmount | integer | Total number of transfer transactions           |

### Transfer Record Fields:

| Field     | Type    | Description                                                 |
|:----------|:--------|:------------------------------------------------------------|
| serial    | string  | Unique identifier for the transfer transaction              |
| currency  | string  | The currency code of the transfer                           |
| from      | integer | The source account type                                     |
| to        | integer | The destination account type                                |
| amount    | string  | The amount transferred                                      |
| status    | integer | Status of the transfer (2: completed)                       |
| timestamp | integer | Unix timestamp of when the transfer was made                |

### Response Example:

```javascript
{
    "transferInvoices": [
        {
            "serial": "20240730margintrans03620885",
            "currency": "USDT",
            "from": 1,
            "to": 3,
            "amount": "10",
            "status": 2,
            "timestamp": 1722326393
        },
        {
            "serial": "20240722margintrans72834842",
            "currency": "BTC",
            "from": 1,
            "to": 3,
            "amount": "1",
            "status": 2,
            "timestamp": 1721629204
        },
        // ... more transfer records ...
    ],
    "transferInvoicesAmount": 39
}
```

In this example:
- The transfers are listed in reverse chronological order.
- Account type 1 typically represents the spot account, while 3 represents the margin account.
- All transfers shown have a status of 2, indicating they were completed successfully.

[Back](../summary.md)