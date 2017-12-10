import unittest
import pycoinmon.common as common


class TestPycoinmon(unittest.TestCase):
    def test_create(self):
        print("--test create--")
        response = [
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
        tabulated_data = common.process_data(response)
        self.assertEqual(len(tabulated_data), 3)

if __name__ == '__main__':
    unittest.main()
