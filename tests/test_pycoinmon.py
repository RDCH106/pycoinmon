import unittest
import pycoinmon.common as common


class TestPycoinmon(unittest.TestCase):

    def setUp(self):
        self.response = [
            {
                "id": "bitcoin",
                "name": "Bitcoin",
                "symbol": "BTC",
                "rank": "1",
                "price_usd": "15653.3",
                "price_btc": "1.0",
                "24h_volume_usd": "14446900000.0",
                "market_cap_usd": "261915508097",
                "available_supply": "16732287.0",
                "total_supply": "16732287.0",
                "max_supply": "21000000.0",
                "percent_change_1h": "0.75",
                "percent_change_24h": "4.73",
                "percent_change_7d": "34.5",
                "last_updated": "1512920953",
                "price_eur": "13304.365802",
                "24h_volume_eur": "12278998186.0",
                "market_cap_eur": "222612466952"
            },
            {
                "id": "ethereum",
                "name": "Ethereum",
                "symbol": "ETH",
                "rank": "2",
                "price_usd": "452.479",
                "price_btc": "0.0288748",
                "24h_volume_usd": "1736900000.0",
                "market_cap_usd": "43552764899.0",
                "available_supply": "96253671.0",
                "total_supply": "96253671.0",
                "percent_change_1h": "0.58",
                "percent_change_24h": "-7.03",
                "percent_change_7d": "-5.36",
                "last_updated": "1512920957",
                "price_eur": "384.58000126",
                "24h_volume_eur": "1476260786.0",
                "market_cap_eur": "37017236998.0"
            }
        ]

    def test_tabulate_data(self):
        print("--test tabulate data--")
        tabulated_data = common.process_data(self.response)
        self.assertEqual(len(tabulated_data), 3)
        # all items must have same number of fields
        for item in tabulated_data:
            self.assertEqual(len(item), len(tabulated_data[0]))

        self.assertEqual(tabulated_data[0][0], common.fields_good_name["rank"])
        self.assertEqual(tabulated_data[0][1], common.fields_good_name["symbol"])
        self.assertEqual(tabulated_data[0][2], common.fields_good_name["price"])
        self.assertEqual(tabulated_data[0][3], common.fields_good_name["percent_change_24h"])
        self.assertEqual(tabulated_data[0][4], common.fields_good_name["percent_change_1h"])
        self.assertEqual(tabulated_data[0][5], common.fields_good_name["market_cap"])

if __name__ == '__main__':
    unittest.main()
