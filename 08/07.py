def func(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print("-------------------")


func()
func(1, 2, 3)
func(a=10, b=20, c=30)
func(1, 2, 3, a=10, b=20, c=30)
