import copy


a = [2, 4, 12, "345"]

b = a[:]
c = a.copy()
d = copy.copy(a)

b.append("new element")
c.pop()
d.reverse()

print(a)
print(b)
print(c)
print(d)
