import telebot   #покдключаем библиотеку телебот
from telebot import types #покдключаем модуль types для кнопок
import requests
import json

bot = telebot.TeleBot('##########################')
API = '######################'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}. Напишите название города, где нужно узнать погоду')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    bot.reply_to(message, f'Погода там: {data["main"]["temp"]}')

bot.polling(none_stop=True)