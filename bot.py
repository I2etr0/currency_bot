import tenge_parser
from key import key
import telebot
from telebot import types

TOKEN = key
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands='start')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kzt = types.KeyboardButton('Тенге')
    markup.add(kzt)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def menu(message):
    if message.text == 'Тенге':
        bot.send_message(message.chat.id,
                         str(f'{tenge_parser.done_tenge}'))


bot.polling(none_stop=True)
