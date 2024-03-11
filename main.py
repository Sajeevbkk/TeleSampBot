import telebot

BOT_TOKEN = '5834635307:AAH0SSwTxpduRdFJBJnPcF-hii7Bt9RKL4U'
bot = telebot.TeleBot(BOT_TOKEN)

# Command: /start or /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Command: /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = "Welcome to the ChatBot! Here are the available commands:\n\n" \
                "/start or /hello - Greet the bot\n" \
                "/help - Display this help message\n" \
                "/settings - Configure bot settings\n" \
                "Feel free to ask anything else!"
    bot.reply_to(message, help_text)

# Command: /settings
@bot.message_handler(commands=['settings'])
def send_settings(message):
    settings_text = "Bot settings:\n" \
                    "- Language: English\n" \
                    "- Notifications: On\n" \
                    "You can customize these settings in the future."
    bot.reply_to(message, settings_text)

# Custom replies based on user input
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    text = message.text.lower()
    if "how are you" in text:
        bot.reply_to(message, "I'm just a bot, but I'm doing fine! How can I assist you?")
    elif "thank you" in text:
        bot.reply_to(message, "You're welcome! 😊")
    else:
        bot.reply_to(message, "I didn't quite catch that. Feel free to ask again!")

# Start polling
bot.polling()
  
