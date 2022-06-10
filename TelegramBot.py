import telebot
from decouple import config

token = config('token')

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)