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
import time
import sys

class PyCoinmon(object):

    def __init__(self):
        if 'PYCHARM_HOSTED' not in os.environ:  # Exclude PyCharm IDE from colorama init
            init()
        self.meta = Metadata()
        self.sourceURL = "https://api.coinmarketcap.com/v1/ticker"

        # Parse arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', action='version', version=self.meta.get_version())
        parser.add_argument('-c', '--convert', dest='currency', help='Convert to your fiat currency', default='usd',
                            choices=['USD', 'AUD', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD',
                                     'HUF', 'IDR', 'ILS', 'INR', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PKR',
                                     'PLN', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'TWD', 'ZAR'],
                            type=lambda s: s.upper())
        parser.add_argument('-f', '--find', dest='symbol',
                            help='Find specific coin data with coin symbol (can be a space seperated list)',
                            metavar='S', type=str, nargs='+')
        parser.add_argument('-l', '--layout', dest='template', help='Select table layout', default='grid',
                            choices=['plain', 'simple', 'grid', 'fancy_grid', 'pipe', 'orgtbl', 'presto', 'psql',
                                     'rst'],
                            type=lambda s: s.lower())
        parser.add_argument('-t', '--top', dest='index',
                            help='Show the top coins ranked from 1 - index according to the market cap', type=int, default=10)
        parser.add_argument('-u', '--update', dest='frequency',
                            help='Update data with frequency specified in seconds. If 0 just show one time.',
                            type=self.check_positive)
        parser.add_argument('-H', '--humanize', dest='humanize', action='store_true', help='Show market cap as a humanized number')
        parser.add_argument('--debug', dest='debug', action='store_true', help='Show debug info when an error occurred')
        self.args = parser.parse_args()

    def __del__(self):
        if deinit is not None:   # Prevent error when argparse raise exception
            deinit()

    @staticmethod
    def check_positive(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return ivalue

    def request_values(self):
        try:
            payload = {'limit': self.args.index, 'convert': self.args.currency}
            return get(self.sourceURL, params=payload)
        except Exception as e:
            template = Colors.RED + "\nAn exception of type {0} occurred\n" + Colors.ENDLINE
            print(template.format(type(e).__name__))
            if self.args.debug:
                template = "{0!r}"
                print(template.format(e.args))
            sys.exit(-1)   # Exit with error

    def print_values(self):
        # Update values
        response = self.request_values()

        # Clear screen
        if self.args.frequency:
            if os.name == 'nt':
                os.system('cls')   # on windows
            else:
                os.system('clear')   # on linux / os x

        # Redraw data
        print(process_title(ascii_title))
        # print(Colors.YELLOW + ascii_title + Colors.ENDLINE)
        if self.args.symbol:
            filtered_data = find_data(response.json(), self.args.symbol)
        else:
            filtered_data = response.json()
        tabulated_data = process_data(filtered_data, currency=self.args.currency, humanize=self.args.humanize)
        Colors.color_data(tabulated_data)
        # table = AsciiTable(tabulated_data)
        # print(table.table)
        print(tabulate(tabulated_data, headers='firstrow',
                       tablefmt=self.args.template, numalign="decimal", stralign="center"))
        print("\n")

    def run(self):
        if self.args.frequency:
            try:
                while True:
                    self.print_values()
                    print("Press Ctrl + C to exit.")
                    time.sleep(int(self.args.frequency))
            except KeyboardInterrupt:
                pass
        else:
            self.print_values()


if __name__ == "__main__":
    pycoinmon = PyCoinmon()
    pycoinmon.run()
