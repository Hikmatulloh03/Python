# Строки и метод строк 

name = "Zakariya" # двойные кавычки 
surname = 'Asharov' # одинарные ковички 
bio = """
Zakariya Asharov is a talented Python developer.
He works at Google.""" 

print(name)
print(surname)
print(bio)

# c помощью встроенной функции  type узнаем тип
print(type(name))

# sentence = 'John is a software engineer. He's a python developer'
# print(sentence)

# File "<stdin>", line 1
#     sentence = 'John is a software engineer. He's a python developer'
#                                                 ^
# SyntaxError: invalid syntax

#  ставим \ перед символом
sentence = 'John is a software engineer. He\'s a python developer'

# или для создания строки используем двойные кавычки
# а для сокращения одинарные
sentence =  "John is a software engineer. He's a python developer"

# Форматирование строк
name = 'John'
surname = 'Nash'
company = 'Google'
bio = """
{0} {1} is a talented Python developer.
He works at {2}.
""".format(name, surname, company)

print(bio)

name = 'John'
surname = 'Nash'
company = 'Google'
bio = f"{name} {surname} is a talented Python developer.\nHe works at {company}."

print(bio)

# Конкантенация
bio = "John" + " Nash" + " is a talented Python developer.\nHe works at " + "Google"
#  обратите внимание на пробелы. Пробел для питона считается отдельным символом

print(bio)

# Метод  str()
name = 'John'
surname = 'Nash'  
age = 25  # (int)

print(name + " " + surname + ". He is " + str(age) + " years old")


name = input("Enter your name: ")
print(f"Hello {name}!")

# Методы строк
text = "uос згзамен нАчнёться через 12 минут!"

print(text.capitalize()) # Преобразует первый символ строки в верхний регистр.
print(text.lower())
print(text.casefold()) # Преобразует строку в нижний регистр (более агрессивно, чем lower()).
print(text.count()) # Подсчитывает количество непересекающихся вхождений подстроки.
print(text.upper()) # Преобразует строку в верхний регистр
# ...