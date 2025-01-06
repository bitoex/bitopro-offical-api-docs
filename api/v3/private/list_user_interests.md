# List User Repays

This API retrieves the user's repayment history in the margin trading system.

# Api Request

**`GET` /margin/user-repays**

# Api Response

The response provides a list of repayment records and the total number of repayment transactions.

**Response Fields:**

| Field        | Type    | Description                                    |
|:-------------|:--------|:-----------------------------------------------|
| repays       | array   | List of repayment records                      |
| repaysAmount | integer | Total number of repayment transactions         |

**Repayment Record Fields:**

| Field                | Type    | Description                                                 |
|:---------------------|:--------|:------------------------------------------------------------|
| serial               | integer | Unique identifier for the repayment transaction             |
| currency             | string  | The currency code of the repayment                          |
| totalRepayAmount     | string  | The total amount repaid (if applicable)                     |
| principalRepayAmount | string  | The amount of principal repaid                              |
| interestRepayAmount  | string  | The amount of interest repaid                               |
| status               | integer | Status of the repayment (1: success)                        |
| timestamp            | integer | Unix timestamp of when the repayment was made               |

**Response Example:**

```javascript
{
    "repays": [
        {
            "serial": 5194488241,
            "currency": "BTC",
            "totalRepayAmount": "0",
            "principalRepayAmount": "8.34235511",
            "interestRepayAmount": "7.38014063",
            "status": 1,
            "timestamp": 1714754343
        },
        {
            "serial": 4948205030,
            "currency": "BTC",
            "totalRepayAmount": "0",
            "principalRepayAmount": "0.00147282",
            "interestRepayAmount": "0.00010464",
            "status": 1,
            "timestamp": 1714756143
        },
        // ... more repayment records ...
    ],
    "repaysAmount": 23
}
```

[Back](../summary.md)