import os 
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]    


def print_field(field):
    os.system('cls')
    print(f'  {field[0]} | {field[1]} | {field[2]}\n'
           '---  ---  ---\n'
          f'  {field[3]} | {field[4]} | {field[5]}\n'
           '---  ---  ---\n'
          f'  {field[6]} | {field[7]} | {field[8]}\n')

def move(who, field):
    stop = 0
    while stop == 0:
        if who == 1:
            symbol = '(X)' 
        elif who == 2:
            symbol = '(0)'                
        move = int(input(f'Игрок №{who} {symbol} ведите номер поля: ')) - 1
        if field[move] == "0" or field[move] == "X":
            print(f'Поле {move + 1} уже занято!!!!') 
        else:
            if who == 1:
                field[move] = "X"
            else:
                field[move] = "0"
            stop = 1 

def check_victory(field): # В случае выигрышной комбинации возвращаем значение
    if field[0] == field[1] == field[2]: return field[0]  
    if field[3] == field[4] == field[5]: return field[3]
    if field[6] == field[7] == field[8]: return field[6]
    if field[0] == field[3] == field[6]: return field[0]
    if field[1] == field[4] == field[7]: return field[1]
    if field[2] == field[5] == field[8]: return field[2]
    if field[0] == field[4] == field[8]: return field[0]
    if field[6] == field[4] == field[2]: return field[6]
    return " "

def game():
    print_field(field)
    who = 1
    i = 0
    while i < 9:
        move(who, field)
        print_field(field)
        # После каждого хода выполняем проверку на победителя
        if check_victory(field) == "X":
            print("Победил игрок №1")
            break
        if check_victory(field) == "0":  # Победа компьютера
            print("Победил игрок №2")
            break  
        i += 1
        if i == 9:
            print('Ничья!')
        # Меняем значение переменной who чтобы изменить игрока
        if who == 1:
            who = 2 
        else: 
            who = 1      
        
game()         