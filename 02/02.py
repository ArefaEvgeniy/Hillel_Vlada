a = 67
b = 67
c = 67

print(id(a))
print(id(b))
print(id(c))

b += 3  # b = b + 3
b /= 2  # b = b / 2

print(id(a))
print(id(b))
print(id(c))

b *= 2
b -= 3
b = int(b)

print(id(a))
print(id(b))
print(id(c))
