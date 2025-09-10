import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("أهلا! البوت شغال ✅")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # ⚠️ بدّل هالجملة بالتوكن تبعك من BotFather
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
