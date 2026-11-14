def decorator(func):
    def wrapper(*args, **kwargs):
        print("-------Starting the function...-------")
        result = func(*args, **kwargs)
        print("-------Ending the function.-------")
        return result
    return wrapper


@decorator
def local_function():
    print("Hello from the local function!")


@decorator
def sum(a, b):
    return a + b


local_function()
print()
result = sum(10, 56)
print(result)
