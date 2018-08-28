# -*- coding: utf-8 -*-

import difflib
import copy
import re
from humanize import intword

fields_good_name = {
    "rank": "Rank",
    "symbol": "Symbol",
    "price": "Price (USD)",
    "percent_change_24h": "Change (24H)",
    "percent_change_1h": "Change (1H)",
    "market_cap": "Market Cap (USD)"
}


class Colors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    ENDLINE = '\033[0m'

    @staticmethod
    def color_data(data):
        data[0][0] = Colors.YELLOW + data[0][0]
        data[0][len(data[0]) - 1] = data[0][len(data[0]) - 1] + Colors.ENDLINE

        for item in data[1:]:
            if item[3] is None:
                item[3] = Colors.YELLOW + "?" + Colors.ENDLINE;
            else:
                if re.search('-\d+\.\d+', item[3]):
                    item[3] = Colors.RED + item[3] + '%' + Colors.ENDLINE
                else:
                    item[3] = Colors.GREEN + item[3] + '%' + Colors.ENDLINE
            if item[4] is None:
                item[4] = Colors. YELLOW + "?" + Colors.ENDLINE
            else:
                if re.search('-\d+\.\d+', item[4]):
                    item[4] = Colors.RED + item[4] + '%' + Colors.ENDLINE
                else:
                    item[4] = Colors.GREEN + item[4] + '%' + Colors.ENDLINE


def process_data(data, fields=['rank', 'symbol', 'price_usd', 'percent_change_24h', 'percent_change_1h', 'market_cap_usd'],
                 currency='USD', humanize=True):

    if currency != 'USD':
        pos = 0
        for field in fields:
            fields[pos] = field.replace('usd', currency.lower())
            pos += 1

    # Initialize structure
    tabulated_data = []
    tabulated_data.append(copy.copy(fields))   # Headers in position 0

    pos = 0
    for header in tabulated_data[0]:   # Headers in position 0
        good_header = difflib.get_close_matches(header, fields_good_name.keys())[0]
        tabulated_data[0][pos] = fields_good_name[good_header]
        if good_header in ['price', 'market_cap']:
            tabulated_data[0][pos] = tabulated_data[0][pos].replace('USD', currency)
        pos += 1

    for item in data:
        tab_item = []
        for field in fields:
            if humanize and re.search('market_cap*', field):
                tab_item.append(intword(int(float(item[field]))))
            else:
                tab_item.append(item[field])
        tabulated_data.append(copy.copy(tab_item))

    return tabulated_data


def find_data(data, symbols):

    symbols = [x.upper() for x in symbols]   # Convert to upper-case
    filtered_items = []
    for item in data:
        if item['symbol'] in symbols:
            filtered_items.append(item)

    return filtered_items
