# Get the limitations and fees

### Get VIP trading fee rate, order fees and limitations, Restrictions of withdrawal fees, The cryptocurrency deposit fee and blockchain confirmation required for crediting, TTCheck fees and limitations

## `GET` /provisioning/limitations-and-fees

## Response sample

```javascript
{
    "tradingFeeRate": [
        {
            "rank": 0,
            "twdVolumeSymbol": "<",
            "twdVolume": "3000000",
            "bitoAmountSymbol": "<",
            "bitoAmount": "7500",
            "makerFee": "0.001",
            "takerFee": "0.002",
            "makerBitoFee": "0.0007",
            "takerBitoFee": "0.0014"
        },
        {
            "rank": 1,
            "twdVolumeSymbol": ">=",
            "twdVolume": "3000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "7500",
            "makerFee": "0.00097",
            "takerFee": "0.00194",
            "makerBitoFee": "0.00068",
            "takerBitoFee": "0.00136"
        },
        {
            "rank": 2,
            "twdVolumeSymbol": ">=",
            "twdVolume": "5000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "20000",
            "makerFee": "0.0007",
            "takerFee": "0.0015",
            "makerBitoFee": "0.00049",
            "takerBitoFee": "0.00105"
        },
        {
            "rank": 3,
            "twdVolumeSymbol": ">=",
            "twdVolume": "30000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "100000",
            "makerFee": "0",
            "takerFee": "0.0014",
            "makerBitoFee": "0",
            "takerBitoFee": "0.00098"
        },
        {
            "rank": 4,
            "twdVolumeSymbol": ">=",
            "twdVolume": "300000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "1000000",
            "makerFee": "0",
            "takerFee": "0.0013",
            "makerBitoFee": "0",
            "takerBitoFee": "0.00091"
        },
        {
            "rank": 5,
            "twdVolumeSymbol": ">=",
            "twdVolume": "550000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "2000000",
            "makerFee": "0",
            "takerFee": "0.0012",
            "makerBitoFee": "0",
            "takerBitoFee": "0.00084"
        },
        {
            "rank": 6,
            "twdVolumeSymbol": ">=",
            "twdVolume": "1300000000",
            "bitoAmountSymbol": ">=",
            "bitoAmount": "5000000",
            "makerFee": "0",
            "takerFee": "0.0011",
            "makerBitoFee": "0",
            "takerBitoFee": "0.00077"
        }
    ],
    "orderFeesAndLimitations": [
        {
            "pair": "BTC/TWD",
            "minimumOrderAmount": "0.0025",
            "minimumOrderAmountBase": "BTC",
            "minimumOrderNumberOfDigits": "0"
        },
        {
            "pair": "BTC/USDT",
            "minimumOrderAmount": "0.005",
            "minimumOrderAmountBase": "BTC",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "LTC/TWD",
            "minimumOrderAmount": "0.01",
            "minimumOrderAmountBase": "LTC",
            "minimumOrderNumberOfDigits": "0"
        },
        {
            "pair": "LTC/USDT",
            "minimumOrderAmount": "0.625",
            "minimumOrderAmountBase": "LTC",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "LTC/BTC",
            "minimumOrderAmount": "0.6",
            "minimumOrderAmountBase": "LTC",
            "minimumOrderNumberOfDigits": "6"
        },
        {
            "pair": "LTC/ETH",
            "minimumOrderAmount": "0.6",
            "minimumOrderAmountBase": "LTC",
            "minimumOrderNumberOfDigits": "6"
        },
        {
            "pair": "ETH/TWD",
            "minimumOrderAmount": "0.005",
            "minimumOrderAmountBase": "ETH",
            "minimumOrderNumberOfDigits": "0"
        },
        {
            "pair": "ETH/USDT",
            "minimumOrderAmount": "0.16",
            "minimumOrderAmountBase": "ETH",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "ETH/BTC",
            "minimumOrderAmount": "0.16",
            "minimumOrderAmountBase": "ETH",
            "minimumOrderNumberOfDigits": "6"
        },
        {
            "pair": "BCH/TWD",
            "minimumOrderAmount": "0.005",
            "minimumOrderAmountBase": "BCH",
            "minimumOrderNumberOfDigits": "0"
        },
        {
            "pair": "BCH/USDT",
            "minimumOrderAmount": "0.07",
            "minimumOrderAmountBase": "BCH",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "BCH/BTC",
            "minimumOrderAmount": "0.1",
            "minimumOrderAmountBase": "BCH",
            "minimumOrderNumberOfDigits": "6"
        },
        {
            "pair": "BCH/ETH",
            "minimumOrderAmount": "0.06",
            "minimumOrderAmountBase": "BCH",
            "minimumOrderNumberOfDigits": "4"
        },
        {
            "pair": "BCHSV/TWD",
            "minimumOrderAmount": "0.5",
            "minimumOrderAmountBase": "BCHSV",
            "minimumOrderNumberOfDigits": "0"
        },
        {
            "pair": "BCD/TWD",
            "minimumOrderAmount": "0.1",
            "minimumOrderAmountBase": "BCD",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "BITO/TWD",
            "minimumOrderAmount": "600",
            "minimumOrderAmountBase": "BITO",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "BITO/USDT",
            "minimumOrderAmount": "600",
            "minimumOrderAmountBase": "BITO",
            "minimumOrderNumberOfDigits": "4"
        },
        {
            "pair": "BITO/BTC",
            "minimumOrderAmount": "600",
            "minimumOrderAmountBase": "BITO",
            "minimumOrderNumberOfDigits": "8"
        },
        {
            "pair": "BITO/ETH",
            "minimumOrderAmount": "600",
            "minimumOrderAmountBase": "BITO",
            "minimumOrderNumberOfDigits": "6"
        },
        {
            "pair": "PANDA/TWD",
            "minimumOrderAmount": "125",
            "minimumOrderAmountBase": "PANDA",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "PANDA/ETH",
            "minimumOrderAmount": "125",
            "minimumOrderAmountBase": "PANDA",
            "minimumOrderNumberOfDigits": "6"
        },
        {
            "pair": "CGP/TWD",
            "minimumOrderAmount": "20",
            "minimumOrderAmountBase": "CGP",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "TRX/TWD",
            "minimumOrderAmount": "560",
            "minimumOrderAmountBase": "TRX",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "MITH/TWD",
            "minimumOrderAmount": "60",
            "minimumOrderAmountBase": "MITH",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "SDA/TWD",
            "minimumOrderAmount": "670",
            "minimumOrderAmountBase": "SDA",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "QNTU/ETH",
            "minimumOrderAmount": "41500",
            "minimumOrderAmountBase": "QNTU",
            "minimumOrderNumberOfDigits": "8"
        },
        {
            "pair": "USDT/TWD",
            "minimumOrderAmount": "32",
            "minimumOrderAmountBase": "USDT",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "RPC/TWD",
            "minimumOrderAmount": "1000",
            "minimumOrderAmountBase": "RPC",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "RPC/ETH",
            "minimumOrderAmount": "1000",
            "minimumOrderAmountBase": "RPC",
            "minimumOrderNumberOfDigits": "8"
        },
        {
            "pair": "XRP/TWD",
            "minimumOrderAmount": "50",
            "minimumOrderAmountBase": "XRP",
            "minimumOrderNumberOfDigits": "4"
        },
        {
            "pair": "EOS/TWD",
            "minimumOrderAmount": "1",
            "minimumOrderAmountBase": "EOS",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "EOS/USDT",
            "minimumOrderAmount": "3",
            "minimumOrderAmountBase": "EOS",
            "minimumOrderNumberOfDigits": "4"
        },
        {
            "pair": "BNB/TWD",
            "minimumOrderAmount": "0.15",
            "minimumOrderAmountBase": "BNB",
            "minimumOrderNumberOfDigits": "2"
        },
        {
            "pair": "BNB/USDT",
            "minimumOrderAmount": "0.45",
            "minimumOrderAmountBase": "BNB",
            "minimumOrderNumberOfDigits": "4"
        }
    ],
    "restrictionsOfWithdrawalFees": [
        {
            "currency": "TWD",
            "fee": "15",
            "minimumTradingAmount": "100",
            "maximumTradingAmount": "1000000",
            "dailyCumulativeMaximumAmount": "2000000",
            "remarks": ""
        },
        {
            "currency": "BTC",
            "fee": "0.0002",
            "minimumTradingAmount": "0.001",
            "maximumTradingAmount": "50",
            "dailyCumulativeMaximumAmount": "100",
            "remarks": ""
        },
        {
            "currency": "LTC",
            "fee": "0.001",
            "minimumTradingAmount": "0.001",
            "maximumTradingAmount": "2000",
            "dailyCumulativeMaximumAmount": "5000",
            "remarks": ""
        },
        {
            "currency": "ETH",
            "fee": "0.002",
            "minimumTradingAmount": "0.002",
            "maximumTradingAmount": "1000",
            "dailyCumulativeMaximumAmount": "2000",
            "remarks": ""
        },
        {
            "currency": "BCH",
            "fee": "0.001",
            "minimumTradingAmount": "0.002",
            "maximumTradingAmount": "500",
            "dailyCumulativeMaximumAmount": "1000",
            "remarks": ""
        },
        {
            "currency": "BCHSV",
            "fee": "0.015",
            "minimumTradingAmount": "0.024",
            "maximumTradingAmount": "500",
            "dailyCumulativeMaximumAmount": "1000",
            "remarks": ""
        },
        {
            "currency": "BTG",
            "fee": "0.001",
            "minimumTradingAmount": "0.01",
            "maximumTradingAmount": "2000",
            "dailyCumulativeMaximumAmount": "5000",
            "remarks": ""
        },
        {
            "currency": "BCD",
            "fee": "0.001",
            "minimumTradingAmount": "0.002",
            "maximumTradingAmount": "10000",
            "dailyCumulativeMaximumAmount": "20000",
            "remarks": "Suspended deposit/withdraw"
        },
        {
            "currency": "BITO",
            "fee": "10",
            "minimumTradingAmount": "150",
            "maximumTradingAmount": "10000000",
            "dailyCumulativeMaximumAmount": "10000000",
            "remarks": ""
        },
        {
            "currency": "PANDA",
            "fee": "500",
            "minimumTradingAmount": "70",
            "maximumTradingAmount": "15000000",
            "dailyCumulativeMaximumAmount": "50000000",
            "remarks": ""
        },
        {
            "currency": "CGP",
            "fee": "1",
            "minimumTradingAmount": "15",
            "maximumTradingAmount": "20000",
            "dailyCumulativeMaximumAmount": "20000",
            "remarks": ""
        },
        {
            "currency": "TRX",
            "fee": "25",
            "minimumTradingAmount": "300",
            "maximumTradingAmount": "200000",
            "dailyCumulativeMaximumAmount": "500000",
            "remarks": ""
        },
        {
            "currency": "MITH",
            "fee": "10",
            "minimumTradingAmount": "30",
            "maximumTradingAmount": "200000",
            "dailyCumulativeMaximumAmount": "500000",
            "remarks": ""
        },
        {
            "currency": "SDA",
            "fee": "25",
            "minimumTradingAmount": "300",
            "maximumTradingAmount": "2000000",
            "dailyCumulativeMaximumAmount": "5000000",
            "remarks": ""
        },
        {
            "currency": "MODL",
            "fee": "300",
            "minimumTradingAmount": "5000",
            "maximumTradingAmount": "5000000",
            "dailyCumulativeMaximumAmount": "10000000",
            "remarks": "Suspended deposit"
        },
        {
            "currency": "QNTU",
            "fee": "1000",
            "minimumTradingAmount": "16700",
            "maximumTradingAmount": "20000000",
            "dailyCumulativeMaximumAmount": "40000000",
            "remarks": ""
        },
        {
            "currency": "USDT/Omni Layer",
            "fee": "5",
            "minimumTradingAmount": "20",
            "maximumTradingAmount": "100000",
            "dailyCumulativeMaximumAmount": "300000",
            "remarks": ""
        },
        {
            "currency": "USDT/ETH-ERC20",
            "fee": "3",
            "minimumTradingAmount": "20",
            "maximumTradingAmount": "100000",
            "dailyCumulativeMaximumAmount": "300000",
            "remarks": ""
        },
        {
            "currency": "RPC",
            "fee": "30",
            "minimumTradingAmount": "600",
            "maximumTradingAmount": "600000",
            "dailyCumulativeMaximumAmount": "1200000",
            "remarks": "Suspended deposit/withdraw"
        },
        {
            "currency": "XEM",
            "fee": "10",
            "minimumTradingAmount": "170",
            "maximumTradingAmount": "200000",
            "dailyCumulativeMaximumAmount": "400000",
            "remarks": ""
        },
        {
            "currency": "XRP",
            "fee": "0.25",
            "minimumTradingAmount": "50",
            "maximumTradingAmount": "50000",
            "dailyCumulativeMaximumAmount": "100000",
            "remarks": ""
        },
        {
            "currency": "EOS",
            "fee": "0.3",
            "minimumTradingAmount": "5",
            "maximumTradingAmount": "5500",
            "dailyCumulativeMaximumAmount": "11000",
            "remarks": ""
        },
        {
            "currency": "BNB",
            "fee": "0.05",
            "minimumTradingAmount": "0.8",
            "maximumTradingAmount": "750",
            "dailyCumulativeMaximumAmount": "1500",
            "remarks": ""
        },
        {
            "currency": "BTT",
            "fee": "17",
            "minimumTradingAmount": "280",
            "maximumTradingAmount": "277800",
            "dailyCumulativeMaximumAmount": "555600",
            "remarks": ""
        },
        {
            "currency": "WINK",
            "fee": "17",
            "minimumTradingAmount": "280",
            "maximumTradingAmount": "277800",
            "dailyCumulativeMaximumAmount": "555600",
            "remarks": ""
        }
    ],
    "cryptocurrencyDepositFeeAndConfirmation": [
        {
            "currency": "TWD",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": ""
        },
        {
            "currency": "BTC",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "4"
        },
        {
            "currency": "LTC",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "5"
        },
        {
            "currency": "ETH",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "BCH",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "BCHSV",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "2"
        },
        {
            "currency": "BTG",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "5"
        },
        {
            "currency": "BCD",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "5"
        },
        {
            "currency": "BITO/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "PANDA/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "CGP/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "TRX",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "MITH/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "SDA",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "1"
        },
        {
            "currency": "MODL/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "QNTU/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "USDT/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "USDT/Omni Layer",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "4"
        },
        {
            "currency": "RPC/ETH-ERC20",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "XEM",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "XRP",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "6"
        },
        {
            "currency": "EOS",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "1"
        },
        {
            "currency": "BNB",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "1"
        },
        {
            "currency": "BTT",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        },
        {
            "currency": "WINK",
            "generalDepositFees": "0",
            "blockchainConfirmationRequired": "20"
        }
    ],
    "ttCheckFeesAndLimitationsLevel1": [
        {
            "currency": "TWD",
            "redeemDailyCumulativeMaximumAmount": "",
            "generateMinimumTradingAmount": "",
            "generateMaximumTradingAmount": "",
            "generateDailyCumulativeMaximumAmount": ""
        },
        {
            "currency": "BTC",
            "redeemDailyCumulativeMaximumAmount": "0.1567",
            "generateMinimumTradingAmount": "0.0002",
            "generateMaximumTradingAmount": "0.0262",
            "generateDailyCumulativeMaximumAmount": "0.1567"
        },
        {
            "currency": "LTC",
            "redeemDailyCumulativeMaximumAmount": "20.14",
            "generateMinimumTradingAmount": "0.03",
            "generateMaximumTradingAmount": "3.36",
            "generateDailyCumulativeMaximumAmount": "20.14"
        },
        {
            "currency": "ETH",
            "redeemDailyCumulativeMaximumAmount": "5.07",
            "generateMinimumTradingAmount": "0.01",
            "generateMaximumTradingAmount": "0.85",
            "generateDailyCumulativeMaximumAmount": "5.07"
        },
        {
            "currency": "BCH",
            "redeemDailyCumulativeMaximumAmount": "6.38",
            "generateMinimumTradingAmount": "0.007",
            "generateMaximumTradingAmount": "1.07",
            "generateDailyCumulativeMaximumAmount": "6.38"
        },
        {
            "currency": "BCHSV",
            "redeemDailyCumulativeMaximumAmount": "6.38",
            "generateMinimumTradingAmount": "0.007",
            "generateMaximumTradingAmount": "1.07",
            "generateDailyCumulativeMaximumAmount": "6.38"
        },
        {
            "currency": "BTG",
            "redeemDailyCumulativeMaximumAmount": "45.1",
            "generateMinimumTradingAmount": "0.1",
            "generateMaximumTradingAmount": "7.6",
            "generateDailyCumulativeMaximumAmount": "45.1"
        },
        {
            "currency": "BCD",
            "redeemDailyCumulativeMaximumAmount": "613",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "103",
            "generateDailyCumulativeMaximumAmount": "613"
        },
        {
            "currency": "BITO",
            "redeemDailyCumulativeMaximumAmount": "34483",
            "generateMinimumTradingAmount": "35",
            "generateMaximumTradingAmount": "5748",
            "generateDailyCumulativeMaximumAmount": "34483"
        },
        {
            "currency": "PANDA",
            "redeemDailyCumulativeMaximumAmount": "23440",
            "generateMinimumTradingAmount": "30",
            "generateMaximumTradingAmount": "3910",
            "generateDailyCumulativeMaximumAmount": "23440"
        },
        {
            "currency": "CGP",
            "redeemDailyCumulativeMaximumAmount": "729",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "122",
            "generateDailyCumulativeMaximumAmount": "729"
        },
        {
            "currency": "TRX",
            "redeemDailyCumulativeMaximumAmount": "44200",
            "generateMinimumTradingAmount": "100",
            "generateMaximumTradingAmount": "7400",
            "generateDailyCumulativeMaximumAmount": "44200"
        },
        {
            "currency": "MITH",
            "redeemDailyCumulativeMaximumAmount": "3750",
            "generateMinimumTradingAmount": "4",
            "generateMaximumTradingAmount": "625",
            "generateDailyCumulativeMaximumAmount": "3750"
        },
        {
            "currency": "SDA",
            "redeemDailyCumulativeMaximumAmount": "107200",
            "generateMinimumTradingAmount": "200",
            "generateMaximumTradingAmount": "17900",
            "generateDailyCumulativeMaximumAmount": "107200"
        },
        {
            "currency": "QNTU",
            "redeemDailyCumulativeMaximumAmount": "1266500",
            "generateMinimumTradingAmount": "1300",
            "generateMaximumTradingAmount": "211100",
            "generateDailyCumulativeMaximumAmount": "1266500"
        },
        {
            "currency": "USDT",
            "redeemDailyCumulativeMaximumAmount": "996",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "166",
            "generateDailyCumulativeMaximumAmount": "996"
        },
        {
            "currency": "RPC",
            "redeemDailyCumulativeMaximumAmount": "36600",
            "generateMinimumTradingAmount": "40",
            "generateMaximumTradingAmount": "6100",
            "generateDailyCumulativeMaximumAmount": "36600"
        },
        {
            "currency": "XEM",
            "redeemDailyCumulativeMaximumAmount": "9700",
            "generateMinimumTradingAmount": "10",
            "generateMaximumTradingAmount": "1700",
            "generateDailyCumulativeMaximumAmount": "9700"
        },
        {
            "currency": "XRP",
            "redeemDailyCumulativeMaximumAmount": "2900",
            "generateMinimumTradingAmount": "2.9",
            "generateMaximumTradingAmount": "500",
            "generateDailyCumulativeMaximumAmount": "2900"
        },
        {
            "currency": "EOS",
            "redeemDailyCumulativeMaximumAmount": "340",
            "generateMinimumTradingAmount": "0.4",
            "generateMaximumTradingAmount": "60",
            "generateDailyCumulativeMaximumAmount": "400"
        },
        {
            "currency": "BNB",
            "redeemDailyCumulativeMaximumAmount": "46",
            "generateMinimumTradingAmount": "0.05",
            "generateMaximumTradingAmount": "8",
            "generateDailyCumulativeMaximumAmount": "46"
        }
    ],
    "ttCheckFeesAndLimitationsLevel2": [
        {
            "currency": "TWD",
            "redeemDailyCumulativeMaximumAmount": "4000000",
            "generateMinimumTradingAmount": "30",
            "generateMaximumTradingAmount": "2000000",
            "generateDailyCumulativeMaximumAmount": "4000000"
        },
        {
            "currency": "BTC",
            "redeemDailyCumulativeMaximumAmount": "20.8889",
            "generateMinimumTradingAmount": "0.0002",
            "generateMaximumTradingAmount": "10.4445",
            "generateDailyCumulativeMaximumAmount": "20.8889"
        },
        {
            "currency": "LTC",
            "redeemDailyCumulativeMaximumAmount": "2684.57",
            "generateMinimumTradingAmount": "0.03",
            "generateMaximumTradingAmount": "1342.29",
            "generateDailyCumulativeMaximumAmount": "2684.57"
        },
        {
            "currency": "ETH",
            "redeemDailyCumulativeMaximumAmount": "675.45",
            "generateMinimumTradingAmount": "0.01",
            "generateMaximumTradingAmount": "337.73",
            "generateDailyCumulativeMaximumAmount": "675.45"
        },
        {
            "currency": "BCH",
            "redeemDailyCumulativeMaximumAmount": "851",
            "generateMinimumTradingAmount": "0.0064",
            "generateMaximumTradingAmount": "425.2605",
            "generateDailyCumulativeMaximumAmount": "851"
        },
        {
            "currency": "BCHSV",
            "redeemDailyCumulativeMaximumAmount": "851",
            "generateMinimumTradingAmount": "0.0064",
            "generateMaximumTradingAmount": "425.2605",
            "generateDailyCumulativeMaximumAmount": "851"
        },
        {
            "currency": "BTG",
            "redeemDailyCumulativeMaximumAmount": "6006.1",
            "generateMinimumTradingAmount": "0.1",
            "generateMaximumTradingAmount": "3003.1",
            "generateDailyCumulativeMaximumAmount": "6006.1"
        },
        {
            "currency": "BCD",
            "redeemDailyCumulativeMaximumAmount": "81633",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "40817",
            "generateDailyCumulativeMaximumAmount": "81633"
        },
        {
            "currency": "BITO",
            "redeemDailyCumulativeMaximumAmount": "4597702",
            "generateMinimumTradingAmount": "35",
            "generateMaximumTradingAmount": "2298851",
            "generateDailyCumulativeMaximumAmount": "4597702"
        },
        {
            "currency": "PANDA",
            "redeemDailyCumulativeMaximumAmount": "3125000",
            "generateMinimumTradingAmount": "30",
            "generateMaximumTradingAmount": "1562500",
            "generateDailyCumulativeMaximumAmount": "3125000"
        },
        {
            "currency": "CGP",
            "redeemDailyCumulativeMaximumAmount": "97182",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "48591",
            "generateDailyCumulativeMaximumAmount": "97182"
        },
        {
            "currency": "TRX",
            "redeemDailyCumulativeMaximumAmount": "5882400",
            "generateMinimumTradingAmount": "100",
            "generateMaximumTradingAmount": "2941200",
            "generateDailyCumulativeMaximumAmount": "5882400"
        },
        {
            "currency": "MITH",
            "redeemDailyCumulativeMaximumAmount": "500000",
            "generateMinimumTradingAmount": "4",
            "generateMaximumTradingAmount": "250000",
            "generateDailyCumulativeMaximumAmount": "500000"
        },
        {
            "currency": "SDA",
            "redeemDailyCumulativeMaximumAmount": "14285800",
            "generateMinimumTradingAmount": "200",
            "generateMaximumTradingAmount": "7142900",
            "generateDailyCumulativeMaximumAmount": "14285800"
        },
        {
            "currency": "QNTU",
            "redeemDailyCumulativeMaximumAmount": "168861900",
            "generateMinimumTradingAmount": "1300",
            "generateMaximumTradingAmount": "84431000",
            "generateDailyCumulativeMaximumAmount": "168861900"
        },
        {
            "currency": "USDT",
            "redeemDailyCumulativeMaximumAmount": "132759",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "66380",
            "generateDailyCumulativeMaximumAmount": "132759"
        },
        {
            "currency": "RPC",
            "redeemDailyCumulativeMaximumAmount": "4879000",
            "generateMinimumTradingAmount": "40",
            "generateMaximumTradingAmount": "2440000",
            "generateDailyCumulativeMaximumAmount": "4879000"
        },
        {
            "currency": "XEM",
            "redeemDailyCumulativeMaximumAmount": "1283000",
            "generateMinimumTradingAmount": "10",
            "generateMaximumTradingAmount": "642000",
            "generateDailyCumulativeMaximumAmount": "1283000"
        },
        {
            "currency": "XRP",
            "redeemDailyCumulativeMaximumAmount": "381000",
            "generateMinimumTradingAmount": "3",
            "generateMaximumTradingAmount": "190500",
            "generateDailyCumulativeMaximumAmount": "381000"
        },
        {
            "currency": "EOS",
            "redeemDailyCumulativeMaximumAmount": "44500",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "22300",
            "generateDailyCumulativeMaximumAmount": "44500"
        },
        {
            "currency": "BNB",
            "redeemDailyCumulativeMaximumAmount": "6100",
            "generateMinimumTradingAmount": "1",
            "generateMaximumTradingAmount": "3100",
            "generateDailyCumulativeMaximumAmount": "6100"
        }
    ]
}
```

[Back](../rest.md)

