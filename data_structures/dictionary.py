# Create a dictionary
student = {
    "name": "Vedant",
    "age": 25,
    "course": "Python",
    "marks": 85
}

# Access values
print("Name:", student["name"])
print("Marks:", student["marks"])

# Update value
student["marks"] = 90

# Add new key-value pair
student["grade"] = "A"

# Check if key exists
if "age" in student:
    print("Age is present")

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# Remove a key
student.pop("age")

print("Final Dictionary:", student)
