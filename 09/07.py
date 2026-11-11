def func(n):
    while n > 1:
        yield n
        n -= 1


a = func(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# for item in a:
#     print(item)
