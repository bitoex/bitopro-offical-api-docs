# Get OTC Price
Get otc currency buy and sell price

# Api Request

**`GET` /v3/price/otc/{currency}**

**Parameters:**

| Header | Path | Query | Type   | Required | Description | Default | Range | Example |
| :----- | :--- | :---- | :----- | :------- | :--------------------------------------------------------------------------------------------------------------------------- | :------ | :---- | :-------- |
|        | currency |      | string | Yes   |  |  | | btc |

# Api Response

**Response Example:**
```javascript
{
    "currency": "btc",
    "buySwapQuotation": {
        "twd": {
            "pricingCurrency": "TWD",
            "exchangeRate": "1130752.513945"
        }
    },
    "sellSwapQuotation": {
        "twd": {
            "pricingCurrency": "TWD",
            "exchangeRate": "1107699.219"
        }
    }
}
```
[Back](../summary.md)