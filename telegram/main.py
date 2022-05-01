import telebot
import ast
import time
import requests
from config import token, password, register_url, confirm_url
from telebot import types

token=token
password=password
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start']) #Объявили ветку для работы по команде <strong>number</strong>
def start_message(message):
    bot.send_message(message.chat.id,'Привет, нажми на кнопку и я зарегистрирую тебя на сайте begegg.')
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Подключаем клавиатуру
    button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True) #Указываем название кнопки, которая появится у пользователя
    keyboard.add(button_phone) #Добавляем эту кнопку
    bot.send_message(message.chat.id, 'Номер телефона', reply_markup=keyboard) #Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)

@bot.message_handler(content_types=['contact']) #Объявили ветку, в которой прописываем логику на тот случай, если пользователь решит прислать номер телефона :)
def contact(message):
    if message.contact is not None:
        keyboard = types.ReplyKeyboardRemove()
        phone = message.contact.phone_number
        #Если присланный объект <strong>contact</strong> не равен нулю
        r = requests.get(register_url + message.contact.phone_number, auth=('diabest_bot', password))
        try:
            data = r.json()
        except Exception as e:
            bot.send_message(message.chat.id, "Не получилось")
            return None
        print(message.contact, data['code']) #Выводим у себя в панели контактные данные. А вообщем можно их, например, сохранить или сделать что-то еще.
        bot.send_message(message.chat.id, 'Твоя ссылка: ' + '\n' +
        confirm_url + '{0}&{1}'.format(phone, data['code']), reply_markup=keyboard)
bot.polling(none_stop=True, interval=0, timeout=0)
#https://habr.com/ru/sandbox/149884/
