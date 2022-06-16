class myhelp:
	@staticmethod
	def getHelpMessages():
		cmds=[]
		cmds.append(cmdhelp("-h", "Help - Displays this message"))
		cmds.append(cmdhelp("-rc", "Regenerated the Config File as per the defaults"))
		cmds.append(cmdhelp("-ak", "Updates the API Key", "-ak <API Key>"))
		cmds.append(cmdhelp("-sk", "Updates the API Secret Key", "-sk <Secret Key>"))
		cmds.append(cmdhelp("-e", "Immediatley ends the program once this argument is reached", "-sk <Secret Key>"))
		cmds.append(cmdhelp("-debug", "Enables the debug logging level"))
		return cmds

	def printHelpMessage():
		cmds=myhelp.getHelpMessages()
		for cmd in cmds:
			help_message=""
			if cmd.usage != "":
				help_message= cmd.token + " : " + cmd.help_sentance + " | " + cmd.usage
			else: 
				help_message= cmd.token + " : " + cmd.help_sentance
			print(help_message)

class cmdhelp:
	token=None
	help_sentance=None
	usage=None

	def __init__(self, token, help_sentance, usage=""):
		self.token=token
		self.help_sentance=help_sentance
		self.usage=usage