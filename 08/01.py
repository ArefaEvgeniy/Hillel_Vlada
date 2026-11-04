name = "Bob"


def func_2():
    global name
    name = "Alice"
    print(f"Hi, {name}!")


def func_3():
    def inner_func():
        name = "Charlie"
        print(f"Hey, {name}!")

    inner_func()
    print(f"Goodbye, {name}!")


func_2()
func_3()
