add10 = lambda x: x + 10

add_two = lambda x, y: x + y

print(add10(21))
print(add_two(21, 31))

a = [1, 2, 3, 4]
li = list(map(lambda x: x * 2, a))
print(li)
li = [x * 2 for x in a]
print(li)

filtr = list(filter(lambda x: x % 2 == 0, a))
print(filtr)

filtr = [x for x in a if x %2 == 0]
print(filtr)

from functools import reduce

product_a = reduce(lambda x, y: x + y, a)
print(product_a)
