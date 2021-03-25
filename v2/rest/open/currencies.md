# ~Get the list of currencies~

# V2 End-of-life (2021-06-30)
**We have already stopped any mantainance support on v2 API. We have scheduled to remove v2 API completely on 2021-06-30. Please migrate your program to you v3 ASAP.**

### Get the list of currencies available and information for each currency

## `GET` /provisioning/currencies

## Response sample

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

[Back](../rest.md)

