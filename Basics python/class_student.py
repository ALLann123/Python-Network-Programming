#!/usr/bin/python3

class Student:
	def __init__(self):
		self.name=input("Enter Name>> ")
		self.course=input("Course of Study: ")
		self.reg_no=input("Reg Number: ")
		self.marks=int(input("Enter Marks:"))

	def display_details(self):
		print()
		print(f"Name:{self.name}")
		print(f"Degree: {self.course}")
		print(f"Reg Number: {self.reg_no}")
		print(f"Marks Scored: {self.marks}")

	def get_grade(self):
		if self.marks >= 80:
			self.display_details()
			print("Student Grade: A")
		elif self.marks >=70:
			self.display_details()
			print("Student Grade: B")
		elif self.marks >=60:
			self.display_details()
			print("Student Grade: C")
		elif self.marks >=50:
			self.display_details()
			print("Student Grade: D")
		else:
			self.display_details()
			print("Failed!! Advised to repeat")

stud_1=Student()
stud_1.get_grade()