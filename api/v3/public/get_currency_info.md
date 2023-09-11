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
      "currency": "TWD",
      "withdrawFee": "15",
      "minWithdraw": "100",
      "maxWithdraw": "1000000",
      "maxDailyWithdraw": "2000000",
      "withdraw": true,
      "deposit": true,
      "depositConfirmation": "0"
    },
    {
      "currency": "USDT (ETH-ERC20)",
      "withdrawFee": "10",
      "minWithdraw": "10",
      "maxWithdraw": "300000",
      "maxDailyWithdraw": "500000",
      "withdraw": true,
      "deposit": true,
      "depositConfirmation": "64"
    },
    {
      "currency": "USDT (BSC-BEP20)",
      "withdrawFee": "0.3",
      "minWithdraw": "10",
      "maxWithdraw": "300000",
      "maxDailyWithdraw": "500000",
      "withdraw": true,
      "deposit": true,
      "depositConfirmation": "15"
    }
  ]
}
```
[Back](../summary.md)