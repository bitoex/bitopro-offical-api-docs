# List User Borrow History

This API retrieves the user's borrowing history in the margin trading system.

# Api Request

**`GET` /margin/user-borrows**

# Api Response

The response provides a list of borrowing records and the total number of borrow transactions.

**Response Fields:**

| Field        | Type    | Description                                     |
|:-------------|:--------|:------------------------------------------------|
| borrows      | array   | List of borrowing records                       |
| borrowsAmount| integer | Total number of borrowing transactions          |

**Borrow Record Fields:**

| Field     | Type    | Description                                                                              |
|:----------|:--------|:-----------------------------------------------------------------------------------------|
| serial    | integer | Unique identifier for the borrowing transaction                                          |
| currency  | string  | The borrowed currency code                                                               |
| amount    | string  | The borrowed amount                                                                      |
| status    | integer | Status of the borrow (1: repay uncompleted, 2: repay completed)                          |
| timestamp | integer | Unix timestamp of the borrowing transaction                                              |

**Response Example:**

```javascript
{
    "borrows": [
        {
            "serial": 5891294291,
            "currency": "BTC",
            "amount": "100",
            "status": 2,
            "timestamp": 1712133627
        },
        {
            "serial": 8853455066,
            "currency": "USDT",
            "amount": "10,000",
            "status": 2,
            "timestamp": 1713345752
        },
        {
            "serial": 9888177692,
            "currency": "BTC",
            "amount": "1",
            "status": 2,
            "timestamp": 1715309159
        },
        {
            "serial": 2548487188,
            "currency": "BTC",
            "amount": "1.5",
            "status": 1,
            "timestamp": 1715323562
        },
        {
            "serial": 7909679636,
            "currency": "BTC",
            "amount": "1",
            "status": 1,
            "timestamp": 1716932630
        },
        {
            "serial": 2349539678,
            "currency": "BTC",
            "amount": "1",
            "status": 1,
            "timestamp": 1717125175
        },
        {
            "serial": 815586174,
            "currency": "BTC",
            "amount": "2",
            "status": 1,
            "timestamp": 1717568493
        },
        {
            "serial": 9404725381,
            "currency": "USDT",
            "amount": "2",
            "status": 1,
            "timestamp": 1718958188
        },
        {
            "serial": 8572772258,
            "currency": "USDT",
            "amount": "15",
            "status": 1,
            "timestamp": 1721292677
        }
    ],
    "borrowsAmount": 9
}
```

[Back](../summary.md)