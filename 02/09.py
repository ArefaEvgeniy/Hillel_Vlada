a = 10
b = "Bob"

print(a, end=" ")
print("dfgjdkhkjsrd")
print(56, sep="---")
print()
print(a, 55, b, "dfgjdkhkjsrd", 56, sep="")

with open("test.txt", "w") as fff:
    print(a, 55, b, "dfgjdkhkjsrd", 56, sep="   ", file=fff)
