# Data Model Detailed Explanation

* [Order Model Relationship](#order-model-relationship)
* [Order Model Explanation](#order-model-explanation)
* [Order Status Explanation](#order-status-explanation)


## Order Model Relationship
[![](https://mermaid.ink/img/pako:eNpt0M0KgzAMB_BXCTnrC_S8HWWDMQajl2CzWegXtR5EffdVrbtsPYX8fyltJmy9YhQonXQcT5rekax0kM-95wjzXNd-ggcZwwkEdNTvaemU_BJVxgIkBkMtg3YQSEeJO77m-pfmu8CSGw-1J4U1lNruL8MKLUdLWuV3T2tPYurYssSVK37RYNKql0yHoCjxWenkI4oXmZ4rpCH52-haFCkOfKDy-6_ibajZF7TtqcJA7un9YZYPwHxpFQ?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpt0M0KgzAMB_BXCTnrC_S8HWWDMQajl2CzWegXtR5EffdVrbtsPYX8fyltJmy9YhQonXQcT5rekax0kM-95wjzXNd-ggcZwwkEdNTvaemU_BJVxgIkBkMtg3YQSEeJO77m-pfmu8CSGw-1J4U1lNruL8MKLUdLWuV3T2tPYurYssSVK37RYNKql0yHoCjxWenkI4oXmZ4rpCH52-haFCkOfKDy-6_ibajZF7TtqcJA7un9YZYPwHxpFQ)

## Order Model Explanation

| key | type | description |
| - | - | - |
| id | string | uniqe id |
| pair | string | order's trading pair which is format by `{BASE}_{QUOTE}` |
| avgExecutionPrice | string | the average execution price of the order. The order remains untraded, signified by a zero-average execution price. | 
| action | string | `BUY` or `SELL` |
| type | string | order type `LIMIT` or `MARKET` or `STOP_LIMIT`|
| status | int | order status, refer to [order status](#order-status-explanation) |
| originalAmount | string | original order amount at the time of placement. |
| remainingAmount | string | remaining order amount. | 
| executedAmount | string | executed order amount. | 
| fee | string | amount of transaction fees. | 
| feeSymbol | string | currency of transaction fees. | 
| bitoFee | string | amount of transaction fees paid on `BITO` | 
| total | string | total order transaction value. | 
| seq | string | order sequnence number | 
| stopPrice | string | trigger price for a stop-limit order. | 
| condition | string | price trigger condition for a stop-limit order. | 
| timeInForce | string | the time in force for an order defines the length of time over which an order will continue working before it is canceled. refer to [tif explanation](./order.md#order-time-in-force-explanation) | 
| createdTimestamp | string | order creation time in msec unit. | 
| updatedTimestamp | string | order updated time in msec unit. | 

## Order Status Explanation
* `-1`: Not Triggered
* `0`:  In progress
* `1`:  In progress \(Partial deal\)
* `2`:  Completed
* `3`:  Completed \(Partial deal\)
* `4`:  Cancelled
* `6`:  Post-only Cancelled
