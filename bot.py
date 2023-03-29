import telebot

bot=telebot.TeleBot('6058279985:AAEuX1mCmt3Pd7wK46NDdQdt7ghOhamx9rI', parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "estoy funcionando")
 
 
bot.infinity_polling()
 