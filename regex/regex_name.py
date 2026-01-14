import re

name = input("Enter student name: ")

pattern = r"^[A-Za-z]+$"

if re.match(pattern, name):
    print("Valid name")
else:
    print("Invalid name (only letters allowed)")
