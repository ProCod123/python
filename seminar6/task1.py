numbers_string = input('Введите список цифр через пробел: ').split()
numbers_list = map(int, numbers_string)


def digits(x):
    if 9 < x < 100:
        return True


sorted_numbers = list(filter(digits, numbers_list))
result_string = ' '.join(map(str, sorted_numbers))

print('Двузначные числа: ', result_string)
