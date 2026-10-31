a = {45, -2, 0, "Vlada", 45, "34", 0, "WWW", 45, (34, 2, 1)}

print(type(a))
print(a)
print(len(a))
print("Vlada" in a)

my_list = [56, 66, 12, 0, 45, 56, 12, 0, 66, 7, 0, 34, 66, 12, 0, 45, 56, 12, 0, 66, 7, 0, 34]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

new_list_2 = list(set(my_list))
print(new_list_2)
