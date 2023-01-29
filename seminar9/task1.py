from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = '5209749192:AAEyxtpL5ndVu8-cs77LgG_W878lqKGaT-I'
bot = Bot(token= BOT_TOKEN)
updater = Updater(token= BOT_TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! ' 
                             'Я Бот удаляющий из текста фрагменты.\n'
                             'Что мне удалить из текста?')

counter = 0
del_str = ''

def voice(update, context):
    global counter
    global del_str
    text = update.message.text
    if counter == 0:
        context.bot.send_message(update.effective_chat.id, 
                                 f'Из текста будет удаляться фрагмент "{text}"')
        context.bot.send_message(update.effective_chat.id, 
                                 'Отравьте сообщением текст из которого нужно удалить фрагмент!')
        del_str = text
        counter = 1
    elif counter == 1: 
        text = del_chars(text, del_str)
        context.bot.send_message(update.effective_chat.id, text)
        context.bot.send_message(update.effective_chat.id, 
                                 'Если хотите изменить удаляемый фрагмент введите команду /new')
        context.bot.send_message(update.effective_chat.id, 'Либо введите другой текст')
        
def del_chars(text, del_str):
    new_text =''
    if del_str in text:
        for i in text.split():
            if del_str not in i:
                new_text += i + ' '        
    else:
        new_text = f'В тексте нет комбинации "{del_str}"'    
    if new_text == '':
       new_text = 'После удаления ничего не осталось(((('            
    return new_text 

def change(update, context):
    global counter
    context.bot.send_message(update.effective_chat.id, 'Введите новый фрагмент:')
    counter = 0
    

start_handler = CommandHandler('start', start)
change_fragment = CommandHandler('new', change)
message_handler = MessageHandler(Filters.text, voice)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(change_fragment)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle() 




