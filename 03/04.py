a = 10

if a > 0:
    print("a is positive")
else:
    if a == 0:
        print("a is zero")
    else:
        print("a is not positive")


print("a is positive") if a > 0 else (print("a is zero") if a == 0 else print("a is not positive"))

vlada = 1 if a > 0 else -1
print(vlada)
