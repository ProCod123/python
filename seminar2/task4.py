# 4)Требуется посчитать сумму чётных чисел, 
# расположенных между числами 1 и N включительно.

number = int(input('Введите число: '))

count = 0
string = ''
for i in range(1, number + 1):
    if i % 2 == 0 :
        count += i
        string += ' + ' + str(i)
print(f'Сумма четных чисел в диапазоне от {1} до {number}\n', string[3:], ' = ', count)        