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
	ooAssets="Output Owned Assets"


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
	def deleteConfig():
		overwriteFile = open("config.cfg","w")
		overwriteFile.close()

	@staticmethod
	def saveConfig():
		# Save any configuration changes
		with open(Config.fileName, "w") as configfile:
			Config.cfg.write(configfile)

	@staticmethod
	def loadConfig():
		Config.cfg.read(Config.fileName)
		logging.info("Config Paramters Loaded")

	@staticmethod
	def generateConfig():
		gereateFileIfNotExist = open("config.cfg","a")
		gereateFileIfNotExist.close()

		Config.cfg.add_section(Config.apisec)
		Config.cfg.set(Config.apisec, Config.apiKey, "<change me>")
		Config.cfg.set(Config.apisec, Config.apiSKey, "<change me>")

		Config.cfg.add_section(Config.botsec)
		Config.cfg.set(Config.botsec, Config.refreshTime, "5")
		Config.cfg.set(Config.botsec, Config.token, "ETH_BTC")

		Config.cfg.add_section(Config.clisec)
		Config.cfg.set(Config.clisec, "Show Graphs", "FALSE")
		Config.cfg.set(Config.clisec, Config.ooAssets, "TRUE")

		Config.saveConfig()
		logging.info("Generated New Config")

	@staticmethod
	def updateApiKey(key):
		Config.cfg.set(Config.apisec, Config.apiKey, key)
		Config.saveConfig()

	@staticmethod
	def updateSKey(key):
		Config.cfg.set(Config.apisec, Config.apiSKey, key)
		Config.saveConfig()

