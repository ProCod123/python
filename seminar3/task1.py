
length = int(input('Определите длину списка: '))
list = []
for number in range(length):
    list.append(int(input(f'Введите значение элемента №{number}: ')))
print(f'Сформирован список: {list}')

sum = 0
terms = ''
for i in range(1, len(list), 2):
    sum += list[i]
    terms += ' + ' + str(list[i])
print(f'Сумма нечётных элементов равна: {terms[3:]} = {sum}')    