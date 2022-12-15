x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))


def quarter(x, y):
    if x != 0 and y != 0:
        if x > 0:
            if y > 0:
                return 1
            else:
                return 4
        else:
            if y > 0:
                return 2
            else:
                return 3
    else:
        print('Координаты не должны быть равны 0!')


print('Номер четверти: ', quarter(x, y))
