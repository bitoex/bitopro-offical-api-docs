# Get Currency Info

Get the list of currencies available and information for each currency

# Api Request

**`GET` /provisioning/currencies**

# Api Response

**Response Example:**

```javascript
{
  "data": [
    {
      "currency": "mith",
      "deposit": true,
      "depositConfirmation": "20",
      "maxDailyWithdraw": "500000",
      "maxWithdraw": "200000",
      "minWithdraw": "30",
      "withdraw": true,
      "withdrawFee": "2"
    },
    {
      "currency": "trx",
      "deposit": true,
      "depositConfirmation": "20",
      "maxDailyWithdraw": "500000",
      "maxWithdraw": "200000",
      "minWithdraw": "300",
      "withdraw": true,
      "withdrawFee": "25"
    }
  ]
}
```
[Back](../summary.md)