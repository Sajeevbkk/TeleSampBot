import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7112992837:AAH3mqoU5STfs9CZ7PcqIKBQFbHbeOCHFDI'
bot = telebot.TeleBot(BOT_TOKEN)

# Define the chat ID of the bot owner (you can find this by sending a message to the bot and checking the chat ID)
owner_chat_id = '1415184461'

# Command: /start or /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Through this Bot You Can Talk to @PiratesDeveloper 😁")

# Command: /help
@bot.message_handler(commands=['know_jarvis'])
def send_help(message):
    help_text = "You Want to Know about Jarvis. See @Know_About_Jarvis"
    bot.reply_to(message, help_text)

# Command: /settings
@bot.message_handler(commands=['settings'])
def send_settings(message):
    settings_text = "Nothing Now. Planning to Add Some Features Soon 😜" 
    bot.reply_to(message, settings_text)

# Custom replies based on user input
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    text = message.text.lower()
    if "how are you" in text:
        bot.reply_to(message, "I'm doing fine! Thanks For Asking 🥰.\n\nWhat help Do you Want?")
    elif "thank you" in text:
        bot.reply_to(message, "You're welcome! 😊")
    elif "movie" in text:
        bot.reply_to(message, "I don't Give Movies. Do you Have Something Else to Ask to Jarvis")
    else:
        bot.reply_to(message, "When Jarvis Came Online He'll Surely Reply To You.")


# Start polling
if __name__ == '__main__':
    bot.polling(none_stop=True)
