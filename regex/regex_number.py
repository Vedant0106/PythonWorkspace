import re

marks = input("Enter marks: ")

pattern = r"^(100|[1-9]?\d)$"

if re.match(pattern, marks):
    print("Valid marks")
else:
    print("Invalid marks")
