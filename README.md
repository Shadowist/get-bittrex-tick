# Overview

This is a simple tool for querying coin information from Bittrex.

# Usage
```python
''' Obtain coin information on a particular date.

    Inputs:
      Date format: %Y-%m-%d %H:%M:%S%z (ex. 18-06-15 14:35:00-07:00)

    Returns:
      List[coin_value, btc_value, usdt_value]
'''
from bittrex import bittrex_api

# Initialize Class
bapi = bittrex_api(market="BTC", coin="ZEN", debug=True)

# Date format: %Y-%m-%d %H:%M:%S%z
data = bapi.query("2018-06-15 14:35:00-07:00")

# Return [coin_value, btc_value, usdt_value]
expected = [0.00295237, 6510.655000000001, 19.221862502350003]
```
