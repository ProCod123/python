
quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('Диапазон значений x (0, +inf) y (0, +inf)')
elif quarter == 2:
    print('Диапазон значений x (0, -inf) y (0, +inf)')
elif quarter == 3:
    print('Диапазон значений x (0, -inf) y (0, -inf)')
elif quarter == 4:
    print('Диапазон значений x (0, +inf) y (0, -inf)')
else:
    print('Вы ввели некорректные данные')
