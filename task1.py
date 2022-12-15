number = int(input('Введите цифру: '))
if number in range(1, 8):
    if number == 6 or number == 7:
        print("ДА")
    else:
        print('НЕТ')
else:
    print("Цифры должны быль в диапазоне 1-7!")
