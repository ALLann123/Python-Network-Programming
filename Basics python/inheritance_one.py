#!/usr/bin/python3

class Person:     #these is the base class
	def __init__(self):
		self.name=input("Whats your name? ")
		self.age=int(input("How Old are you? "))

class worker(Person):   #is the derived class inheriting from Person and also acts as the base class for player
	def __init__(self):
		print()
		print("Employee Information")
		Person.__init__(self)
		self.job=input("Occupation>> ")
		self.salary=int(input("Salary Earned: "))

	def display_details(self):
		print()
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")
		print(f"JOB: {self.job}")
		print(f"Salary: {self.salary}")

class player(worker):    #is the derived class inheriting from both class worker and person acting as base classes
	def __init__(self):
		print("Information About Player")
		Person.__init__(self)
		worker.__init__(self)
		print()
		print("Sport Details")
		self.sport=input("Sport Played: ")
		self.position=input("Position onthe pitch: ")

	def display_details(self):
		worker.display_details(self)
		print(f"Sport: {self.sport}")
		print(f"Position Played: {self.position}")

employee_1=player()
employee_1.display_details()
