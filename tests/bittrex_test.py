import unittest
from bittrex import bittrex_api


class Core(unittest.TestCase):
    def test__query(self):
        bapi = bittrex_api(debug=True)

        # %Y-%m-%d %H:%M:%S%z
        data = bapi.query("2018-06-15 14:35:00-07:00")
        expected = [0.00295237, 6510.655000000001, 19.221862502350003]

        self.assertEqual(expected, data)
