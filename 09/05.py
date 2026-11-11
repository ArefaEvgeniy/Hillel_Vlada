def fn(n):
    if n % 2 == 0:
        return n * 2
    return n + 1


my_list = [1, 2, 3, 4, 5, -100, 6, 0, 8, 9, 10]

new_list = list(map(fn, my_list))
print(new_list)

new_list_2 = list(map(lambda n: n * 2 if n % 2 == 0 else n + 1, my_list))
print(new_list_2)

list_2 = list(filter(lambda n: n % 2 == 0, my_list))
print(list_2)

list_3 = list(filter(lambda n: n * 2, my_list))
print(list_3)
