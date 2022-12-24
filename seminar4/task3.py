numbers = input('Введите цифры через пробел: ')
list = numbers.split()
result = []
for i in list:
    if list.count(i) == 1:
        result.append(i)
print('Неповторяющиеся цифры последовательности: ', ' '.join(result))        