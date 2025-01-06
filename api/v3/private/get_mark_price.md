# Get Margin Mark Price

This API retrieves the current mark prices for margin trading.

# Api Request

**`GET` /margin/mark-price**

# Api Response

The response provides a list of cryptocurrencies and their corresponding mark prices.

**Response Fields:**

| Field       | Type   | Description                               |
|:------------|:-------|:------------------------------------------|
| tokenPrices | object | An object containing price data for tokens |

**Token Price Fields:**

| Field    | Type   | Description                      |
|:---------|:-------|:---------------------------------|
| currency | string | The cryptocurrency code          |
| price    | string | The current mark price of the token |

**Response Example:**

```javascript
{
    "tokenPrices": {
        "BTC": {
            "currency": "BTC",
            "price": "66319.99734855"
        },
        "ETH": {
            "currency": "ETH",
            "price": "3442.62213333"
        },
        "USDT": {
            "currency": "USDT",
            "price": "1"
        }
    }
}
```

[Back](../summary.md)