import os
import telebot
import requests

TOKEN = "8913640665:AAFPOiEhLsZl-n4kpJ74rtmzSB_7ffytyw8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🔥 Free Fire Bot Live!\n\n"
        "Commands:\n"
        "👉 /like ind <UID>\n"
        "👉 /visit ind <UID>"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['like', 'visit'])
def handle_ff_actions(message):
    try:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Sahi tareeqa use karein: /like ind <UID> ya /visit ind <UID>")
            return
        
        command = parts[0][1:]
        region = parts[1]
        uid = parts[2]

        bot.reply_to(message, f"Aapki request process ho rahi hai...\nCommand: {command}\nRegion: {region}\nUID: {uid}")
        
        # Yahan aap apna Free Fire API endpoint ya request add kar sakte hain jo likes/visits bhejega.
        
    except Exception as e:
        bot.reply_to(message, f"Error aa gaya: {str_err := str(e)}")

bot.infinity_polling()
    
