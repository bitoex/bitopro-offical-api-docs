# Deprecated Get ticker: Use Get tickers instead

### The ticker is a high level overview of the state of the market. It shows you the current best bid and ask, as well as the last trade price. It also includes information such as daily volume and how much the price has moved over the last day

## `GET` /ticker/{pair}

## Parameters

| Header | Path | Query | Type | Required | Description | Default | Range | Example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | pair |  | string | Yes | The trading pair in format ${BASE}\_${QUOTE}, Please follow the [link](https://www.bitopro.com/fees) to check the pair list. |  |  | bito\_eth |

## Response sample

```javascript
{
  "high": "7000",
  "lastPrice": "7000",
  "low": "6000",
  "timestamp": 1508753757000,
  "volume": "16.7"
}
```

[Back](../rest.md)

