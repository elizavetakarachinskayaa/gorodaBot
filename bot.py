# для работы с ботом
__author__ = 'Elizaveta Karachinskaya'
import telebot
import config
import db
from liza_bot import *
#соединение с ботом
bot = telebot.TeleBot(config.token)

#Отвечает на команды

@bot.message_handler(commands=['start'])
def send_welcome(message):
    message.from_user.id
    bot.reply_to(message, start(message.text))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    query = "SELECT  answers FROM commands WHERE id=2" #запрос из бд для справки help
    result = db.query(query)
    bot.reply_to(message, result)

#Отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    gorod = message.text.title()
    # gorod = input('Введите город\n').title()
    # try:
    status = proverka(gorod)
    if status == -1:
        bot.send_message(message.chat.id, 'Город начинается с другой буквы')
    elif status == -2:
        bot.send_message(message.chat.id, 'Такого города нет')
    else:
        bot.reply_to(message, bot_reply())




#Запуск бота
bot.polling()