import re

phone_number = input("Enter US phone number: ")

pattern = r"^(?:\+1\s?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}$"

if re.match(pattern, phone_number):
    print("Valid US phone number")
else:
    print("Invalid US phone number")
