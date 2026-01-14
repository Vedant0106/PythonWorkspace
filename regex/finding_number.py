import re

text = input("Write your name and age :")

numbers = re.findall(r"\d+", text)
print(numbers)
