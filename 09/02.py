# 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


number = 900
print(factorial(number))

result = 1
while number > 1:
    result *= number
    number -= 1

print(result)
