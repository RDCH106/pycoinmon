from setuptools import setup
from pycoinmon.metadata import Metadata

metadata = Metadata()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """"
🐍 Python Port 🐍 Based on `COINMON`_

    💰 Cryptocurrency price ticker CLI.

Check cryptocurrencies’ prices, changes on your console. Best CLI tool
for those who are both **Crypto investors** and **Engineers**.

All data comes from `coinmarketcap.com`_ APIs.

Installation
------------

You can install or upgrade pycoinmon with:

``$ pip install pycoinmon --upgrade``

Or you can install from source with:

::

    $ git clone https://github.com/RDCH106/pycoinmon.git --recursive
    $ cd pycoinmon
    $ pip install .

Usage
-----

To check the top 10 cryptocurrencies ranked by their market cap, simply
execute

::

    $ pycoinmon

Options
~~~~~~~

You can use the ``-c`` (or ``--convert``) with the fiat currency symbol
to find in terms of another currency. The default currency is USD and it
supports AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF,
IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK,
SGD, THB, TRY, TWD, ZAR.

::

    $ pycoinmon -c eur // convert prices to Euro
    $ pycoinmon -c jpy // convert prices to Yen

You can use the ``-f`` (or ``--find``) with coin symbol to search
cryptocurrencies. You can add symbols seperated by space.

::

    $ pycoinmon -f btc // search coins included keyword btc
    $ pycoinmon -f btc eth // search coins included keyword btc or eth

You can use the ``-t`` (or ``--top``) with the index to find the top n
cryptocurrencies ranked by their market cap.

::

    $ pycoinmon -t 50 // find top 50
    $ pycoinmon -t 1000 // find top 1000

You can use the ``-H`` (or ``--humanize``) to display market cap in
humanized format.

::

    $ pycoinmon -H // show market cap in humanized format like 58.9 billion

You can use the ``-h`` (or ``--help``) to find all valid options of
pycoinmon

::

    $ pycoinmon -h

.. _COINMON: https://github.com/bichenkk/coinmon
.. _coinmarketcap.com: https://coinmarketcap.com/
    """


setup(
    name = 'pycoinmon',
    packages = ['pycoinmon'],
    install_requires = requirements(),
    version = metadata.get_version(),
    license = 'MIT',
    description = 'The cryptocurrency price tool on CLI',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/pycoinmon',
    entry_points={
        'console_scripts': ['pycoinmon=pycoinmon.main:main'],
    },
    keywords = 'bitcoin criptocurrency crypto ticker python cli price-tracker command-line',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)