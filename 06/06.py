my_set = {56, 66, 12, 0, 45, "7", 34}

print(my_set)
my_set.add(100)
print(my_set)
new_set = {"Hello", "World", 77}
my_set.add(frozenset(new_set))
print(my_set)
