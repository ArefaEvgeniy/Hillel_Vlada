a = 0
b = 0

if a > 100:
    print("a is greater than 100")
elif a > 0:
    print("a is positive")
    a /= 2  # a = a / 2
    if a == 0:
        print("a is zero!!!")
    print("End if")
elif b == 0:
    print("b is zero")
elif a == 0 and b == 0:
    print("a is zero")
elif a < -1000:
    print("a is less than 1000")
else:
    print("a is negative")
    a *= 2

print("a:", a)
