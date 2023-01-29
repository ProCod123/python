import random

amount = 120
max_move = 28

def message(amount):
    print(f'Сейчас на столе {amount} конфет')


def next_move(candy, move, human_move):
    global amount
    if move == 'man':
        trigger = False
        while trigger == 0:
#            human_move = int(input('Введите количество конфет: '))
            if human_move > 28:
                print(f'За один ход можно взять не больше {max_move} конфет')
            else:
                trigger = True    
        amount -= human_move
    elif move == 'computer':
        if amount > 28:
            computer_move = random.randint(1,28)
            amount -= computer_move
            print(f'Компьютер взял {computer_move} конфет')
        elif amount <= 28:
            print(f'Компьютер взял {amount} конфет')
            amount = 0
    return amount 


def game():
    move = 'man'
    while amount > 0:
        message(amount)
        next_move(amount, move)
        if move == 'man':
            move = 'computer'
        elif move == 'computer':
            move = 'man'
    else:
        if move != 'man':
            print('Вы победили!!!')    
        else:
            print('Вы проиграли(((((')   
game()