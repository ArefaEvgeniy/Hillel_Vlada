import time


number = int(int(input("Enter a number: ")))

result = 1
while number > 1:
    print(number)
    # time.sleep(1)
    if number % 5 == 0:
        number -= 1
        continue
    result *= number
    if result > 1000000:
        print("The result is too large to compute.")
        break
    number -= 1
else:
    print("ELSE")

print(f"The factorial of {number} is {result}")
