def decorator(func):
    def wrapper():
        print("-------Starting the function...-------")
        func()
        print("-------Ending the function.-------")
    return wrapper


@decorator
def local_function():
    print("Starting the local function...")
    print("Hello from the local function!")
    print("Ending the local function.")


@decorator
def main():
    print("This is the main function.")


@decorator
def sum():
    a = 10
    b= 56
    print(f"The sum of {a} and {b} is: {a + b}")


local_function()
print("----------")
main()
print("----------")
sum()
