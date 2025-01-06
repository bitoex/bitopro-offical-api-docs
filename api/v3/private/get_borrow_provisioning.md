# Get Borrow Provisioning

This API retrieves the leverage settings information for different cryptocurrencies.

# Api Request

**`GET` /margin/provisioning/borrow**

# Api Response

The response is a JSON object where each key represents a cryptocurrency code, and the value is an object containing the borrow provisioning details for that cryptocurrency.

**Response Fields:**

| Field                       | Type    | Description                                                                             |
|:----------------------------|:--------|:----------------------------------------------------------------------------------------|
| currency                    | string  | The cryptocurrency code                                                                 |
| maxSystemAmount             | string  | The maximum amount that can be borrowed from the platform                               |
| maxUserAmount               | string  | The maximum amount a single user can borrow                                             |
| systemBorrowedAmount        | string  | The amount already borrowed from the platform                                           |
| systemAvailableBorrowAmount | string  | The remaining amount available for borrowing from the platform                          |
| borrowStatus                | integer | Whether borrowing is available for this currency (0: off, 1: on, 2: under maintenance)  |
| transferStatus              | integer | Whether transfer to margin account as collateral is allowed (0: off, 1: on, 2: under maintenance) |
| annualInterestPercentage    | string  | Current annual interest rate percentage (1 represents 1%)                               |

**Response Example:**

```javascript
{
    "BTC": {
        "currency": "BTC",
        "maxSystemAmount": "500.00000000",
        "maxUserAmount": "100",
        "systemBorrowedAmount": "130.00592162",
        "systemAvailableBorrowAmount": "369.99407838",
        "borrowStatus": 1,
        "transferStatus": 1,
        "annualInterestPercentage": "1"
    },
    "ETH": {
        "currency": "ETH",
        "maxSystemAmount": "10000.00000000",
        "maxUserAmount": "100",
        "systemBorrowedAmount": "186.65450087",
        "systemAvailableBorrowAmount": "9813.34549913",
        "borrowStatus": 1,
        "transferStatus": 1,
        "annualInterestPercentage": "1"
    },
    "USDT": {
        "currency": "USDT",
        "maxSystemAmount": "1100000.00000000",
        "maxUserAmount": "800000",
        "systemBorrowedAmount": "256240.33640959",
        "systemAvailableBorrowAmount": "843759.66359041",
        "borrowStatus": 1,
        "transferStatus": 1,
        "annualInterestPercentage": "1"
    }
}
```

[Back](../summary.md)