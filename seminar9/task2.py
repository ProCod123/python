from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import requests


BOT_TOKEN = '5209749192:AAEyxtpL5ndVu8-cs77LgG_W878lqKGaT-I'

def send_message(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text,
    }
    response = requests.get('https://api.telegram.org/bot'+ BOT_TOKEN + '/sendMessage', params=params)








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
def data(update, context):
    human_move = int(update.message.text)    
    next_move(update, context, human_move)
    
 


def next_move(update, context, human_move):
    global amount
    global move
    if move == 'man':
        trigger = False
        while trigger == False:
            if human_move > 28:
                text = f'За один ход можно взять не больше {max_move} конфет!!!'
                context.bot.send_message(update.effective_chat.id, text)
                return
            else:
                trigger = True    
        amount -= human_move
    elif move == 'computer':
        if amount > 28:
            computer_move = random.randint(1,28)
            amount -= computer_move
            text = f'Компьютер взял {computer_move} конфет'
        elif amount <= 28:
            text = f'Компьютер взял {amount} конфет'
            amount = 0
    return amount 
    
    

start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, data)

dispatcher.add_handler(start_handler)

dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle() 
