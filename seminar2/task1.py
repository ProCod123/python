# 1) Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
list = []
rezl =[]

for i in range(1, number + 1):
    fac = 1
    res = ''
    for j in range(1, i + 1):
        fac = fac * j
        res += '*' + str(j) 
    list.append(fac)
    rezl.append(res[1:])
    
print(list, tuple(rezl))
