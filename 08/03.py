def func(a, b=1, c=0):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("-------------------")


a = 10
b = 88
func(b, 100, a)
func(b, 100)
func(b)
