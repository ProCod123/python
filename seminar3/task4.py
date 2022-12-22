number = int(input('Введите число: '))

bin_list = []
while number != 0:
    bin_list.append(number % 2) 
    number = number // 2
bin_list.reverse()    
print(f'Двоичная форма числа: {bin_list}')    
