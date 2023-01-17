import random
import time

amount = 120
max_move = 28

def message(amount):
    print(f'Сейчас на столе {amount} конфет')


def next_move(candy, move):
    global amount
    if move == 'man':
        human_move = int(input('Введите количество конфет: '))
        amount -= human_move
    elif move == 'computer':
        computer_move = random.randint(1,28)
        amount -= computer_move
        print(f'Компьютер взял {computer_move} конфет')
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