import telebot

TOKEN = "7246698272:AAG5Go4rvJMd9eQ8p_v3ZQGDjrq18DPeTFA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحباً! البوت يعمل الآن بنجاح 🌸")

bot.polling()
