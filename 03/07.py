my_list_1 = [3, 0, 4.34, "RRR", True, [1, 2, 3], "Hello"]
print(id(my_list_1))
my_list_2 = []
my_list_3 = [10,]

my_list_1.reverse()
print(id(my_list_1))
print(my_list_1)
my_list_1.append("New element")
print(id(my_list_1))
print(my_list_1)

print(len(my_list_1))
print(len(my_list_2))
print(len(my_list_3))

print("RRR" in my_list_1)
print(2 in my_list_1)
print([1, 2, 3] in my_list_1)
