from collections import Counter

a = "aaaabbbccd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.most_common(2))