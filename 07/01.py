my_dict = {"name": "Alice", "age": 30, "city": "New York"}

print(my_dict["name"])
my_dict["name"] = "Bob"
print(my_dict["name"])
print(my_dict)
my_dict.update({"age": 31, "city": "Los Angeles", "country": "USA"})
print(my_dict)
my_dict.update({"children": {"name": "Charlie", "age": 5}})
print(my_dict)
if "phone" in my_dict:
    print(my_dict["phone"])
print(my_dict["name"])
print(my_dict.get("name", "Not Found"))
print(my_dict.get("phone", "Not Found"))
