import telebot
from decouple import config


token = config('token')


bot = telebot.TeleBot(token)


RANDOM_TASKS = ['������� ����', '������� Python', '������ ������', '�������� �����']


HELP = '''
/help  - ������� ������ ��������� ������
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
    date = command[1]
    task = command[2]
    text = '������ ' + task + '��������� �� ����' + date
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['random'])
def random_add(message):



bot.polling(none_stop=True)