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

# Print basic details
print("Name:", information["name"])
print("Age:", information["age"])

# Print home city
print("Home City:", information["address"]["home"]["city"])

# Print native address zip code
print("Native ZIP Code:", information["address"]["natives"]["zip"])

# Print hobbies
print("Hobbies:", information["hobbies"])
