""""
Area Calculator Example
Author: Araceli M. SIERRA
"""

from __future__ import print_function
raw_input = input

print("Welcome, this is the begginning...")
name = raw_input("What's your name?")
option = raw_input('Enter C for "Circle" or T for "Triangle": ').upper()

if option == "C":
	radius = float(raw_input("Enter radius: "))
	area = 3.14 * (radius ** 2)
	print("Circle base is: %s" % area)
elif option == "T":
	base = float(raw_input("Enter base: "))
	height = float(raw_input("Enter height: "))
	area = .5 * base * height
	print("Triangle base is: %s" % area)
else:
	print("Value not found: %s" % option)
	
print('Exiting...')