def decorator(func):
    def wrapper():
        print("-------Starting the function...-------")
        func()
        print("-------Ending the function.-------")
    return wrapper


def local_function():
    print("Starting the local function...")
    print("Hello from the local function!")
    print("Ending the local function.")


local_function()
my_func = decorator(local_function)
print()
my_func()
