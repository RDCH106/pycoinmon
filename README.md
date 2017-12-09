![logo](https://raw.githubusercontent.com/RDCH106/pycoinmon/master/logo.png)

# About pyCOINMON

🐍 Python Port 🐍 Based on [COINMON](https://github.com/bichenkk/coinmon)

> 💰 Cryptocurrency price ticker CLI.

Check cryptocurrencies' prices, changes on your console.
Best CLI tool for those who are both **Crypto investors** and **Engineers**.

All data comes from [coinmarketcap.com](https://coinmarketcap.com/) APIs.

## Installation

You can install from source with:

```
$ git clone https://github.com/RDCH106/pycoinmon.git --recursive
$ cd pycoinmon
```

## Usage

To check the top 10 cryptocurrencies ranked by their market cap, simply execute
```
$ python pycoinmon
```

### Options

You can use the `-c` (or `--convert`) with the fiat currency symbol to find in terms of another currency.
The default currency is USD and it supports AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD, ZAR.

```
$ python pycoinmon -c eur // convert prices to Euro
$ python pycoinmon -c jpy // convert prices to Yen
```

You can use the `-t` (or `--top`) with the index to find the top n cryptocurrencies ranked by their market cap.

```
$ python pycoinmon -t 50 // find top 50
$ python pycoinmon -t 1000 // find top 1000
```

You can use the `-h` (or `--help`) to find all valid options of pycoinmon

```
$ python pycoinmon -h
```
