while True:
    age = input("Please enter your age: ")
    if age.isdigit() and 0 < int(age) < 120:
        break

    print("Invalid input. Please enter a valid age between 1 and 119.")
