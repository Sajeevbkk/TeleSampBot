import telebot

BOT_TOKEN = '7112992837:AAH3mqoU5STfs9CZ7PcqIKBQFbHbeOCHFDI'
OWNER_ID = '1415184461'
bot = telebot.TeleBot(BOT_TOKEN)

# Dictionary to keep track of chat IDs
user_chat_ids = {}

# Command: /start
@bot.message_handler(commands=['start'])
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

@bot.message_handler(func=lambda message: True)
def forward_to_owner(message):
    # Check if the message is from the owner
    if str(message.from_user.id) == OWNER_ID:
        # If the message is a reply to a forwarded message, send it back to the original user
        if message.reply_to_message and message.reply_to_message.forward_from:
            target_user_id = message.reply_to_message.forward_from.id
            bot.send_message(target_user_id, message.text)
    else:
        echo_all(message)
        # Forward the message to the owner
        forwarded_message = bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        # Store the user's chat ID to allow replying
        user_chat_ids[forwarded_message.message_id] = message.chat.id

# Custom replies based on user input
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    text = message.text.lower()
    if str(message.from_user.id) != OWNER_ID:
        if "how are you" in text:
            bot.reply_to(message, "I'm doing fine! Thanks For Asking 🥰.\n\nWhat help Do you Want?")
        elif "thank you" in text:
            bot.reply_to(message, "You're welcome! 😊")
        elif "movie" in text:
            bot.reply_to(message, "I don't Give Movies. Do you Have Something Else to Ask to Jarvis")
        else:
            bot.reply_to(message, "When Jarvis Came Online He'll Surely Reply To You.")

print('PROGRAM STARTED')
# Start pollin
while True:
    try:
        bot.polling()
    except:
        continue
print('PROGRAM STOPPED')
