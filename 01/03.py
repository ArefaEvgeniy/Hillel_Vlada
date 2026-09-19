from langdetect import detect


lang = detect("Bonjour tout le monde")
print(detect("Цей текст надрукований українською мовою"))

print(lang)

a = 67
print(a)
