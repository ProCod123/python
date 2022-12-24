
import random

rate = int(input('Введите степень: '))
result = ''
for i in range(rate, -1, -1):
    rate = random.randint(1, 100)
    if i > 1:
        result += f'{rate}x^{i} + '
    elif i == 1:
        result += f'{rate}x + '  
    else:
        result += str(rate)      

print(result)    