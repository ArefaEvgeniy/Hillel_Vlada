a = 67
b = "Hello"

print(id(a))
print(id(b))
print(b)

b = a
print(b)
print(id(a))
print(id(b))

a = a + 3
print(a)
print(b)
print(id(a))
print(id(b))