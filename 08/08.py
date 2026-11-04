def func(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("-------------------")


vlada = [56, 34, 89]
func(vlada[0], vlada[1], vlada[2])
func(*vlada)  # func(56, 34, 89)
