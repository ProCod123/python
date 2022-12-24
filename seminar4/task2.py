
number = int(input('Введите число: '))
# Проверяем является ли число сложным
for n in range(2, number):
    if number % n == 0:
        status = True
        break
else:
    status = False

# Разкладываем на множители
if status == True:
    result = []
    length = number 
    while number >= 2:
        for i in range(2,length):
            if number % i == 0:
                number = number / i
                result.append(i)
                break
    print(' * '.join(map(str,result)))      
else:
    print('Число простое')
    

