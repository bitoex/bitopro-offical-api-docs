
# Change Log
| Date       | Version | Description                                                                                                                                                                                       |
| :--------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2024/09/24 | v3.5.17 | Add `orderIDs` query parameter for [List Orders Data](./api/v3/private/get_orders_data.md) api. |
| 2024/05/30 | v3.5.16 | Add `clientID` field into [Open Orders WS stream](./ws/private/open_orders_stream.md) and [History Orders WS stream](./ws/private/history_orders_stream.md) |
| 2024/04/18 | v3.5.15 | Fix [Get Orders Data API](./api/v3/private/get_orders_data.md) and [Get Trades Data API](./api/v3/private/get_trades_data.md) orderID shift and tradeID shift bug, change shift logic from `>=` to `<=`.|
| 2024/03/28 | v3.5.14 | Add [Get Open Orders API](./api/v3/private/get_open_orders_data.md).|
| 2024/01/16 | v3.5.13 | Update [History Orders Ws Stream](./ws/private/history_orders_stream.md) and [Open Orders Ws Stream](./ws/private/open_orders_stream.md), it will only publish updated orders.|
| 2023/10/31 | v3.5.12 | Add [Get OTC Price](./api/v3/public/get_otc_price.md) API.|
| 2023/09/14 | v3.5.11 | Add [User Trade Ws Stream](./ws/private/user_trade_stream.md)|
| 2023/09/08 | v3.5.10 | Add ignoreTimeLimitEnable for [List Orders Data](./api/v3/private/get_orders_data.md) and API documentation structure adjustment.|
| 2023/09/08 | v3.5.10 | Update [Get Currency Info](./api/v3/public/get_currency_info.md) api response with currency protocol and depositConfirmation  |
| 2023/09/08 | v3.5.10 | Increase CreateOrder & BatchCreateOrders & CancelOrder & CancelAllOrders API rate limit                                                                                                           |
| 2023/09/08 | v3.5.10 | Add [History Order Ws Stream](./ws/private/history_orders_stream.md)  |
| 2023/03/28 | v3.5.9  | Add 50 limit for [OrderBook API](restful-api_V3.md/#get-orderbook-data) and [OrderBook WS](web-socket-api_V3.md/#orderbook-stream)                                                                |
| 2022/05/23 | v3.5.8  | Add BSC Protocol for [Withdrawal API](restful-api_V3.md/#create-withdraw-invoice)                                                                                                                 |
| 2022/04/28 | v3.5.7  | Add Percent for [CreateOrder API](restful-api_V3.md/#create-an-order)                                                                                                                             |
| 2022/03/15 | v3.5.6  | Add ClientID for [CreateOrder API](restful-api_V3.md/#create-an-order)                                                                                                                            |
| 2022/02/16 | v3.5.5  | Add [Private Websocket Stream](web-socket-api_V3.md/#private-websocket-stream).                                                                                                                   |
| 2021/12/23 | v3.5.4  | Add [All Trades](restful-api_V3.md/#) auth api.                                                                                                                                                   |
| 2021/12/23 | v3.5.4  | [Cancel multiple orders](restful-api_V3.md/#cancel-batch-orders) and [Cancel all orders](restful-api_V3.md/#cancel-all-orders) to allow `1` requests per second per IP.                           |
| 2021/04/13 | v3.5.3  | Post-only added to [Create Order](restful-api_V3.md/#create-an-order) and [Create batch limit/market orders](restful-api_V3.md/#create-batch-orders) . New order `status` 6 for post-only cancel. |
| 2021/01/21 | v3.5.2  | [All Orders](restful-api_V3.md/#list-orders-data), parameter change. `statusKind` `Done` only include status 2 and 3. New parameter `status` added to retrieve single specified `status`.         |
| 2021/01/05 | v3.5.1  | Support [All Orders](restful-api_V3.md/#list-orders-data), deprecated Order List                                                                                                                  |
| 2020/05/19 | v3.5.0  | Support [Withdraw](restful-api_V3.md/#create-withdraw-invoice) and [Withdraw status](// todo put link) API                                                                                        |
|            |         | Support [Create batch limit/market orders](restful-api_V3.md/#create-batch-orders)                                                                                                                |
| 2020/03/31 | v3.3.0  | Support [Cancel all](restful-api_V3.md/#cancel-all-orders) and [Cancel batch](restful-api_V3.md/#cancel-batch-orders) APIs                                                                        |
| 2019/11/19 | v3.0.0  | Add support for Stop Limit orders. Stop Limit order fields added to all related API response.                                                                                                     |
|            |         | Add `feeSymbol` in [Get order list](restful-api_V3.md/#list-orders-data) is now in lowercase                                                                                                      |
|            |         | Removed Get order history API                                                                                                                                                                     |
|            |         | Removed Get ticker API                                                                                                                                                                            |
|            |         | Add `tradable` to [Get the account balance](restful-api_V3.md/#get-user-balance) API                                                                                                              |