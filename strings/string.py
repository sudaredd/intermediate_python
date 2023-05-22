from timeit import default_timer as timer

my_str = "Hello world"
my_substr = my_str[1:5]
print(my_substr)

for c in my_str:
    print(c)

my_str = "    Hello world    "
print(my_str)
my_str = my_str.strip()
print(my_str)

print(my_str.upper())
print(my_str.lower())
print(my_str.find("el"))
print(my_str.count("o"))
print(my_str.replace("world","Universe"))

my_str = "how are you doing"
list = my_str.split()
new_str = ' '.join(list)
print(list)
print(new_str)

params = ["a"] * 10000000

#bad
start = timer()
new_str=''

for c in params:
    new_str +=c
stop = timer()
print("diff is ", stop-start)

#good
start = timer()
new_param_str = "".join(params)
stop = timer()
print("diff is ", stop-start)
# print(new_param_str)


# %s, format, f string