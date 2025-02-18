#!/usr/bin/python3
import os

with open('name.txt', 'w') as f:  #create a txt file
	f.write("WHO ARE WE?")

pwd=os.getcwd()   #use the library to get the current working directory
print(f"current working directory: {pwd}")
print()

#now list files inthe directory
list_directory=os.listdir(pwd)    #store the directories in a list the loop through them using a for loop
for directory in list_directory:
	print('[+] ',directory)

#read the txt file
print("*********************")
with open('name.txt','r')as f:
	print(f.read())
