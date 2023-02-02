from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

BOT_TOKEN = '5209749192:AAEyxtpL5ndVu8-cs77LgG_W878lqKGaT-I'
bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! '
                             'Я Бот-калькулятор!\n'
                             'Отправь мне пример в формате приведенном ниже\n'
                             'Пример: 12 + 3 * 3 - 1 + 5 / 5 + 6 * 3')



def data(update, context):
    expression = update.message.text
    user_id = update.effective_chat.id
    res = result(expression)
    context.bot.send_message(update.effective_chat.id, f'Результат: {res}')
    logging(expression, user_id, res)


def result(expression):
    list_format = expression.split()
    operations = ['/', '*', '-', '+']
    for i in operations:
        while i in list_format:
            index = list_format.index(i)
            if i == '/':
                dev = float(list_format[index - 1]) / float(list_format[index + 1])
            elif i == '*':
                dev = float(list_format[index - 1]) * float(list_format[index + 1])
            elif i == '-':
                dev = float(list_format[index - 1]) - float(list_format[index + 1])
            elif i == '+':
                dev = float(list_format[index - 1]) + float(list_format[index + 1])
            del list_format[index - 1:index + 2]
            list_format.insert(index - 1, dev)
    return round(list_format[0], 2)


def logging(expression, user_id, result):
    with open("log.txt", "a", encoding='utf-8') as f:
        now = datetime.now().replace(microsecond=0)
        record = (expression.ljust(44, " ") + '| ' + str(result).ljust(12, " ") + '| '
                  + str(user_id).ljust(13, " ") + '| ' + str(now) + '|' + '\n')
        f.write(record)


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, data)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()

