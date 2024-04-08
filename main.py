import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('##########################') 

@bot.message_handler(commands=['start'])  #при нажатии СТАРТ

def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Отправить картинку')
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Здравствуйте!', reply_markup=markup) #отправить сообщение _, вывести кнопки
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        webbrowser.open('https://github.com/') #открыть сайт
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Отправить картинку':
        file = open('./IMG.png', 'rb')
        bot.send_photo(message.chat.id, file) #отправить фото
        bot.register_next_step_handler(message, on_click)



@bot.message_handler(commands=['hello'])  #при нажатии /hello
def site(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}') #отправить сообщение _, имя пользователя

@bot.message_handler(commands=['site', 'website'])  #при нажатии site
def main(message):
    webbrowser.open('https://github.com/') #открыть сайт

@bot.message_handler(commands=['help'])  #при нажатии /help
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b>', parse_mode='html') #отправить сообщение в формате html


@bot.message_handler(content_types=['photo'])  #при отправке фото
def get_photo(message):
    bot.reply_to(message, 'Какое красивок фото') #ОТВЕТ на сообщение с фото, вывести сообщение

@bot.message_handler()  #при написании сообщения пользователем
def info(message):
    if message.text.lower() == 'привет':
       bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}') #отправить сообщение _, имя пользователя 
    elif message.text.lower() == 'id':
       bot.reply_to(message,  f'ID, {message.from_user.id}') #ОТВЕТ на сообщение , вывести ID
    else:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://github.com/')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
        btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
        markup.row(btn2, btn3)
        bot.reply_to(message, 'Выберете кнопку', reply_markup=markup)
    
        

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    elif callback.data == 'edit': 
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id -1)
    


bot.infinity_polling()