from myquery import *
import time
import threading
from myquery import *
import logging
import sys

class botSummary:
	thread=None 
	config=None

	def __init__(self, jsonData):
		self.thread=threading.Thread(target=self.threads, args=())
		self.config=jsonData
		logging.info("Account Summary Bot Started")
		#print("hello")

	def threads(self):
		while True:
			tokens=[]
			currencies=[]
			dollar_total=0
			for bot in range(len(self.config["bots"])):
				t=self.config["bots"][bot]["trade_token"]
				#print(t)
				tokens.append(t)
				c=t.split("_")
				co=currency(c[0], t)
				currencies.append(co)
				dollar_total=dollar_total+currencies[bot].getDollarValue()
			logging.info("<" + self.config["account_summary"]["known_as"] +"> Total Account Dollar Value $" + str(dollar_total))
			refreshTime=self.config["account_summary"]["refresh_time"]
			time.sleep(refreshTime)




class currency:
	currency=None
	trade_token=None
	def __init__(self, currency,trade_token):
		self.currency=currency
		self.trade_token=trade_token

	def getBalance(self):
		return myquery.getCurrencySummary(self.currency)["result"]["accounts"][0]["balance"]

	def getPrice(self):
		return myquery.getBidPrice(self.trade_token)

	def getDollarValue(self):
		value=self.getBalance()*self.getPrice()
		return value