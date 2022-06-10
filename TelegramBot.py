import telebot
from decouple import config

token = config('token')

bot = telebot.TeleBot(token)