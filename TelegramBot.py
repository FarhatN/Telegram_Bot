import telebot
from decouple import config


token = config('token')


bot = telebot.TeleBot(token)


HELP = '''
/help  - вывести список доступных команд
'''


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)