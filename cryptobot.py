import coloredlogs
import os
import time
import logging
import sys
import datetime
import threading
from config import *
import requests
from myquery import *
from bots.botManager import *

def initialiseLogs():
	madeDIR=False
	if not os.path.exists("logs"):
		os.makedirs("logs")
		print("Logs Directory Made")
		madeDIR=True

	time = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
	logFname="logs/crypto_log_"+time+".log"
	lvl=logging.DEBUG
	logging.basicConfig(level=lvl,format="%(asctime)s [%(levelname)s] %(message)s",handlers=[logging.FileHandler(logFname)])
	coloredlogs.install(level=lvl,fmt="[%(asctime)s] [%(levelname)s] [%(message)s]",handlers=[logging.StreamHandler(sys.stdout)])
	logging.info("Program Started")

	if madeDIR==True:
		logging.warning("Logs Directory Does Not Exsist")
		logging.info("Logs Directory Made")

def run():
	initialiseLogs()
	Config.init()
	botManager.initialiseBots();



if __name__=='__main__':
	run()