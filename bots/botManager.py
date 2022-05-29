import json
from myquery import *
import threading
from bots.botSummary import *

class botManager:
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