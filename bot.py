from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

# حط التوكن مباشر هون للتجربة
TOKEN = "8223338009:AAEq7NoAattxNKtxRxn0gbR7AS5Ub358meQ"

application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running ✅")

application.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    application.run_polling()
