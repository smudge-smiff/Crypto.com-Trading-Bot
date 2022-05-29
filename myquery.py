import hmac
import hashlib
import time
import requests
import json
from config import *

class myquery:
	url="https://api.crypto.com/v2/"

	### Get Request Methods
	@staticmethod
	def getBidPrice(iname):
		method="public/get-ticker"
		ans=myquery.getResponse(method, "instrument_name=" + iname)
		return ans["result"]["data"]["b"]

	def getResponse(method, args):
		ans=requests.get(myquery.url+method+"?" + args)
		res=ans.json()
		return res

	### Post Request Methods
	@staticmethod
	def getCurrencySummary(cur):
		method="private/get-account-summary"
		req = {
			"id":12,
			"method": method,
			"api_key": myquery.getApiKey(),
			"params": {
				"currency": cur
			},
			"nonce": myquery.getNonce()
		}
		stmt=myquery.prepStatement(req)
		res=myquery.executeStmt(method, stmt)
		return res
		#print(json.dumps(res, indent=4, sort_keys=True))

	@staticmethod
	def getAccountSummary():
		method="private/get-account-summary"
		req = {
			"id":12,
			"method": method,
			"api_key": myquery.getApiKey(),
			"params": {},
			"nonce": myquery.getNonce()
		}
		stmt=myquery.prepStatement(req)
		res=myquery.executeStmt(method, stmt)
		return res
		#print(json.dumps(res, indent=4, sort_keys=True))

	@staticmethod
	def getTrades():
		method="private/get-trades"
		req = {
			"id":12,
			"method": method,
			"api_key": myquery.getApiKey(),
			"params": {
				"start_ts": 1622245713000
			},
			"nonce": myquery.getNonce()
		}
		stmt=myquery.prepStatement(req)
		myquery.executeStmt(method, stmt)

	@staticmethod
	def getOrderHistory():
		method="private/get-order-history"
		req = {
			"id":12,
			"method": method,
			"api_key": myquery.getApiKey(),
			"params": {
				"start_ts": 1622245713000
			},
			"nonce": myquery.getNonce()
		}
		stmt=myquery.prepStatement(req)
		res=myquery.executeStmt(method, stmt)

	@staticmethod
	def getApiKey():
		return Config.cfg.get(Config.apisec, Config.apiKey)

	@staticmethod
	def getNonce():
		return int(time.time() * 1000)

	@staticmethod
	def executeStmt(uri, stmt):
		#print(json.dumps(stmt, indent=4, sort_keys=True))
		ans=requests.post(myquery.url+uri, json=stmt, headers={'Content-Type':'application/json'})
		ans=ans.json()
		return ans
		#print(json.dumps(ans, indent=4, sort_keys=True))

	@staticmethod
	def prepStatement(req):
		paramString=""

		if "params" in req:
			paramString=myquery.params_to_str(req['params'], 0)

		sigPayload = req['method'] + str(req['id']) + req['api_key'] + paramString + str(req['nonce'])
		skey=Config.cfg.get(Config.apisec, Config.apiSKey)
		req['sig'] = hmac.new(
			bytes(str(skey), 'utf-8'),
			msg=bytes(sigPayload, 'utf-8'),
			digestmod=hashlib.sha256
		).hexdigest()
		return req

	@staticmethod
	def params_to_str(obj, level):
		MAX_LEVEL = 3
		if level >= MAX_LEVEL:
			return str(obj)

		return_str = ""
		for key in sorted(obj):
			return_str += key
			if isinstance(obj[key], list):
				for subObj in obj[key]:
					return_str += params_to_str(subObj, ++level)
			else:
				return_str += str(obj[key])
		return return_str