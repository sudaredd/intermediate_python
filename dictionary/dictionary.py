mydict = {"name": "dars", "age": 38, "city": "nyc"}
mydict1 = dict(name="sud", age=41, city="JC")
print(mydict)
print(mydict1)

# check if key exists
if 'name' in mydict:
    print(f"name is {mydict['name']}")
else:
    print("doesn't exist")

# loop

for k in mydict:
    print("key is ", k)

for k in mydict.keys():
    print("with keys key is ", k)

for v in mydict.values():
    print("value is ", v)

for k, v in mydict.items():
    print("key and value ", k, v)

# keys allows only immutable like string, integer, tuple
tup = (8, 7)
mydictg = {tup: 15}
print(mydictg)


# delete entry
del mydict['name']
print(mydict)
mydict.pop('age')
print(mydict)
