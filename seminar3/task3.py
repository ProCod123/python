import random

length = int(input('Определите длину списка: '))
list = []
list_fract_part = []
for i in range(length):
    random_number = round(random.random() * 10, 2)
    list.append(random_number)
    list_fract_part.append(round(random_number % 1, 2))
print(f'Сформирован список: {list}')

max_part = max(list_fract_part)
min_part = min(list_fract_part)
print(f'{max_part} - {min_part} = {round(max_part - min_part, 2)}')    