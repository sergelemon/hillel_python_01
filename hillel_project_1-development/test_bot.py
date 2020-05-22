from telebot import TeleBot, types
import requests

# bot = TeleBot("1093892954:AAEjM1ua7zGkDXuNuTsVHlR4l1arnoqDzB8")
bot = TeleBot('1070416517:AAERRxi5rJ14jFGB5ZVe2mDbt6FBt7Uvpfg')

# @bot.message_handler(commands=['start'])
# def new_user(message):
#     bot.reply_to(message, 'Welcome')

@bot.message_handler(commands=['start'])
def new_user(message):
    user_id = message.from_user.id
    url = 'http://127.0.0.1:5000/users/start'
    response = requests.post(url, data={'id': user_id})
    bot.reply_to(message, response.text)

bot.polling()
