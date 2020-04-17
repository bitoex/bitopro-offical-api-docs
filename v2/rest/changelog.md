# Changelog

| Date | Version | Description |
| :--- | :--- | :--- |
| 2019/10/15 |  | Version 2 API will not be updated unless for bugs and security issues. |
| 2019/10/15 | v2.8.0 | Deprecate [Get order history](changelog.md) API |
| 2019/09/17 | v2.8.0 | Add [Trading hitory](changelog.md) API for fetching candlestick data. |
| 2019/08/20 | v2.7.0 | Add 2 fields for trading pairs to provide more information on Order Book.   1. `orderBookQuotePrecision`: max number of decimal places for quote on Order Book.    2. `orderBookQuoteScaleLevel`: number of levels quote can be scaled on Order Book. |
|  |  | Add `total` field to [Get order history](changelog.md), [Get order list](changelog.md) and [Get an order](changelog.md) response. |
|  |  | Add `scale` to Get order book endpoint to specify scale of return data, default is 0. Valid scale values are different by pair. For more detail, please refer the field `orderBookQuoteScaleLevel` of [Get the list of available pairs](changelog.md). |
| 2019/07/19 | v2.6.0 | Add 2 APIs for getting pairs available for trade and currencies information.   1. [Get trading pairs](changelog.md) for pairs currently open for trade and related information.   2. [Get currencies](changelog.md) for supported currencies and related information. |
| 2019/07/16 | v2.5.4 | The `limit` to [Get order book](changelog.md) endpoint to specify limit of return data, default is 5. Valid limit values are 1, 5, 10 or 20. |
| 2019/06/24 | v2.5.3 | For more reasonable, we add an open order limit to [Create an order](changelog.md) endpoint, the default limit is **200**. Notice that we'll adjust the limit if necessary. |
| 2019/06/10 | v2.5.2 | Add an optional query parameter `limit` to [Get order book](changelog.md) endpoint to specify limit of return data, default is -1 will return all of data. |
| 2019/02/02 | v2.3.2 | Modify string enum values to uppercase, such as `action` and `type` for [Create an order](changelog.md), [Cancel an order](changelog.md), [Get an order](changelog.md), [Get order history](changelog.md) and [Get order list](changelog.md). |
|  |  | [Get ticker](changelog.md) Deprecated: Use [Get tickers](changelog.md) instead. |
| 2019/04/30 | v2.3.1 | Replace `base` and `quote` with `pair` in [Get tickers](changelog.md) response structure. |
|  |  | Update response structure of [Get the recent trades](changelog.md) API. |
| 2019/04/26 | v2.3.0 | Add [Get tickers](changelog.md) API. |
| 2019/04/03 | v2.2.1 | Add `stake` field to the [account balance](changelog.md) endpoint, which is the cumulative amount summed by your holding, for more detail, please refer [Holding Bouns Program](https://www.bitopro.com/landing_pages/stake). |
| 2019/04/01 | v2.2.0 | Modify [Create an order](changelog.md) API convention. |
|  |  | Modify [Cancel an order](changelog.md) API convention. |
| 2019/01/25 | v2.0.3 | Add `total` field to the [order-book](changelog.md) endpoint, which is the cumulative amount summed by price according action \(buy: from high to low, sell: from low to high\). |
|  |  | Add parameter `active` to the [get order list](changelog.md) endpoint to specify active\(in progress\) orders only, default is **false**. |
| 2019/01/16 | v2.0.2 | Correct the ambiguous samples for `timestamp`, all align to **millisecond** instead of second. |
|  |  | Merge the parameters `base` and `quote` into `pair` for the CreateOrder and CancelOrder endpoints, i.e. **{ base: 'bito', quote: 'eth' } -&gt; { pair: 'bito\_eth' }**. |
|  |  | Add more description for order status on the field `status`. |

[Back](rest.md)

