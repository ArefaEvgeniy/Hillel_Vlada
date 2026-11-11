def sum(a, b):
    if a > b:
        return a - b
    else:
        return a + b


print(sum(15, 6))
qw = lambda a, b: a - b if a > b else a + b
print(qw(15, 6))
