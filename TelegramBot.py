import telebot
from decouple import config


token = config('token')


bot = telebot.TeleBot(token)


HELP = '''
/help  - вывести список доступных команд
'''


tasks = {}


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    bot.send_message(message.chat.id, ' оманда прин€та')


bot.polling(none_stop=True)