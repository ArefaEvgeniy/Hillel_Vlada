import copy


a = [2, 4, [1, 2, 3], 12, "345"]

b = copy.deepcopy(a)

b[2].append("new element")

print(a)
print(b)
