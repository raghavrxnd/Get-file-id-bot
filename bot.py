import os
import telebot

API_TOKEN = os.getenv("8235721726:AAHx8anmjFtCz_f4GM9MNUdDfnUvqnaVqI4")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.reply_to(message, f"Video ID:\n{message.video.file_id}")

bot.polling()