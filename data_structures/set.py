set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

# Union
print(set_a | set_b)
# Output: {1, 2, 3, 4, 5, 6, 7}

# Intersection
print(set_a & set_b)
# Output: {4, 5}

# Difference (A - B)
print(set_a - set_b)
# Output: {1, 2, 3}

# Difference (B - A)
print(set_b - set_a)
# Output: {6, 7}

# Symmetric Difference
print(set_a ^ set_b)
# Output: {1, 2, 3, 6, 7}
