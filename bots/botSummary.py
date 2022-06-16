from myquery import *
import time
import threading
from myquery import *
import logging
import sys
from currency import *

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
				co.update()
				currencies.append(co)
				logging.info("Holding:" + co.trade_token + " x " +  str(co.getBalance()) + " @ $" + str(co.getPrice()))
				dollar_total=dollar_total+currencies[bot].getDollarValue()

			logging.info("<" + self.config["account_summary"]["known_as"] +"> Total Account Dollar Value $" + str(dollar_total))
			refreshTime=self.config["account_summary"]["refresh_time"]
			time.sleep(refreshTime)
