# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в 
# списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

import random

number =int(input('Введите цифру: '))
list = []
for i in range(-number, number + 1):
    list.append(i)
print('Список заполненный числами из промежутка [-N, N]:\n', list) 

# Заполняем список индексов случайными числами
index = []
for item in range(5):
    index.append(random.randint(0, len(list) - 1))
print('\nСписок индексов: ', index)

# Перемножаем элементы согласно выбранному индексу
result = 1
string = ''
for ind in index:
    result *= list[ind]
    string += '*' + str(list[ind]) 
print('\nОтвет: ',string[1:], ' = ', result)    