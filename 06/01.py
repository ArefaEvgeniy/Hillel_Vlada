t = (1, "hello", [3, 4, 5])
a = [1, "hello", [3, 4, 5]]

print(type(t))
t[2].append(6)
print(t)

b = list(t)
