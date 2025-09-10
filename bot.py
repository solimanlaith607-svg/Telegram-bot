import os
from telegram.ext import Application, CommandHandler

# جلب التوكن من Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

# تعريف أوامر بسيطة
async def start(update, context):
    await update.message.reply_text("أهلا! البوت شغال ✅")

async def help_command(update, context):
    await update.message.reply_text("الأوامر المتاحة:\n/start - بدء البوت\n/help - المساعدة")

def main():
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()

    # إضافة الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()

