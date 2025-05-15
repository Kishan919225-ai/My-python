

import re

name = input("Enter name: ")
pattern1="^[a-zA-Z]+$"
if re.match(pattern1,name):
    print(f"NAME:{name}")
else:
    print("invalid name")

contact = input("Enter your contact no.: ")
pattern2= "^[0-9]{10}$"
if re.match(pattern2,contact):
    print(f"Contact no.:{contact}")
else:
    print("Invalid contact no.")

address=input("Enter adddress: ")
pattern3="^[a-zA-z1-9]+$"
if re.match(pattern3,address):
    print(f"ADDRESS:{address}")

# class,object,constructor,inheritenace,scope,,setter and getter