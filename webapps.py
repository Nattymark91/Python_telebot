import telebot 
from telebot import types


bot = telebot.TeleBot('##############################################')

@bot.message_handler(commands=['start'])
def start(message):
     markup = telebot.types.InlineKeyboardMarkup()
     webAppTest = types.WebAppInfo('https://github.com/')
     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', web_app=webAppTest ))
     bot.send_message(message.chat.id, 'Здравствуйте', reply_markup=markup) 

bot.polling(none_stop=True)