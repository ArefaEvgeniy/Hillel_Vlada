def decorator(func):
    def wrapper():
        print("-------Starting the function...-------")
        func()
        print("-------Ending the function.-------")
    return wrapper


@decorator  # local_function = decorator(local_function)
def local_function():
    print("Starting the local function...")
    print("Hello from the local function!")
    print("Ending the local function.")


local_function()
