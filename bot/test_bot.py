from telebot import TeleBot, types

bot = TeleBot('1070416517:AAERRxi5rJ14jFGB5ZVe2mDbt6FBt7Uvpfg')

@bot.message_handler(commands=['start'])
def new_user(message):
    bot.reply_to(message, 'Welcome')

@bot.message_handler()
def echo(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn1 = types.KeyboardButton('Test 1')
    btn2 = types.KeyboardButton('Test 2')
    markup.add(btn1, btn2)
    bot.reply_to(message, message.text, reply_markup=markup)


bot.polling()
