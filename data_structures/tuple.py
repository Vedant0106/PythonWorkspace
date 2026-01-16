# Tuple slicing example

myTuple = ("Apple", 10, "Orange", "Grapes", 20.0, 10)

# 3. Slicing from index 2 up to (but not including) index 4
print(myTuple[2:4])        # Output: ('Orange', 'Grapes')

# 4. Slicing from the beginning up to index 4
print(myTuple[:4])         # Output: ('Apple', 10, 'Orange', 'Grapes')

# 5. Slicing from index 2 to the end
print(myTuple[2:])         # Output: ('Orange', 'Grapes', 20.0, 10)

# 6. Slicing with negative indices
print(myTuple[-4:-1])      # Output: ('Orange', 'Grapes', 20.0)


sensor_readings = ("2026-01-16", 22.5, "Sunny", 1013.2, 45, "North", "Active")

# get the weather condition
print(sensor_readings[2])  # Output: Sunny

# very last item
print(sensor_readings[-1]) # Output: Active

# last three items
print(sensor_readings[-3:]) # Output: (45, 'North', 'Active')
