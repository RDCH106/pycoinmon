# -*- coding: utf-8 -*-

import argparse
from requests import get


class Metadata:
    def __init__(self):
        self.__version__ = '0.0.1'
        self.__author__ = 'Rubén de Celis Hernández'

    def get_version(self):
        return self.__version__

    def get_author(self):
        return self.__author__


meta = Metadata()
sourceURL = "https://api.coinmarketcap.com/v1/ticker"

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version=meta.get_version())
parser.add_argument('-c', '--convert', dest='currency', help='Convert to your fiat currency', default='usd')
parser.add_argument('-f', '--find', dest='symbol',
                    help='Find specific coin data with coin symbol (can be a space seperated list)',
                    metavar='S', type=str, nargs='+')
parser.add_argument('-t', '--top', dest='index',
                    help='Show the top coins ranked from 1 - index according to the market cap', type=int)
parser.add_argument('-H', '--humanize', action='store_true', help='Show market cap as a humanized number')
args = parser.parse_args()


payload = {'limit': 10, 'convert': 'EUR'}
response = get(sourceURL, params=payload)

print(response.json())
