#!/usr/bin/python3

class Protocol(object):
	#create a constructor for initialization operations
	def __init__(self, name, port, descri):
		self.name=name
		self.port=port
		self.descri=descri
	def getProtocol_info(self):
		print(f"Name: {self.name}")
		print(f"Port:{self.port}")
		print(f"Description: {self.descri}")

ssh=Protocol("SSH",22,"is used for remote access mostly on servers")
ssh.getProtocol_info()
print()
ftp=Protocol("FTP", 21,"File sharing over the network")
ftp.getProtocol_info()

