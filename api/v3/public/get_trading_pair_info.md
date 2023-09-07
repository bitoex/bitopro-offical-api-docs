# Get Trading Pair Info

Get a list of pairs available for trade.

# Api Request

**`GET` /provisioning/trading-pairs**

# Api Response

**Response Example:**

```javascript
{
  "data": [
    {
      "pair": "mv_twd",
      "base": "mv",
      "quote": "twd",
      "basePrecision": "8",
      "quotePrecision": "3",
      "minLimitBaseAmount": "0.01",
      "maxLimitBaseAmount": "100000",
      "minMarketBuyQuoteAmount": "3",
      "orderOpenLimit": "200",
      "maintain": false,
      "orderBookQuotePrecision": "3",
      "orderBookQuoteScaleLevel": "5",
      "amountPrecision": "2"
    },
    {
      "pair": "ape_usdt",
      "base": "ape",
      "quote": "usdt",
      "basePrecision": "8",
      "quotePrecision": "4",
      "minLimitBaseAmount": "1",
      "maxLimitBaseAmount": "10000000",
      "minMarketBuyQuoteAmount": "5",
      "orderOpenLimit": "200",
      "maintain": false,
      "orderBookQuotePrecision": "4",
      "orderBookQuoteScaleLevel": "4",
      "amountPrecision": "4"
    }
  ]
}
```
[Back](../summary.md)