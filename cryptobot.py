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
from cmdhelp import *


def initialiseLogs(loggingLevel):
	madeDIR=False
	if not os.path.exists("logs"):
		os.makedirs("logs")
		print("Logs Directory Made")
		madeDIR=True

	time = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
	logFname="logs/crypto_log_"+time+".log"
	logging.basicConfig(level=loggingLevel,format="%(asctime)s [%(levelname)s] %(message)s",handlers=[logging.FileHandler(logFname)])
	coloredlogs.install(level=loggingLevel,fmt="[%(asctime)s] [%(levelname)s] [%(message)s]",handlers=[logging.StreamHandler(sys.stdout)])
	logging.info("Program Started")

	if madeDIR==True:
		logging.warning("Logs Directory Does Not Exsist")
		logging.info("Logs Directory Made")

def help():
	myhelp.printHelpMessage()
	sys.exit()

def regenConfig():
	Config.deleteConfig()
	Config.cfg = configparser.ConfigParser()
	Config.generateConfig()
	Config.init()

def regenBotConfig():
	botManager.regenerateDefaultBotConfiguration()
	print("Bot Configuration Regenerated")

def run():
	Config.init()
	botManager.initialiseBots();

def checkArgs(args):
	if args[1]=="-debug":
		initialiseLogs(logging.DEBUG)
		logging.info("DEBUG Mode Selected")
	else:
		initialiseLogs(logging.INFO)
	Config.init()
	for i in range(len(args)):
		#print(args[i])
		if args[i] == "-h":
			help()
		elif args[i] == "-rc":
			regenConfig()
		elif args[i] == "-rb":
			regenBotConfig()
		elif args[i] == "-ak":
			key=args[i+1]
			Config.updateApiKey(key)
			logging.warning("API Key Updated")
		elif args[i] == '-sk':
			key=args[i+1]
			Config.updateSKey(key)
			logging.warning("API Secret Key Updated")
		elif args[i] == "-e":
			time.sleep(0.01)#Delay so any logging in the sister thread can be completed
			logging.warning("Exit Argument Given - exiting now")
			sys.exit()
	#run()

if __name__=='__main__':
	
	if len(sys.argv) > 1:
		checkArgs(sys.argv)
	else:
		initialiseLogs(logging.INFO)
		run()

