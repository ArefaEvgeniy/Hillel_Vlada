def func(a, b, *args):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {args}")
    sum = 0
    for i in args:
        sum += i
    print(f"sum: {sum}")
    print("-------------------")


a = 10
b = 88
func(b, 100, a)
func(b, 100, a, 56, -56, 888, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009)
func(b, 100)
