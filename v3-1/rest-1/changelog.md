# Change Log

| Date | Version | Description |
| :--- | :--- | :--- |
| 2021/04/14 | v3.5.4 | In [Get Withdraw](auth/get-withdraw.md), add `timestamp` field and deprecate `datetime` field. Support [Get Withdraw History](auth/get-withdraw-history.md) and [Get Deposit History](auth/get-deposit-history.md).
| 2021/04/13 | v3.5.3 | Post-only added to [Create Order](auth/create-order.md) and [Create batch limit/market orders](auth/create-batch-limitmarket.md) . New order `status` 6 for post-only cancel. |
| 2021/01/21 | v3.5.2 | [All Orders](auth/all-order.md), parameter change. `statusKind` `Done` only include status 2 and 3. New parameter `status` added to retrieve single specified `status`. |
| 2021/01/05 | v3.5.1 | Support [All Orders](auth/all-order.md), deprecated [Order List](auth/order-list.md) |
| 2020/05/19 | v3.5.0 | Support [Withdraw](auth/withdraw.md) and [Withdraw status](auth/get-withdraw.md) API |
|  |  | Support [Create batch limit/market orders](auth/create-batch-limitmarket.md) |
| 2020/03/31 | v3.3.0 | Support [Cancel all](auth/cancel-all.md) and [Cancel batch](auth/cancel-batch.md) APIs |
| 2019/11/19 | v3.0.0 | Add support for Stop Limit orders. Stop Limit order fields added to all related API response. |
|  |  | Add `feeSymbol` in [Get order list](auth/order-list.md) is now in lowercase |
|  |  | Removed [Get order history](../../v2/rest/auth/history.md) API |
|  |  | Removed [Get ticker](../../v2/rest/open/ticker.md) API |
|  |  | Add `tradable` to [Get the account balance](auth/account-balance.md) API |

[Back](rest.md)

