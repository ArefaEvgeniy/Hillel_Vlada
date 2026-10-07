age = input("Enter your age: ")

if not age.isdigit() or int(age) == 0:  #  age = "45" -> True   age = "45a" -> False
    print("Invalid age. Please enter a positive number.")
elif int(age) <= 10:
    print("Milk")
elif int(age) < 18:
    print("Juice")
elif int(age) <= 50:
    print("Beer")
elif int(age) <= 100:
    print("Tea")
else:
    print("Invalid age. Please enter a positive number.")
