# -*- coding: utf-8 -*-

import argparse
from requests import get
from tabulate import tabulate
from pycoinmon.common import process_data, find_data, Colors
from pycoinmon.ascii import ascii_title, process_title
from pycoinmon.metadata import Metadata
#from terminaltables import AsciiTable
from colorama import init, deinit
import os


class PyCoinmon(object):

    def __init__(self):
        if 'PYCHARM_HOSTED' not in os.environ:  # Exclude PyCharm IDE from colorama init
            init()
        self.meta = Metadata()
        self.sourceURL = "https://api.coinmarketcap.com/v1/ticker"

    def __del__(self):
        deinit()

    def run(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', action='version', version=self.meta.get_version())
        parser.add_argument('-c', '--convert', dest='currency', help='Convert to your fiat currency', default='usd')
        parser.add_argument('-f', '--find', dest='symbol',
                            help='Find specific coin data with coin symbol (can be a space seperated list)',
                            metavar='S', type=str, nargs='+')
        parser.add_argument('-t', '--top', dest='index',
                            help='Show the top coins ranked from 1 - index according to the market cap', type=int, default=10)
        parser.add_argument('-H', '--humanize', action='store_true', help='Show market cap as a humanized number')
        args = parser.parse_args()

        payload = {'limit': args.index, 'convert': args.currency}
        response = get(self.sourceURL, params=payload)

        print(process_title(ascii_title))
        # print(Colors.YELLOW + ascii_title + Colors.ENDLINE)
        if args.symbol:
            filtered_data = find_data(response.json(), args.symbol)
        else:
            filtered_data = response.json()
        tabulated_data = process_data(filtered_data, currency=args.currency)
        Colors.color_data(tabulated_data)
        # table = AsciiTable(tabulated_data)
        # print(table.table)
        print(tabulate(tabulated_data, headers='firstrow', tablefmt="grid"))
        print("\n")


if __name__ == "__main__":
    pycoinmon = PyCoinmon()
    pycoinmon.run()
