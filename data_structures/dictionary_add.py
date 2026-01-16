# Creating a dictionary
myFriends = {
    "Ravi": 20,
    "Amit": 22,
    "Sneha": 21
}

# Deleting the whole dictionary
del myFriends
# print(myFriends.items())  # This would cause an Error because the variable is gone


# Nested dictionary example
information = {
    "name": "Alice",
    "age": 28,
    "address": {
        "home": {
            "street": "123 Main St",
            "city": "Wonderland",
            "zip": "12345"
        },
        "work": {
            "street": "456 Work Rd",
            "city": "Worktown",
            "zip": "67890"
        },
        "natives": {
            "street": "456 Work Rd",
            "city": "Worktown",
            "zip": "67890"
        }
    },
    "hobbies": ["reading", "traveling", "swimming"]
}

# Accessing dictionary values
print(information["name"])
print(information["address"]["home"]["city"])
print(information["hobbies"][1])
