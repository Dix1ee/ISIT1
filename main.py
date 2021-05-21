import telebot
import requests
from telebot import types

bot = telebot.TeleBot('1844595727:AAEnUXhgP2YiryXkfBunV9ZO9R7t6n7cOMI')
response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
EUR = response.json()["Valute"]["EUR"]["Value"]
USD = response.json()["Valute"]["USD"]["Value"]
RUB = float
RUB1 = float


# /start - выбор валют
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton('RUB → $')
        btn2 = telebot.types.KeyboardButton('RUB → €')
        btn3 = telebot.types.KeyboardButton('$ → RUB')
        btn4 = telebot.types.KeyboardButton('€ → RUB')


        markup.add(btn1, btn2)
        markup.add(btn3, btn4)


        msg = bot.send_message(message.chat.id, 'Выберите операцию', reply_markup=markup)
        bot.register_next_step_handler(msg, currency)


def currency(message):
    if message.text == 'RUB → €':
        msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
        bot.register_next_step_handler(msg, eur)
    elif message.text == 'RUB → $':
        msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
        bot.register_next_step_handler(msg, usd)
    elif message.text == '$ → RUB':
        msg = bot.send_message(message.chat.id, 'Введите сумму в долларах')
        bot.register_next_step_handler(msg, rub)
    elif message.text == '€ → RUB':
        msg = bot.send_message(message.chat.id, 'Введите сумму в евро')
        bot.register_next_step_handler(msg, rub1)

    else:
        msg = bot.send_message(message.chat.id, 'Введите корректные данные')
        bot.register_next_step_handler(msg, currency)


def eur(message):
    try:
        bot.send_message(message.chat.id, round(float(message.text) / EUR, 3))


    except ValueError:
        bot.send_message(message.chat.id, 'Введите число')


def usd(message):
    try:
        bot.send_message(message.chat.id, round(float(message.text) / USD, 3))
    except ValueError:
        bot.send_message(message.chat.id, 'Введите число')

def rub(message):
    try:
        bot.send_message(message.chat.id, round(float(message.text) * USD, 3))
    except ValueError:
        bot.send_message(message.chat.id, 'Введите число')

def rub1(message):
    try:
        bot.send_message(message.chat.id, round(float(message.text) * EUR, 3))
    except ValueError:
        bot.send_message(message.chat.id, 'Введите число')



bot.polling()
