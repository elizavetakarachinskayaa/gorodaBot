# для работы с ботом
__author__ = 'Elizaveta Karachinskaya'
import telebot
import config
import db
#соединение с ботом
bot = telebot.TeleBot(config.token)

#Отвечает на команды
@bot.message_handler(commands=['start'])
def send_welcome(message):
    query = "SELECT  answers FROM commands WHERE id=1"
    result = db.query(query)


    bot.reply_to(message, result)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    query = "SELECT  answers FROM commands WHERE id=2" #запрос из бд для справки help
    result = db.query(query)
    bot.reply_to(message, result)

#Отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

#Запуск бота
bot.polling()