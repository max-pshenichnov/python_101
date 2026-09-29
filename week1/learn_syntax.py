"""
В этом файле мы изучаем синтаксис питонга
"""

'''
так тоже можно оставлять заметки
'''

# так оформляются комментарии

import math
import turtle

variable = 100
print(variable**2 + 13)
print(variable*13 + 16)

# Alt + Shift + стрелка вниз = быстро скопировать строку!

print(f"наш ответ номер один: {variable**2 + 25}")
print("наш ответ номер один: ", variable**2 + 25, sep="")

seconds_in_min = 60
mins_in_hour = 60
hours_in_day = 24
days_in_year = 365

seconds_in_year = seconds_in_min * mins_in_hour * hours_in_day * days_in_year
print(f"секунд в году: {seconds_in_year}")

# Необычная арифметика питонга
our_number = 42
print(our_number**2) # квадрат
print(our_number**3) # куб
print(our_number / 7) # делим на 7
print(our_number * 10) # умножить на 10
print(our_number // 10) # деление нацело
print(our_number % 10) # остаток от деления

our_number += 1

print(math.pi)

our_sine = round(math.sin(math.pi/2), 6)
our_cosine = round(math.cos(math.pi/2))

print(f"синуз: {our_sine}")
print(f"козинуз: {our_cosine}")

# про типы данных
my_name = "Joe Mama"
my_age = 69
my_city = "Moscow"
my_wine = 2.5

first_group = ["Макс", "Даша", "Кристина"]
second_group = [
    "Олег", 
    "Сергей", 
    "Сергей"
]

print(type(my_name))
print(type(my_age))
print(type(my_city))
print(type(my_wine))
print(type(first_group))
print(type(second_group))

# Ctrl + Shift + Alt = увеличение курсора!

my_secret_system = {0:"выходи", 
                    1:"не выходи", 
                    2:"пей", 
                    3:"читай",
                    4:"спи",
                    5:"учись"}

print(type(my_secret_system))
print(my_secret_system[0])
print(my_secret_system[1])

# Тест с именем
student_name = "Петров Петр Петрович"
smth = student_name.split()

print(type(smth))
print(smth[0])
print(smth[1])
print(smth[2])
print(len(smth))

print(smth[:2])
print(smth[-2:])

print("Hello World!")