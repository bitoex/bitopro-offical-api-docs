# Order Operation Detailed Explanation

- [Order Type Explanation](#order-type-explanation)
- [Order Time-In-Force Explanation](#order-time-in-force-explanation)

## Order Type Explanation
### Limit Order:
A limit order is a type of order used in trading financial instruments like stocks or cryptocurrencies. When you place a limit order, you specify a particular price at which you want to buy or sell an asset. This order will only be executed if the market reaches your specified price or better. If the market doesn't reach your set price, the order remains open until it's either filled or canceled. Limit orders give you control over the price at which you trade but do not guarantee immediate execution.

### Market Order:
A market order is the simplest type of order. When you place a market order, you're instructing your broker to buy or sell an asset immediately at the current market price. Market orders are executed quickly, but the exact price at which the order is filled may vary, especially in volatile markets. Market orders are ideal when you prioritize speed over price precision.

### Stop-Limit Order:
A stop-limit order is a combination of two order types: a stop order and a limit order. It is used to manage risk and control the price at which a trade is executed. First, you set a stop price, which triggers the order when the market reaches a specific level. Once triggered, the stop order becomes a limit order with a predefined price. This means that the trade will only be executed at the specified limit price or better. Stop-limit orders are commonly used to enter or exit a position when a certain price level is reached, providing more control compared to a market order.

These three order types offer traders different levels of control and flexibility when executing trades, allowing them to tailor their trading strategies to their specific goals and risk tolerance.

## Order Time-In-Force Explanation

Time-in-force (TIF) is a parameter used in trading to specify how long an order remains active and under what conditions it will be executed or canceled. It helps traders define the duration and behavior of their orders in the market. There are several common time-in-force options supported by BitoPro:

### Good 'Til Cancelled (GTC):
A GTC order remains active until it's either executed, manually canceled by the trader, or reaches a specified expiration date set by the broker or exchange. These orders can persist for an extended period, sometimes even indefinitely.
### POST-Only: 
The "POST-Only" TIF option compels orders to function as maker trades, ensuring that they are posted onto the order book without immediate matching against existing orders. This choice typically guarantees that your order qualifies for maker fees.