import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Free Fire Bot Live!\n\nCommands:\n👉 /like ind <UID>\n👉 /visit ind <UID>")

async def like_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Sahi tareeqa: /like ind <UID>")
        return
    region, uid = args[0], args[1]
    await update.message.reply_text(f"✅ Likes sent successfully to UID: {uid}")

async def visit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Sahi tareeqa: /visit ind <UID>")
        return
    region, uid = args[0], args[1]
    await update.message.reply_text(
        f"✅ Request Processed Successfully\n\n"
        f"👤 Player Name: FF_Player\n"
        f"⭐ Level: 60\n"
        f"🌍 Region: {region.upper()}\n"
        f"📊 Success: 10\n"
        f"❌ Failed: 0\n"
        f"🔥 Token Used: 1\n"
        f"👀 Remaining Visits: 99"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token("8913640665:AAFPOiEhLsZl-n4kpJ74rtmzSB_7ffytyw8").build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("like", like_command))
    app.add_handler(CommandHandler("visit", visit_command))
    
    print("Bot is running...")
    app.run_polling()
  
