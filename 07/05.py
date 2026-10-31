def calculate_average(b, a):
    if b > a:
        result = (b + a) / 2 + a
    else:
        result = b * a // 2

    print(result)


...
a = 56
b = 45
calculate_average(a, b)
...
z = 78
calculate_average(99, z)
...
e = 9
calculate_average(e, 99)
...
