import requests
from datetime import datetime

import logging
FORMAT = '%(asctime)-15s [%(levelname)s] %(filename)s(%(lineno)d): %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('zen_tx_utils')
logger.setLevel(logging.INFO)


class bittrex_api():
	''' Some useful tools using the Bittrex API.'''

	coin = ""  # Any available, defaults to ZEN
	market = ""  # BTC or ETH
	coin_market_history = []
	usdt_market_history = []

	def __init__(self, market="BTC", coin="ZEN", debug=False):
		''' market = BTC/ETH, coin = any available '''

		if debug:
			logger.setLevel(logging.DEBUG)

		self.coin = coin
		self.market = market
		self.refresh()

	def refresh(self):
		''' Refresh coin history data. '''

		response = requests.post("https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName={}-{}&tickInterval=day".format(self.market, self.coin))
		self.coin_market_history = response.json()['result']

		response = requests.post("https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=USDT-{}&tickInterval=day".format(self.market))
		self.usdt_market_history = response.json()['result']

	def query(self, date_string):
		''' Obtain coin information on a particular date.

					Inputs:
						Date format: %Y-%m-%d %H:%M:%S%z (ex. 18-06-15 14:35:00-07:00)

					Returns:
						List[coin_value, btc_value, usdt_value]
		'''

		logger.debug("Bittrex query: {}".format(date_string))
		convert = date_string[:-3] + date_string[-2:]
		logger.debug("Converted to date format: {}".format(convert))
		test_date = datetime.strptime(convert, "%Y-%m-%d %H:%M:%S%z")

		coin_value = 0
		for entry in self.coin_market_history:
			comp_date = datetime.strptime(entry['T'], "%Y-%m-%dT%H:%M:%S")
			if test_date.date() == comp_date.date():
				coin_value = (entry['O'] + entry['C']) / 2

		btc_value = 0
		usdt_value = 0
		for entry in self.usdt_market_history:
			comp_date = datetime.strptime(entry['T'], "%Y-%m-%dT%H:%M:%S")
			if test_date.date() == comp_date.date():
				btc_value = (entry['O'] + entry['C']) / 2
				usdt_value = coin_value * btc_value
		return [coin_value, btc_value, usdt_value]
