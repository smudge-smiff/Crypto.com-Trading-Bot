import configparser
import logging
import os.path

class Config:

	fileName="config.cfg";
	cfg = configparser.ConfigParser()

	apisec="API Configuration"
	apiKey="api key"
	apiSKey="secretKey"

	botsec="Bot Configuration"
	refreshTime="Refresh Time"
	token="Token"

	clisec="Client Configuration"



	@staticmethod
	def init():
		file_exists = os.path.exists(Config.fileName)

		if not file_exists:
			logging.warning("Config File Does NOt Exsist")
			Config.generateConfig()
		else:
			logging.info("Config File Found")

		Config.loadConfig()

	@staticmethod
	def loadConfig():
		Config.cfg.read(Config.fileName)
		logging.info("Config Paramters Loaded")

	@staticmethod
	def generateConfig():
		gereateFileIfNotExist = open("config.cfg","a")
		gereateFileIfNotExist.close()

		Config.cfg.add_section(apisec)
		Config.cfg.set(apisec, apiKey, "<change me>")
		Config.cfg.set(apisec, apiSKey, "<change me>")

		Config.cfg.add_section(botsec)
		Config.cfg.set(botsec, refreshTime, "5")
		Config.cfg.set(botsec, token, "ETH_BTC")

		Config.cfg.add_section(clisec)
		Config.cfg.set(clisec, "Show Graphs", "FALSE")

		Config.saveConfig(Config.fileName)
		logging.info("Generated New Config")

	@staticmethod
	def saveConfig(configName):
		# Save any configuration changes
		with open(configName, "w") as configfile:
			Config.cfg.write(configfile)
