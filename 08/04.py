def func(a, b, c=0):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("-------------------")


a = 10
b = 88
func(c=b, b=100, a=a)
func(b=100, c=b, a=a)
func(c=b, a=a, b=100)
func(b, c=99, b=100)
func(b, b=100)
# func(1, c=99, a=200)
# func(b, 100)
# func(b)
