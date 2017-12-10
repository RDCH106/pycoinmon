# -*- coding: utf-8 -*-

import difflib
import copy

fields_good_name = {
    "rank": "Rank",
    "symbol": "Symbol",
    "price": "Price (USD)",
    "percent_change_24h": "Change (24H)",
    "percent_change_1h": "Change (1H)",
    "market_cap": "Market Cap (USD)"
}


def process_data(data, fields=['rank', 'symbol', 'price_usd', 'percent_change_24h', 'percent_change_1h', 'market_cap_usd'],
                 currency='USD'):

    if currency.upper() != 'USD':
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
            tabulated_data[0][pos] = tabulated_data[0][pos].replace('USD', currency.upper())
        pos += 1



    for item in data:
        tab_item = []
        for field in fields:
            tab_item.append(item[field])
        tabulated_data.append(copy.copy(tab_item))


    return tabulated_data
