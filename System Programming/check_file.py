#!/usr/bin/python3
import os     #provides us with access to different functions on our OS
import sys    
'''we are able to interact with the OS, filesystem and permissions'''

if len(sys.argv)==2:
	filename=sys.argv[1]
	if not os.path.isfile(filename):
		print('[-]'+filename+' does not exist')
		exit(0)
	if not os.access(filename,os.R_OK):
		print('[-] '+filename + ' access denied')
		exit(0)