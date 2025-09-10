import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# إعداد اللوجز
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# أوامر البوت
def start(update, context):
    update.message.reply_text("أهلا! البوت شغال ✅")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # جلب التوكن من Environment Variables
    TOKEN = os.getenv("TOKEN")

    if not TOKEN:
        logger.error("⚠️ ما لقيت التوكن! لازم تضيف Environment Variable اسمو TOKEN في Render")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
