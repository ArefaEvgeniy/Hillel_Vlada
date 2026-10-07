my_list_1 = [3, 0, 4.34, "RRR", True, [1, 2, 3], "Hello"]

print(my_list_1[0])
print(my_list_1[3])
print(my_list_1[5][1])
print(my_list_1[len(my_list_1) - 1])
print(my_list_1[-1])
print(my_list_1[-2])

print(my_list_1[1:5])

print(my_list_1[3:])
print(my_list_1[0:])
print(my_list_1[:])
print(my_list_1[3::2])
print(my_list_1[::3])
print(my_list_1[:3:2])

print(my_list_1[-1:-4:-1])
print(my_list_1[-1::-1])
print(my_list_1[::-1])

if len(my_list_1) > 9:
    print(my_list_1[9])

if len(my_list_1) > 5:
    print(my_list_1[5])

my_list_2 = []

if len(my_list_2) > 0:
    print(my_list_2[-1])
