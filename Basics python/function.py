#!/usr/bin/python3

#this a function iterating through a dictionary

def check_value(dict,item):
	for key, value in dict.items():
		if value==item:
			return True
	return False

students={"marks":200,"age":22,"name":"Allan"}

print(check_value(students,23))