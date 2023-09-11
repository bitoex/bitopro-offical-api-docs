# ~Get the list of available pairs~

# V2 End-of-life (2021-06-30)
**We have already stopped any mantainance support on v2 API. We have scheduled to remove v2 API completely on 2021-06-30. Please migrate your program to you v3 ASAP.**

### Get a list of pairs available for trade

## `GET` /provisioning/trading-pairs

## Response sample

```javascript
{
  "data": [
    {
      "base": "xem",
      "basePrecision": "8",
      "maintain": false,
      "maxLimitBaseAmount": "100000000",
      "minLimitBaseAmount": "320",
      "minMarketBuyQuoteAmount": "0.15",
      "orderOpenLimit": "200",
      "pair": "xem_eth",
      "quote": "eth",
      "quotePrecision": "6"
    },
    {
      "base": "eth",
      "basePrecision": "8",
      "maintain": false,
      "maxLimitBaseAmount": "100000000",
      "minLimitBaseAmount": "0.16",
      "minMarketBuyQuoteAmount": "0.005",
      "orderOpenLimit": "200",
      "pair": "eth_btc",
      "quote": "btc",
      "quotePrecision": "6"
    }
  ]
}
```

[Back](../rest.md)

