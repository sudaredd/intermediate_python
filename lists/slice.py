mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = mylist[0:5]

print(a)

lists_org = ['banana', 'apple', 'grapes']
list_cpy = lists_org.copy()
list_cpy1 = list(lists_org)
list_cpy2 = lists_org[:]

print(lists_org)
print(list_cpy)

list_cpy.append('orange')
print(lists_org)
print(list_cpy)
print(list_cpy1)
print(list_cpy2)