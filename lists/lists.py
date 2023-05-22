mylist = ['banana',  'strawberry', 'apple']

print(mylist[0])
print(mylist[-1])


#loop
for fruit in mylist:
    print(fruit)

# to check item in list

if 'strawberry' in mylist:
    print('strawberry exists')

print(len(mylist))

mylist.append('sapota')

print(mylist)

mylist.insert(1, 'black berry')
print(mylist)

#remove last element
mylist.pop()
print(mylist)

mylist.remove('banana')
print(mylist)

sorted_l = sorted(mylist)
print(sorted_l)
print(mylist)
mylist.sort()
print(mylist)

mylist.clear()
print(mylist)

