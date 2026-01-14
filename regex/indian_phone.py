import re

phone_number = input("Enter Indian phone number: ")

pattern = r"^(?:\+91|91)?[6-9]\d{9}$"

if re.match(pattern, phone_number):
    print("Valid Indian phone number")
else:
    print("Invalid Indian phone number")
