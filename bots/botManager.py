import json
from myquery import *
import threading
from bots.botSummary import *

class botManager:
	@staticmethod
	def initialiseBots():
		with open("bots.json", "r") as read_file:
			data = json.load(read_file)
		bs=botSummary(data)

		try:
			bs.thread.start()
			while bs.thread.is_alive(): 
				bs.thread.join(1)  # not sure if there is an appreciable cost to this.
		except (KeyboardInterrupt, SystemExit):
			logging.warning("Key Board Interrupt Recieved, Exiting Thread(s)")
			sys.exit()

	@staticmethod
	def regenerateDefaultBotConfiguration():
		defaultBotJson={
			"account_summary": {
				"refresh_time": 5,
				"known_as": "SummaryBot"
			},
			"bots": [
				{
					"id": 1,
					"trade_token": "SPELL_USDC",
					"refresh_time": 1,
					"bs_threshold_perc": 1
				},
				{
					"id": 1,
					"trade_token": "RNDR_USDT",
					"refresh_time": 10,
					"bs_threshold_perc": 1
				}
			]
		}
		jsonTarget = open("bots.json", "w")
		jsonTarget.write(json.dumps(defaultBotJson, indent=4, sort_keys=False))
		jsonTarget.close()
