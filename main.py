import telebot
import pydirectinput


API_TOKEN = 'Your token'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Save")
    markup.add("Load")
    bot.send_message(message.chat.id, '👋', reply_markup=markup)

@bot.message_handler(regexp='Save')
def echo_message(message):
    bot.send_message(message.chat.id, 'Saving...')
    pydirectinput.press('f5')

@bot.message_handler(regexp='Load')
def echo_message(message):
    bot.send_message(message.chat.id, 'Loading...')
    pydirectinput.press('f8')

bot.infinity_polling(timeout = 25)