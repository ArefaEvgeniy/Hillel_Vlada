template_1 = "My name is {} and I am {} years old. {} is good name."
template_2 = "My name is {0} and I am {1} years old. {0} is good name."
template_3 = "My name is {name:^6} and I am {age:^6} years old. {name:^6} is good name."

a = "John"
b = 25.45

print(template_1)
print(template_1.format(a, b, a))
print(template_1.format("Vlada", 24, "Vlada"))
print(template_2.format("Vlada", 24))
print(template_3.format(age=24, name="Vlada"))
