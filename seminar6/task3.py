number = input('Введите вещественное число: ').split('.')
res = sum(list(map(int, number[-1])))
print(res)
