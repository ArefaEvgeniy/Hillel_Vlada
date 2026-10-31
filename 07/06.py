def hello():
    print("Hello, World!")


def calculate_average(b, a):
    if b > a:
        result = (b + a) / 2 + a
    else:
        return b * a // 2

    return result, b, a


...
a = 56
b = 45
c = calculate_average(a, b)
print(c)
hello()
...
z = 78
hello()
w = calculate_average(66, z)
print(w + 5)
...
e = 9
r = hello()
print(r)
calculate_average(e, 99)
...
