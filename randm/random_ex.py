import random

rnd = random.randrange(1, 10)
print(rnd)

mylist = list("ABCDEFGH")
print(mylist)
c1 = random.choice(mylist)
print(c1)

# picks unique elements
print(random.sample(mylist, 4))

# could pick duplicate
print(random.choices(mylist, k=3))

random.shuffle(mylist)
print(mylist)