a = "   Hello, World!  It's   my      dog.          "

new_list = a.strip().split()
print(new_list)
b = " ".join(new_list)
print(b)
