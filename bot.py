import os
import telebot

API_TOKEN = os.getenv("BOT_TOKEN")  # ✅ will be set later in Heroku/Glitch
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.reply_to(message, f"Video ID:\n{message.video.file_id}")

bot.polling()