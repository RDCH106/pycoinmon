# -*- coding: utf-8 -*-

import argparse
from requests import get
from tabulate import tabulate
import re
from pycoinmon.common import process_data, colors
from pycoinmon.ascii import ascii_title
from pycoinmon.metadata import Metadata
#from terminaltables import AsciiTable


class PyCoinmon(object):

    def __init__(self):
        self.meta = Metadata()
        self.sourceURL = "https://api.coinmarketcap.com/v1/ticker"

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

        print(colors.YELLOW + ascii_title + colors.ENDLINE)
        tabulated_data = process_data(response.json(), currency=args.currency)
        self.color_data(tabulated_data)
        # table = AsciiTable(tabulated_data)
        # print(table.table)
        print(tabulate(tabulated_data, headers='firstrow', tablefmt="grid"))
        print("\n")

    @staticmethod
    def color_data(data):
        data[0][0] = colors.YELLOW + data[0][0]
        data[0][len(data[0]) - 1] = data[0][len(data[0]) - 1] + colors.ENDLINE

        for item in data[1:]:
            if re.search('-\d+\.\d+', item[3]):
                item[3] = colors.RED + item[3] + '%' + colors.ENDLINE
            else:
                item[3] = colors.GREEN + item[3] + '%' + colors.ENDLINE
            if re.search('-\d+\.\d+', item[4]):
                item[4] = colors.RED + item[4] + '%' + colors.ENDLINE
            else:
                item[4] = colors.GREEN + item[4] + '%' + colors.ENDLINE


if __name__ == "__main__":
    pycoinmon = PyCoinmon()
    pycoinmon.run()
