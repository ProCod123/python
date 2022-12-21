
length = int(input('Определите длину списка: '))
list = []
for number in range(length):
    list.append(int(input(f'Введите значение элемента №{number}: ')))
print(f'Сформирован список: {list}')

result = []
middle = int((len(list) - 1)/2)
for i in range(middle + 1):
    result.append(list[i] * list[-i - 1])
print(f'Ответ: {result}')   