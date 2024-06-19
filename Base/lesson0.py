# это однострочный комментарий

"""
Это многострочный комментарий
Здесь можно продолжать писать
Это будет проигнорировано при исполнении
"""

print("Hello world!")
print("Hikmatulloh")

# Арифметические операции +, -, *, /, **, //, %
print(12 + 5) # Сложени
print(34 - 13) # Вычитание 
print(56 * 4) # Умножение
print(76 / 4) # Деление (классическое или истинное деление)
print(5 * 7) # Возведение в степень
print(17 // 3) # Деление с округлением вниз
print(5 % 7) # Деление по модулю (вычисляет остаток от деления)

# Переменные
number = 23
print(number) # Выводить 23

name = "Hikmatulloh"
print(name) # Выводить Hikmatulloh

a = 14
b = 12.5
# print(a + b)
c = a + b
print(c)
print(a - b)

# Типы данных 
# int(integer) = 12, 34, 56 целые числы 
# float = 12.4, 45.3, 15.3 число с остатком
# str(string) = "Hello", "hikmatulloh" строки 
# bool(booling) = логический тип данных, возврашает True или False

print(type(a))
print(type(b))
print(type(name))

test_1 = print(bool(21 > 4))
test_2 = print(bool(21 < 4))

# Операторы сравнение 
print(a > b, b < a) # Больше, меньше
print(a == b) # Равно
print(a != b) # Не равно
print(a >= b) # Больше или равно
print(a <= b) # Меньше или равно 

# Ввод данных (функция input)
name = input("Enter your name: ")
print("Hi",name)

# Калькулятор 
number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

print(number_1 + number_2)

# Касса 
samsa = int(input("Канча самса: "))
chay = int(input("Канча чай: "))
nan = float(input("Канча нан: "))
summa = (samsa * 80) + (chay * 10) + (nan * 30)

print("Сизден",summa, "сом")