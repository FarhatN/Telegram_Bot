import telebot
from decouple import config
from random import choice


token = config('token')


bot = telebot.TeleBot(token)


RANDOM_TASKS = ['������� ����', '������� Python', '������ ������', '�������� �����']


HELP = '''
������ ��������� ������:
/help  - ������� ������ ��������� ������
/print  - �������� ��� ������ �� �������� ����
/todo - �������� ������
/random - �������� �� ������� ��������� ������
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


@bot.message_handler(commands=['add', 'todo'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    add_todo(date, task)
    bot.send_message(message.chat.id, f'������ {task} ��������� �� ���� {date}')


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('�������', task)
    bot.send_message(message.chat.id, f'������ {task} ��������� �� �������')


@bot.message_handler(commands=['show', 'print'])
def print_(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f'[ ] {task}\n'
    else:
        tasks = '����� ���� ���'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)