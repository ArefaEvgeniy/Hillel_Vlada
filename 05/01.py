a = "Hello, World! It's my dog."
b = 'Hello, "World!"'
c = 'Hello, "World!" ' + "It's my dog."
d = "Hello, \"World!\" It\'s my\n dog."
e = """Hello, "World!" It's my dog."""
f = r"\n - this is a new line"

print(a)
print(b)
print(a == b)
print(c)
print(a + b)
print(d)
print(e)
print(f)

print(a.upper())
print(a)
