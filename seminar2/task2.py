# 2) Требуется найти наименьший натуральный делитель целого числа N, 
# отличный от 1.
# Пример:
# n = 15: Ответ: 3
# Для n = 35: Ответ: 5

number = int(input('Введите число: '))

for i in range(2, number + 1):
    if number % i == 0:
        print('Наименьший натуральный делитель:', i)
        break