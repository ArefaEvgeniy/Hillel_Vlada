def func(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("-------------------")


vlada = {"b": 34, "a": 56, "c": 89}

func(**vlada)  # func(a=56, b=34, c=89)
