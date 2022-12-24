import math

length = int(input('Выберите количество знаков после запятой: '))
pi = math.pi
print(pi*(10**length)//1/(10**length))



