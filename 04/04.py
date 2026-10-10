my_list = [23, 0, -34, 345, 12, 99, -120, 45, 67, 89]

result = 0
indexes = []
for index, value in enumerate(my_list):
    if value <= 0:
        indexes.append(index)
        continue
    result += value
print(f"The sum of positive numbers in the list is: {result}")
print(f"The indexes of non-positive numbers in the list are: {indexes}")
