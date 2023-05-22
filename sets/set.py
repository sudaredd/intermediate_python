odds = {1, 3, 5, 7}
even = {0, 2, 4, 6}
prime = {2, 3, 5, 7}

print("union", odds.union(even))
print("intersection", odds.intersection(even))
print("intersection", odds.intersection(prime))