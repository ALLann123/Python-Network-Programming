#!/usr/bin/python3

with open("file.txt",'r') as f:
	for line in f:
		print(f"Line: {line}")