name = "Bob"


def func_2():
    name = "Alice"
    print(f"Hi, {name}!")
    return name


def func_3():
    def inner_func():
        name = "Charlie"
        print(f"Hey, {name}!")

    inner_func()
    print(f"Goodbye, {name}!")
    return inner_func


def func_4(func):
    print("start func_4")
    func()
    print("end func_4")


name = func_2()
vlada = func_3()

vlada()
print("--------------")
# inner_func()
func_4(vlada)
