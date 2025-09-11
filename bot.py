import telebot

# التوكن تبعك
TOKEN = "8223338009:AAEq7NoAattxNKtxRxn0gbR7AS5Ub358meQ"
bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اهلا بك في بوت Ichanci Lith 👋")

# رد على أي رسالة
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"انت كتبت: {message.text}")

# تشغيل البوت
bot.polling()
