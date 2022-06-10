import telebot
from decouple import config
from random import choice


token = config('token')


bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Сделать бота', 'Выучить Python', 'Решить задачу', 'Написать текст']


HELP = '''
/help  - вывести список доступных команд
'''


todos = dict()


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
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date tasks:
        text = date.upper() + '\n'
        for tasks in tasks[date]:
            text = text + '0' + task + '\n'
    else:
        text = 'Задач на эту дату нет'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)