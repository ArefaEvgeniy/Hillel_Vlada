my_list = [23, 0, -34, 345, 12, 99, -120, 45, 67, 89]

index = 0
result = 0
while index < len(my_list):
    if my_list[index] <= 0:
        index += 1
        continue
    result += my_list[index]
    index += 1
print(f"The sum of positive numbers in the list is: {result}")


result_2 = 0
for vlada in my_list:
    if vlada <= 0:
        continue
    result_2 += vlada
print(f"The sum of positive numbers in the list is: {result_2}")
