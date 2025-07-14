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
            "protocol": "main",
            "twdWithdrawMonthly": null
        },
        {
            "currency": "APE (ETH-ERC20)",
            "fee": "2.93",
            "minimumTradingAmount": "5.86",
            "maximumTradingAmount": "72700",
            "dailyCumulativeMaximumAmount": "727000",
            "remarks": "Suspended withdraw",
            "protocol": "erc20",
            "twdWithdrawMonthly": null
        },
        {
            "currency": "TRX",
            "fee": "75",
            "minimumTradingAmount": "300",
            "maximumTradingAmount": "200000",
            "dailyCumulativeMaximumAmount": "500000",
            "remarks": "",
            "protocol": "main",
            "twdWithdrawMonthly": null
        },
        {
            "currency": "TWD",
            "fee": "30",
            "minimumTradingAmount": "100",
            "maximumTradingAmount": "2000000",
            "dailyCumulativeMaximumAmount": "2000000",
            "remarks": "",
            "protocol": "main",
            "twdWithdrawMonthly": "5000000"
        },
        {
            "currency": "USDC (Binance Smart Chain)",
            "fee": "0.057",
            "minimumTradingAmount": "1",
            "maximumTradingAmount": "50000",
            "dailyCumulativeMaximumAmount": "100000",
            "remarks": "",
            "protocol": "bsc",
            "twdWithdrawMonthly": null
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

## Response Fields

### restrictionsOfWithdrawalFees

| Field | Type | Description |
|-------|------|-------------|
| currency | string | The currency code |
| fee | string | Withdrawal fee amount |
| minimumTradingAmount | string | Minimum withdrawal amount |
| maximumTradingAmount | string | Maximum withdrawal amount per transaction |
| dailyCumulativeMaximumAmount | string | Daily cumulative maximum withdrawal amount |
| remarks | string | Additional remarks or notes |
| protocol | string | Protocol used for the withdrawal |
| twdWithdrawMonthly | string/null | Monthly TWD withdrawal limit. Only has value when currency is "TWD", null for other currencies |

[Back](../summary.md)