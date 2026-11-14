def vegatable(func):
    def wrapper():
        print("tomato")
        func()
        print("salad")
    return wrapper


def bear(func):
    def wrapper():
        print("/------------------\\")
        func()
        print("\_________________/")
    return wrapper


@bear
@vegatable
def sandwich():
    print("Becone")


sandwich()
