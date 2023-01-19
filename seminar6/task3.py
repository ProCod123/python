number = input('Введите вещественное число: ').split('.')
res = sum(list(map(int, number[0] + number[-1])))
print(res)
