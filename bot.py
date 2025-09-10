import os
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

# قراءة التوكن من Environment
TOKEN = os.getenv("TOKEN")

application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running ✅")

application.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    application.run_polling
