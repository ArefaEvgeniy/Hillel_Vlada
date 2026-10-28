my_str = "Привіт, цей текст містить українські літери та символи."

a = my_str.encode('utf-8')
print(my_str)
print(a)
print(a.decode('Windows-1251'))
