from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import requests

BOT_TOKEN = '5209749192:AAEyxtpL5ndVu8-cs77LgG_W878lqKGaT-I'

bot = Bot(token= BOT_TOKEN)
updater = Updater(token= BOT_TOKEN)
dispatcher = updater.dispatcher

amount = 120
max_move = 28
move = 'man'


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! '
                             'Я Бот с которым можно поиграть в "Конфетки" '
                             f'На столе лежить {amount} конфет, за один ход можно взять не больше {max_move} конфет. '
                             'Человек делает ход первым!')
    context.bot.send_message(update.effective_chat.id, 'Сделайте ход')


def data(update, context):
    player_move = int(update.message.text)
    game(update, context, player_move)


def human_move(human_move):
    global amount
    amount -= human_move
    text = f'Осталось {amount} конфет'
    return text


def computer_move(computer_move):
    global amount
    if amount > 28:
        computer_move = random.randint(1,28)
        amount -= computer_move
        text = f'Компьютер взял {computer_move} конфет. \n Осталось: {amount} \n Сделайте ход'
    elif amount <= 28:
        text = f'Компьютер взял {amount} конфет'
        amount = 0
    return text


def game(update, context, player_move):
    global move
    while amount > 0:
        if move == 'man':
            if player_move <= 28:
                text = human_move(player_move)
                context.bot.send_message(update.effective_chat.id, text)
            else:
                text = f'За один ход можно взять не более {max_move} конфет!!!'
                context.bot.send_message(update.effective_chat.id, text)
                break
            move = 'computer'     
        elif move == 'computer':
            text = computer_move(computer_move)
            context.bot.send_message(update.effective_chat.id, text)
            move = 'man'
            break
    if amount == 0:
        winner = 'Компьютер' if move == 'man' else 'Человек'
        context.bot.send_message(update.effective_chat.id, f'{winner} победил!!!')


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, data)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle() 
