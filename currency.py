from myquery import *
import time
import threading
from myquery import *
import logging
import sys


class currency:
	currency=None
	trade_token=None
	balance=0
	price=0
	def __init__(self, currency,trade_token):
		self.currency=currency
		self.trade_token=trade_token
		self.update()

	def update(self):
		self.setBalance()
		self.setPrice()

	def setBalance(self):
		self.balance = myquery.getCurrencySummary(self.currency)["result"]["accounts"][0]["balance"]

	def getBalance(self):
		return self.balance

	def setPrice(self):
		self.price = myquery.getBidPrice(self.trade_token)

	def getPrice(self):
		return self.price

	def getDollarValue(self):
		value=self.getBalance()*self.getPrice()
		return value
	