def func(a, b, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"kwargs: {kwargs}")
    print("-------------------")


a = 10
b = 88
func(c=b, b=100, a=a, d=1000, e=-45, f=999)

