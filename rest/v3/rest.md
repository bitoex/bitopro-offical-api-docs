# Open API Document（v3.0.0）for BitoPro

## [Changelog](changelog.md)

##### The API service is hosted at **https://api.bitopro.com/v3**. Our rate limit policy:

* Open API
  * `600` requests per minute per IP
* Auth API
  * `600` requests per minute per IP
  * `600` requests per minute per user account

#### For all endpoints require authentication, you should create the API key at [BitoPro](https://www.bitopro.com/api)

## [Authentication](../authentication.md)

## HTTP Status Codes

* 2xx Success
  * `200` OK
* 4xx Client errors
  * `401` Unauthorized api key
  * `403` Forbidden
  * `409` Try to send the same request more than once
  * `422` Data parsing error
  * `429` Rate limits exceed
* 5xx Server errors
  * `502` Bad gateway
  * `503` Service unavailable

## Order status

* `-1`: Not Triggered
* `0`:  In progress
* `1`:  In progress (Partial deal)
* `2`:  Completed
* `3`:  Completed (Partial deal)
* `4`:  Cancelled

## Fee fields

* `fee` as fee paid
* `feeSymbol` as symbol for `fee`
* `bitoFee` as fee paid in **BITO**

## Endpoints

### `Open`

| Endpoint                                                 | URL                               | Example                                               |
| -------------------------------------------------------- | --------------------------------- | ----------------------------------------------------- |
| [Get order book](open/order-book.md)                     | `GET` /order-book/{pair}          | https://api.bitopro.com/v3/order-book/bito_twd        |
| [Get the list of currencies](open/currencies.md)         | `GET` /provisioning/currencies    | https://api.bitopro.com/v3/provisioning/currencies    |
| [Get the list of available pairs](open/trading-pairs.md) | `GET` /provisioning/trading-pairs | https://api.bitopro.com/v3/provisioning/trading-pairs |
| [Get tickers](open/tickers.md)                           | `GET` /tickers/{pair}             | https://api.bitopro.com/v3/tickers                    |
| [Get the recent trades](open/trades.md)                  | `GET` /trades/{pair}              | https://api.bitopro.com/v3/trades/bito_twd            |
| [Get trading history](open/trading-history.md)           | `GET` /trading-history/{pair}     | https://api.bitopro.com/v3/trading-history/btc_twd?resolution=1w&from=1550822974&to=1566375034 |

### `Auth`

| Endpoint                                           | URL                            | Example                                              |
| -------------------------------------------------- | ------------------------------ | ---------------------------------------------------- |
| [Get the account balance](auth/account-balance.md) | `GET` /accounts/balance        | https://api.bitopro.com/v3/accounts/balance          |
| [Get order list](auth/order-list.md)               | `GET` /orders/{pair}           | https://api.bitopro.com/v3/orders/bito_twd           |
| [Create an order](auth/create-order.md)            | `POST` /orders/{pair}          | https://api.bitopro.com/v3/orders/bito_twd           |
| [Cancel an order](auth/cancel-order.md)            | `DELETE` /orders/{pair}/{id}   | https://api.bitopro.com/v3/orders/bito_twd/123456789 |
| [Get an order](auth/get-order.md)                  | `GET` /orders/{pair}/{orderId} | https://api.bitopro.com/v3/orders/bito_twd/123456789 |