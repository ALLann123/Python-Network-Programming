#!/usr/bin/python3

try:
	num_one=int(input("Enter first number>> "))
	num_two=int(input("Enter Second number>> "))
	result=num_one/num_two
	print(f"Division: {result}")
except ZeroDivisionError:
	print()
	print("Division By error not permitted!!")
except KeyboardInterrupt:
	print()
	print("Detecting keyboard Interrupt")
except ValueError:
	print()
	print("Enter Number!!")