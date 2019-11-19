![logo](https://raw.githubusercontent.com/RDCH106/pycoinmon/master/logo.png)

# About pyCOINMON

[![PyPI](https://img.shields.io/pypi/v/pycoinmon.svg)](https://pypi.python.org/pypi/pycoinmon)
[![PyPI](https://img.shields.io/pypi/pyversions/pycoinmon.svg)](https://pypi.python.org/pypi/pycoinmon)
[![PyPI](https://img.shields.io/pypi/l/pycoinmon.svg)](https://github.com/RDCH106/pycoinmon/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/RDCH106/pycoinmon.svg?branch=master)](https://travis-ci.org/RDCH106/pycoinmon)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/30fca0e3463649f88584cd89c118eac2)](https://www.codacy.com/app/RDCH106/pycoinmon?utm_source=github.com&utm_medium=referral&utm_content=RDCH106/pycoinmon&utm_campaign=badger)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-😄-1EAEDB.svg)](https://saythanks.io/to/RDCH106)

🐍 Python Port 🐍 Based on [COINMON](https://github.com/bichenkk/coinmon)

> 💰 Cryptocurrency price ticker CLI.

Check cryptocurrencies' prices, changes on your console.
Best CLI tool for those who are both **Crypto investors** and **Engineers**.

All data comes from [coinmarketcap.com](https://coinmarketcap.com/) APIs.

## Installation

You can install or upgrade pycoinmon with:

`$ pip install pycoinmon --upgrade`

Or you can install from source with:

```
$ git clone https://github.com/RDCH106/pycoinmon.git --recursive
$ cd pycoinmon
$ pip install .
```

If you are Windows user, you can download binaries of latest release from here:

https://github.com/RDCH106/pycoinmon/releases/latest

## Usage

To check the top 10 cryptocurrencies ranked by their market cap, simply execute
```
$ pycoinmon
```

### Options

You can use the `-c` (or `--convert`) with the fiat currency symbol to find in terms of another currency.
The default currency is USD and it supports AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD, ZAR.

```
$ pycoinmon -c eur // convert prices to Euro
$ pycoinmon -c jpy // convert prices to Yen
```

You can use the `-f` (or `--find`) with coin symbol to search cryptocurrencies. You can add symbols seperated by space.

```
$ pycoinmon -f btc // search coins included keyword btc
$ pycoinmon -f btc eth // search coins included keyword btc or eth
```

You can use the `-l` (or `--layout`) with template name to print the table with different style.
The default layout template is grid and it supports plain, simple, fancy_grid, pipe, orgtbl, presto, psql, rst.

```
$ pycoinmon -l plain // show table with plain style
$ pycoinmon -l fancy_grid // show table with fancy_grid style
```

You can use the `-t` (or `--top`) with the index to find the top n cryptocurrencies ranked by their market cap.

```
$ pycoinmon -t 50 // find top 50
$ pycoinmon -t 1000 // find top 1000
```

You can use the `-u` (or `--update`) with the refresh frequency in seconds. The value must be bigger than 0.

```
$ pycoinmon -u 10 // update data each 10 seconds
```

You can use the `-H` (or `--humanize`) to display market cap in humanized format.

```
$ pycoinmon -H // show market cap in humanized format like 58.9 billion 
```

You can use the `-h` (or `--help`) to find all valid options of pycoinmon.

```
$ pycoinmon -h
```

You can use the `--debug` to show debug info when an error occurred.

```
$ pycoinmon --debug
```

## Screenshot

![pycoinmon screenshot](https://raw.githubusercontent.com/RDCH106/pycoinmon/master/pycoinmon.png)
