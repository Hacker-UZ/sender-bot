from telebot import TeleBot, types
from keep_alive import keep_alive
keep_alive()

bot = TeleBot(token="6762980475:AAGel7RcxF2tnGHVuKhrB5W2Io1PERdMHJs")
admin = 6775405766

@bot.message_handler()
def start(message: types.Message):
    bot.forward_message(admin, message.chat.id, message.message_id)

bot.polling()