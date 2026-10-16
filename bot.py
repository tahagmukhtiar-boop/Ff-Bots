import os
import telebot
import requests

TOKEN = "8913640665:AAFPOiEhLsZl-n4kpJ74rtmzSB_7ffytyw8"
bot = telebot.TeleBot(TOKEN)

# Daily cooldown track karne ke liye dictionary
user_likes_count = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🔥 Free Fire Bot Live!\n\n"
        "Commands:\n"
        "👉 /like ind <UID>\n"
        "👉 /visit ind <UID>\n"
        "👉 /like pk <UID>\n"
        "👉 /visit pk <UID>"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['like', 'visit'])
def handle_ff_actions(message):
    try:
        user_id = message.from_user.id
        parts = message.text.split()
        
        if len(parts) < 3:
            bot.reply_to(message, "Sahi tareeqa use karein:\n/like ind <UID>\n/visit ind <UID>")
            return
        
        command = parts[0][1:]
        region = parts[1].lower()
        uid = parts[2]

        if command == 'like':
            # 220-like daily limit check
            current_count = user_likes_count.get(user_id, 0)
            if current_count >= 220:
                bot.reply_to(message, "❌ Aapki aaj ki 220 likes ki limit poori ho chuki hai! Kal try karein.")
                return
            
            # Yahan Free Fire like API request lagegi
            bot.reply_to(message, f"⏳ Processing...\nRegion: {region.upper()}\nUID: {uid}\nLikes bheje ja rahe hain!")
            
            # Counter update
            user_likes_count[user_id] = current_count + 10 # Jitne likes ja rahe hain
            
        elif command == 'visit':
            # Yahan Free Fire profile visit API request lagegi
            bot.reply_to(message, f"⏳ Processing...\nRegion: {region.upper()}\nUID: {uid}\nProfile visit ki ja rahi hai!")
            
    except Exception as e:
        bot.reply_to(message, f"Error aa gaya: {str(e)}")

bot.infinity_polling()
                               
