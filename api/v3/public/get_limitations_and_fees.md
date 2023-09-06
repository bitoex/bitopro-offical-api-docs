# Get Limitations and Fees
Get VIP trading fee rates, order fees, and limitations. Learn about withdrawal fee restrictions. Understand the cryptocurrency deposit fee and the number of blockchain confirmations required for crediting. Also, TTCheck fees and limitations.

# Api Request
**`GET` /provisioning/limitations-and-fees**

# Api Response

**Response Body Example:**
```javascript
{
    "tradingFeeRate": [
        {
            "rank": 0,
            "twdVolumeSymbol": "<",
            "twdVolume": "3000000",
            "bitoAmountSymbol": "<",
            "bitoAmount": "3000",
            "makerFee": "0.001",
            "takerFee": "0.002",
            "makerBitoFee": "0.0008",
            "takerBitoFee": "0.0016",
            "rankCondition": "or",
            "gridBotMakerFee": "0.0005",
            "gridBotTakerFee": "0.0005"
        },
        {
            "rank": 1,
            "twdVolumeSymbol": ">=",
            "twdVolume": "3000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "3000",
            "makerFee": "0.0009",
            "takerFee": "0.0018",
            "makerBitoFee": "0.00072",
            "takerBitoFee": "0.00144",
            "rankCondition": "or",
            "gridBotMakerFee": "0.0005",
            "gridBotTakerFee": "0.0005"
        }
    ],
    "restrictionsOfWithdrawalFees": [
        {
            "currency": "ADA",
            "fee": "0.5",
            "minimumTradingAmount": "1",
            "maximumTradingAmount": "20000",
            "dailyCumulativeMaximumAmount": "50000",
            "remarks": "",
            "protocol": "main"
        },
        {
            "currency": "APE (ETH-ERC20)",
            "fee": "2.93",
            "minimumTradingAmount": "5.86",
            "maximumTradingAmount": "72700",
            "dailyCumulativeMaximumAmount": "727000",
            "remarks": "Suspended withdraw",
            "protocol": "erc20"
        }
    ],
    "cryptocurrencyDepositFeeAndConfirmation": [
        {
            "currency": "ADA",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "300"
        },
        {
            "currency": "APE (ETH-ERC20)",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "12"
        }
    ],
    "ttCheckFeesAndLimitationsLevel1": [
        {
            "currency": "BCD",
            "redeemDailyCumulativeMaximumAmount": "613",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "103",
            "generateDailyCumulativeMaximumAmount": "613"
        },
        {
            "currency": "BCH",
            "redeemDailyCumulativeMaximumAmount": "6.38",
            "generateMinimumTradingAmount": "0.007",
            "generateMaximumTradingAmount": "1.07",
            "generateDailyCumulativeMaximumAmount": "6.38"
        }
    ],
    "ttCheckFeesAndLimitationsLevel2": [
        {
            "currency": "BCD",
            "redeemDailyCumulativeMaximumAmount": "81633",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "40817",
            "generateDailyCumulativeMaximumAmount": "81633"
        },
        {
            "currency": "BCH",
            "redeemDailyCumulativeMaximumAmount": "851",
            "generateMinimumTradingAmount": "0.0064",
            "generateMaximumTradingAmount": "425.2605",
            "generateDailyCumulativeMaximumAmount": "851"
        }
    ]
}
```
[Back](../summary.md)
