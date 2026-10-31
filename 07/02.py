my_dict = {"name": "Alice", "age": 30, "city": "New York", "country": "USA"}

for item in my_dict.values():
    print(item)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print("-------------")
for key, value in my_dict.items():
    print(f"{key}: {value}")
